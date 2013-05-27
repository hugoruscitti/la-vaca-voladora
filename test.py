#!/usr/bin/env python
# Instrucciones:
#
#     para iniciar este juego, escribir:
#
#           python test.py

import random
import pilas


class Estado:

    def __init__(self, vaca):
        self.vaca = vaca
        self.iniciar()

    def iniciar(self):
        pass



class Ingresando(Estado):

    def iniciar(self):
        self.contador = 0
        self.vaca.x = -380
        self.vaca.x = [-170], 0.5

    def actualizar(self):
        self.contador += 1

        if self.contador > 50:
            self.vaca.estado = Volando(self.vaca)

class Volando(Estado):

    def iniciar(self):
        self.contador = 0

    def actualizar(self):
        velocidad = 5

        if pilas.mundo.control.arriba:
            self.vaca.y += velocidad
        elif pilas.mundo.control.abajo:
            self.vaca.y -= velocidad

        if self.vaca.y > 210:
            self.vaca.y = 210
        elif self.vaca.y < -210:
            self.vaca.y = -210

        self.contador += 0.2

        if (self.contador % 2) < 1:
            self.vaca.imagen.definir_cuadro(3)
        else:
            self.vaca.imagen.definir_cuadro(4)


class Perdiendo(Estado):

    def iniciar(self):
        self.vaca.imagen.definir_cuadro(0)
        self.vaca.centro = ('centro', 'centro')
        pass

    def actualizar(self):
        self.vaca.rotacion += 7
        self.vaca.escala += 0.01
        self.vaca.x += 1
        self.vaca.y -= 1
        pass




class Vaca(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self)
        grilla = pilas.imagenes.cargar_grilla('data/sprites.png', 5, 1)
        grilla.definir_cuadro(3)
        self.imagen = grilla
        self.centro = (140, 59)
        self.radio_de_colision = 40
        self.x = -170
        self.estado = Ingresando(self)

    def actualizar(self):
        self.estado.actualizar()

    def perder(self):
        self.estado = Perdiendo(self)
        t = pilas.actores.Texto("Has perdido ...")
        t.escala = 0
        t.escala = [1], 0.5

class Enemigo(pilas.actores.Bomba):

    def __init__(self):
        pilas.actores.Bomba.__init__(self)
        self.izquierda = 320
        self.y = random.randint(-210, 210)

    def actualizar(self):
        self.x -= 5
        pilas.actores.Bomba.actualizar(self)

class Item(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self, 'estrella.png')
        self.escala = 0.5
        self.izquierda = 320
        self.y = random.randint(-210, 210)

    def actualizar(self):
        self.izquierda -= 5

        if self.derecha < -320:
            self.eliminar()


class Nube(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self)
        velocidad = random.randint(2, 10)
        self.velocidad = velocidad
        self.escala = velocidad / 10.0
        self.transparencia = velocidad * 6
        self.z = - (velocidad -5)
        self.x = random.randint(-320, 320)
        self.y = random.randint(-210, 210)

        rutas_imagenes_nubes = [
                'data/nube1.png',
                'data/nube2.png',
        ]
        self.imagen = random.choice(rutas_imagenes_nubes)

    def actualizar(self):
        self.x -= self.velocidad

        if self.derecha < -320:
            self.reiniciar_posicion()

    def reiniciar_posicion(self):
        self.izquierda = 320
        self.y = random.randint(-210, 210)


pilas.iniciar()

fondo = pilas.fondos.Fondo('data/nubes.png')
puntos = pilas.actores.Puntaje(x=-290, y=210)
vaca = Vaca()
items = []
enemigos = []

def crear_item():
    un_item = Item()
    items.append(un_item)
    return True

pilas.mundo.agregar_tarea(2, crear_item)




def cuanto_toca_item(v, i):
    i.eliminar()
    puntos.aumentar(10)
    puntos.escala = 2
    puntos.escala = [1], 0.2
    puntos.rotacion = random.randint(30, 60)
    puntos.rotacion = [0], 0.2

pilas.mundo.colisiones.agregar(vaca, items, cuanto_toca_item)


def crear_enemigo():
    un_enemigo = Enemigo()
    enemigos.append(un_enemigo)
    return True

pilas.mundo.agregar_tarea(3.3, crear_enemigo)


def cuanto_toca_enemigo(vaca, enemigo):
    vaca.perder()
    enemigo.eliminar()


pilas.mundo.colisiones.agregar(vaca, enemigos, cuanto_toca_enemigo)




Nube()
Nube()
Nube()
Nube()
Nube()
Nube()
Nube()

pilas.ejecutar()

#!/usr/bin/env python
# Instrucciones:
#
#     para iniciar este juego, escribir:
#
#           python test.py

import random
import pilas

class Vaca(pilas.actores.Actor):

    def __init__(self):
        pilas.actores.Actor.__init__(self)
        self.imagen = 'data/vaca_volando.png'
        self.centro = (140, 59)
        self.radio_de_colision = 40
        self.x = -170

    def actualizar(self):
        velocidad = 5

        if pilas.mundo.control.arriba:
            self.y += velocidad
        elif pilas.mundo.control.abajo:
            self.y -= velocidad

        if self.y > 210:
            self.y = 210
        elif self.y < -210:
            self.y = -210

class Enemigo(pilas.actores.Bomba):

    def __init__(self):
        pilas.actores.Bomba.__init__(self)
        self.izquierda = 320
        self.y = random.randint(-210, 210)

    def actualizar(self):
        self.x -= 5

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

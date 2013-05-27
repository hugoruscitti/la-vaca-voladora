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


pilas.iniciar()

fondo = pilas.fondos.Fondo('data/nubes.png')
vaca = Vaca()
Item()

pilas.ejecutar()

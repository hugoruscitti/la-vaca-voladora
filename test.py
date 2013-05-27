#!/usr/bin/env python
# Instrucciones:
#
#     para iniciar este juego, escribir:
#
#           python test.py

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


pilas.iniciar()

fondo = pilas.fondos.Fondo('data/nubes.png')
vaca = Vaca()

pilas.ejecutar()

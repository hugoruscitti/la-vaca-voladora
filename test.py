#!/usr/bin/env python
# Instrucciones:
#
#     para iniciar este juego, escribir:
#
#           python test.py

import pilas

pilas.iniciar()

fondo = pilas.fondos.Fondo('data/nubes.png')
pelota = pilas.actores.Pelota()


pilas.ejecutar()

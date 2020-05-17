from manimlib.imports import *
import random

class Plot1(Scene):
    def construct(self):
        picosPadas = []
        picosPadas.append(Circle(radius=1,color=ORANGE))
        picosPadas.append(Annulus(inner_radius=0, outer_radius=1, color=ORANGE))
        picosVidus = []
        picosVidus.append(Circle(radius=0.8,color=YELLOW))
        picosVidus.append(Annulus(inner_radius=0, outer_radius=.8, color=YELLOW))



        self.play(ShowCreation(picosPadas[0]))
        self.play(ShowCreation(picosPadas[1]))
        self.play(ShowCreation(picosVidus[0]))
        self.play(ShowCreation(picosVidus[1]))
        self.wait(3)

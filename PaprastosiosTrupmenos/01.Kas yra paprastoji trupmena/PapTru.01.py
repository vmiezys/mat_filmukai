from manimlib.imports import *
import random

class Plot1(Scene):
    def construct(self):
        def kurkPica(picosDydis):
            picosPadas = []
            picosPadas.append(Circle(radius=picosDydis,color=ORANGE))
            picosPadas.append(Annulus(inner_radius=0, outer_radius=picosDydis, color=ORANGE))

            picosVidus = []
            picosVidus.append(Circle(radius=0.9*picosDydis,color=YELLOW))
            picosVidus.append(Annulus(inner_radius=0, outer_radius=.9*picosDydis, color=YELLOW))
            pagardoDydis = 0.1
            picosPagardai = []
            picosPagardai.append(Annulus(inner_radius=0, outer_radius=pagardoDydis*picosDydis, color=RED))
            picosPagardai.append(Annulus(inner_radius=0, outer_radius=pagardoDydis*picosDydis, color=RED))
            picosPagardai.append(Annulus(inner_radius=0, outer_radius=pagardoDydis*picosDydis, color=RED))
            picosPagardai.append(Annulus(inner_radius=0, outer_radius=pagardoDydis*picosDydis, color=RED))
            picosPagardai.append(Line(picosPagardai[0].get_left(),picosPagardai[0].get_right(),color=GREEN))
            picosPagardai.append(Line(picosPagardai[0].get_left(),picosPagardai[0].get_right(),color=GREEN))
            picosPagardai.append(Line(picosPagardai[0].get_left(),picosPagardai[0].get_right(),color=GREEN))
            picosPagardai.append(Line(picosPagardai[0].get_left(),picosPagardai[0].get_right(),color=GREEN))
            picosPagardai.append(Annulus(inner_radius=0, outer_radius=pagardoDydis*picosDydis, color=RED))

            pagarduJudesioMultiplieris = 0.4
            #MESA
            picosPagardai[0].shift(UP*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[0].shift(LEFT*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[1].shift(UP*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[1].shift(RIGHT*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[2].shift(DOWN*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[2].shift(LEFT*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[3].shift(DOWN*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[3].shift(RIGHT*picosDydis*pagarduJudesioMultiplieris)
            #ZOLELES
            picosPagardai[4].shift(RIGHT*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[4].rotate(-PI/4)
            picosPagardai[5].shift(LEFT*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[5].rotate(-PI/4)
            picosPagardai[6].shift(UP*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[6].rotate(PI/4)
            picosPagardai[7].shift(DOWN*picosDydis*pagarduJudesioMultiplieris)
            picosPagardai[7].rotate(PI/4)

            return VGroup(*picosPadas,*picosVidus,*picosPagardai)

        pica = kurkPica(1)
        picaDidele = kurkPica(1.5)

        self.play(ShowCreation(pica[0]))
        self.play(FadeIn(pica[1]))
        self.play(ShowCreation(pica[2]))
        self.play(FadeIn(pica[3]))
        self.play(FadeIn(pica[4:]))
        self.play(ApplyMethod(pica.shift,LEFT*3))
        self.wait(2)

        self.play(ShowCreation(picaDidele[0]))
        self.play(FadeIn(picaDidele[1]))
        self.play(ShowCreation(picaDidele[2]))
        self.play(FadeIn(picaDidele[3]))
        self.play(FadeIn(picaDidele[4:]))
        self.play(ApplyMethod(picaDidele.shift,RIGHT*2))

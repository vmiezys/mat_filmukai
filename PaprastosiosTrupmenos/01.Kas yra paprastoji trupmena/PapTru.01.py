from manimlib.imports import *
import random

class Plot1(Scene):
    def construct(self):

        trupmenos = [[5,7],[2,3]]
        trupmenos.append([trupmenos[0][0]*trupmenos[1][0],trupmenos[1][1]*trupmenos[0][1]])
        trupmenos_tex = [
            "{" + str(trupmenos[0][0]) + " \\over " + str(trupmenos[0][1]) + "}",
            "{" + str(trupmenos[1][0]) + " \\over " + str(trupmenos[1][1]) + "}",
            "{" + str(trupmenos[2][0]) + " \\over " + str(trupmenos[2][1]) + "}"
        ]
        dauginti = [trupmenos[0][0]/trupmenos[0][1],trupmenos[1][0]/trupmenos[1][1]]
        sandauga = dauginti[0]*dauginti[1] #ISTRINTI VELIAU
        dauginti.append(sandauga)

        fiksuotas_ekrano_dydis = 13
        didziausias_gautas_skaicius = max(dauginti[0],dauginti[2],1)
        didziausias_x = math.ceil(didziausias_gautas_skaicius) * 1.2

        melyna_vienetine_atkarpa = fiksuotas_ekrano_dydis/didziausias_x
        raudona_vienetine_atkarpa = melyna_vienetine_atkarpa * dauginti[0]

        ilgo_ticko_multiple = 1.5
        ticko_dydis = 0.16

        line0 = NumberLine(
            color=BLUE,
            x_max=didziausias_x,
            unit_size=melyna_vienetine_atkarpa,
            include_numbers=True,
            include_tip=True,
            numbers_with_elongated_ticks = [0,1],
            line_to_number_buff = MED_LARGE_BUFF,
            x_min = 0,
            longer_tick_multiple = ilgo_ticko_multiple,
            tick_size = ticko_dydis
        )

        line0.to_edge(LEFT)
        line0.shift(DOWN)


        pirmos_trupmenos_kartotiniai_tex_mobject = []
        antros_trupmenos_kartotiniai_tex_mobject = []
        for i in range(trupmenos[0][1]-1): #range(5) outputina [0,1,2,3,4]
            temp = TexMobject("{" + str(i+1)," \\over ",str(trupmenos[0][1]) + "}")
            temp.scale(0.6)
            pirmos_trupmenos_kartotiniai_tex_mobject.append(temp)
        for i in range(trupmenos[1][1]-1): #range(5) outputina [0,1,2,3,4]
            temp = TexMobject("{" + str(i+1)," \\over ",str(trupmenos[1][1]) + "}")
            temp.scale(0.6)
            antros_trupmenos_kartotiniai_tex_mobject.append(temp)

        line = NumberLine(
            color=BLUE,
            x_max=1,
            unit_size=melyna_vienetine_atkarpa,
            include_numbers=True,
            include_tip=False,
            tick_frequency=1/trupmenos[0][1],
            numbers_with_elongated_ticks = [0,1],
            line_to_number_buff = MED_LARGE_BUFF,
            x_min = 0,
            longer_tick_multiple = ilgo_ticko_multiple,
            tick_size = ticko_dydis
        )

        line.to_edge(LEFT)
        line.shift(DOWN)

        vardikliai1 = []
        for i in range(trupmenos[0][1]):
            vardikliai1.append(str(i+1))
        vardikliai1_mobject = TextMobject(*vardikliai1)

        for i in range(trupmenos[0][1]):
            vardikliai1_mobject[i].move_to(line.number_to_point( (i+0.5)/(trupmenos[0][1])),DOWN)
            vardikliai1_mobject[i].shift(UP*0.1)
            vardikliai1_mobject[i].scale(0.7)




        tickai1 = line.get_tick_marks()
        for i in range(1, trupmenos[0][1]):
            pirmos_trupmenos_kartotiniai_tex_mobject[i-1].move_to(tickai1[i].get_bottom(),UP)
            pirmos_trupmenos_kartotiniai_tex_mobject[i-1].shift(DOWN*0.25)
        pirmos_trupmenos_kartotiniai_vgroup = VGroup(*pirmos_trupmenos_kartotiniai_tex_mobject)

        nulis = line.number_to_point(0)

        line2 = NumberLine(   #TA, KURI ANT MĖLYNO UŽSIRYŠKINA RAUDONAI
            color=RED,
            x_max=1,
            include_tip=False,
            include_numbers=False,
            #longer_tick_multiple = 3,
            unit_size=raudona_vienetine_atkarpa,
            label_direction=UP,
            line_to_number_buff = MED_LARGE_BUFF,
            x_min = 0,
            longer_tick_multiple = ilgo_ticko_multiple,
            tick_size = ticko_dydis
        )

        line2.move_to(nulis,LEFT)

        line3 = line2.copy() #TA, Į KURIĄ PAKELIAME LINE2
        line3.shift(UP)

        raudono0_tickas = line3.number_to_point(0)
        raudono1_tickas = line3.number_to_point(1)
        melyno0_tickas = line.number_to_point(0)
        melyno1_tickas = line.number_to_point(dauginti[0])

        sujungimas0 = DashedLine(melyno0_tickas,raudono0_tickas)
        sujungimas1 = DashedLine(melyno1_tickas,raudono1_tickas)

        line4 = line3.copy()
        line4.add_numbers(0)
        line4.add_numbers(1)

        line6 = NumberLine(
            color=RED,
            x_max=1,
            include_tip=False,
            include_numbers=False,
            numbers_with_elongated_ticks = range(math.floor(line0.get_length()/raudona_vienetine_atkarpa)),
            unit_size=raudona_vienetine_atkarpa,
            label_direction=UP,
            line_to_number_buff = MED_LARGE_BUFF,
            tick_frequency = 1/trupmenos[1][1],
            x_min = 0,
            longer_tick_multiple = ilgo_ticko_multiple,
            tick_size = ticko_dydis
        )

        nulis4 = line4.number_to_point(0)
        line6.move_to(nulis4,LEFT)

        vardikliai2 = []
        for i in range(trupmenos[1][1]):
            vardikliai2.append(str(i+1))
        vardikliai2_mobject = TextMobject(*vardikliai2)

        for i in range(trupmenos[1][1]):
            vardikliai2_mobject[i].move_to(line6.number_to_point( (i+0.5)/(trupmenos[1][1])),DOWN)
            vardikliai2_mobject[i].shift(UP*0.1)
            vardikliai2_mobject[i].scale(0.7)

        tickai2 = line6.get_tick_marks()
        for i in range(1, trupmenos[1][1]):
            antros_trupmenos_kartotiniai_tex_mobject[i-1].move_to(tickai2[i].get_top(),DOWN)
            antros_trupmenos_kartotiniai_tex_mobject[i-1].shift(UP*0.25)
        antros_trupmenos_kartotiniai_vgroup = VGroup(*antros_trupmenos_kartotiniai_tex_mobject)

        raudono_tickas = line.number_to_point(sandauga)
        melyno_tickas = line6.number_to_point(dauginti[1])

        sujungimas = DashedLine(melyno_tickas,raudono_tickas)
        #sujungimas.set_color(YELLOW)

        tekstas1 = TextMobject("Apskaičiuokime sandaugą")
        tekstas2 = TexMobject(trupmenos_tex[0]," \\cdot ",trupmenos_tex[1],"=",trupmenos_tex[2])
        tekstas1.to_edge(UP)
        tekstas2.move_to(tekstas1.get_bottom(),UP)
        tekstas2.shift(DOWN*0.25)
        tekstas2[4:5].set_color(YELLOW)

        jungiancios_linijos=[]
        for i in range(trupmenos[1][1]+1):
            raudono_tickas_temp = line6.number_to_point(i/trupmenos[1][1])
            melyno_tickas_temp = line.number_to_point((i/trupmenos[1][1])*dauginti[0])
            jungiancios_linijos.append(DashedLine(raudono_tickas_temp,melyno_tickas_temp))

        jungiancios_linijos_vgroup = VGroup(*jungiancios_linijos)
        sandaugos_tickas = line.get_tick(sandauga)
        sandaugos_tickas.set_color(YELLOW)
        klaustukas = TextMobject("?")
        klaustukas.set_color(YELLOW)
        klaustukas.move_to(sandaugos_tickas.get_bottom(),UP)
        klaustukas.shift(DOWN*0.25)

        sandaugos_skaicius = TexMobject("{",str(trupmenos[0][0]*trupmenos[1][0]),"\\over",str(trupmenos[0][1]*trupmenos[1][1]),"}")
        sandaugos_skaicius.scale(0.6)
        sandaugos_skaicius.set_color(YELLOW)
        sandaugos_skaicius.move_to(klaustukas)
        sandaugos_skaicius.set_y(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1][1].get_center()[1])

        sandaugos_skaicius_klaustukas = TexMobject("{","\\text{?}","\\over",str(trupmenos[0][1]*trupmenos[1][1]),"}")
        sandaugos_skaicius_veiksmas_skaitiklis = str(trupmenos[0][0]*trupmenos[1][1]) + ":" + str(trupmenos[1][1]) + "\\cdot" + str(trupmenos[1][0])
        sandaugos_skaicius_veiksmas = TexMobject("{",sandaugos_skaicius_veiksmas_skaitiklis,"\\over",str(trupmenos[0][1]*trupmenos[1][1]),"}")

        sandaugos_skaicius_klaustukas.scale(0.6)
        sandaugos_skaicius_klaustukas.set_color(YELLOW)
        sandaugos_skaicius_klaustukas.move_to(sandaugos_skaicius)

        sandaugos_skaicius_veiksmas.scale(0.6)
        sandaugos_skaicius_veiksmas.set_color(YELLOW)
        sandaugos_skaicius_veiksmas.move_to(sandaugos_skaicius)

        line7 = NumberLine(
            color=BLUE,
            x_max=1,
            unit_size=melyna_vienetine_atkarpa,
            include_numbers=False,
            include_tip=False,
            tick_frequency=1/(trupmenos[0][1]*trupmenos[1][1]),
            numbers_with_elongated_ticks = [0,1],
            tick_size = 0.08,
            x_min = 0,
            longer_tick_multiple = ilgo_ticko_multiple
        )
        line7.move_to(line0.number_to_point(0),LEFT)
        mazi_tickai = line7.get_tick_marks()
        mazi_tickai_reikalingi = []
        for i, tickas in enumerate(mazi_tickai):
            if tickas.get_length() < 0.2:
                if i % trupmenos[1][1] != 0:
                    tickas.set_color(YELLOW)
                    mazi_tickai_reikalingi.append(tickas)

        line8 = Line(line.number_to_point(0),line.number_to_point(dauginti[0]))

        line8.move_to(line0.number_to_point(0),LEFT)

        mazi_tickai_vgroup = VGroup(*mazi_tickai_reikalingi)
        mazi_tickai_vgroup2 = mazi_tickai_vgroup.copy()
        mazi_tickai_vgroup2.set_color(BLUE)

        didesnieji_tickai = line.get_tick_marks().copy()
        for i in didesnieji_tickai:
            i.scale(2)

        skaiciukai = []
        for i in range(trupmenos[0][1]*trupmenos[1][1]):
            temp_skaicius = (i % trupmenos[1][1])+1
            temp_skaicius_mobject = TextMobject(str(temp_skaicius))
            temp_skaicius_mobject.move_to(line0.number_to_point((i+0.5)/(trupmenos[0][1]*trupmenos[1][1])))
            temp_skaicius_mobject.shift(UP*0.25)
            temp_skaicius_mobject.scale(0.6)
            skaiciukai.append(temp_skaicius_mobject)

        skaiciukai_vgroup = VGroup(*skaiciukai)
        skaiciukai_vgroup2 = skaiciukai_vgroup.copy()

        brace_mazas = Brace(line8)
        brace_mazas_tekstas = brace_mazas.get_tex(str(trupmenos[0][0]))
        brace_mazas_tekstas2 = TexMobject(str(trupmenos[0][0])," \\cdot ",str(trupmenos[1][1]))
        brace_mazas_tekstas2.move_to(brace_mazas_tekstas)
        brace_mazas_tekstas3 = [str(trupmenos[1][1])]
        for i in range(trupmenos[0][0]-1):
            brace_mazas_tekstas3.append("+")
            brace_mazas_tekstas3.append(str(trupmenos[1][1]))
        brace_mazas_tekstas3 = TexMobject(*brace_mazas_tekstas3)
        brace_mazas_tekstas3.move_to(brace_mazas_tekstas)


        brace_viso = Brace(line7)
        brace_viso_tekstas = brace_viso.get_tex(str(trupmenos[0][1]))
        brace_viso_tekstas2 = TexMobject(str(trupmenos[0][1])," \\cdot ",str(trupmenos[1][1]))
        brace_viso_tekstas2.move_to(brace_viso_tekstas)
        brace_viso_tekstas3 = [str(trupmenos[1][1])]
        for i in range(trupmenos[0][1]-1):
            brace_viso_tekstas3.append("+")
            brace_viso_tekstas3.append(str(trupmenos[1][1]))
        brace_viso_tekstas3 = TexMobject(*brace_viso_tekstas3)
        brace_viso_tekstas3.move_to(brace_viso_tekstas)

        temp1 = str(trupmenos[0][0]) + "\\cdot" + str(trupmenos[1][1])
        temp2 = str(trupmenos[0][1]) + "\\cdot" + str(trupmenos[1][1])
        trup_su_PPTS = TexMobject("{",temp1,"\\over",temp2,"}")
        trup_su_PPTS.scale(0.6)
        trup_su_PPTS.move_to(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1][1])
        trup_su_PPTS.shift(DOWN*0.25)

        trup_po_PPTS = TexMobject("{",trupmenos[0][0]*trupmenos[1][1],"\\over",trupmenos[2][1],"}")
        trup_po_PPTS.scale(0.6)
        trup_po_PPTS.move_to(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1][1])



    #GROJARAŠTIS
        self.play(Write(tekstas1))
        self.play(Write(tekstas2[0:3]))
        self.wait()
        self.play(ShowCreation(line0))
        self.wait()
        self.play(ApplyMethod(tekstas2[0].scale,7/5))
        self.wait()
        self.play(ApplyMethod(tekstas2[0][2:].set_color,YELLOW))
        self.wait()
        self.play(
            FadeIn(line),
            ReplacementTransform(tekstas2[0][2:].copy(),vardikliai1_mobject),
            ApplyMethod(tekstas2[0][2:].set_color,WHITE)
        )
        self.wait()
        self.play(
            ReplacementTransform(tekstas2[0].copy(),pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1])
        )
        self.wait(3)
        self.play(
            FadeOut(vardikliai1_mobject),
            ApplyMethod(tekstas2[0].scale,5/7)
        )
        self.wait()
        self.play(ShowCreation(line2))
        self.wait()
        self.play(
            ShowCreation(sujungimas0),
            ShowCreation(sujungimas1),
            ReplacementTransform(line2,line3)
        )
        self.play(FadeIn(line4))
        self.wait()
        self.play(FadeOut(sujungimas0),FadeOut(sujungimas1))
        self.play(ApplyMethod(tekstas2[2].scale,7/5))
        self.play(ApplyMethod(tekstas2[2][2:].set_color,YELLOW))
        self.wait()
        self.play(
            FadeIn(line6),
            ReplacementTransform(tekstas2[2][2:].copy(),vardikliai2_mobject),
            ApplyMethod(tekstas2[2][2:].set_color,WHITE)
        )
        self.play(
            ReplacementTransform(tekstas2[2].copy(),antros_trupmenos_kartotiniai_vgroup[trupmenos[1][0]-1])
        )
        self.wait(3)
        self.play(
            FadeOut(vardikliai2_mobject),
            ApplyMethod(tekstas2[2].scale,5/7)
        )
        self.wait()
        self.play(ShowCreation(sujungimas))
        self.play(FadeIn(sandaugos_tickas),FadeIn(klaustukas))
        self.wait(2)
        self.play(ApplyMethod(klaustukas.scale,1.8),run_time=3)
        self.wait(2)

        self.play(
            FadeOut(klaustukas),
            FadeOut(sujungimas),
            FadeOut(sandaugos_tickas)
        )
        self.play(
            GrowFromPoint(brace_mazas, line.number_to_point(0)),
            ApplyMethod(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1].shift,DOWN*0.25)
            )
        self.play(Write(brace_mazas_tekstas))
        self.wait(2)
        self.play(ApplyMethod(antros_trupmenos_kartotiniai_vgroup[trupmenos[1][0]-1][2].scale,2))
        self.wait()
        self.play(
            ReplacementTransform(antros_trupmenos_kartotiniai_vgroup[trupmenos[1][0]-1][2].copy(),mazi_tickai_vgroup[:trupmenos[0][0]*(trupmenos[1][1]-1)]),
            ApplyMethod(antros_trupmenos_kartotiniai_vgroup[trupmenos[1][0]-1][2].scale,1/2)
        )
        self.wait()
        self.play(Write(skaiciukai_vgroup[:trupmenos[0][0]*trupmenos[1][1]]))
        self.wait()
        self.play(
            ReplacementTransform(skaiciukai_vgroup[:trupmenos[1][1]],brace_mazas_tekstas3[0]),
            FadeOut(brace_mazas_tekstas)
        )
        for i in range(trupmenos[0][0]-1):
            self.play(
                ReplacementTransform(skaiciukai_vgroup[(i+1)*trupmenos[1][1]:(i+2)*trupmenos[1][1]],brace_mazas_tekstas3[i*2+1:i*2+3])
            )
        self.wait()
        self.play(ReplacementTransform(brace_mazas_tekstas3,brace_mazas_tekstas2))
        self.wait(2)
        self.play(
            ReplacementTransform(brace_mazas_tekstas2.copy(),trup_su_PPTS[1:3]),
            FadeOut(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1][0:2])
        )
        self.wait(2)
        self.play(
            ReplacementTransform(brace_mazas, brace_viso),
            ReplacementTransform(brace_mazas_tekstas2,brace_viso_tekstas)
            )
        self.wait()
        self.play(FadeInFrom(mazi_tickai_vgroup[trupmenos[0][0]*(trupmenos[1][1]-1):],UP))
        self.play(Write(skaiciukai_vgroup2))
        self.wait()
        self.play(
            ReplacementTransform(skaiciukai_vgroup2[:trupmenos[1][1]],brace_viso_tekstas3[0]),
            FadeOut(brace_viso_tekstas),
            ApplyMethod(trup_su_PPTS[1:3].shift,DOWN),
            ApplyMethod(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1][2:].shift,DOWN)
        )
        for i in range(trupmenos[0][1]-1):
            self.play(
                ReplacementTransform(skaiciukai_vgroup2[(i+1)*trupmenos[1][1]:(i+2)*trupmenos[1][1]],brace_viso_tekstas3[i*2+1:i*2+3])
            )
        self.wait()
        self.play(
            ReplacementTransform(brace_viso_tekstas3,brace_viso_tekstas2),
            ApplyMethod(trup_su_PPTS[1:3].shift,UP),
            ApplyMethod(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1][2:].shift,UP)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(brace_viso_tekstas2.copy(),trup_su_PPTS[3:]),
            FadeOut(pirmos_trupmenos_kartotiniai_vgroup[trupmenos[0][0]-1][2:])
        )
        self.wait(2)
        self.play(
            FadeOut(brace_viso_tekstas2),
            FadeOut(brace_viso),
            ApplyMethod(trup_su_PPTS.shift,UP*0.25)
        )
        self.wait()
        self.play(ReplacementTransform(trup_su_PPTS,trup_po_PPTS))
        self.play(ReplacementTransform(mazi_tickai_vgroup,mazi_tickai_vgroup2))
        self.wait(2)
        self.play(
            FadeIn(klaustukas),
            FadeIn(sujungimas),
            FadeIn(sandaugos_tickas)
        )
        self.wait(2)
        self.play(ReplacementTransform(klaustukas,sandaugos_skaicius_klaustukas))
        self.wait()
        self.play(FadeInFrom(jungiancios_linijos_vgroup,direction=UP))
        self.play(ReplacementTransform(sandaugos_skaicius_klaustukas,sandaugos_skaicius_veiksmas))
        self.wait(3)
        self.play(ReplacementTransform(sandaugos_skaicius_veiksmas,sandaugos_skaicius))
        self.wait()
        self.play(
            Write(tekstas2[3:4]),
            ReplacementTransform(sandaugos_skaicius[:].copy(),tekstas2[4:5]),
            FadeOut(jungiancios_linijos_vgroup)
        )
        self.wait(5)

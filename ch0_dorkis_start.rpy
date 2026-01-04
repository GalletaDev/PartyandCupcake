
# do = Dorki
# mc = Metz
# sa = Sasha
# he = Hector
# li = Lili
# cor = Presidente
# w = ??? alguien desconocido



screen end_screen_dead():

    pass
    #add "grey_dead_imagen"
    #add "dorki grey"
    #add "glitch_consecutive"
    #text _("Ohu, sorry, not file search...")
    #vbox:
    # textbutton _("Volver al menu") action Jump("end_start")
    # textbutton _("REINICIAR") action ...


label end_party_cookie:
    #play music the_end_music
    call screen end_screen_dead


label end_start:
    scene black with dissolve
    $ renpy.pause(1.0, hard=True)
    return





label start:
    $ renpy.stop_skipping()
    stop music fadeout 1.0
    # show screen console_chapter()
    ##########################
    if chapter.get_quantity() <= 1:
        show intro_text:
            align(.5, .5)
            zoom 1.65
            pos(.5, .5)
            anchor(.5, .5)
            alpha 0.0
            linear .2 alpha 1.0
            pause 1.0
            linear .45 alpha 0.0

    $ renpy.pause(2.0, hard=True)
    hide intro_text
    $ renpy.pause(.2, hard=True)
    if chapter.get_quantity() < 2:
        $ chapter.add_ch()
        jump starts_force_init
    else:
        jump starts_force



label starts_force:
    stop music fadeout 1.0
    play sound transition_sound
    scene white with effect_tic_tac
    hide screen glitch_blocks
    $ renpy.pause(.75, hard=True)
    play sound reloj_sound_normal
    $ reset_name_characters()
    $ chapter.add_ch()
    show reloj_tic_tac
    show background_pink_blur:
        pause 0.6
        easeout 2.0 alpha 0.4
    show cubes_red_background:
        yoffset 100
        ease 1.2 yoffset -600
        easeout 2.7 yoffset 600  
    with Dissolve(.2)   

    show layer master at shake_try(r=5)
    $ renpy.pause(3.2, hard=True)
    stop sound fadeout 1.7
    scene black with Dissolve(.6)
    play sound transition_sound
    pause 0.1
    if persistent.actived_cap_120:
        $ chapter.set_ch(120)

    $ jump_label = get_jump_label()
    show layer master
    $ renpy.pause(predict=True)
    jump expression jump_label



label starts_force_init:
    stop music fadeout 1.0
    $ reset_name_characters()
    $ jump_label = get_jump_label()

    $ renpy.pause(predict=True)
    jump expression jump_label











label starts_end:
    stop music
    play sound transition_sound
    show layer master
    scene white with effect_tic_tac
    hide screen glitch_blocks
    $ renpy.pause(.75, hard=True)
    play sound glass
    play sound reloj_sound_extreme
    $ reset_name_characters()
    $ chapter.add_ch()
    show reloj_tic_tac
    show crist1
    show crist2
    show crist3
    show background_pink_blur:
        pause 0.6
        easeout 2.0 alpha 0.7 
    with Dissolve(.2)   

    show layer master at shake_try(r=12)
    $ renpy.pause(7.5, hard=True)
    stop sound fadeout 1.7
    scene black with Dissolve(.6)
    play sound transition_sound
    pause 0.1
    $ jump_label = get_jump_label()
    show layer master
    $ renpy.pause(predict=True)
    jump expression jump_label    




image end_chapter1 = Transform("images/future_1.png", matrixcolor=SaturationMatrix(0))
image end_chapter2 = Transform("images/future_2.png", matrixcolor=SaturationMatrix(0))
image animation_end_chapter3:
    alpha 0.56
    "end_chapter1"
    pause 3.2
    "end_chapter2" with Dissolve(.5)

image prota_fade:
    "images/mc_corruption.png"
    alpha 0.0
    pause .45
    ease .25 alpha 0.7
    pause .75
    ease .25 alpha 0.0



label starts_end_game:
    $ persistent.actived_cap_120 = False
    stop music
    play sound transition_sound
    show layer master
    scene white with effect_tic_tac
    hide screen glitch_blocks
    $ renpy.pause(.75, hard=True)
    play sound glass
    play sound reloj_sound_extreme
    $ reset_name_characters()
    $ chapter.set_ch(130)
    show reloj_tic_tac
    show crist1
    show crist2
    show crist3
    show background_pink_blur:
        pause 0.6
        easeout 2.0 alpha 0.7 

    show animation_end_chapter3 zorder 99
    show prota_fade zorder 102
    with Dissolve(.2)   

    show layer master at shake_try(r=12)
    $ renpy.pause(7.5, hard=True)
    stop sound fadeout 1.7
    scene black with Dissolve(.6)
    play sound transition_sound
    pause 0.1
    show layer master
    $ renpy.pause(predict=True)
    jump expression "normal_1_dorkis" 





label normal_0_dorkis:
    scene corridor
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.9:
        show dorki_ grey at pos_t11
    else:
        show dorki_ dorki at pos_t11
    with Dissolve(.2)
    if persistent.chapter_actual > 80 and renpy.random.random() < 0.8:
        play sound glass
        show crist1
        show crist2
        show crist3
    else:
        pass


    if persistent.chapter_actual > 100 and renpy.random.random() < 1.00:
        play sound tos
        show blood_particules zorder 70:
            xalign 0.5
            yalign 0.76
        "....."
        "Aun no..."

    play music bg_dorkis_happy_long
    if persistent.day > 20 and not persistent.chapter_actual > 50:
        do "!Hola, me llamo Dorki, soy repostera de Party Cookie¡"

        mc "Antes de que sigas, tengo que decirte algo."

        show dorki_ normal
        do "¿Que?"

        do "¿Acaso no te convencí?"
    else:
        do "!Hola, me llamo Dorki, soy repostera de Party Cookie¡"

        do "Ya que andabas buscando un club, pensé en invitarte y te ofreciste como todo un desesperado"

        mc "Vaya falsas propuesta..."

        mc "Ni e dicho nada, ademas que lo dijiste todo tu, no yo."

        do "No lo arruines Metz, Ahora mismo andamos desesperado por miembros."

        show dorki_ normal
        do "!Ahora mismo¡, necesitamos de tu gran ayuda."

        show dorki_ sad2
        do "Enserio que andamos pobres."

        mc "Ummm...."

        "Pensándolo sutilmente, encontré una respuesta razonable."

    mc "No."

    # scene coop_dia
    # show choko angry1 at pos_t11
    # with Dissolve(.75)

    show dorki_ lol1
    show layer master at shake_try(r=4)
    do "!¿Por que?¡"

    mc "Obviamente no me uniré en esos clubes cursis de puras chicas."
    show layer master at shake_try(r=2)
    # show choko animation_angry
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.1:
        show screamer:
            pause 0.4
        $ renpy.pause(0.4, hard=True)
        hide screamer
    show dorki_ sad
    do "!P-pero¡{nw=1.5}"

    mc "Ya no se diga mas."

    mc "Me voy a buscar algún otro club que no sea tuyo."
    show dorki_ sad2
    do "!No, por favor, haré lo que sea con tal de que te unas¡"

    show layer master at shake_try(r=5)
    show dorki_ suprise
    if persistent.chapter_actual > 50:
        play sound blood_small1
    mc "!Oye, suéltame¡"

    "Mientras me sostiene del brazo Dorki, solo hago mas fuerza para poder soltarme..."

    show dorki_ lol3
    do "!Por favor{w=2.0}, andamos con poco presupuesto{w=2.0}, ayude a chicas muy indefensas a salvar a los niños con hambre¡"

    mc "¿Que rayos tiene que ver un club de repostería con el hambre mundial?"
    show layer master
    show dorki_ lol1
    do "¿Te convencí?"

    mc "Emm..."
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.5:
        show crist1 
        play sound glass
    mc "No."

    show dorki_ sad
    mc "!Y me voy¡"

    scene black with wipeleft
    "Al caminar de frente con los dientes bien apretados, solo pensé lo molesto que debe ser ese club si hay mas de ella."

    scene corridor 
    with Dissolve(.45)
    "Muy buena decisión miá en no unirme..."

    "Al menos así evito la contaminación de idiotez"
    show black zorder 10
    "!BLOOMM¡"

    "Sentí un golpe fuerte, solo sentí como me caí al piso"

    $ sa_name = "???"
    "Pero al mismo tiempo se a escuchado varias ollas sonando."
    hide black
    show sasha_ angry at pos_t11

    sa "!Ay¡"

    sa "Eso si que dolió"

    show sasha_ normal
    sa "Oh no, ahora tengo que arreglar todo esto."
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.8:
        show crist1 
        show crist2
        play sound glass
    mc "Perdón te..."

    mc "..."

    "Oh dios, es una de las coordinadora de la escuela."

    "Dicen que es cruel como un rey que quiere el trono devuelta."

    "Como el agua y aceite."
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.1:
        show screamer:
            pause 0.4
        $ renpy.pause(0.4, hard=True)
        hide screamer

    mc "Y-Yo realmente, lo siento, no fue mi intención."

    mc "Solo alguien que no conozco..."

    show layer master at shake_try(r=3)
    show sasha_ lol
    sa "No te preocupes, tan solo andaba un poco apresurada, no vi el camino."

    sa "Pero un chico como 'tu', me tiro todo al suelo."
    show sasha_ normal2
    mc "Comprensible."

    mc "Y por que traes tantas ollas encima..."

    mc "¿Te ayudo?."

    show sasha_ confusion
    sa "No gracias, podre sola."

    mc "De acuerdo..."

    scene black with wipeleft
    "Supongo que me salve de la temible coordinadora"

    "Bueno, ¿en que estaba?."

    "!Ah si¡, buscar un club."

    centered "Paso el tiempo. y creo que tuve problemas en buscar club."

    centered "Llego el estrés, ya que no quisiera quedarme atrás por solo no unirme a ese tonto club."

    centered "Por favor, no me obliguen a unirme a ese lugar..."

    scene corridor
    if persistent.chapter_actual > 80 and renpy.random.random() < 1.0:
        play sound glass
        show crist1
        show crist2
        show crist3

    mc "Rayos..."

    mc "Solo miro la pared buscando algún gramo de motivación."

    mc "Y siento que..."

    mc "Viendo la lista de clubes disponibles..."

    mc "Queda{w}, Party Cookie..."

    mc "!Nooo¡."

    "!Por que me castigas de este modo universo¡"

    "Se supone que ahora tengo que unirme con esa gente"

    "No puedo hacer nada ya..."

    "Tengo que..."
    jump jump_choice_game_1

label jump_choice_game_1:
    menu:

        "Rogar para entrar en otro (Suplicar)" if not chapter.get_quantity() > 100:
            "Ya entendí..."
            "Voy a suplicar por unirme alguno."
            "Levanté una falda para demostrar compromiso con mi misión. ¡Ese fue mi error! Ahora soy presidente del país. Pero no me uní al club. ¡Misión cumplida!"
            scene black with Dissolve(.2)
            mc "!Muy bien¡."
            mc "!Aquí voy¡"
            centered "Termine siendo expulsado de la escuela por levantarle la falda a alguien..."
            centered "Fue una estupidez pero..."
            centered "!No me uní al club¡"
            centered "!Lo cual estoy feliz¡"
            jump start

        "Irme a casa, y no tener club... (Perezoso)" if not chapter.get_quantity() > 100:
            "Bueno, adiós a la escuela."
            "Voy a ser rebelde."
            scene black with Dissolve(.2)
            centered "Al final me robaron es a mi por tonto."
            centered "Pero valió la pena cada minuto."
            centered "Y segundo..."
            centered "!Ya que no me uní a ese club¡"
            centered "!Estoy feliz¡"
            jump start

        "Buscar algún melón que tocar (Indignarte)" if chapter.get_quantity() > 15 and not chapter.get_quantity() > 100:
            "Voy a buscar a cualquier para tocar algún melon."
            "Es un poco raro de mi parte pero al menos..."
            "!No me uniré al club¡"
            "!ESTA HECHO¡"
            scene black with Dissolve(.2)
            centered "Al final me expulsaron a mi por pervertido."
            centered "Fue un error de mi. hacer algo tan indecente para no unirme a un club."
            centered "!Pero no me uni¡"
            centered "!Lo cual estoy feliz¡"
            jump start

        "Decir que eres todo un hombre (A lo contrario)" if chapter.get_quantity() > 25 and not chapter.get_quantity() > 100:
            "No hay otra."
            "Toco ir con san pedro para así..."
            "No unirme al club."
            scene black with Dissolve(.2)
            centered "Al final me tire en mis ultimo segundo de pensamiento."
            centered "Al menos... no me uni al club"
            centered "!Lo cual estoy---{nw=1.0}"
            jump start

        "Decir que es guapa Dorki (¿Castigo?)" if chapter.get_quantity() > 30 and not chapter.get_quantity() > 100:
            "No creí tomar esa decisión tan desesperante..."
            "Hasta me sorprendo de mi mismo por tal inesperada idea"
            "Pero prefiero morirme antes que decirle linda a Dorki"
            scene black with Dissolve(.2)
            centered "Eh..."
            centered "!FIN¡"
            jump start

        "??????????????????????" if chapter.get_quantity() > 70:
            "No hay otra."
            jump start

        "??????????????????????" if chapter.get_quantity() > 70:
            "No hay otra."
            jump start

        "??????????????????????" if chapter.get_quantity() > 70:
            "No hay otra."
            jump start




        "Unirme a Party Cookie":
            jump history_end_base





label history_end_base:

    scene black with wipeleft
    "Supongo que no tengo opción..."

    "Debo aceptar la dura realidad de como llegamos."

    "Solo debo seguir, ya no hay mas nada que pueda hacer."

    "¿Que podría hacer para no unirme a ese club tan..."

    "Bueno...{w} mejor me callo y sigo con el hecho."

    "Solo llego al club de Party Cookie."

    "Aun me quedo impresionado por la falta de decisiones que e tomado."

    scene coop_dia with Dissolve(.75)
    "Al abrir la puerta, solo veo en mi alrededor bandejas y platillos."

    "Parece que han cocinado hace poco."

    "Aunque...{w} admito que huele bien el lugar."
    show sasha_ confusion at pos_t11
    if persistent.chapter_actual > 100 and renpy.random.random() < 1.00:
        play sound tos
        show blood_particules zorder 70:
            xalign 0.5
            yalign 0.76
        "...."
        "Yo..."
    sa "Oh, ¿eres tu?"
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.7:
        play music bg_dorki_happy_reverse
        show crist1 
        play sound ambruto
    "Parece que me tope con la misma persona a la que me choque antes."

    mc "¡Hola!, ¿que tal de nuevo?"

    show sasha_ lol
    sa "Aquí ordenando las mesas para comenzar los primeros dias."
    show sasha_ confusion
    sa "Me llamo Sasha, ya que no me he presentado"

    $ sa_name = "Sasha"

    mc "Oh un gusto, yo Metz encantado"

    "Sueno lo mas educado posible para no parecer un puto grosero..."

    show sasha_ normal
    mc "Y bien, que otras actividades hacen aquí"

    mc "Vine para poder unirme."

    show sasha_ normal2
    sa "¿Enserio? ¿te gusta la repostería?"

    mc "Digamos... que me gusta los dulces y quisiera aprender."

    show sasha_ confusion
    sa "Entonces estas en el lugar indicado, se bienvenido al club."

    sa "Deja iré con la presidencia para que te mencionen al club."

    mc "De acuerdo."

    hide sasha_
    "Una lastima que no fuera un club que me guste mas que esto..."

    "No e visto a esa idiota por aquí, al menos..."

    "Mientras andaba pensando un poco... escuche la puerta abriéndose de forma rustica"

    "¿Alguien empujo a la pobre puerta?"
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.5:
        play music bg_dorkis_happy_long 
        play sound ambruto
    show layer master at shake_try(r=4)
    show dorki_ lol1 at pos_t11
    do "¿QUE?"

    do "¿Metz?"

    "Oh no..."

    "Por favor no..."
    show dorki_ dorki

    do "!Veo que te uniste¡"

    do "Eres todo un grande Metz."

    mc "Por favor cállate."

    show dorki_ lol3
    do "No oigo ni un pio insulto de ti. ahora mismo ando pesada de utensilios para el club"

    show dorki_ dorki
    do "!Vaya que me dieron lo mas pesado¡"

    mc "Dios..."
    stop music fadeout 3.0
    "¿Puedo tirarme de un puente?"

    show dorki_ normal
    do "Y bien, ya que parece que te uniste a Party cookie."

    show dorki_ lol1
    do "¿Por que no empezamos por lo bueno?"


label jump_choice_game_2:
    scene black
    with dissolve
    menu:

        "Me voy (Irse del club)" if not chapter.get_quantity() > 100:
            scene coop_dia
            show dorki_ shock at pos_t11
            with Dissolve(.2)
            do "¡Hey, no te vayas!"
            scene black with wipeleft
            "Me fui del club sin mirar atrás."
            "Antes de que el virus de la dorki-idiotez me infectara y empezara a decir '¡Ganbatte!' en cada frase."
            "¡Me fui por fin!"
            centered "¡Lo cual me hace feliz!"
            jump start

        "Tirarse un pedo (Literalmente)" if chapter.get_quantity() > 25 and not chapter.get_quantity() > 100:
            scene coop_dia
            show dorki_ shock at pos_t11
            with Dissolve(.2)
            play sound pedo_flow
            "*PUFFFFF*"
            show dorki_ confusion
            do "¿Qué...?"
            do "....."
            do "¿Esto fue una declaración de guerra?"
            mc "¿Qué?"
            show layer master at shake_try(r=14)
            play sound pedo_flow_long
            show dorki_ jums5
            do "*PUFFFFFFFFFFFFFFFFFFFFFFFFFFFF*"
            mc "¡¿QUÉ ES ESE PODER?!{nw=2.0}"
            scene black
            "Lo olí y morí al instante."
            "Mi alma ascendió, pero no sin antes gritar..."
            centered "¡AL MENOS ME FUI DEL CLUB!"
            jump start

        "Agarras un cuchillo en el acto (Miedo)" if chapter.get_quantity() > 45 and not chapter.get_quantity() > 100:
            scene coop_dia
            show dorki_ confusion at pos_t11
            with Dissolve(.2)
            stop music
            mc "Te voy a matar..."
            play music bg_dorkis_happy_long_reverse
            show dorki_ jums6
            do "¿Que?"
            do "!No espera¡"
            show layer master:
                pos(.5, .8)
                anchor(.5, .5)
                zoom 1.75
            pause .25
            show blood_particules zorder 70:
                xalign 0.5
                yalign 0.7
            play sound blood_small3
            show dorki_ jums4
            do "!AHHHHHHHHHHH¡{nw=1.0}"
            scene black

            "La sangre derrama en mi cara es tan sutil"
            centered "¡AL MENOS ME FUI DEL CLUB POR HOMICIDIO!"
            jump start


        "Responder de forma fría a Dorki (Sublime)" if chapter.get_quantity() > 10 and not chapter.get_quantity() > 100:
            scene coop_dia
            show dorki_ confusion at pos_t11
            with Dissolve(.2)
            mc "Solo eres alguien que pierde el tiempo en esto..."
            show dorki_ sad
            do "Si lo soy, ¿y que pasa?"
            mc "¿Acaso no te importa nada de lo que ocurra?"
            show dorki_ normal
            do "Si me importa, pero con toda sinceridad. no me importa."
            do "Hago lo que hago. y si no te gusta este lugar."
            do "Por que..."
            show dorki_ sad2
            do "Puedo ser yo que te cause esa incomodidad."
            show dorki_ sad
            do "Entonces vete..."
            jump start

        "Romper con Dorki (No son relación, ¿pero como reaccionara?)" if chapter.get_quantity() > 20 and not chapter.get_quantity() > 100:
            scene coop_dia
            show dorki_ confusion at pos_t11
            with Dissolve(.2)
            mc "Terminamos Dorki"
            show dorki_ shock
            do "¿Que?, ¿Terminamos de que?"
            mc "De nuestra... relación."
            do "...."
            show dorki_ lol1
            do "¿Que mierdas andas diciendo?"
            do "¿Teníamos una relación?"
            show dorki_ lol3
            do "!C-C-Cuando ya lo hicimos o como¡"
            "Por favor...{w} dejare pasar esta de una vez."
            centered "!FIN¡"
            jump start


        "??????????????????????" if chapter.get_quantity() > 70:
            "No hay otra."
            jump start

        "??????????????????????" if chapter.get_quantity() > 70:
            "No hay otra."
            jump start

        "??????????????????????" if chapter.get_quantity() > 70:
            "No hay otra."
            jump start


        "¿Hacer alguna idea de como empezar?":
            jump history_end_base2


label history_end_base2:
    scene coop_dia
    show dorki_ normal at pos_t11
    with dissolve
    play music bg_dorkis_happy_long
    if persistent.chapter_actual > 80 and renpy.random.random() < 1.0:
        show layer master:
            matrixcolor SaturationMatrix(0)
        play sound glass
        show crist1
        show crist2
        show crist3
    mc "Podemos seguir ordenando estos utensilios"
    show dorki_ dorki
    do "!Excelente idea¡"

    do "Mientras esperamos a los demás miembros, podemos hablar todo el día"

    "Parece un sufrimiento no verbal..."
    show dorki_ normal
    do "!Sabes¡ pensé que serias un bago que no hace absolutamente nada"

    do "Pero al menos te uniste."

    mc "Ya veo, al menos se que no seré peor que tu."
    show dorki_ sad2
    do "Ta bien, igual puedo ser peor yo."

    mc "Al menos lo aceptas..."

    "Mientras arreglo, parece que alguien entro al club"
    show dorki_ confusion at pos_t31
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.8:
        show sasha_ confusion at pos_t33:
            matrixcolor InvertMatrix(1.0)
    else:
        show sasha_ confusion at pos_t33
    sa "Chicos, esta todo listo"
    show sasha_ happy
    sa "Muchas gracias por unirte Metz."

    sa "Este club sera todo un sueño de la repostería"
    show layer master at shake_try(r=3)
    show dorki_ lol1
    do "!Increíble¡"

    show sasha_ normal2
    sa "Dorki, tu presentaras al club al presidente."

    show dorki_ dorki
    do "!Comprendo¡ la dejare impresionada presidenta."

    show sasha_ confusion
    sa "No se te olvide que tu eres la vicepresidenta, la impresión tuya lo sera todo."
    show dorki_ lol3
    do "Comprendido..."

    show sasha_ happy
    sa "Mientras tanto, los ayudare aquí."

    sa "Ahora mismo no creo que tarden mucho Hector y Lili en llegar."

    "¿Que? hay mas miembros en este lugar"
    show layer master at shake_try(r=2)
    "!BLOOOM¡"

    "Quien golpeo la puerta asi de grosero..."

    $ he_name = "Hector"
    show dorki_ confusion at pos_t31
    show sasha_ normal at pos_t32
    show hector_ normal at pos_t33
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.4:
        stop music
        show hector_ corrupted
        show sasha_ shock
        show dorki_ jums2
        show crist1
        play sound ondes_sound
        he "Hola, buenos Diasssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss{nw}"
        show dorki_ confusion
        show sasha_ normal
        show hector_ normal
        hide crist1
        stop sound
        play music bg_dorkis_happy_long

    he "Hola, buenos Dias"
    mc "Bueno días."
    if persistent.chapter_actual > 100 and renpy.random.random() < 1.00:
        play sound tos
        show blood_particules zorder 70:
            xalign 0.5
            yalign 0.76
        "..."
        "Por que..."
    show dorki_ dorki
    do "!Hola Hector¡"

    do "Sigues siendo frio como siempre"

    he "¿Y tu una tonta sin remedio?"
    show dorki_ lol2
    do "Que halago me has dicho allí."

    he "Algo para recordarte que eres así."
    show dorki_ sad2
    do "Eh..."

    hide sasha_
    hide dorki_
    hide hector_
    "Ya me cae bien este tipo."
    "Y bien, esta persona se llama Hector..."

    "Por su entrada parece alguien mas normal que Dorki."

    "Y no parecen llevarse bien."

    show hector_ normal at pos_t11
    he "Supongo que eres el nuevo, ¿No?"

    mc "Si, me llamo Metz y tu debes ser Hector."

    if persistent.chapter_actual > 50 and renpy.random.random() < 0.7:
        show hector_ shock:
            ease 20 xoffset -800
    else:
        show hector_ normal
    
    he "Exacto, ¿y que te gusto de este club?"
    mc "Bueno...{w} sinceramente no tenia otra opcion."
    show hector_ happy
    he "Somos dos, al final, el club que queria unirme se lleno, ni modo dije yo..."
    he "Y pues entre aqui."
    mc "Vaya..."
    he "Si, solo vengo por hacer pasteles."
    he "Me gustan mucho."

    hide hector_
    "Al menos razón tiene de ir aca..."

    "Otra vez suena la puerta, pero esta vez."

    "Suena suave, que maravilla."

    show lili_ sad2 at pos_t11
    if persistent.chapter_actual > 50 and renpy.random.random() < 0.9:
        show crist1
        show crist3
        play sound glass
    li "Hola a todos."
    show dorki_ dorki at pos_t21
    show lili_ normal at pos_t22
    $ li_name = "Lili"
    do "!Lili, bienvenido de vuelta¡"

    he "Hola."
    show dorki_ lol1
    sa "Lili, que tal, quieres seguir por donde lo dejamos en como hacer donuts."

    show dorki_ sad2
    li "Si."

    show lili_ confusion
    li "¿Oh?, se a unido alguien nuevo."

    hide dorki_
    show lili_ confusion at pos_t11
    mc "Si... ja, me llamo Metz y tu Lili."

    show lili_ normal
    li "Claro, encantada, espero que te sientas cómodo."

    show lili_ lol
    li "Y que Dorki no te ponga loco al principio"

    mc "Gracias la verdad..."

    hide lili_
    "Pensamos igual de que Dorki molesta mucho..."

    show dorki_ dorki at pos_t21
    show hector_ normal at pos_t22
    do "!Bueno Hector, hagamos fuerza en brazo¡"

    he "No voy a tocar tus manos mugrientas."

    show dorki_ sad
    do "Que malo, y eso que soy chica..."

    hide dorki_
    hide hector_ 
    "Parece muy normal este club"

    "Tal vez, me quede."

    "Por esta vez, diré que..."

    "Quisiera unirme a ver su potencial."
    stop music fadeout 1.0

    if chapter.get_quantity() <= 2:
        mc "Pero..."

        "¿Si realmente ir aquí no es el objetivo de todo?"

        "¿Seré yo el que se equivoca que esto es el final?."

        "No..."

        "No es el final, solo es una pizca que no libere."

        "Necesito arreglarlo, lo antes posible."

        "Aunque me cueste la vida."

        "Ya veras...{w} Dorki"


    jump start







# label good_result:
#     do "Si lo tienes, el portavoz de la humanidad fue siempre y siempre sera."

#     do "Nunca nos detuvieron, por esa razón estamos aquí aun."

#     do "Pero bien..."

#     do "Aun así..."

#     do "¿Te unirás al club?"

#     menu:

#         "Si":
#             jump glitch_s

#         "No":
#             jump glitch_s



# label empatic_result:

#     do "Que bien..."

#     $ renpy.quit()




# label glitch_s:

#     do "No sera así"

#     $ renpy.quit()

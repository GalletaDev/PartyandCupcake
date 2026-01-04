label normal_1_dorkis:
    $ persistent.complex_game = True

    play music bg_dorkis_happy fadeout 1.0
    scene corridor
    show dorki_ sad at pos_t11
    with Dissolve(.2)

    mc "No."
    show dorki_ suprise
    show layer master at shake_try(r=6)
    do "!¿Por que?¡"

    mc "Obviamente no me uniré en esos clubes cursis de puras chicas."
    show dorki_ sad
    do "!P-pero¡{nw=1.5}"

    mc "Ya no se diga mas."

    mc "Me voy a buscar algún otro club que no sea tuyo."
    show dorki_ suprise
    do "!No, por favor, haré lo que sea con tal de que te unas¡"

    mc "!Oye, suéltame¡"

    "Mientras me sostiene del brazo Dorki, sentí una sensación un poco diferente..."
    show dorki_ lol3
    do "!Por favor{w=2.0}, andamos con poco presupuesto{w=2.0}, ayude a chicas muy indefensas a salvar a los niños con hambre¡"

    mc "¿Que rayos tiene que ver un club de repostería con el hambre mundial?"
    show dorki_ sad
    do "¿Te convencí?"

    "¿No había visto esto antes?"

    "Mejor no hago nada mas que solo seguir el ritmo..."

    mc "Emm..."
    show dorki_ sad2
    mc "No."

    mc "!Y me voy¡"

    scene black with wipeleft
    "Al caminar de frente con los dientes bien apretados, solo pensé lo molesto que debe ser ese club si hay mas de ella."
    scene corridor with wipeleft
    "Muy buena decisión mía en no unirme..."

    "Al menos así evito la contaminación de idiotez"
    show layer master at shake_try(r=7)
    "!BLOOMM¡"

    "Sentí un golpe fuerte, solo sentí como me caí al piso"

    $ sa_name = "???"
    "Pero al mismo tiempo se a escuchado varias ollas sonando."
    show sasha_ angry at pos_t11
    sa "!Ay¡"

    sa "Eso si que dolió"
    show sasha_ confusion
    sa "Oh no, ahora tengo que arreglar todo esto."

    mc "Perdón te..."
    show sasha_ normal
    mc "..."

    "Oh dios, es una de las coordinadora de la escuela."

    "Dicen que es cruel como un rey que quiere el trono devuelta."

    "Como el agua y aceite."

    mc "Y-Yo realmente, lo siento, no fue mi intención."

    mc "Solo alguien que no conozco..."
    show sasha_ lol
    sa "No te preocupes, tan solo andaba un poco apresurada, no vi el camino."

    mc "Oh, comprensible."
    show sasha_ normal2
    mc "Y por que traes tantas ollas encima..."

    mc "¿Te ayudo?."
    show sasha_ angry
    sa "No gracias, podre sola."

    mc "De acuerdo..."
    scene black with wipeleft
    "Supongo que me salve de la temible coordinadora"

    "Bueno, ¿en que estaba?."

    "!Ah si¡, buscar un club."

    centered "Paso el tiempo. y creo que tuve problemas en buscar club."

    centered "Llego el estrés, ya que no quisiera quedarme atrás por solo no unirme a ese tonto club."

    centered "Por favor, no me obliguen a unirme a ese lugar..."

    scene corridor with wipeleft
    mc "Rayos..."

    mc "Solo miro la pared buscando algún gramo de motivación."

    mc "Y siento que..."

    mc "Viendo la lista de clubes disponibles..."

    mc "Queda{w}, Party and Cupcake..."

    mc "!Nooo¡."

    "!Por que me castigas de este modo universo¡"

    "Se supone que ahora tengo que unirme con esa gente"

    "No puedo hacer nada ya..."

    "Tengo que..."
    jump jump_choice_game_false

label jump_choice_game_false:
    menu:

        "Unirme a Party and Cupcake":
            jump history_end_base_false





label history_end_base_false:

    "Supongo que no tengo opción..."

    "Debo aceptar la dura realidad de como llegamos."

    "Solo debo seguir, ya no hay mas nada que pueda hacer."

    "¿Que podría hacer para no unirme a ese club tan..."

    "Bueno...{w} mejor me callo y sigo con el hecho."

    "Solo llego al club de Party and Cupcake."

    "Aun me quedo impresionado por la falta de decisiones que e tomado."
    scene coop_dia with wipeleft
    "Al abrir la puerta, solo veo en mi alrededor bandejas y platillos."

    "Parece que han cocinado hace poco."

    "Aunque...{w} admito que huele bien el lugar."
    show sasha_ normal at pos_t11
    sa "Oh, ¿eres tu?"

    "Parece que me tope con la misma persona a la que me choque antes."

    mc "¡Hola!, ¿que tal de nuevo?"
    show sasha_ happy
    sa "Ja ja, aquí ordenando las mesas para comenzar los primeros Dias."
    show sasha_ normal
    sa "Me llamo Sasha, ya que no me he presentado"

    $ sa_name = "Sasha"

    mc "Oh un gusto, yo Metz encantado"
    
    "Sueno lo mas educado posible para no parecer un puto grosero..."

    mc "Y bien, que otras actividades hacen aquí"

    mc "Vine para poder unirme."
    show sasha_ confusion
    sa "¿Enserio? ¿te gusta la repostería?"

    mc "Digamos... que me gusta los dulces y quisiera aprender."
    show sasha_ normal
    sa "Entonces estas en el lugar indicado, se bienvenido al club."

    sa "Deja ire con la presidencia para que te mencionen al club."

    mc "De acuerdo."
    hide sasha_
    "Una lastima que no fuera un club que me guste mas que esto..."

    "No e visto a esa idiota por aquí, al menos..."

    "Mientras andaba pensando un poco... escuche la puerta abriéndose de forma rustica"

    "¿Alguien empujo a la pobre puerta?"
    show dorki_ suprise at pos_t11
    do "¿QUE?"

    do "¿Metz?"

    "Oh no..."

    "Por favor no..."
    show dorki_ dorki
    do "!Veo que te uniste¡"

    do "Eres todo un grande Metz."

    mc "...."
    show dorki_ normal
    do "Oh, y ese silencio, primera vez que no me insultas"

    mc "Por nada..."
    show dorki_ confusion
    do "El fin."

    show dorki_ lol1
    do "!Vaya que me dieron lo mas pesado¡"

    mc "Dios..."

    "¿Puedo tirarme de un puente?"
    show dorki_ normal
    do "Y bien, ya que parece que te uniste a Party and Cupcake."

    show dorki_ dorki
    do "¿Por que no empezamos por lo bueno?"
    
    jump jump_choice_game_2_false


label jump_choice_game_2_false:
    menu:

        "¿Hacer alguna idea de como empezar?":
            jump history_end_base2_false


label history_end_base2_false:
    stop music fadeout 2.0
    mc "Podemos seguir ordenando estos utensilios que traites"

    show dorki_ dorki2
    do "!Excelente idea¡"

    do "Mientras esperamos a los demás miembros, podemos hablar todo el dia"

    "Parece un sufrimiento no verbal..."
    play music bg_dorkis_happy_long
    show dorki_ confusion
    do "!Sabes¡ pense que serias un bago que no hace absolutamente nada"
    show dorki_ dorki2
    do "Pero al menos te uniste."

    mc "Ya veo, al menos se que no sere peor que tu."
    show dorki_ sad2
    do "Ta bien, igual puedo ser peor yo."
    
    mc "Al menos lo aceptas..."
    hide dorki_
    "Mientras arreglo, parece que alguien entro al club"
    show sasha_ normal at pos_t11
    sa "!Chicos, esta todo listo¡"
    show sasha_ happy
    sa "Muchas gracias por unirte Metz."

    sa "Este club sera todo un sueño de la repostería"
    show sasha_ happy at pos_t21
    show dorki_ dorki at pos_t22
    do "!Increíble¡"

    sa "Dorki, tu presentaras al club al presidente."
    show dorki_ lol1
    do "!Comprendo¡ la dejare impresionada presidenta."
    show sasha_ angry
    sa "No se te olvide que tu eres la vicepresidenta, la impresión tuya lo sera todo."
    show dorki_ normal
    do "Comprendido."
    hide dorki_
    show sasha_ angry at pos_t11
    sa "Mientras tanto, los ayudare aquí."

    sa "Ahora mismo no creo que tarden mucho Hector y Lili en llegar."
    hide sasha_
    "¿Que? hay mas miembros en este lugar"
    show layer master at shake_try(r=7)
    "!BLOOOM¡"

    "Quien golpeo la puerta asi de grosero..."

    $ he_name = "Hector"
    show hector_ normal at pos_t11
    he "Hola, buenos Dias"

    mc "Bueno Dias."
    show hector_ normal at pos_t21
    show dorki_ dorki2 at pos_t22
    do "!Hola Hector¡"

    do "Sigues siendo frio como siempre"
    show hector_ confusion
    he "¿Y tu una tonta sin remedio?"
    show dorki_ lol3
    do "Que halago me has dicho allí."
    show hector_ happy
    he "Algo para recordarte que eres asi."
    show dorki_ lol1
    do "Eh..."
    hide dorki_
    "Ya me cae bien este tipo."
    show hector_ normal at pos_t11
    "Y bien, esta persona se llama Hector..."

    "Por su entrada parece alguien mas normal que Dorki."

    "Y no parecen llevarse bien."
    show hector_ confusion
    he "Supongo que eres el nuevo, ¿No?"

    mc "Si, me llamo Metz y tu debes ser Hector."
    show hector_ happy
    he "Si, solo vengo por hacer pasteles."
    he "Me gustan mucho."

    "Al menos razón tiene de ir aca..."
    hide hector_
    "Otra vez suena la puerta, pero esta vez."
    
    "Suena suave, que maravilla."
    show lili_ normal at pos_t11
    li "Hola a todos."
    show lili_ normal at pos_t21
    show dorki_ dorki at pos_t22
    $ li_name = "Lili"
    do "!Lili, bienvenido de vuelta¡"
    show lili_ normal at pos_t31
    show dorki_ dorki at pos_t32
    show hector_ happy at pos_t33
    he "Hola."
    show lili_ normal at pos_t41
    show dorki_ dorki at pos_t42
    show hector_ happy at pos_t43
    show sasha_ happy at pos_t44

    sa "Lili, que tal, quieres seguir por donde lo dejamos en como hacer donuts."
    show lili_ lol

    li "Si."
    hide dorki_ 
    hide sasha_
    hide hector_
    show lili_ confusion at pos_t11
    li "¿Oh?, se a unido alguien nuevo."

    mc "Si... ja, me llamo Metz y tu Lili."
    show lili_ sad2
    li "Claro, encantada, espero que te sientas cómodo."

    mc "Ya veo, gracias."
    hide lili_
    show dorki_ lol1 at pos_t21
    show hector_ normal at pos_t22
    do "!Bueno Hector, hagamos fuerza en brazo¡"
    show hector_ confusion
    he "No voy a tocar tus manos mugrientas."
    show dorki_ sad2
    do "Que malo, y eso que soy chica..."
    hide dorki_
    hide hector_
    "Sea chica o no, es importante ser pulcro..."

    "Parece muy normal este club"

    "Tal vez, me quede."

    "Por esta vez, dire que..."
    
    "Quisiera unirme a ver su potencial."
    show dorki_ dorki at pos_t11
    mc "Oye, Dorki."
    show dorki_ normal
    do "¿Si?."

    mc "Bienvenida a Party and Cupcake."
    show dorki_ lol1
    do "¿Eh?, no me había unido ya, jaja."

    do "Que cosas dices."

    mc "Si... digo cosas."
    show dorki_ normal
    mc "Tonta..."

    mc "En ese caso, ¿como se supone que hacemos el festival?"
    show dorki_ normal at pos_t21
    show hector_ normal at pos_t22
    he "Diría yo que..."
    show hector_ happy

    he "Solo hay que ser bastantes postres...{w} hasta que el hambre de los invitados este satisfecha."
    show dorki_ confusion at pos_t31
    show hector_ normal at pos_t32
    show sasha_ angry at pos_t33
    sa "No necesariamente debe ser eso, seria algo como..."

    sa "Una grandiosa presentación, eso es lo que no falta."
    show dorki_ suprise
    do "Y eso acaso ayuda en algo..."
    show dorki_ confusion at pos_t41
    show hector_ normal at pos_t42
    show sasha_ angry at pos_t43
    show lili_ normal at pos_t44
    li "Si ayuda mucho."
    show lili_ confusion
    li "Obviamente teniendo una presentación bastante buena, lleva al club a la fama de la escuela."
    show sasha_ normal
    sa "Ni tanto a esos extremos..."

    mc "¿Por que no?"
    show sasha_ angry
    sa "Oh."
    show dorki_ normal
    show hector_ confusion
    he "¿Tienes una mejor idea?"

    mc "Si."

    mc "Dorki, por que no presentas al club con tus palabras."
    show dorki_ lol1
    do "¿Yo?"

    show lili_ lol
    show hector_ confusion
    show dorki_ sad
    li "¿Estas seguro que sea Dorki?"

    he "Ella ni si quiera sabe invitar a miembros y va a presentar al club."
    show sasha_ angry
    sa "No lo se Metz... es un poco mas lejos de lo que dices..."

    mc "Yo confió en ella..."

    mc "Les aseguro que no decepcionara con ello."

    sa "...."
    show sasha_ sad
    sa "Apenas te unes y das una propuesta muy grande."
    show lili_ confusion
    show hector_ normal 
    show dorki_ dorki
    do "Puedo hacerlo."
    show dorki_ lol3
    do "Aunque no me vean capaz, tiene razón Hector, nunca invite algún miembro aquí."
    show dorki_ sad
    do "Denme una oportunidad"
    hide dorki_
    show lili_ sad2 at pos_t33
    show hector_ confusion at pos_t31
    show sasha_ happy at pos_t32
    "Todos miran a Dorki con confusión, ¿confiar en su palabra?"

    "Pero, Sasha se siente muy feliz y LiLi también."

    "Hector es el único que esta confuso"
    hide hector_
    hide lili_
    hide sasha_
    show dorki_ sad at pos_t11
    mc "Tu puedes Dorki, confiamos en ti."

    do "...."
    show dorki_ dorki2
    do "Esta bien, no los defraudare chicos."
    scene black with Dissolve(2)
    centered "Solo nos preparamos hasta el final"

    centered "Con esfuerzo y valor en nuestros corazones, vimos una oportunidad para ser conocidos."

    centered "Recuerdo los momentos malos de la realidad y momentos donde ya el fin se acerco"

    centered "Pero eso no me hizo no querer vivir, si no, ver lo que realmente el mundo quiere demostrar."

    centered "Y ahora..."

    centered "Llego el ultimo día para presentarnos"

    "Ya preparado todo, no falta mucho que el presidente de los clubes venga"

    "Veo a Dorki muy nerviosa a pesar de lo que practico."

    mc "¿Estas bien?"
    show dorki_ sad at pos_t11
    do "Si, solo, quisiera no fallar sabes Metz."

    mc "Nee..."

    mc "No pasa nada, solo se Dorki."

    do "...."
    show dorki_ dorki
    stop music fadeout 1.5
    do "Eso haré"
    scene black 

    with Dissolve(3)
    $ quick_menu = False
    play music "audio/bg_dorkis_end.ogg"
    call screen credist_folder()

    scene black
    with Dissolve(.45)
    stop music
    return






screen credist_folder():

    zorder 10

    default count = 0

    add "reloj_tic_tac"
    add "prota_fade"
    add "black" at Transform(alpha=0.75)
    add "cubes_red_background" at shake_slayer(ts=4.0)

    vbox:
        align(.5, .5)
        if count == 0:
            text "{color=#fff}🧁Party and Cupcake🧁" at Transform(zoom=1.5)
        elif count == 1:
            text "{color=#fff}Developed by GalletaDev"
        elif count == 2:
            text "{color=#fff}Art/programming/music by GalletaDev"
        elif count == 3:
            text "{color=#fff}Sound/Video reloj_tic_tac Pixabay.com"
        else:
            text _("Gracias por jugar <3")
            timer 35 action Return(True)

    textbutton "Skip":
        at Transform(zoom=1.5)
        align(.9, .75)
        action Return(True)


    timer 20 action SetLocalVariable("count", count + 1) repeat True


    # la historia real....

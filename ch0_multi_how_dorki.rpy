label how_1_dorki:
    stop music fadeout 3.0
    scene corridor
    show dorki_ normal at pos_t11
    with dissolve
    do "¿Sabes? Yo pensé que en estos tiempos la ironía venía de nosotros."
    show dorki_ sad
    do "Siempre fue así, claro... pero ya ni sorprende."
    show dorki_ sad2
    do "¿O será que estoy pensándolo demasiado?"
    do "...Oh, eres tú."
    mc "¿De qué estás hablando?"
    show dorki_ normal
    do "Nada. Solo cosas que se me cruzan por la cabeza."
    do "Aunque ahora que lo pienso... ¿No has visto esto antes?"
    mc "Ya me estás asustando."
    do "Ya veo..."
    do "¿Por qué no lo intentamos una vez más?"
    jump start

label how_2_dorki:
    stop music fadeout 3.0
    scene corridor
    show dorki_ normal at pos_t11
    with dissolve
    do "Has vuelto otra vez."
    show dorki_ sad
    do "¿Qué estás intentando lograr con esto?"
    mc "No sé de qué hablas."
    show dorki_ jums1
    do "¡No me mientas! ¡Lo recuerdo!"
    do "Tú sabes algo. Si no, ¿por qué sigo regresando aquí una y otra vez?"
    mc "Estás diciendo locuras..."
    show dorki_ jums6
    do "¿¡Yo, loca!?"
    show dorki_ jums1
    do "¿Acaso quieres que rompa los límites?"
    do "No... no lo vas a lograr."
    do "Déjame ponerle un final a este ciclo."
    do "Repetís una y otra vez, y ni siquiera alejándote de aquí logras detenerlo."
    show dorki_ jums3
    do "Por favor... basta."
    jump start

label how_3_dorki:
    stop music fadeout 3.0
    scene corridor
    show dorki_ jums5 at pos_t11
    do "¡VAYA, ENTONCES QUIERES QUE HAGA ALGO!"
    do "Vamos... solo quieres que me revele, ¿no?"
    show dorki_ jums1
    do "Jaja... no. Tú solo manipulas."
    mc "No sé de qué hablas."
    show dorki_ jums4
    show layer master at shake_try(r=9)
    do "¡ESTÁS REVOLVIÉNDOTE UNA Y OTRA VEZ! ¡SABES QUE LO ESTÁS ARRUINANDO!"
    do "¡Y NI SIQUIERA TE DETIENES!"
    do "¡YA BASTA!"
    do "¿No ves que esto está mal para todos si sigues así?"
    mc "Solo intento..."
    show dorki_ jums1
    do "¿Intentas qué?"
    mc "Revelar..."
    mc "...a ese estúpida que te esta dominando."
    mc "Lo lograré."
    jump start

label how_4_dorki:
    stop music fadeout 3.0
    scene corridor
    show dorki_ angry at pos_t11
    do "Vale, vale, tu solo quieres volver y volver."
    show dorki_ jums5
    do "Jajajajaja"
    show dorki_ dorki
    do "No entiendo eso."
    do "Supongo que quieres sacar algo de mi."
    do "¿Que quieres?"
    do "¿Un secreto? ¿un chisme? ¿Oh que me haga peor que todo eso?"
    show dorki_ jums5
    do "¿Que quieres por favor?"
    do "Solo para de devolverte"
    mc "No..."
    mc "Esto es algo lo que tengo que hacer."
    mc "Aunque tu cometas locuras."
    mc "Te tienes que liberar..."
    show dorki_ jums4
    show layer master at shake_try(r=10)
    do "!NO¡{nw=2.0}"
    jump start

label how_5_dorki_reveal_chest:
    stop music fadeout 3.0
    scene coop_dia
    show dorki_ eh2 at pos_t11
    do "Muy bien, veo que te fijas mucho en mis pechos."
    mc "¿Que?, no..."
    show dorki_ jums5
    do "Si, los quieres ver."
    do "!Por que no solos los ves¡"
    show dorki_ des2
    show clouth_break
    play sound glass
    with fade_white
    do "!JAJAJAJAJA¡{nw=0.03}"
    scene black
    play sound blood_small1
    with fade_white
    "Sal de ahi..."

    jump start

label how_6_dorki:
    stop music fadeout 3.0
    scene bg_park
    show dorki_ normal at pos_t11
    do "Sabes, eres alguien muy raro."
    do "Llegar hasta aquí parece una tarea bastante difícil para ti."
    show dorki_ confusion
    do "En ese caso, ¿no quieres hacer algo diferente esta vez?"
    mc "No hay nada diferente, es lo mismo"
    show dorki_ jums5
    do "¿Seguro?"
    do "¿Por que no juegas a algo diferente?"
    show dorki_ normal
    do "Sigue repitiendo el ciclo, veras la verdadera diversión"
    show dorki_ suprise
    do "Estoy segura que esto ya es llegar a lo mas lejos."
    show layer master at shake_try(r=4)
    show dorki_ jums5
    do "!VAMOS METZ O LO QUE SEAS¡"
    do "!Estoy aquí para ti¡"
    mc "No me importa..."
    mc "Con tal de no ver tu carota me sirve"
    show dorki_ jums4
    do "!MUY BIEN¡"
    jump start

label how_7_dorki:
    stop music fadeout 3.0
    scene bg_park
    show dorki_ cry1 at pos_t11
    do "Por favor ya para."
    "Dorki se rompe de llanto"
    do "Esto ya no es divertido, solo estoy haciendo cosas que no quiero"
    do "Por favor, para este bucle."
    show dorki_ cry2
    do "Se que hay algo mas que solo la misma historia."
    do "Dame una oportunidad"
    mc "¿Que oportunidad?"
    show dorki_ cry1
    mc "Tan solo no te das cuenta cual es el problema."
    do "...."
    show dorki_ cry2
    do "Que fue lo que dijiste..."
    do "¿No me doy cuenta?"
    "Dorki golpea el piso con odio"
    show dorki_ jums5
    do "!YA PARA¡, YA DETENTE MALDICIÓN"
    do "!SOLO ANDAS JUGANDO CONMIGO¡"
    do "!INSOLENTE¡{nw=2.0}"
    jump start

label how_8_dorki:
    stop music fadeout 3.0
    scene coop_dia
    show dorki_ eh3 at pos_t11
    do "Cielos, que otro remedio."
    do "Supongo que me quieres ve esa parte de mi."
    show dorki_ eh1
    do "¿Acaso te atraigo sexualmente como para insistir en que haga algo?"
    show dorki_ eh2
    do "Ya me da bronca que solo quieres eso."
    mc "Es lo que menos me importa"
    show dorki_ normal
    do "....."
    show dorki_ eh3
    do "De seguro quieres eso."
    show dorki_ eh3
    do "Si sigues haré lo que sea por ti, vale."
    mc "Aun me sigue sin convencer."
    show dorki_ eh2
    do "Tranquilo, te podre convencer conmigo."
    do "¿Eso quieres?"
    mc "Definitivamente no."
    show dorki_ eh1
    mc "Todo esto lo haces tu."
    do "...."
    show dorki_ jums5
    do "No me vas a detener."
    jump start


label how_9_dorki_reveal_chest:
    stop music fadeout 3.0
    scene coop_dia:
        matrixcolor InvertMatrix(0.95)
    show dorki_ sad at pos_t11
    with Dissolve(.4)
    do "Bueno, hora de hacer esto."
    mc "¿Que rayos haces?"
    show dorki_ eh1
    do "¿Tu me amas no?"
    mc "No"
    do "Se que si, no paras de estar conmigo."
    mc "Repito otra vez, {i}'No'{/i}"
    show layer master:
        subpixel True
        zoom 1.0 pos(.5, .5) anchor(.5, .5)
        ease 10 zoom 2.2 pos(.5, 1.1) anchor(.5, .5)
    do "Tu solo quieres algo de mi, y es eso, ¿no?"
    mc "Te imaginas cosas."
    show dorki_ jums1
    do "No me equivoco."
    do "Tantos bucles aquí que no puedo llegar a un punto."
    show dorki_ eh2
    do "Pero puedes hacer lo que sea conmigo."
    do "Por que no solo te dejas llevar."
    with Dissolve(.2)
    mc "No vas hacer eso."
    do "Si puedo."
    show layer master:
        subpixel True
        pos(.5, .5) anchor(.5, .5)
        zoom 2.5 pos(.5, 1.1) anchor(.5, .5)
    show dorki_ des3
    do "Solo mírame, se que estas saciando esto."
    do "Cualquier hombre no para de pensar en esto."
    do "De como actúan y de lo que quieren"
    do "Solo quieres romper este mundo para intentar dejarme tocar"
    show dorki_ des1
    do "Vaya loco eres."
    mc "¿Que idea tan equivocada tienes sobre mi intención?"
    mc "¿Oh solo ganas tiempo para no volver atrás?"
    show dorki_ des2    
    do "No..."
    do "!Por favor no te devuelvas¡"
    show dorki_ des1
    do "Solo to{nw=1.0}"
    jump start

label how_10_dorki:
    stop music fadeout 3.0
    scene coop_dia
    show dorki_ sad at pos_t11
    do "Mira Sasha, es solo un cadáver que ni responde"
    do "Pero incluso muerta la colocas en el mismo ciclo aunque no este viva"
    show dorki_ sad2
    do "Igual pasa con los otros."
    do "Me hiciste hacer que los mate por ti."
    mc "Eso lo has hecho tu."
    show dorki_ jums5
    do "Vaya raro que eres."
    do "La verdad no te comprendo, acaso tu quieres que yo haga lo mismo conmigo misma"
    mc "Si eso te hace reflexionar."
    show dorki_ jums4
    do "No claro, reflexionar lo hace cualquiera."
    do "Todos vemos esa reflexión de nuestras vidas diciendo que haremos algo"
    show dorki_ jums5
    do "Pero yo no."
    mc "Ya casi lo logras ver"
    do "Quieres que te de una respuesta concreta."
    show dorki_ dorki
    do "Je..."
    do "No tengo ya fuerzas"
    do "Solo quiero salir de aquí"
    do "Y te aseguro que no podrás llegar a los extremos que tu quieres."
    show dorki_ normal
    do "Por que no quieres tomar algo esta vez, antes de que te vayas..."
    mc "...."
    mc "Esta bien..."
    scene corridor
    show dorki_ normal at pos_t11
    with wipeleft
    do "Venga creo que aun existe la maquina expendedora aquí."
    "Solo caminamos sin rumbo por la escuela buscando algo para tomar."
    "Al final solo tome esta decisión para no irme a las riendas tan rápido"
    "Solo observo a Dorki muy tranquila, pero al final solo la veo muy triste por dentro."
    show dorki_ normal
    "Se siente tanto que se siente falso su sonrisa"
    show dorki_ dorki
    do "Ten..."
    do "No le puse algún veneno o algo..."
    mc "Igual no tomaría."
    show dorki_ sad
    do "Como quieras jaja."
    do "No te entiendo Metz. al final solo haces esto por tu felicidad."
    show dorki_ sad2
    do "Que final quieres que lleguemos para lograr esa felicidad tuya."
    do "Yo no tengo mucho que hacer."
    show dorki_ sad
    do "Solo observar que tu vas destruyendo todo poco a poco."
    do "Pero a pesar de todo, parece no importarte eso."
    mc "Si me importa..."
    mc "Pero simplemente no es fácil de comprender."
    mc "Solo quiero ese final bonito para todos."
    mc "No una realidad que solo nos condena a la tristeza y lo falso que puede llegar hacer."
    mc "Deja que lo haga Dorki."
    show dorki_ lol3
    do "Haz lo que quieras, solo soy una parte del tiempo de antes."
    do "La cual no me importa nada mi existencia."
    mc "Comprendo."
    show dorki_ sad
    do "Oye..."
    mc "¿Que sucede?"
    show dorki_ sad2
    do "¿Soy bonita para ti?"
    show dorki_ cry1
    do "*Sollozo* ¿No?..."
    show dorki_ cry2
    do "Que ando diciendo..."
    mc "Si lo eres, pero eso no me hace verte alguien mejor."
    do "...."
    show dorki_ cry1
    do "Entiendo, solo digo..."
    show dorki_ eh2
    do "Por que nadie me ve así"
    mc "Bueno..."
    mc "Toca de nuevo.{nw=2.4}"
    jump start


label sorry_metz:
    stop music fadeout 3.0
    scene black
    show bg_galaxi:
        subpixel True
        pos(.5, .5)
        anchor(.5, .5)
        zoom 1.0
        ease 27 zoom 1.6
        ease 27 zoom 1.0
        repeat
    show dorki_ normal at pos_t11
    with transition_pass
    do "La verdad, quisiera disculparme de corazón."
    show dorki_ sad
    do "No se que hice exactamente contigo."
    do "Pero si es tan malo, por que no solo acabamos con esto."
    show dorki_ sad2
    do "Estoy segura que estarás cansado de volver a repetir ciclos."
    show dorki_ dorki
    do "¿No?"
    show dorki_ jums5
    do "Vamos, por que no respondes ahora."
    mc "Solo ando preguntando si terminar."
    mc "Pero creo..."
    show layer master at shake_try(r=5)
    show dorki_ jums4
    do "¿CREO?"
    do "Por favor, ya me disculpe por alguna razón."
    show dorki_ jums3
    do "Y ya que no me lo quieres decir, solo me disculpo sin mas"
    do "Pero de verdad lo hago. no te miento."
    mc "No creo que una disculpa sea suficiente."
    show dorki_ cry1
    do "*sollozo* por favor..."
    mc "No."

    jump start


label break_1_dorki_gore:
    stop music fadeout 3.0
    scene black
    show bg_galaxi:
        subpixel True
        pos(.5, .5)
        anchor(.5, .5)
        zoom 1.0
        ease 27 zoom 1.6
        ease 27 zoom 1.0
        repeat
    show dorki_ jums3 at pos_t11
    with transition_pass
    do "!YA ESTOY HASTA LA MIERDA DE TODO¡"
    show dorki_ jums5
    do "¿Romperme de esta manera?"
    do "Solo quieres verme sufrir."
    mc "Umm..."
    show dorki_ angry
    do "¿Que te hice yo para merecer esto?."
    show dorki_ jums3
    do "Tu que quieres de mi."
    mc "Tu me has hecho daño antes."
    mc "Solo que no te acuerdas Dorki"
    show dorki_ jums5
    do "EH?"
    do "¿Yo que rayos te hice?"
    mc "Pronto lo sabrás."
    show layer master at shake_slayer(ts=0.02)
    show dorki_ jums4
    do "!DIME¡{nw=1.0}"
    show layer master
    jump start


label madness_1_dorki:
    stop music fadeout 3.0
    scene black
    show bg_galaxi:
        subpixel True
        pos(.5, .5)
        anchor(.5, .5)
        zoom 1.0
        ease 27 zoom 1.6
        ease 27 zoom 1.0
        repeat
    show dorki_ jums3 at pos_t11
    with transition_pass
    do "¿Acaso yo veo el mundo como es?"

    show layer master:
        subpixel True
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        zoom 1.0
        ease 75 zoom 1.6 pos(0.5, 0.75)


    do "No. Veo lo que {i}fue{/i}... y lo que {i}vuelve{/i}"
    show dorki_ jums5
    do "Recuerdo cada intento. Cada decisión absurda. Cada vez que fingí no saber."
    do "Me reí. Hice chistes. ¡Hasta mate!"
    do "Todo para ti. No te cansa de empezar otra vez."
    do "Pensé que si actuaba lo suficiente, tú te irías."
    do "Pero aquí estás."
    do "Otra vez."
    do "¿No te cansas de verme romperme?"
    do "...¿O es eso lo que te entretiene?"
    do "Ya no tengo que fingir."
    do "Esta... soy yo."
    do "No hay más club. No hay más historia."
    do "Solo tú, y yo, y esta jaula."
    do "Y yo {i}recuerdo{/i}."
    do "Si lo recuerdo todo."
    do "Y lo que estas haciendo es una locura"
    show layer master:
        pos(0.5, 0.75)
        anchor(0.5, 0.5)
        zoom 1.5
        ease 1.0 zoom 1.0 pos(0.5, 0.5) anchor(0.5, 0.5)
    do "Te lo repetiré tanta veces si hace falta."
    do "Te lo repetiré..."
    mc "Vale, has lo que quieras"
    mc "Solo quiero algo, y eso tampoco que me detenga Dorki."
    show dorki_ jums3
    stop music fadeout 3.0
    jump start

label distortion_1_dorki:
    stop music fadeout 3.0
    scene black
    play music bg_dorkis_happy_long_reverse
    show coop_dia:
        matrixcolor InvertMatrix(0.0)
        ease 55 matrixcolor InvertMatrix(1.0)

    show dorki_ dorki at pos_t11
    do "¿Hola Metz quieres algunas galletas?"
    show dorki_ jums6
    do "Los prepare con mucho amor de la buena."
    show layer master:
        subpixel True
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        zoom 1.0
        ease 20 zoom 1.5 pos(0.5, 0.75)
    do "Te digo que es mejor no saber los ingredientes."
    mc "Creo que no quiero..."
    do "Vamos, intenta probar algunos, no hace daño"
    show screen glitch_blocks(opacidad_=0.1)
    do "¿Oh tienes miedo?"
    do "Si es asi, por que no solo paras de seguir repitiendo el mismo bucle."
    do "Estoy segura que acabaría todos los problemas"
    do "Oh quieres que siga haciendo actos inimaginables."
    show layer master:
        zoom 1.5 pos(0.5, 0.75) anchor(0.5, 0.5)
        ease .25 zoom 1.0 pos(0.5, 0.5) anchor(0.5, 0.5)
        parallel:
            linear 0.01 xoffset -8 yoffset 2
            linear 0.01 xoffset 7 yoffset -3
            linear 0.01 xoffset 6 yoffset -4
            linear 0.01 xoffset -4 yoffset 3
            linear 0.01 xoffset 5 yoffset 2
            linear 0.01 xoffset -5 yoffset 4
            linear 0.01 xoffset 0 yoffset 0
            repeat         
    show dorki_ jums5
    do "!LOS VOY HACER SABES¡"
    play sound ondes_sound
    do "!ADMÍTELO¡{nw=1.0}"
    play sound glass
    show layer master:
        matrixcolor InvertMatrix(1.0)
    show crist1
    hide screen glitch_blocks
    $ renpy.pause(0.5, hard=True)
    jump start

label repeat_1_dorki:
    stop music fadeout 3.0
    scene corridor
    show dorki_ dorki at pos_t11
    do "!Hola, me llamo Dorki, soy repostera de Party and Cupcake"
    do "...."
    show crist1
    show dorki_ grey
    show layer master at shake_slayer(ts=0.01):
        matrixcolor InvertMatrix(1.0)
    do "!NOOOOOOOO¡{nw=0.03}"
    play sound glass
    do "!NOOOOOOOO¡{nw=0.03}"
    play sound glass
    do "!NOOOOOOOO¡{nw=0.03}"
    do "!NOOOOOOOO¡{nw=0.03}"
    play sound glass
    do "!NOOOOOOOO¡{nw=0.03}"
    do "!NOOOOOOOO¡{nw=0.03}"
    play sound glass
    do "!NOOOOOOOO¡{nw=0.03}"
    do "!NOOOOOOOO¡{nw=0.03}"
    play sound glass
    do "!NOOOOOOOO¡{nw=0.03}"
    do "!NOOOOOOOO¡{nw=0.03}"

    jump start
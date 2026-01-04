label talk_1_dorki:
    scene bg_park with Dissolve(.75)
    "Andamos afuera de casa, mientras tanto veo el sol mas brillante que antes."
    "Espero no incomodar a Dorki"
    show dorki_ confusion at pos_t11
    do "¿Oye, no has hecho algo últimamente?"
    mc "No realmente, solo he estado pensando en cómo será el futuro, nada más."
    show dorki_ dorki
    do "Ya veo..."
    do "Yo ahora mismo pienso mucho en eso."
    mc "¿Por que?"
    show dorki_ sad2
    do "Es que, mis padres se van a divorciar mañana."
    mc "Ohu..."
    do "Si..."
    show dorki_ sad
    do "A veces la vida apesta, cosas inesperadas te llegan a pesar de no desearlas."
    do "Trato de no pensarlo mucho, ¿sabes?"
    mc "Comprendo."
    mc "Entonces, yo te apoyo Dorki. no estas sola."
    show dorki_ normal
    do "....."
    show dorki_ cry1
    do "Gracias Metz."
    scene black with Dissolve(.25)
    "No se que haría si no contara con Dorki"
    jump start

label talk_2_dorki:
    "Mientras tanto en el salón de clases, espero a los demás miembros."
    "Yo ahora mismo ando preparando donuts para el club."
    "Tarde un rato... pero de seguro les gustara."
    scene coop_dia with dissolve
    $ sa_name = "Sasha"
    $ he_name = "Hector"
    show sasha_ happy at pos_t11
    sa "Que tal señor vicepresidente."
    sa "Aun andas preparando esos donuts bien perfectos."
    mc "Obviamente, solo añado unos toques mas, así quedaran geniales."
    show sasha_ normal
    sa "Espero que sea así."
    hide sasha_
    "Sasha se va del salón, supongo que va a buscar mas ingredientes para los otros postres"
    "Escucho a Sasha diciendo hola a alguien, sera ¿Hector o Lili?"
    show hector_ normal at pos_t11
    he "Hola, buenos días."
    mc "Que tal Hector, ¿te lo pasa de bomba?"
    show hector_ sad
    he "Ya quisiera, el examen de hoy si fue difícil, a pesar que estudie, pero al menos saque excelente"
    mc "Por los pelos, jaja."
    he "Ni modo, era eso o reprobar."
    mc "¿No has visto a Lili?."
    show hector_ normal
    he "La verdad no, anda desaparecida últimamente."
    mc "De seguro anda ocupada por algunos preparativos de su clase."
    show hector_ happy
    he "Puede ser cierto."
    hide hector_
    "Parece que otra vez la puerta hace ruido."
    "Me pregunto que sera esta vez."
    show dorki_ sad at pos_t11
    do "¿Hola?"
    mc "Oh, Dorki."
    jump start

label talk_3_dorki_gore:
    scene coop_dia 
    show dorki_ sad at pos_t11
    with dissolve
    mc "Dorki, ¿que haces aquí?"
    show dorki_ dorki
    do "Solo quería visitarte, ¿no puedo?"
    mc "Si pero... ahora mismo ando ocupado preparando postres para el club."
    show dorki_ confusion
    do "Ya veo."
    show dorki_ dorki
    do "¿Que tal si me uno?"
    mc "Eso..."
    mc "No es necesario si no quieres."
    show dorki_ suprise
    do "No, yo si quiero, donde firmo."
    mc "Dorki, se que es mucho pedir, pero por ahora no creo que necesitemos..."
    show dorki_ normal
    mc "...a nadie más."
    show dorki_ sad
    do "¿...?"
    show dorki_ sad2
    do "No quieres que me una. y-y eso de la nada."
    mc "Solo..."
    mc "No se..."
    show dorki_ cry2
    do "...."
    do "Ya comprendo, tu me has dicho que te gusta alguien, ¿no?"
    mc "¿Que?, mencione eso..."
    show dorki_ cry1
    do "Andas raro ya, no eres así en lo absoluto."
    "Dorki se seca las lagrimas"
    show dorki_ jums3
    do "Yo quería unirme, pero tu intentas o quieres que no me una."
    do "De seguro alguien del club te gusta. para no meterme todo el tiempo, quieres que no me una."
    mc "¿Podemos dejar el tema?"
    show dorki_ jums2
    do "No seas un tonto."
    do "Y yo pensando que eras alguien bastante amable, pero veo que solo busca relación, que al final, no se sabe si sera bueno."
    mc "¿Que sabrás tu?"
    show dorki_ jums5
    do "Mucho, y yo me fié de alguien así."
    do "Lo siento, Metz, no me uniré"
    "Dorki se va en silencio"
    "Que le pasa a ella...{w} como supo todo eso..."

    jump start

label talk_4_dorki:
    scene coop_dia 
    with dissolve
    "El ambiente en el club es silencioso. El sol apenas entra por las ventanas, y las sombras parecen más largas de lo normal."
    show dorki_ sad at pos_t11
    mc "Dorki... ¿qué haces aquí tan temprano?"
    do "Solo... quería verte. ¿Eso está mal?"
    mc "No, claro que no. Pero justo ahora estoy preparando los últimos detalles para el festival. El club está bastante ocupado."
    do "¿Y yo no puedo ayudarte?"
    mc "No es eso. Solo que... esta vez ya estamos organizados, no necesitamos más manos."
    show screen glitch_blocks()
    show dorki_ jums5 zorder 15
    play music bg_dorkis_tension
    with dissolve
    do "¿Más manos...? ¿O solo las de alguien más?"
    mc "...No empieces con eso, por favor."
    show dorki_ jums3 at shake_try(r=4)
    do "Ya veo. Lo entiendo. Hay alguien más. Por eso ya no soy necesaria, ¿verdad?"
    mc "¿Dorki?"
    show dorki_ jums5 zorder 15 at pos_t11
    do "Todo este tiempo pensé que podía hacer algo bien. Que podía estar a tu lado, ayudar, compartir esto. Pero ya no soy la vicepresidenta. ¿Verdad?"
    mc "...¿Qué estás diciendo?"
    show crist1
    play sound glass
    show dorki_ jums2
    do "He estado pensando mucho. Hay cosas que tú no recuerdas... cosas que yo no puedo olvidar."
    mc "¿De qué hablas?"
    show dorki_ jums1
    do "Lili."
    show crist2
    play sound glass
    mc "...¿Qué?"
    "De pronto, el aire se vuelve más pesado. La puerta del club se entreabre sola, dejando entrar una ráfaga de viento frío."
    do "No te has preguntado por qué Lili no viene últimamente, ¿cierto?"
    mc "Dorki... basta."
    show dorki_ jums5
    do "Ella... no debería haber estado allí. No tenía que ver nada. Pero lo hizo. Y entonces—"
    "Un grito se escucha a lo lejos, proveniente del pasillo."
    sa "¡¡¡ALGUIEN VENGA RÁPIDO!!!{nw=3.0}"
    show crist3
    play sound glass
    mc "...¿Sasha?"
    "Corro hacia la puerta, pero Dorki se queda inmóvil. Sus ojos, vacíos."
    do "Y otra vez... el ciclo empieza."
    mc "¿Qué estás diciendo?"
    do "Cada vez que me doy cuenta, ya es tarde. Cada vez que me miras, ya no me recuerdas."
    show black zorder -1 at Transform(zoom=5.0, yoffset=-1000, xoffset=-1000)
    "Sientes un fuerte zumbido en los oídos. Todo comienza a temblar ligeramente."
    show layer master at zoom_z_layer(z=-0.1, linear_time=90)
    do "Esta vez... sufriré como debe ser.{nw=4.0}"
    "El mundo se distorsiona frente a tus ojos. Todo se vuelve blanco. Un pitido agudo perfora tus pensamientos.{nw=4.5}"
    "Y entonces... repites... {nw=2.6}"
    scene black
    hide screen glitch_blocks



    with dissolve

    jump start

label talk_5_dorki:
    scene coop_dia 
    with dissolve
    "Mientras tanto en el club, estoy preparando las bombas de crema para añadir mas variedad."
    "Lili me acompaña mientras los demás andan en sus clases terminando sus estudios"
    $ li_name = "Lili"
    show lili_ normal at pos_t11
    li "Y...{w} que tal te va haciendo estos preparativos."
    mc "Bien, solo que se vuelve pesado con el tiempo..."
    show lili_ sad2
    play music bg_dorkis_sad
    li "Me imagino, estamos hace 1 hora con esto."
    mc "Si, y tu como has estado con lo tuyo."
    show lili_ normal
    li "Igual de pesado, te digo que si tuviera varias manos, terminaría con todo."
    mc "Ya veo..."
    mc "Al final no se termina así de rápido, lleva su tiempo"
    show lili_ sad
    li "¿No quisieras repetir el día para poder lograr lo que sea?"
    mc "La verdad... es que si."
    "Hubo una pausa de silencio por unos segundos. ¿tan así fue la respuesta?"
    mc "Y que quisieras repetir."
    show lili_ sad2
    li "Bueno...{w} este día en concreto."
    show lili_ sad
    li "Es lo único que me mantiene tranquila, sin demandas, sin tareas."
    li "Solo aquí haciendo postres, lo mas tranquilo del mundo"
    mc "Eso es cierto."
    show lili_ lol
    li "¿Y tu que día quieres repetir?"
    mc "Yo, repetiría estando aquí también."
    show lili_ normal
    li "Juju, pensamos igual lo mismo Metz"
    mc "Quien no quiere estar tranquilo y al mismo tiempo con una chica..."
    show lili_ lol
    li "...Jeje"

    jump start

label talk_6_dorki:
    scene black
    with dissolve

    "A Lili la encontraron desangrada en los baños de chicas."
    "Esto causo revuelo en la escuela."
    "Mientra tanto, yo estoy aquí en el club no haciendo mucho..."
    "Mirando un poco afuera. respirando el aire frió."
    "Por que me siento horrible, pensando que Lili no va a volver jamas..."
    "Solo miro la ventana, todo el club esta en silencio."
    "El sonido de la lluvia es lo que escucho."
    "Sin tan solo hubiera estado mas seguido con Lili, tal vez ella no quisiera estar sola."
    "Y yo no me sentiría de esta forma tan desastrosa"
    scene corridor 
    show dorki_ normal at pos_t11
    with dissolve
    do "¿En que andas pensando?"
    mc "En nada..."
    mc "Solo cosas..."
    show dorki_ eh2
    do "Comprendo."
    do "Sabes que eres lindo cuando piensas mucho."
    mc "...."
    mc "En que mierda andas diciendo."
    mc "¿Sabes que murió una integrante del club"
    show dorki_ normal
    do "Si lo se..."
    do "Perdón por sonar como alguien{w} que no se preocupa."
    show dorki_ sad
    do "Pero la verdad ella estaba mal desde un principio."
    mc "¿Que sabes tu?"
    show dorki_ sad
    do "Ella la maltratan."
    show dorki_ sad2
    mc "...."
    "Mis oídos comienzan a zumbar, ya parece que avance el tiempo."
    "Siento que todo es mas lento."
    show dorki_ normal
    do "Metz, no todas las personas tienen la misma suerte que tu."
    show dorki_ sad
    do "Digamos que ella tenia tantos problemas, que llego a esos puntos."
    do "Yo la conocía muy bien en realidad"
    show dorki_ confusion
    do "De hecho..."
    do "No siempre iba a este club por alguna razón."
    show dorki_ normal
    do "Solo estaba aquí para liberarse un rato."
    do "Pero desde que le dijiste, (Quien no quiere estar tranquilo y al mismo tiempo con una chica...)"
    show dorki_ sad2
    do "Eso la destruyo por dentro como no tienes idea."
    do "Una chica pensando que si tiene una relación, ese alguien le causaría problemas."
    show dorki_ normal
    do "Es tanto así, que tuvo que llegar a esos extremos."
    do "¿Piensas que es tu culpa?"
    show dorki_ sad
    do "No Metz, no lo es, es solo mala suerte."
    show layer master at shake_slayer(ts=0.01)
    do "Nunca te sientas mal en algo así."
    do "Por que tu no la mataste, solo fue ella misma."
    mc "*Sollozo*{nw=3.0}"
    mc "!YA BASTA¡{nw=2.0}"
    # el reloj retrocede sin parar

    jump start

label talk_7_dorki:
    scene corridor:
        matrixcolor InvertMatrix(1.0)

    mc "!POR QUE VUELVO AQUÍ¡"
    mc "Por que me devuelves otra vez con lo mismo..."
    mc "Solo quiero vivir en paz."
    mc "!PARA DE REVELAR MI REALIDAD¡"
    mc "!BASTAAAAAAAAAAAA¡{nw=1.0}"
    show white with Dissolve(.25)
    # el reloj tiltea sin parar
    jump start

label talk_8_dorki:

    scene coop_dia
    with Dissolve(.25)
    "Llego al club, pensando en como olvidar lo de antes."
    $ sa_name = "Sasha"
    $ he_name = "Hector"
    show sasha_ normal at pos_t11
    sa "Metz, ¿eres tu?"
    mc "Si, que pasa."
    show sasha_ sad
    sa "Solo que, fui una mala presidenta..."
    sa "Uno de nuestros miembros se a ido, por mi falta de responsabilidad"
    show sasha_ angry
    sa "Tan solo pudiera hacer algo."
    sa "Pero no, no hice nada."
    he "No tienes que ser tan dura Sasha."
    show sasha_ shock
    sa "!Pero si es verdad¡"
    show sasha_ sad
    sa "Sin tan solo hubiéramos hecho algo."
    show sasha_ sad at pos_t21
    show hector_ sad at pos_t22
    he "No te preocupes, ya no hay nada que pudiéramos hacer."
    he "Solo es cuestión de que ella, no nos quería ver tristes."
    show sasha_ angry
    sa "Tienes razón, Lili no nos quiere ver así."
    mc "Estoy de acuerdo..."
    mc "No podemos dejarnos caer. podemos sufrir por ella por partir."
    mc "Pero debemos seguir aquí, en el club."
    mc "El único lugar..."
    show black zorder 6:
        alpha 0.6

    show dorki_ sad zorder 9 at pos_t11
    with Dissolve(1.0)
    do "Que le daba paz."

    # el reloj se detuvo se pudre...
    jump start

label talk_9_dorki:
    scene coop_dia:
        matrixcolor ColorizeMatrix("#7e7e7e", "#000000")
    with dissolve
    mc "Estoy cansando ya."
    mc "Ya parece que el tiempo no quiere que sea feliz"
    mc "Solo quiere darme la verdad."
    show dorki_ normal at pos_t11
    do "Eso parece, y te digo que cambiando el tiempo de esa forma, no conseguirás nada."
    do "No entiendo que buscas hacer."
    mc "Solo..."
    mc "Deshacerme de ti."
    mc "Eres como un grano en el culo cuando te escucho."
    mc "No paras de estar en mi cabeza, repitiendo lo mismo una y otra vez."
    mc "Tan solo eres un virus que no sale de mi cabeza."
    do "...."
    show dorki_ sad
    do "Tal vez sea todo eso, pero yo no tuve la culpa de nada."
    mc "Si la tienes, tu eres la causante de todo mis males."
    show dorki_ sad2
    do "...por que no quieres cargar en la culpa."
    do "Se lo estas dando a alguien mas que no tiene nada que ver."
    do "Tan solo veo que no te quieres culpar."
    do "De hecho, la culpa no es tuya ni es mía."
    show dorki_ normal
    do "Entonces que sentido tiene que sigas repitiendo el tiempo."
    mc "...."
    mc "Aceptar lo que fue antes..."
    mc "Pero veo que es difícil, muy difícil, tan solo siento que antes seria lo que realmente fue en realidad"
    do "Ya veo."
    show dorki_ sad2
    do "Por que no solo quedo yo en terminar con esto."
    mc "No lo hagas, ya todo esto acabaría."
    do "Entonces... de quien la culpa de todo esto."
    label choice_kick_culp:
        menu:

            "Seguir culpándote":
                show dorki_ confusion
                do "¿Es tu culpa?"
                do "Pero esto no lo hiciste tu."
                show dorki_ angry
                do "¿Lo entiendes?"
                show dorki_ normal
                mc "Ya sabia..."
                mc "Es solo que..."
                mc "No quiero seguir, tan solo quiero comprender, ¿Por que?"
                show dorki_ sad
                do "Rompe esa duda Metz, seguro todo sera al final"
                jump end_choice_talk_9

            "Dorki":
                show dorki_ confusion
                do "¿Mi culpa es la solución de tu realidad?"
                do "Por favor, no te sientas orgulloso en un momento así."
                do "Lo mejor es que intentes pensar que..."
                show dorki_ normal
                do "Todo lo hiciste tu."
                do "Yo ni los demás no tuvimos nada que ver."
                jump choice_kick_culp

            "Sasha":
                show dorki_ sad2
                do "Sasha ni sabe que es esto."
                do "Que malo eres culpando a alguien que no tiene nada que ver"
                do "Al menos, la arrogancia si lo tienes aun."
                jump choice_kick_culp

            "Hector":
                show dorki_ dorki
                do "Creo que Hector ni se molestaría en culpar a los demás"
                do "El pensaría lógicamente."
                do "No como tu, que culpas a cualquiera sin razón."
                jump choice_kick_culp

            "Lili":
                show dorki_ sad
                do "Lili a pesar de lo que hizo, no tiene culpa de nada."
                do "Una vida difícil para ella."
                do "La vas a culpar por que se deprime todos los días..."
                show dorki_ sad2
                do "Eso es algo muy rencoroso de tu parte."
                do "Y parece que ni empatía tienes."
                jump choice_kick_culp


    label end_choice_talk_9:
        mc "Entonces..."
        mc "Volveré..."
        jump start

label talk_10_dorki:
    "A pesar de todo, estamos todos en el club."
    "Sasha esta preparando cupcakes mientras que Hector prepara el molde de hornear"
    scene coop_dia:
        matrixcolor ColorizeMatrix("#7e7e7e", "#000000")
    play music bg_dorkis_sad
    show sasha_ dark at pos_t11
    $ sa_name = "d8h8qwd"
    $ glitext = glitchtext(25)
    sa "[glitext]"
    mc "Si jaja, me imagino lo difícil que es hacer eso"
    $ he_name = "2E2JE89"
    $ glitext = glitchtext(32)
    show sasha_ dark at pos_t21
    show hector_ corrupted at pos_t22
    he "[glitext]"
    mc "Vaya Hector...."
    mc "Cada vez veo que te cuesta mas."
    show lili_ corrupted at pos_t32:
        xoffset -100
    show sasha_ dark at pos_t31
    show hector_ corrupted at pos_t33
    $ he_name = "2dddddd9"
    $ glitext = glitchtext(55)
    li "[glitext]"
    show dorki_ sad at pos_t11
    do "Hey..."
    mc "¿Si?"
    do "¿Acaso no los ves?"
    mc "¿Veo que?, a mis amigos."
    mc "Ja... ja, están muy normales para mi"
    mc "A que no..."
    $ glitext = glitchtext(25)
    show dorki_ sad2
    show sasha_ dark at pos_t31
    show hector_ corrupted at pos_t33
    he "[glitext]"
    show dorki_ sad
    do "¿Esto no esta bien, acaso no quieres seguir?"
    mc "¡NO, DEBO QUEDARME AQUI!"
    mc "¡SI VUELVO OTRA VEZ, PODRIA PONERSE PEOR!"
    do "Cálmate"
    do "Solo queda algo por hacer..."
    do "Últimamente ya no sigues por mi"
    mc "Por ti..."
    do "Si, supongo que..."
    do "Debo terminar con esto..."
    do "Pero antes de que siga, puedo..."
    show dorki_ eh1
    do "Besarte."
    mc "¿Que?."
    do "Metz, tu siempre me gustaste, con tan solo disfrutar un ultimo momento contigo."
    show dorki_ cry1
    do "Solo quiero eso..."
    do "Es tu oportunidad que por fin cumplas tu deseo."
    show dorki_ sad
    do "Solo..."
    mc "Bien.{nw}"
    show black zorder 99
    "No lo pensé dos veces, solo bese a Dorki con fuerza, intentando no dejarla ir."
    "No paro de negarme, ella parece no incomodarse..."
    "Solo..."
    "Solo....."
    "Lo dejare hasta aquí..."
    hide black
    show dorki_ jums5
    do "Te amo{w} Metz"
    stop music
    show dorki_ gore2
    "....."
    "......."
    ".........."
    show dorki_ gore1
    show layer master at shake_try(r=3)
    play sound sound_gore_small1
    show blood_particules zorder 70:
        xalign 0.5
        yalign 0.76
    "............."
    "................"
    show layer master at shake_try(r=8)
    play sound sound_gore_small2
    show blood_particules zorder 70:
        xalign 0.5
        yalign 0.55
        zoom 2.0
    $ try_again_bool = 0
    play music bg_dorkis_sad
    show black zorder 99:
        alpha 0.0
        ease 99 alpha 1.0
    label loop_again_effect:
        $ try_again_bool += 100
        if try_again_bool <= 5500:
            "....................{nw=0.2}"
            "....................{nw=0.2}"
            "....................{nw=0.2}"
            "....................{nw=0.2}"
            "....................{nw=0.2}"
            "....................{nw=0.2}"
            jump loop_again_effect
        else:
            $ renpy.stop_skipping()
            mc "Odio esto..."
            mc "Este tiempo lo va a pagar."
            mc "Si es así, cuantas veces tengo que repetir."
            "Que mas da, solo intentare dar lo mejor posible"
            "Si es es llegar a tal extremo, solo para tener un final feliz"
            "Solo vamos..."
    $ renpy.stop_skipping()
    jump start



label talk_11_dorki:
    scene coop_dia:
        matrixcolor ColorizeMatrix("#7e7e7e", "#000000")
    mc "Por que volví aquí..."
    mc "¿No pudo repetir?"
    mc "Oh no...."

    "Parece que me veo a mi mismo alli tirado en el piso."
    "Pienso que algo anda mal."
    "Un momento..."
    "No puede ser, Dorki logro detener el tiempo."
    "¿Me pudo detener?"
    mc "Lo has hecho Dorki..."
    mc "Pudiste detenerme, pero hacer algo bastante arriesgado."
    mc "Y ademas..."
    mc "Como podre repetir."
    mc "Lo volveré hacer."

    jump start


label talk_12_dorki:
    scene bg_galaxi:
        subpixel True
        alpha 1.0
        pos(.5, .5)
        anchor(.5, .5)
        zoom 1.0
        ease 27 zoom 1.6
        ease 27 zoom 1.0
        repeat

    show coop_dia zorder 1:
        alpha 1.0
        matrixcolor InvertMatrix(1.0)
    
    show dorki_ dorki zorder 4 at pos_t42:
        matrixcolor SaturationMatrix(0)
    show sasha_ normal zorder 4 at pos_t41:
        matrixcolor SaturationMatrix(0)
    show lili_ normal zorder 4 at pos_t43:
        matrixcolor SaturationMatrix(0)
    show hector_ normal zorder 4 at pos_t44:
        matrixcolor SaturationMatrix(0)
    mc "Cielos..."
    mc "¡Ya esto es una estupidez!"
    show layer master at shake_try(r=4)
    "Golpeo los pupitres con fuerzas, tiro cualquier cosa, agobiándome de mi mismo de no entender, por que no vuelvo."
    "Simplemente, me enojo con todo"
    "¡Por que me ocurre ahora esto!"
    "¿Ahora que hago para salir del bucle?"
    mc "...."
    show layer master at shake_try(r=4)
    "Quedo yo, solo eso romperé todo y volveré al ciclo"
    "Pero... no quiero hacerlo."
    "¿Como se supone que tengo que volver entonces?."
    mc "Dorki, estoy seguro que esto es la solución"
    "Voy corriendo en los corredores en la escuela."
    mc "No hay absolutamente nada."
    "Ni estudiante, ni luz, solo oscuridad bastante poco atractivo"
    "El sol parece no existir."
    "Esto es lo que sucede si vuelves varias veces."
    "Intentando conseguir algo mejor que mi realidad, ¿es de tanto riesgo?"
    scene corridor:
        matrixcolor InvertMatrix(1.0) 
    with wipeleft
    mc "Que es eso."
    "Veo una fuente oscura al final de las escaleras, como si no tuviera nada luego de eso."
    "El mundo solo recuerda esto, lo demás parece no existir."
    mc "Ni bajar del edificio, ni tampoco salir viendo las ventanas."
    "Estoy intentando darme un idea de donde rayos ir."
    "Pero recordando el salón del club, allí si se ve afuera"
    "Me devuelvo al club mientra que Dorki y los demás están aquí aun"
    scene coop_dia zorder 1:
        matrixcolor InvertMatrix(1.0)
    
    show dorki_ dorki zorder 4 at pos_t42:
        matrixcolor SaturationMatrix(0)
    show sasha_ normal zorder 4 at pos_t41:
        matrixcolor SaturationMatrix(0)
    show lili_ normal zorder 4 at pos_t43:
        matrixcolor SaturationMatrix(0)
    show hector_ normal zorder 4 at pos_t44:
        matrixcolor SaturationMatrix(0)
    "Solo observo las ventana, y verifico si se pueden abrir."
    "...."
    "Si se pudieron abrir."
    "Y parece existir el afuera..."
    "¿Por que solo el club es el lugar donde parece mas real que todo lo demás?"
    "No entiendo muy bien."
    "Solo decido ver aun mas afuera intentando ver si alrededor no esta igual."
    "...."
    "No parece cambiar nada, solo el cielo gris y la escuela muy vacía"
    "Aunque la ciudad admito que ni se ve muy bien, hay mucha niebla."
    "Tan solo tomo algo para lograr bajar, lo bueno es que solo estoy a un piso."
    "Agarro todas las ropas de Sasha, Hector y Dorki para hacer un nulo incluyendo el mio."
    "No tengo mucho tiempo..."
    "Amarro todo con prisa, intentando que se mantengan bien apretados y que no se rompan."
    "....."
    "Vale, ya pude lograrlo."
    "Lanzo la cuerda con ropas amarradas a la ventana, para así obtener con que bajar a este edificio."
    "Pude bajar sin problemas."
    scene bg_park:
        matrixcolor SaturationMatrix(0)
    "Al tocar el césped veo que es todo normal"
    "Pero..."
    "Mas lejos parece lo mismo que en la escalera."
    "Si voy a ese lugar..."
    "Volveré a romper el bucle."
    "Entonces vamos a lado oscuro de esto..."

    jump start


label talk_13_dorki:
    "No pares..."
    jump start


label talk_14_dorki:
    scene corridor
    show crist1 zorder 9
    show crist2 zorder 8
    show layer master:
        matrixcolor InvertMatrix(1.0)

    mc "¿Tengo que aceptar el tiempo?"
    "Si en mis manos tengo lo posible, para que pararlo"
    mc "¡NO LO HARE!"
    play sound "audio/terremoto.ogg"
    show layer master at shake_try(r=12):
        matrixcolor InvertMatrix(1.0)
    "El mundo se distorsiona mas a medida que mis palabras hacen temblar el mundo"
    "No rendirme es lo que teme."
    "En esto no me rendiré esta vez, sin antes pelear."
    show dorki_ cry2 at pos_t11
    do "¡POR FAVOR HAZLO!"
    "Las ultimas palabras que diré es no rendirme."
    jump start









image black_par1 = "gui/particules_black.webp"
image purples = "gui/particules_black2.webp"

image particule_azul = "gui/azul_particula.png"

image choice_random_particules:
    choice:
        "black_par1"
    choice:
        "purples"

    pause .90
    repeat


image murcielago_animation:
    ChaoticSpiral("black_par1", count=44, max_radius=400, max_size=400, spin_speed=1.0)
image murcielago_animation2:
    ChaoticSpiral("purples", count=32, max_radius=900, max_size=800, spin_speed=3.0)
image murcielago_animation3:
    ChaoticSpiral("particule_azul", count=22, max_radius=400, max_size=400, spin_speed=1.0)








label talk_15_dorki:
    play music bg_dorkis_sad
    scene bg_galaxi:
        subpixel True
        pos(.5, .5)
        anchor(.5, .5)
        zoom 1.0
        ease 27 zoom 1.6
        ease 27 zoom 1.0
        repeat
    "Nace una estrella..."
    "En tus ojos ve algo que ilumina tu camino."
    "Algo que no sabes."
    "Tienes miedo de cruzar."
    "Pero simplemente caminas recto a tocar esa estrella."
    "Corres y corres."
    "Hasta que..."
    "Hasta...."
    show layer master:
        matrixcolor InvertMatrix(1.0)
    show crist1
    stop music
    play sound glass
    $ renpy.pause(1, hard=True)

    scene black
    play music bg_dorkis_end_music fadeout 1.0
    show layer master:
        subpixel True
        zrotate 12
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        zoom 2.0
        ease 3 zoom 1.05 zrotate 0
    show bg_cinematic zorder 9
    show dorki_ dark_animation zorder 10:
        subpixel True
        zoom 0.56
        xalign 0.5
        yalign 0.5
        block:
            ease 25 yoffset -45
            ease 25 yoffset 45
            repeat
    show particules_red_blosson zorder 12
    show vignette_down zorder 13
    with Dissolve(.25)

    do "Las tinieblas de nuestras lagrimas caen."
    do "Todos en nuestro paso es un tiempo sin sentido."
    do "O soy yo..."

    show layer master:
        subpixel True
        zrotate 0
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        zoom 1.05
        ease 2 zoom 2.1 pos(0.5, 0.5) anchor(0.5, 0.30) zrotate 0

    do "Por favor para de caminar hacia adelante."
    mc "Dorki..."
    do "¿Acaso es algo que tengo que hacer?"
    do "¿Tu verdad? mi verdad."
    do "Ya tu verdad acaba aquí."
    show layer master
    with Dissolve(.5)


    show white zorder 20:
        alpha 1.00
        linear .35 alpha 0.00



    show layer master at shake_slayer(ts=0.01)
    show dorki_ dark3 at pos_t11
    do "Para siempre{nw=2.2}"
    scene white
    with Dissolve(.25)
    mc "Cielos{nw=2.0}"

    scene black
    show corridor at shake_slayer(ts=0.06):
        matrixcolor BrightnessMatrix(0.5)
        ease 25 matrixcolor BrightnessMatrix(0.0)
    show vignette_1
    $ renpy.music.play("audio/edit/running_person.mp3", channel='sound', loop=True)
    "Comienzo a correr a toda velocidad hasta la ventana del final{nw=3.0}"
    "Puede que así rompa el tiempo de alguna manera{nw=3.0}"
    do "!No lo harás¡{nw=3.0}"
    show vignette_2:
        subpixel True
        zoom 1.0
        ease 40 zoom 0.8 pos(0.5, 0.5) anchor(0.5, 0.5)
    play sound sound_gore_small1
    "Me agarro de la pierna izquierda con fuerza.{nw=3.0}"
    show layer master
    play sound glitch
    show vignette_2:
        subpixel True
        zoom 1.0 alpha 1.00 pos(0.5, 0.5) anchor(0.5, 0.5)
        ease 0.5 zoom 1.6 pos(0.5, 0.5) anchor(0.5, 0.5) alpha 0.0
    "Intento golpearlo con todas mis fuerzas hasta liberarme.{nw=3.0}"
    show vignette_2:
        subpixel True
        zoom 1.6 alpha 0.0
        ease 0.5 zoom 1.0 pos(0.5, 0.5) anchor(0.5, 0.5) alpha 1.0
    show corridor at shake_slayer(ts=0.04):
        matrixcolor BrightnessMatrix(0.5)
        ease 25 matrixcolor BrightnessMatrix(0.0)
    do "!No, detente¡{nw=3.0}"
    mc "Es mi ultima oportunidad{nw=3.0}"
    play sound sound_gore_small2
    show vignette_1
    hide vignette_2
    with Dissolve(.2)
    "Vuelvo a iniciar la carrera de llegar hasta la ventana.{nw=3.0}"
    $ renpy.music.play("audio/edit/running_person.mp3", channel='sound', loop=True)
    "Debo lograrlo.{nw=3.0}"
    $ do_name = _("")
    do "!No lo harás¡{nw=2.0}"
    "Al ver atrás veo algo cubriendo todo alrededor.{nw=3.0}"
    "El miedo me hace correr mas a pesar de no ser tan rápido{nw=3.0}"
    "La adrenalina fluye en mi, por que se que puedo morir aquí{nw=3.0}"
    "Debo lograrlo.{nw=3.0}"
    "Solo un poco...{nw=3.0}"
    show corridor zorder 99:
        subpixel True
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        zoom 1.0
        ease 7 zoom 4.0 pos(0.6, 0.6) anchor(0.5, 0.5)

    $ renpy.pause(2.0, hard=True)
    stop music 
    scene white
    stop sound fadeout 2.0
    with Dissolve(.35)
    "Salí volando a la ventana, pensando si esto ya es todo{nw=3.0}"
    "Pero ya que se que el tiempo esta allí, no podre tener miedo{nw=3.0}"
    scene black
    stop music
    play sound glass
    show crist1
    "Es todo o nada. volveré cada ciclo, !hasta encontrarlo¡{nw=3.0}"


    # $ renpy.notify("Pausar")
    # $ renpy.pause(99, hard=True)
    $ persistent.actived_cap_120 = True
    jump starts_end

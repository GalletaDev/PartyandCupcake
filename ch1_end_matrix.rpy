label world_break_matrix:
    scene bg_galaxi:
        subpixel True
        pos(.5, .5)
        anchor(.5, .5)
        zoom 1.0
        ease 27 zoom 1.6
        ease 27 zoom 1.0
        repeat
    show choko normal at pos_t11
    show layer master:
        subpixel True
        zoom 1.8 rotate 10 pos(0.5, 0.5) anchor(0.5, 0.5)
        pause 2.5
        easeout 2 zoom 1.0 rotate 0 pos(0.5, 0.5) anchor(0.5, 0.5)
    with remoline_pass
    cho "Vaya, vaya..."
    show choko shock 
    cho "Llegaste hasta aquí solo para obtener lo que quieres"
    show choko victory
    cho "Jaja, cielos, no pensé en verte aquí"
    cho "Pudiste lograr romper el tiempo para solo verme."
    cho "!Locura de la buena¡"

    show choko normal
    mc "Para de bromear..."
    mc "¿Quien eres exactamente?"
    show choko love zorder 2
    cho "Me llamo Choko, no soy la Dorki que conoces."

    $ cho_name = "Choko"
    mc "Que locura."

    mc "Desde que Dorki comenzó a comportarse como toda una loca o incluso, ¿enamorarse de mi?"
    mc "Me di cuenta que ni era Dorki, si no tu."
    show choko normal
    mc "Ves lo sexual o lo absurdo como gracioso, Dorki no llega a esos extremos."

    cho "Lo se, lo se."
    show choko victory
    cho "Pero de eso se trata la diversión, incluso la vida sexual o amorosa es divertido."
    show choko creepy1
    play sound ondes_sound
    cho "O incluso matar."
    show choko victory
    cho "Por esa razón ya que repetías mucho el tiempo."
    show choko normal
    cho "¿Por que no hacer algo totalmente diferente esta vez?"
    cho "Eso es lo que hizo que usara a Dorki como herramienta para que te detengas."
    show choko confusion
    cho "Pero veo que ni si quiera te sirvió eso."

    mc "Dorki, era alguien de corazón."
    show choko normal
    mc "Pero ya que tu objetivo es poseer a las persona con esas características."
    mc "Me querías engañar para lograr lo mismo..."

    show choko creepy1
    play sound glass
    cho "¿Lo mismo?"
    cho "Tu tienes un corazón de mierda, a ti te vale igual quien sea tu amigo o no."
    cho "Es mas, me da asco que me digas que tu también, eras un objetivo"
    show choko victory
    cho "Increíble jaja."
    play music bg_dorkis_despadation fadeout 1.0
    mc "Pero..."
    mc "En realidad no era la razón real de esto."
    mc "Querías que dejara de devolver el tiempo siempre."
    show layer master at shake_try(r=15)
    show choko animation_angry
    cho "!!Ahora si nos entendemos¡¡."
    cho "Igualmente yo soy la chica mágica de la diversión"
    cho "Era humana, pero en 1990 acabe totalmente arruinada en mi mente."
    cho "Pero alguien me dijo que seria feliz, si tomaba una decisión."
    cho "De obtener el poder de la diversión eterna."
    show choko victory
    cho "¿Increíble no?"

    mc "¿Y por que luces tan joven aun?"
    show choko confusion
    cho "Pues..."
    cho "Fue a costa de mi mortalidad, ya no puedo morir de vejez."
    show choko creepy2
    cho "Pero que mas da."
    show choko normal
    mc "...."
    "Esto es malo, ¿llegue tan lejos solo para morir aquí?"
    "No..."
    "Ya lo hubiera hecho, pero parece que no quiere matarme."

    mc "Si eres tan fuerte por que no me matas y ya..."
    show choko confusion
    cho "No puedo, tu controlas el tiempo{w}, si te mato, voy a retroceder como todo lo demás."
    cho "Por eso no puedo hacerlo."
    show choko creepy1
    cho "Pero..."
    cho "Lo que puedo hacer es intentar hacerte sufrir."

    "Esto ya no es bueno..."
    show choko victory
    cho "Entonces, por que no solo nos divertimos."
    cho "Se que es algo absurdo, pero por que no..."
    show choko creepy1
    cho "Jugamos..."
    show layer master at shake_try(r=15)
    show choko animation_angry
    cho "!PIEDRA, PAPEL O TIJERAS¡"

    mc "¿Que?"
    show choko victory
    cho "Yo soy la chica mágica de la diversión, lo mas absurdo es mi estilo."
    show choko normal
    cho "Pero obviamente cumplo con mi palabra."

    cho "Si yo gano varias veces, te comenzare a quitar o cortar cada parte de tu cuerpo."
    show choko creepy2
    cho "Lo mejor es que puedo volver a colocártelo para que no te mueras."
    show choko normal
    cho "!Espero que pierdas¡"
    show choko shock
    cho "Pero..."

    cho "Y si tu ganas, puedes hacerme lo que quieras."

    mc "Eh..."

    "Se escucho raro esa propuesta, pero si eso hace que se detenga, puede que lo logre."
    "Pero ese juego es muy aleatorio..."
    "No se que haré si logra ganarme..."
    "Y puede que duela."
    "Un momento.{w} intento morderme mi brazo si siento algo de dolor."
    show choko creepy1
    cho "Que rayos, yo hago payasadas, pero tu te pasas de mi."
    show choko victory
    cho "Me encanta."

    "Cielos..."
    "Al hacer eso me di cuenta que no siento dolor."
    "¿Sera devolverse tantas veces?"
    "Puede que no sienta dolor si me quita una extremidad"
    "O eso espero..."
    stop music fadeout 2.0
    show choko love
    cho "Bueno, empezamos tonto."
    show choko normal
    mc "Mira quien habla..."

    "Tengo que salvar a Dorki, si no lo hago..."
    "Como obtendré el milagro del final temporal."
    play music bg_dorkis_battle
    jump piedra_papel_tijera


label death_player_end:
    stop music fadeout 2.0
    scene corridor
    show dorki_ dorki at pos_t11:
        matrixcolor InvertMatrix(1.0)
    with dissolve_scene

    python:
        player_rps = ""
        enemy_rps = ""
        str_rps = ""
        life_choko = 300
        life_player = 300
        round_game_choko = 1

    play sound transition_sound
    "Aun no puedo morir aqui..."
    play music bg_dorkis_battle fadein 2.0
    jump piedra_papel_tijera


default player_rps = ""
default enemy_rps = ""
default str_rps = ""

default life_choko = 300
default life_player = 300
default round_game_choko = 1

label piedra_papel_tijera:
    # scene coop_dia:
    #     matrixcolor SepiaMatrix()
    #     zoom 1.4

    scene black:
        zoom 1.6
    show remoline_infinity:
        zoom 1.2


    if life_choko >= 200:
        show choko mode_colors at pos_t11
    elif life_choko >= 150:
        show choko creepy2 at pos_t11   
    elif life_choko >= 50:
        show choko creepy4 at pos_t11   
    elif life_choko <= 0:
        jump death_choko_end

    if life_player <= 0:
        jump death_player_end
    with dissolve_scene

    show layer master:
        subpixel True
        zoom 1.0
        pos(0.5, 0.5)
        anchor(0.5, 0.5)
        choice:
            ease 10 zoom 1.3 pos(0.5, 0.5) anchor(0.5, 0.5) rotate 2
            pause 1.2
            ease 10 zoom 1.0 pos(0.5, 0.5) anchor(0.5, 0.5) rotate 0
        choice:
            ease 10 zoom 1.4 pos(0.65, 0.65) anchor(0.5, 0.5) rotate 3
            pause 1.2
            ease 10 zoom 1.0 pos(0.5, 0.5) anchor(0.5, 0.5) rotate 0  
        choice:
            ease 10 zoom 1.2 pos(0.60, 0.35) anchor(0.5, 0.5) rotate -1
            pause 1.2
            ease 10 zoom 1.0 pos(0.5, 0.5) anchor(0.5, 0.5) rotate 0     
        repeat    
    
    if life_choko >= 300:
        cho "¡Piedra, papel o tijeras! Vamos a divertirnos."
    elif life_choko >= 250:
        cho "Tal vez no me importa desaparecer, mejor te mato."
    elif life_choko >= 200:
        cho "Esto no se te hará fácil"
    elif life_choko >= 150:
        cho "Vaya loco que eres, como osas de seguir."
    elif life_choko >= 100:
        cho "Es mejor que pares ya..."
        cho "Oh si no Dorki sufrirá igual que tu"
    elif life_choko >= 50:
        cho "!Muy bien¡, ya mejor es para, ¿no?"
        cho "!POR FAVOR DETENTE YA¡"


    # DIALOGO
    ###################
    call screen animation_rps_menu()
    ###################
    show layer master at shake_try(r=7)
    if life_choko >= 101:
        hide choko
        show animation_choko_remoline

    $ renpy.pause(1.5, hard=True)
    $ choices = ["rock", "paper", "scissors"]
    
    # 💭 comportamiento adaptativo
    if renpy.random.random() < 0.2:
        $ chance_to_cheat = min(25, 5 + 2 * 5)
        if renpy.random.randint(1,100) <= chance_to_cheat:
            # predict game
            if player_rps == "rock":
                $ enemy_rps = "paper"
                $ str_rps = _("Papel")
            elif player_rps == "paper":
                $ enemy_rps = "scissors"
                $ str_rps = _("Tijeras")
            else:
                $ enemy_rps = "rock"
                $ str_rps = _("Piedra")
        else:
            $ enemy_rps = renpy.random.choice(choices)
    else:
        $ enemy_rps = renpy.random.choice(choices)

    # "[chr2_game.g_name] eligió [str_rps]."
    window hide
    window auto
    show screen rps_show_status(player_=player_rps, enemy_=enemy_rps)
    $ renpy.pause(5.7, hard=True)
    hide animation_choko_remoline

    # 💥 Resultado
    if player_rps == enemy_rps:
        # play sound fail_sfx
        if life_choko >= 101:
            show choko angry1 at pos_t11
        "Empate."
        cho "¿Como que empate?."
        mc "Qué coincidencia..."
    elif (
        (player_rps == "rock" and enemy_rps == "scissors") or
        (player_rps == "paper" and enemy_rps == "rock") or
        (player_rps == "scissors" and enemy_rps == "paper")
    ):
        # play sound win_sfx
        $ life_choko -= 50
        if life_choko >= 101:
            hide choko_clon_sys1
            show choko creepy1 at pos_t11
        else:
            show choko creepy2 at pos_t11            
        with Dissolve(.2)
        cho "Mierda..."
        if life_choko >= 101:
            show choko animation_angry
            show layer master at shake_try(r=15)
            cho "Tsk... Ganaste."
            cho "Supongo que puedes hacerme lo que quieras ahora..."
        mc "Hazte daño."
        if not life_choko >= 51:
            cho "...."
        else:
            show choko confusion
            cho "¿Que?"
        show layer master

        cho "No..."
        show white zorder 99:
            alpha 0.8
            linear .7 alpha 0.0

        show blood_particules_details
        if not life_choko >= 101:
            show choko creepy4
            play sound blood_small3
            cho "....."
            "Ella se corta de la nada, como si sus movimientos no fuera por su voluntad"
        else:
            show choko creepy2
            play sound blood_small2
            cho "Uff...."
            "Ella se corta de la nada, como si sus movimientos no fuera por su voluntad"
            cho "Ya lo veras..."
            hide white
            hide blood_particules_details
            cho "Esa jugada de hacerme daño por mi misma esta de locos..."
    else:
        # play sound fail_sfx
        $ life_player -= 50
        if not life_choko >= 101:
            "....."
            cho "...."
            cho "Tienes suerte que no me pueda mover imbécil"
            "Ya comienza a debilitarse Choko"
        else:
            show choko hurra at pos_t11
            cho "¡Jajaja! Perdedor~"
            show choko creepy1
            cho "Ahora sí... hora de empezar el show de los cortes~"
            if renpy.random.random() < 0.2:
                play sound blood_small2
                show blood_particules zorder 70:
                    xalign 0.5
                    yalign 0.76  
                show choko_attack
                "Solo me corto la mano sin merito de usarla..."
                "Aunque, no duele ya."
                "Esto es muy raro no sentir nada realmente."
            elif renpy.random.random() < 0.3:
                play sound blood_small3
                show blood_particules zorder 70:
                    xalign 0.5
                    yalign 0.76 
                show choko_attack 
                "Me corto la pierna derecha, y no sentí ningún dolor"
                
            elif renpy.random.random() < 0.5:
                play sound blood_small2
                show blood_particules zorder 70:
                    xalign 0.5
                    yalign 0.76  
                show black zorder 99:
                    xoffset -500
                "Mi ojo derecho se me salio"
                "Supongo que lo quito también..."
                hide black
                with Dissolve(.2)
                "Pero en un par de minutos volvió a su lugar"
            else:
                play sound blood_small2
                show black zorder 99
                "Mi cabeza fue cortada, pero como dije..."
                "No siento dolor."
                "Acaso me hizo tan mal devolverme en el tiempo."
                hide black 
                with Dissolve(.2)
                "Hizo que ya no sintiera nada."
                cho "Ni con eso te mueres..."

    # 💀 Reacción progresiva

    jump expression "piedra_papel_tijera"






label death_choko_end:
    scene coop_dia:
        matrixcolor SepiaMatrix()
    stop music fadeout 2.0
    play sound ambruto
    show choko creepy4 at pos_t11
    with Dissolve(.2)
    cho "...."
    cho "No..."
    play music bg_dorkis_sad
    cho "Perdí en mi propio juego..."
    mc "¿Bueno, ultimo deseo?"
    cho "...."
    cho "Una cosa..."
    cho "Solo quería que alguien me entendiera... pero terminé convirtiéndome en un monstruo."
    cho "Tan solo quieres romper todo para conseguirlo."
    mc "Si eso es conseguir mi objetivo, haría todo."
    cho "Eres un..."
    cho "Tonto."
    mc "No era mi intención... pero tú lo elegiste, Choko."
    cho "No sere la única que te vea aquí."
    cho "Las demás de seguro te verán como una amenaza para todos..."
    cho "Yo solo hacia mi deber por mi castigo."
    pause 0.7
    cho "Chimi... Azgalo... Toruma... Elios..."
    cho "Lo siento...{nw=3.0}"
    stop music
    window hide
    window auto
    play sound sound_blood_much
    show choko animation_explode_blood
    show choko_head_fly_1
    show choko_head_fly_2
    show choko_head_fly_3
    # show choko_head_fly_4
    show gore_animation_blood
    show blood_particules_ect
    pause 1.0
    show blood_particules_ect
    pause 1.0
    show blood_particules_ect
    show blood_particules_ect
    $ renpy.pause(5.0, hard=True)
    scene black 
    with dissolve

    mc "Habías dicho que si ganaba, podría hacer lo que quiera"
    mc "Y tus palabras o retos, no los puedes romper."
    mc "Es la regla de tus poderes."
    mc "Ahora..."
    play sound tos
    show blood_particules zorder 70:
        xalign 0.5
        yalign 0.76
    mc "Yo..."
    mc "Dorki, espero que estes bien por fin."
    mc "Aunque nunca exististe, en mi corazón y el tiempo si lo harán"
    mc "Vamos..."
    play sound tos
    show blood_particules zorder 70:
        xalign 0.5
        yalign 0.76    
    mc "No puedo mas."
    mc "Ya mi cuerpo rechaza volver."
    mc "Pero ya es el ultimo, por favor."
    mc "Vuelve..."


    jump starts_end_game






transform pase_rps_rock:
    xalign 0.75 yalign 0.75 zoom 1.25
    block:
        linear 3 xalign 0.5 yalign 0.25
        linear 3 xalign 0.25 yalign 0.75
        linear 3 xalign 0.75 yalign 0.75
        repeat

transform pase_rps_paper:
    xalign 0.25 yalign 0.75 zoom 1.25
    block:
        linear 3 xalign 0.75 yalign 0.75
        linear 3 xalign 0.5 yalign 0.25
        linear 3 xalign 0.25 yalign 0.75
        repeat

transform pase_rps_scissors:
    xalign 0.5 yalign 0.25 zoom 1.25
    block:
        linear 3 xalign 0.25 yalign 0.75
        linear 3 xalign 0.75 yalign 0.75
        linear 3 xalign 0.5 yalign 0.25
        repeat


screen animation_rps_menu():

    sensitive True

    frame:
        align(0.5, 0.15)
        padding(20, 20)
        text _("{font=fonts/chipi.ttf}!Elije¡")


    imagebutton:
        at pase_rps_rock
        idle "images/rps/button_rock_player.png"
        hover "images/rps/button_rock_enemy.png"
        action [SetVariable("player_rps", "rock"), Return(True)]

    imagebutton:
        at pase_rps_paper
        idle "images/rps/button_paper_player.png"
        hover "images/rps/button_paper_enemy.png"
        action [SetVariable("player_rps", "paper"), Return(True)]

    imagebutton:
        at pase_rps_scissors
        idle "images/rps/button_scissors_player.png"
        hover "images/rps/button_scissors_enemy.png"
        action [SetVariable("player_rps", "scissors"), Return(True)]




image number1_rps = Text("{font=fonts/chipi.ttf}{color=#b40000}{size=190}1{/size}{/color}{/font}")
image number2_rps = Text("{font=fonts/chipi.ttf}{color=#a25400}{size=166}2{/size}{/color}{/font}")
image number3_rps = Text("{font=fonts/chipi.ttf}{color=#00bc03}{size=144}3{/size}{/color}{/font}")

transform rps_animation_image:
    subpixel True
    zoom 2.2
    ease_back .25 zoom 1.5
    parallel:
        linear 0.01 xoffset -8 yoffset 2
        linear 0.01 xoffset 7 yoffset -3
        linear 0.01 xoffset 6 yoffset -4
        linear 0.01 xoffset -4 yoffset 3
        linear 0.01 xoffset 5 yoffset 2
        linear 0.01 xoffset -5 yoffset 4
        linear 0.01 xoffset 3 yoffset -6
        linear 0.01 xoffset 4 yoffset -8
        linear 0.01 xoffset -6 yoffset 1
        linear 0.01 xoffset 4 yoffset 2
        linear 0.01 xoffset 0 yoffset 0
        repeat 6

transform rps_animation_number:
    subpixel True
    zoom 1.5 xalign 0.5 yalign 0.5
    linear .25 zoom 1.0 xalign 0.5 yalign 0.5
    pause 0.8
    repeat 3

image text_progress_rps:
    "number3_rps"
    pause 1.0
    "number2_rps"
    pause 1.0
    "number1_rps"
    pause 1.0
    Null(width=100)

screen rps_show_status(player_, enemy_):

    zorder 90
    default show_status = False
    modal True

    add "text_progress_rps" at rps_animation_number

    timer 3.0 action SetLocalVariable('show_status', True)

    if show_status:
        hbox:
            align(0.5, 0.35)
            spacing 450
            if player_:
                frame:
                    padding(20, 20)
                    vbox:
                        text "{font=fonts/chipi.ttf}{color=#3103a5}You{/color}{/font}"
                        add "images/rps/button_[player_]_player.png" at rps_animation_image
            if enemy_:
                frame:
                    padding(20, 20)
                    vbox:
                        text "{font=fonts/chipi.ttf}{color=#a50372}Choko{/color}{/font}"
                        add "images/rps/button_[enemy_]_enemy.png" at rps_animation_image


    frame:
        align(0.1, 0.85)
        padding(20, 20)
        text "{font=fonts/chipi.ttf}{color=#3103a5}You{/color}{/font}: [life_player]" at Transform(zoom=1.2)

    frame:
        align(0.85, 0.85)
        padding(20, 20)

        text "{font=fonts/chipi.ttf}{color=#a50372}Choko{/color}{/font}: [life_choko]" at Transform(zoom=1.2)


    timer 5.5 action Hide("rps_show_status", transition=Dissolve(.2))
init python:
    import math
    import random


init python:

    nonunicode = "¡!¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchtext(length: int):
        output = ""

        for x in range(length):
            output += renpy.random.choice(nonunicode)
        return output

default do_name = "Dorki"
default mc_name = "Metz"
default sa_name = "Sasha"
default he_name = "Hector"
default li_name = "Lili"
default cor_name = _("Presidente")
default w_name = "???"
# default cho_name = "Choko"


init python:
    def random_color():
        colors = [
            "#FF0000", "#001EFF", "#33F000", "#EA00FF",
            "#00FFD2", "#5A00FF", "#FF9C00", "#FFEA00", "#FFFFFF"
        ]
        return renpy.random.choice(colors)





default cho_name = "Choko"

define cho = Character("[cho_name]", image="choko", color="#d117fb")



define do = Character("[do_name]", image='dorki_', dinamic=True, color="#c600b9")
define mc = Character("[mc_name]", image='metz_', color="#0f5400")


define sa = Character("[sa_name]", image='sasha_', color="#5c6200")
define he = Character("[he_name]", image='hector_', color="#225154")

define li = Character("[li_name]", image='lili_', color="#3b184c")
define cor = Character("[cor_name]", image='president', color="#fff")
define w = Character("[w_name]", color="#fff") # cualquiera



default persistent.complex_game = False

default persistent.chapter_actual = 0
default persistent.chapter_loop = False


default persistent.end_cap_120 = False

default persistent.actived_cap_120 = False


image intro_text = Text("🧁Party and cupcake🧁")

default chapter = ChapterBool()
default persistent.day = 0

default image_view_detail = ""

image screamer = "images/cg/screamer.png"


# transform para cambiar colores suavemente
transform color_wipe_anim:
    xalign 0.5 yalign 0.5
    block:
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        easein 4.0 matrixcolor TintMatrix(random_color())
        ease 4.0 matrixcolor TintMatrix(random_color())
        repeat

image pass_remoline = At("images/background_color.png", color_wipe_anim)

image remoline_infinity:
    At("images/remoline_black.png", color_wipe_anim)
    block:
        xpan 0 ypan 180
        linear 10 xpan 360 ypan -180
        repeat

image black = Solid("#000")
image white = Solid("#fff")

image bg_galaxi = Transform("images/bg/bg_galaxi.jpg", size=(1920, 1280))
image bg_cinematic = "images/bg/cinematic.png"

image vignette_1:
    "images/border_black.png"
    block:
        alpha 1.0
        linear .75 alpha 0.2
        repeat

image vignette_2:
    "images/border_black2.png"
    block:
        alpha 1.0
        linear .75 alpha 0.8
        repeat






image reloj_tic_tac = Movie(play="images/reloj_movie.webm", size=(1920, 1080))


##################################################
# DORKI

image blood = Solid("#850000")
image blood_solid = Transform("blood", size=(84, 84))

image blood_img = Transform("gui/blood.webp", size=(124, 124))

image blood_particules:
    zoom 2.0
    xpos 700
    ypos 1650
    xoffset 100
    yoffset 1700
    rotate 180
    ParticuleGravity("blood", count=55, max_radius=700, duration=0.6, max_size=100, gravity=880.0)

image blood_particules_details:
    zoom 1.5
    xalign 0.5
    yalign 0.5
    pos(0.5, 0.5)
    anchor(0.5, 0.5)
    ParticuleGravity("blood_img", count=20, max_radius=700, duration=0.6, max_size=100, gravity=880.0)


image blood_particules_ect:
    zoom 1.3
    xalign 0.5
    yalign 0.5
    pos(0.5, 0.5)
    anchor(0.5, 0.5)
    ParticuleGravity("blood", count=40, max_radius=400, duration=1.0, max_size=100, gravity=910.0)


transform move_slow_cinematic:
    ease 2.0 yoffset -65
    ease 2.0 yoffset 0
    repeat

transform shake_off:
    ease 0.07 yoffset -20
    ease 0.07 yoffset 0
    pause 0.5
    repeat 5

transform shake_cierra:
    ease 0.04 yoffset -35
    ease 0.04 yoffset 0
    repeat

image cinematic_dorki_chainsaw = Composite(
    (1920, 1080),
    (0, 0), "dorki_cg_1_base",
    (0, 0), "chainsaw_animation")


image not_dorki_chainsaw = Composite(
    (1920, 1080),
    (0, 0), "dorki_cg_1_base",
    (0, 0), At("compositer_cierra2", shake_cierra))


image dorki_cg_1_base = "images/cg/dorki_base.png"
image dorki_cg_2_base = "images/cg/base_2.png"

image cierra_normal = "images/cg/cierra_a1.png"

image cierra_frame1 = "images/cg/cierra_a1.png"
image cierra_frame2 = "images/cg/cierra_a3.png"

image cierra_frame1_move = "images/cg/cierra_a2.png"
image cierra_frame2_move = "images/cg/cierra_a4.png"

image compositer_cierra1 = Composite(
    (1920, 1080),
    (0, 0), "slow1_cierra_move")

image compositer_cierra2 = Composite(
    (1920, 1080),
    (0, 0), "fast2_cierra_move",
    (0, 0), "frame_motion_cierra")

image chainsaw_animation:
    At("compositer_cierra1", shake_off)
    4.0
    At("compositer_cierra2", shake_cierra)
    0.3

image frame_motion_cierra:
    "images/cg/effect_1.png"
    0.02
    "images/cg/effect_2.png"
    0.02
    "images/cg/effect_3.png"
    0.02
    repeat

image fast2_cierra_move:
    "cierra_frame1_move"
    0.03
    "cierra_frame2_move"
    repeat

image slow1_cierra_move:
    "cierra_frame1"
    0.03
    "cierra_frame1"
    repeat

##################################################

image dorki_ grey = "images/dorki/dorki_grey.png"
image dorki_ black = "images/dorki/black1.png"

image dorki_ dark1 = "images/dorki/black1.png"
image dorki_ dark2 = "images/dorki/black2.png"
image dorki_ dark3 = "images/dorki/black3.png"

image dorki_ dark_animation:
    choice:
        "dorki_ dark1"
        1.2
        "dorki_ dark2"
        1.2
    choice:
        "dorki_ dark1"
        0.01
        "dorki_ dark3"
        0.01
        "dorki_ dark1"
        0.01
        "dorki_ dark3"
        0.01
        "dorki_ dark1"
        0.01
        "dorki_ dark3"
        0.01
    repeat



image dorki_ normal = "images/dorki/dorki_normal.png"
image dorki_ dorki = "images/dorki/dorki_dorki.png" # es lo mismo que feliz
image dorki_ dorki2 = "images/dorki/dorki_dorki2.png" # es lo mismo que feliz
image dorki_ sad = "images/dorki/dorki_sad.png"
image dorki_ sad2 = "images/dorki/dorki_sad2.png"
image dorki_ angry = "images/dorki/dorki_normal.png"
image dorki_ suprise = "images/dorki/dorki_suprise.png"
image dorki_ confusion = "images/dorki/dorki_confusion.png"
image dorki_ lol1 = "images/dorki/dorki_lol1.png"
image dorki_ lol2 = "images/dorki/dorki_lol2.png"
image dorki_ lol3 = "images/dorki/dorki_lol3.png"

image dorki_ cry1 = "images/dorki/dorki_cry1.png"
image dorki_ cry2 = "images/dorki/dorki_cry2.png"
image dorki_ cry3 = "images/dorki/dorki_cry3.png"

image dorki_ shock = "images/dorki/scene_jumscare/dorki_jumscare.png"
image dorki_ jums1 = "images/dorki/scene_jumscare/dorki_jumscare.png"
image dorki_ jums2 = "images/dorki/scene_jumscare/dorki_jumscare0.png"
image dorki_ jums3 = "images/dorki/scene_jumscare/dorki_jumscare2.png"
image dorki_ jums4 = "images/dorki/scene_jumscare/dorki_jumscare3.png"
image dorki_ jums5 = "images/dorki/scene_jumscare/dorki_jumscare4.png"
image dorki_ jums6 = "images/dorki/scene_jumscare/dorki_jumscare5.png"

image dorki_ eh1 = "images/dorki/scene_ehh/dorki_blur1.png"
image dorki_ eh2 = "images/dorki/scene_ehh/dorki_blur2.png"
image dorki_ eh3 = "images/dorki/scene_ehh/dorki_blur3.png"

image dorki_ gore1 = "dorki/scene_jumscare/dorki_gore.png"
image dorki_ gore2 = "dorki/scene_jumscare/dorki_gore_2.png"

image clouth_break: 
    "images/dorki/scene_no/clouth_break.png"
    0.4
    Null(width=100)


image censure_dorki = Null(width=100)

image dorki_ des_im1 = "images/dorki/scene_no/dorki.png"
image dorki_ des_im2 = "images/dorki/scene_no/dorki_2.png"
image dorki_ des_im3 = "images/dorki/scene_no/dorki_3.png"

image dorki_ des1 =  Composite(
    (1480, 1890),
    (0, 0), "dorki_ des_im1",
    (0, 0), "censure_dorki")

image dorki_ des2 =  Composite(
    (1480, 1890),
    (0, 0), "dorki_ des_im2",
    (0, 0), "censure_dorki")

image dorki_ des3 =  Composite(
    (1480, 1890),
    (0, 0), "dorki_ des_im3",
    (0, 0), "censure_dorki")





image dorki_clon_sys1:
    RGBTrail("images/dorki/black1.png", offset=80, speed=0.1)
    subpixel True
    xcenter 950
    zoom 0.70
    yoffset -440
    ypos 1000
    function sound_effect_ondas
    block:
        easein 2.0 xoffset -250
        easein 2.0 xoffset 620
        easein 2.0 xoffset 160
        pause 2.5
        repeat

image red_s = Solid("#ff0000")
image red_solid = Transform("red_s", size=(12, 12))

image white_s = Solid("#fff")
image white_solid = Transform("white_s", size=(12, 12))

image vignette_down:
    "images/bg/exttr.png"
    alpha 1.0
    block:
        ease 7 alpha 0.4
        ease 7 alpha 0.75
        ease 12 alpha 0.1
        repeat


image particules_white_blosson = SnowBlossom(
    "white_solid", 
    count=35, 
    border=55, 
    xspeed=(22, 220), 
    yspeed=(100, 440), 
    start=5, 
    fast=False, 
    horizontal=False)


image particules_red_blosson = SnowBlossom(
    "red_solid", 
    count=120, 
    border=55, 
    xspeed=(22, 220), 
    yspeed=(100, 220), 
    start=9, 
    fast=False, 
    horizontal=False)

##################################################
# SASHA

image sasha_ normal = "sasha/sasha_normal.png"
image sasha_ confusion = "sasha/sasha_confusion.png"
image sasha_ happy = "sasha/sasha_happy.png"
image sasha_ lol = "sasha/sasha_lol.png"
image sasha_ normal2 = "sasha/sasha_neutral.png"
image sasha_ angry = "sasha/sasha_angry.png"
image sasha_ sad = "sasha/sasha_sad.png"

image sasha_ shock = "sasha/sasha_shock.png"

image sasha_ dark:
    "images/sasha/corrupted/crr1.png"
    0.1
    "images/sasha/corrupted/crr2.png"
    0.1
    "images/sasha/corrupted/crr3.png"
    0.1
    choice:
        "images/sasha/corrupted/crr4.png"
        0.1
    choice:
        "images/sasha/corrupted/crr1.png"
    repeat


##################################################
# LILI


image lili_ normal = "images/lili/lili_normal.png"
image lili_ dude = "images/lili/lili_dude.png"
image lili_ sad = "images/lili/lili_sad.png"
image lili_ sad2 = "images/lili/lili_sad2.png"
image lili_ lol = "images/lili/lili_lol.png"
image lili_ confusion = "images/lili/lili_confusion.png"
image lili_ shock = "images/lili/lili_shock.png"

image lili_ corrupted = "images/lili/corrupted/lili_corrupted.png"

######################################################################
# HECTOR
# aun me falta hacerlo


image hector_ normal = "hector/hector_normal.png"
image hector_ happy = "hector/hector_happy.png"
image hector_ confusion = "hector/hector_confusion.png"
image hector_ sad = "hector/hector_sad.png"
image hector_ shock = "hector/hector_shock.png"
image hector_ corrupted = "images/hector/hector_corrupcion.png"

######################################################################
##################################################
# CHOKO

# Ejemplo de efecto arcoiris hacia atras
# puede ser posible si logramos que se sincronice los movimientos



# image whites_s = Solid("#ffffff")
# image whites_solid = Transform("whites_s", size=(12, 12))

# image purple = Solid("#6600a6")
# image purple_solid = Transform("purple", size=(32, 32))

image effect_parti_pink:
    "gui/particule.pink.webp"
    ease 1.0 alpha 0.00
    ease .75 alpha 1.00
    repeat

image effect_parti_purple:
    "gui/particule.purple.webp"
    ease 1.0 alpha 0.00
    ease .75 alpha 1.00
    repeat

image effect_parti_white:
    "gui/particule.red.webp"
    ease 1.0 alpha 0.00
    ease .75 alpha 1.00
    repeat

image purple_particules:
    zoom 1.5
    xpos 1300
    ypos 1600
    xoffset 450
    yoffset 550
    rotate 80
    AnimationCube("effect_parti_purple", count=8, frequency=0.4, max_size=900, speed=0.01, amount=1.2, cycle_duration=2.2)

image pinks_particules:
    zoom 1.5
    xpos 1300
    ypos 1600
    xoffset -20
    yoffset 520
    rotate 30
    AnimationCube("effect_parti_pink", count=15, frequency=0.4, max_size=1200, speed=0.02, amount=1.2, cycle_duration=2.2)

image whites_particules:
    zoom 1.7
    xpos 1300
    ypos 1600
    xoffset -100
    yoffset 550
    AnimationCube("effect_parti_white", count=11, frequency=0.4, max_size=1000, speed=0.02, amount=1.0, cycle_duration=2.0)

#########################################################################################################
#########################################################################################################

image choko animation_explode_blood:
    "images/choko/part3.png"
    2.0
    block:
        easeout 1.5 yoffset 700

image choko_head_fly_1:
    "images/choko/head_1.png"
    subpixel False
    align(0.5, 0.3)
    zoom 0.66

    block:
        easein .25 yoffset -225 xoffset 0 rotate 0
        ease 1.7 yoffset 900 xoffset 0 rotate 360

image choko_head_fly_2:
    "images/choko/head_2.png"
    subpixel False
    align(0.5, 0.25)
    zoom 0.66

    block:
        easein .25 yoffset -270 xoffset 0 rotate 0
        ease 2.0 yoffset 900 xoffset 0 rotate 190


image choko_head_fly_3:
    "images/choko/body_1.png"
    subpixel False
    align(0.70, 0.45)
    zoom 0.66
    xzoom -1.0    

    block:
        rotate 120
        easein .25 yoffset -140 xoffset -55 
        ease 0.9 yoffset 900 xoffset -82 rotate 50

image choko_head_fly_4:
    "images/choko/body_1.png"
    subpixel False
    align(0.3, 0.45)
    zoom 0.66
    xzoom -1.0

    block:
        easein .25 yoffset -80 xoffset 57 rotate -30
        ease 0.85 yoffset 900 xoffset 67 rotate 70


image gore_animation_blood:
    "images/choko/blood1.png"
    0.1
    "images/choko/blood2.png"
    0.1
    Null(width=100)




image choko normal = "choko/choko_normal.png"
image choko victory = "choko/choko_victory.png"

image choko confusion = "choko/choko_confusion.png"
image choko confusion2 = "choko/choko_confusion2.png"
image choko love = "choko/choko_love.png"
image choko shock = "choko/choko_shock.png"

image choko creepy1 = "choko/choko_creepy1.png"
image choko creepy2 = "choko/choko_creepy2.png"
image choko creepy3 = "choko/choko_creepy3.png"
image choko creepy4 = "choko/choko_creepy4.png"

image choko angry1 = "choko/choko_angry_1.png"
image choko angry2 = "choko/choko_angry_2.png"

image choko mode_colors = Composite((1480, 1890), (0, 0), "choko_clon_sys2", (0, 0), "choko victory")
image choko mode_colors2 = Composite((1480, 1890), (0, 0), "choko_clon_sys1", (0, 0), "choko normal")

image choko hurra = "images/choko/choko_hurra.png"
image choko hurra2 = "images/choko/choko_hurra2.png"

image choko animation_angry:
    function sound_terremoto
    "choko angry2"
    pause 0.17
    "choko angry1"
    pause 0.17
    "choko angry2"
    pause 0.17
    "choko angry1"
    pause 0.17
    "choko angry2"
    pause 0.17
    "choko angry1"
    pause 0.17
    "choko angry2"
    pause 0.17
    "choko angry1"
    pause 0.17
    "choko angry2"
    pause 0.17
    "choko angry1"
    pause 0.17



image animation_choko_remoline:
    zoom 0.62 xalign 0.5
    block:
        "choko remoline"
        ease .45 xalign 0.15 
        pause 0.2
        "choko hurra"
        pause 0.1
        "choko remoline"
        ease .45 xalign 0.8
        pause 0.2
        xzoom -1.0
        "choko hurra2"
        pause 0.2
        "choko remoline"
        ease .45 xalign 0.5
        pause 0.1
        xzoom 1.0
        "choko victory"


image choko_attack:
    "images/choko/fr1.png"
    0.01
    "images/choko/fr2.png"
    0.01
    "images/choko/fr3.png"
    0.01
    "images/choko/fr4.png"
    0.01
    "images/choko/fr5.png"
    0.01
    "images/choko/fr6.png"
    0.01
    Null(width=100)


image choko_clon_sys1:
    RGBTrail("choko/choko_clon.png", offset=188, speed=0.1)

image choko_clon_sys2:
    RGBTrail("choko/choko_clon2.png", offset=188, speed=0.1)

image choko remoline:
    "images/choko/rem1.png"
    0.04
    "images/choko/rem2.png"
    0.04
    repeat

######################################################################
##################################################




# me dio un poco de flojera con hecto xd

transform zoom_z_layer(p_x=0.5, p_y=0.5, z=1.5, linear_time=1.0):
    subpixel True
    anchor (p_x, p_y)   # El centro
    pos (p_x, p_y)      # Posición en el centro de la pantalla
    zoom 1.0
    linear linear_time zoom z
    block:
        ease .45 zoom 1.0
        block:
            linear 0.01 xoffset -8 yoffset 2
            linear 0.01 xoffset 7 yoffset -3
            linear 0.01 xoffset 6 yoffset -4
            linear 0.01 xoffset -4 yoffset 3
            linear 0.01 xoffset 5 yoffset 2
            linear 0.01 xoffset -5 yoffset 4
            linear 0.01 xoffset 0 yoffset 0
            repeat 7


init python:
    def reset_alpha(trans, st, at):
        trans.alpha = 1.0
        return None

    def reset_zoom(trans, st, at):
        trans.zoom = 0.62
        return None



transform t_position(x=950, z=0.62, yoff=40, y=1.00):
    subpixel True
    zoom z
    yanchor 1.00
    yoffset yoff
    ypos y

    on show:
        function reset_alpha
        function reset_zoom
        zoom 0.64 alpha 0.00
        xcenter x
        ease .2 zoom z alpha 1.00
    on replace:
        function reset_alpha
        function reset_zoom
        choice:
            easein .1 yzoom 0.99
            easein .1 yzoom 1.00
        choice:
            easein .1 yzoom 1.01
            easein .1 yzoom 1.00
        choice:
            pass
        easein .2 xcenter x
    on hide:
        function reset_alpha
        function reset_zoom
        linear .45 zoom 0.60 alpha 0.00


transform pos_t11:
    t_position(x=950)

transform pos_t21:
    t_position(x=550)

transform pos_t22:
    t_position(x=1300)

transform pos_t31:
    t_position(x=280)

transform pos_t32:
    t_position(x=960)

transform pos_t33:
    t_position(x=1550)


transform pos_t41:
    t_position(x=320)

transform pos_t42:
    t_position(x=680)

transform pos_t43:
    t_position(x=1150)

transform pos_t44:
    t_position(x=1550)



transform shake_try(ts=0.01, r=9):
    linear ts xoffset -8 yoffset 2
    linear ts xoffset 7 yoffset -3
    linear ts xoffset 6 yoffset -4
    linear ts xoffset -4 yoffset 3
    linear ts xoffset 5 yoffset 2
    linear ts xoffset -5 yoffset 4
    linear ts xoffset 3 yoffset -6
    linear ts xoffset 4 yoffset -8
    linear ts xoffset -6 yoffset 1
    linear ts xoffset 4 yoffset 2
    linear ts xoffset 0 yoffset 0
    repeat r

transform shake_slayer(ts=0.03, z=1.0):
    zoom z
    linear ts xoffset -8 yoffset 2
    linear ts xoffset 7 yoffset -3
    linear ts xoffset 6 yoffset -4
    linear ts xoffset -4 yoffset 3
    linear ts xoffset 5 yoffset 2
    linear ts xoffset -5 yoffset 4
    linear ts xoffset 3 yoffset -6
    linear ts xoffset 4 yoffset -8
    linear ts xoffset -6 yoffset 1
    linear ts xoffset 4 yoffset 2
    linear ts xoffset 0 yoffset 0
    repeat





image cubes_red_background = "cubes_background.png"
image background_pink_blur = "background_blur.png"

image cube_red = "cube_just.png"

image black = "#000"
image white = "#fff"



image noise_a:
    "noise1.jpg"
    0.001
    "noise2.jpg"
    0.001   
    "noise3.jpg"
    0.001  
    "noise4.jpg"
    0.001
    repeat  

image noise = Transform("noise_a", size=(1920, 1080))


screen glitch_blocks(opacidad_=0.5):

    zorder 6

    add "noise" at glitch_alpha_static(opacity=0.16)
    add GlitchSlices(max_offset=32, num_blocks=10) at glitch_estatic(opacity=0.1)
    add GlitchSlices(max_offset=32, num_blocks=8) at glitch_estatic(opacity=0.2)
    add GlitchSlices(max_offset=32, num_blocks=8) at glitch_estatic(opacity=0.14)



transform glitch_estatic_yp:
    ypan 0 alpha 0.40
    block:
        linear 0.5 xpan 360 ypan 90 zoom 1.05 alpha 0.55
        xpan 0 ypan 0 zoom 1.00 alpha 0.2
        repeat



transform glitch_alpha_static(opacity=0.2):
    alpha opacity
    choice:
        linear .8 alpha 0.02*0.4
        linear .8 alpha 0.4
    choice:
        linear .8 alpha 0.02*0.2
        linear .8 alpha 0.4
    pause 3.5
    repeat



transform glitch_estatic(opacity=0.1):
    alpha opacity xalign 0.5
    choice:
        linear 2 yoffset -1150 alpha 0.02*0.4
    choice:
        linear 1.4 yoffset 1150 alpha 0.02*0.4
    choice:
        linear 1 yoffset -1150 alpha 0.02*0.2
    choice:
        linear 1.2 yoffset 1150 alpha 0.02*0.4
    repeat      



init python:
    def sound_effect_ondas(trans, st, at):
        renpy.music.play('audio/oceano.ogg', channel='sound', loop=True)

    def sound_terremoto(trans, st, at):
        renpy.music.play('audio/terremoto.ogg', channel='sound', loop=False)


define transition_pass = MultipleTransition([
    False, ImageDissolve("images/infinity_pass.png", 2.4, ramplen=64),
    Solid("#fff"), Dissolve(.2),
    Solid("#000"), ImageDissolve("images/infinity_pass.png", 0.2, ramplen=64),
    Solid("#fff"), Dissolve(.2),
    Solid("#000"), ImageDissolve("images/infinity_pass.png", 0.2, ramplen=32), 
    Solid("#fff"), ImageDissolve("images/infinity_pass.png", 2.5, ramplen=32, reverse=True),
    True])


define dissolve_scene = MultipleTransition([
    False, ImageDissolve("images/infinity_pass.png", 0.5, ramplen=64),
    Solid("#000"), Dissolve(.2),
    Solid("#fff"), Dissolve(.2),
    True])


define wipeleft = MultipleTransition([
    False, ImageDissolve("images/background_color.png", 0.5, ramplen=64),
    Solid("#000"), ImageDissolve("images/background_color.png", 0.5, ramplen=64),
    True])


define fade_white = Fade(0.2, 0.0, 0.2, color='#fff')

define effect_tic_tac = MultipleTransition([
    False, ImageDissolve("images/infinity_pass.png", 1.5, ramplen=64),
    Solid("#fff"), Dissolve(.2),
    Solid("#000"), ImageDissolve("images/infinity_pass.png", 0.2, ramplen=64),
    Solid("#fff"), Dissolve(.2),
    Solid("#000"), ImageDissolve("images/infinity_pass.png", 0.7, ramplen=64, reverse=True),
    True])


define remoline_pass = MultipleTransition([
    False, ImageDissolve("images/remoline_with.png", 1.0, ramplen=32),
    Solid("#360b2c"), Dissolve(.2),
    Solid("#000"), ImageDissolve("images/remoline_with.png", 0.75, ramplen=32), 
    Solid("#000"), Dissolve(.2),
    Solid("#2a0a27"), ImageDissolve("images/remoline_with.png", 2.0, ramplen=64, reverse=True),
    True])




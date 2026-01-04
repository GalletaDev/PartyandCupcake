label assassin_1_sasha:
    stop music fadeout 3.0
    scene coop_dia
    show dorki_ jums6 at pos_t22
    show sasha_ normal at pos_t21
    do "Hola Sasha"
    $ sa_name = "Sasha"
    show sasha_ sad
    sa "Eh? donde estoy"
    show dorki_ jums5
    do "Me están obligando a hacer cosas realmente desesperantes."
    show dorki_ gore2
    do "Espero que entiendas."
    show sasha_ shock:
        ease 5 xoffset -80
    sa "N-No, y eso que tienes alli."
    do "Oh, un regalo para ti."
    do "Es para ver tu hermosa, cara..."
    show layer master at shake_try(r=6)
    show sasha_ shock
    sa "¿Que?"
    scene black
    show coop_dia

    play sound chainsaw_now
    play music bg_dorkis_day_gore
    show cinematic_dorki_chainsaw
    show layer master at zoom_z_layer(p_x=0.7, p_y=0.25, z=1.3, linear_time=0.5)
    with Dissolve(.25)
    
    window hide
    window auto
    $ renpy.pause(5.0, hard=True)
    do "!Venga que caiga el confeti de la fiesta¡{nw=2.0}"
    hide cinematic_dorki_chainsaw
    show dorki_cg_2_base at shake_cierra
    show layer master at shake_slayer(ts=0.01, z=1.08)
    
    show coop_dia:
        matrixcolor InvertMatrix(0.0)
        ease 2 alpha 1.00 matrixcolor InvertMatrix(1.0)
    
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"



    show layer master
    hide dorki_cg_2_base
    show not_dorki_chainsaw
    hide blood_particules
    show layer master at zoom_z_layer(p_x=0.7, p_y=0.25, z=1.3, linear_time=0.5)
    with Dissolve(.25)
    do "!Que lindo¡"
    do "A pesar de todo sabemos que tu eres una terrible presidenta"
    do "Siempre lo fuiste perra."
    do "Ahora tocara el siguiente que se me cruce"
    "Sera mejor irme en este tiempo..."
    stop music fadeout 3.0
    show layer master
    jump start



label assassin_2_lili:
    stop music fadeout 3.0
    scene coop_dia
    show dorki_ jums6 at pos_t22
    show lili_ normal at pos_t21

    do "Vaya, hola Lili..."
    $ li_name = "Lili"
    show lili_ confusion
    li "¿Que?"
    li "¿Donde estoy?"
    show lili_ sad2
    do "Estas en el regalo tuyo."
    show dorki_ jums5 
    do "Ahora mismo estoy dando todo de mi para poder..."
    do "Darte un premio."
    show dorki_ gore2
    show lili_ shock:
        ease 5 xoffset -80
    do "Jeje... JAJAJA"
    do "Esto realmente es una perdida de tiempo haciendo esto."
    show lili_ shock:
        ease 5 xoffset -100
    li "Dorki por lo que sea que hice, te aseguro que nunca creí nada de ti."
    li "Si es por las mentiras de varios Días, te digo que yo no fui"
    scene black
    show screamer at zoom_z_layer(linear_time=0.01)
    do "Eh?"
    do "Eso que importa perra."
    show screamer at zoom_z_layer(linear_time=0.2)
    do "!Solo importa hacer confeti con tu{w} cara¡"
    show screamer at zoom_z_layer(linear_time=0.06)
    li "!ESPERA¡{nw=2.0}"
    scene black
    show coop_dia
    play music bg_dorkis_day_gore
    play sound chainsaw_now
    show layer master at zoom_z_layer(p_x=0.7, p_y=0.25, z=1.3, linear_time=0.5)
    show cinematic_dorki_chainsaw
    with Dissolve(.25)
    
    window hide
    window auto
    $ renpy.pause(8.0, hard=True)

    hide cinematic_dorki_chainsaw
    show dorki_cg_2_base at shake_cierra
    show layer master at shake_slayer(ts=0.01, z=1.08)
    
    show coop_dia:
        matrixcolor InvertMatrix(0.0)
        ease 3 alpha 1.00 matrixcolor InvertMatrix(0.7)
    
    show blood_particules 
    li "!AHHHHHHHH¡{nw=0.2}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"

    show layer master
    hide dorki_cg_2_base
    show not_dorki_chainsaw
    hide blood_particules
    show layer master at zoom_z_layer(p_x=0.7, p_y=0.25, z=1.3, linear_time=0.5)
    with Dissolve(.25)


    do "A pesar de ser una cara bonita."
    do "Eres una pesada para decir que tu solo sufres"
    do "No seas tonta, el mundo esta mas feo que tu."

    "Su temperamento exagero un poco..."
    stop music fadeout 3.0
    show layer master
    jump start

label assassin_3_hector:
    stop music fadeout 3.0

    scene coop_dia
    show dorki_ jums6 at pos_t22
    show hector_ shock at pos_t21

    play music bg_dorkis_day_gore
    do "Hector, te presento a la moto sierra rompe tripas."
    do "¿Te gusta el nombre que le di?"
    $ he_name = "Hector idiot"
    show hector_ happy
    he "Oh, si vamos, ya deseaba eso"
    he "Siempre desee que me cortaran las tripas"
    play sound ambruto
    stop music
    show dorki_ confusion
    do "...."
    show dorki_ sad
    do "Bueno..."
    show dorki_ sad2
    do "Eso fue inesperado"
    show dorki_ sad
    do "Esto..."
    show dorki_ lol2
    do "Tsk, no importa..."
    play music bg_dorkis_day_gore
    show dorki_ gore2
    do "!Bueno, aquí vamos¡"
    do "Vamos a hacer galletas y confeti contigo"

    scene black
    show coop_dia
    play sound chainsaw_now
    show cinematic_dorki_chainsaw
    show layer master at zoom_z_layer(p_x=0.7, p_y=0.25, z=1.3, linear_time=0.5)
    with Dissolve(.25)
    
    $ renpy.pause(8.0, hard=True)

    hide cinematic_dorki_chainsaw
    show dorki_cg_2_base at shake_cierra
    show layer master at shake_slayer(ts=0.01, z=1.08)
    show coop_dia:
        matrixcolor InvertMatrix(0.0)
        ease 3 alpha 1.00 matrixcolor InvertMatrix(0.7)
    

    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"
    show blood_particules 
    do "!JAJAJAJAJA¡{nw=0.3}"
    do "!JAJAJAJAJA¡{nw=0.3}"  

    show layer master
    hide dorki_cg_2_base
    show not_dorki_chainsaw
    hide blood_particules
    show layer master at zoom_z_layer(p_x=0.7, p_y=0.25, z=1.3, linear_time=0.5)
    with Dissolve(.25)

    do "Solo dire que eres raro."

    "Hasta yo me sorprendí..."
    "Y confirmo..."
    show layer master
    stop music fadeout 3.0
    jump start

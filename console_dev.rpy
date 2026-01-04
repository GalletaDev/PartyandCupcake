

screen console_chapter():

    default show_screen_console = True

    tag console   # para poder ocultar con hide screen console

    key "p" action [
        If(show_screen_console,
        true=SetLocalVariable("show_screen_console", False),
        false=SetLocalVariable("show_screen_console", True))
    ]

    if show_screen_console:
        frame:
            xalign 0.02
            yalign 0.02
            xsize 320
            ysize 380

            vbox:
                text "{size=18}{i} CONSOLE - Capítulo / Decisiones {/i}{/size}"

                spacing 8
                text "Cap actual: [chapter.get_quantity()]"
                text "Día: [persistent.day]"
                text "Loop: [chapter.get_loop_view()]"
                text "Expression dorki: [image_view_detail]"

                bar:
                    xsize 280
                    ysize 25
                    value AnimatedValue(value=int(chapter.get_quantity()), range=100, delay=.75)

                text "{size=14} Últimos registros (más recientes arriba): {/size}"

                text "Presiona 'p' para ocultar"



init python:
    class ChapterBool:
        def __init__(self):
            self.update_from_persistent()

        def update_from_persistent(self):
            self.chapter = persistent.chapter_actual
            self.while_bucle = persistent.chapter_loop

        def sync_to_persistent(self):
            persistent.chapter_actual = self.chapter
            persistent.chapter_loop = self.while_bucle
            renpy.save_persistent()

        def add_ch(self, add=1):
            self.chapter += add
            self.sync_to_persistent()
            self.update_from_persistent()

        def return_ch(self, rem=1):
            self.chapter -= rem
            self.sync_to_persistent()
            self.update_from_persistent()

        def set_ch(self, chapter):
            self.chapter = chapter
            self.sync_to_persistent()
            self.update_from_persistent()

        def view_status(self):
            value1 = print(f"Chapter copy:{self.chapter}/ copy loop{self.while_bucle}")
            value2 = print(f"data real chapter:{persistent.chapter_actual}/ data loop real:{persistent.chapter_loop}")
            return print(value1, value2)

        def get_quantity(self):
            return self.chapter

        def get_loop_view(self):
            return self.while_bucle

        def reset(self, reset_=0):
            self.chapter = reset_
            self.while_bucle = False
            print(f"Chapter copy:{self.chapter}/ Chapter real:{persistent.chapter_actual}")
            self.sync_to_persistent()

        def check_condition_and_revert(self, ok=False):
            self.while_bucle = bool(ok)
            if not self.while_bucle:
                self.while_bucle = False
                renpy.notify("While True")
            else:
                self.while_bucle = False
                renpy.notify("While False")
                self.return_ch()



init python:

    def reset_name_characters():
        global he_name, li_name, sa_name, do_name
        sa_name = "???"
        li_name = "???"
        he_name = "???"
        do_name = "Dorki"

    def reset_day_game():
        persistent.day = 1
        renpy.save_persistent()
    
    def reset_game_full():
        global chapter
        chapter.reset()
        persistent.day = 1
        persistent.actived_cap_120 = False
        persistent.end_cap_120 = False
        renpy.save_persistent()

    def active_game_reset_button():
        persistent.complex_game = True
        renpy.save_persistent()     

    def off_game_reset_button():
        persistent.complex_game = False
        renpy.save_persistent()     

init python:
    # 130: "normal_1_dorkis",

    def get_jump_label():
        dict_chapter_all = {
        120: "world_break_matrix",
        105: "talk_15_dorki",
        104: "talk_14_dorki",
        103: "talk_13_dorki",
        102: "talk_12_dorki",
        101: "talk_11_dorki",
        100: "talk_10_dorki",
        99: "talk_9_dorki",
        98: "talk_8_dorki",
        97: "talk_7_dorki",
        96: "talk_6_dorki",
        95: "talk_5_dorki",
        94: "talk_4_dorki",
        93: "talk_3_dorki_gore",
        92: "talk_2_dorki",
        91: "talk_1_dorki",
        90: "sorry_metz",
        85: "how_10_dorki",
        78: "how_9_dorki_reveal_chest",
        74: "how_8_dorki",
        70: "how_7_dorki",
        65: "assassin_3_hector",
        55: "assassin_2_lili",
        45: "break_1_dorki_gore",
        35: "repeat_1_dorki",
        34: "how_6_dorki",
        33: "how_5_dorki_reveal_chest",
        29: "how_4_dorki",
        25: "madness_1_dorki",
        24: "assassin_1_sasha",
        15: "distortion_1_dorki",
        13: "how_3_dorki",
        10: "how_2_dorki",
        5:  "how_1_dorki",
        }

        chapter_num = chapter.get_quantity()

        # Capítulos muy altos (explícito)
        if chapter_num >= 130:
            return "normal_1_dorkis"
        elif chapter_num >= 120:
            return "world_break_matrix"

        if chapter_num in dict_chapter_all:
            return dict_chapter_all[chapter_num]

        # Aleatoriedad para 50 < x <= 80
        if 50 < chapter_num <= 80:
            r = renpy.random.random()
            if r < 0.6:
                return "jump_choice_game_" + str(renpy.random.randint(1, 2))
            else:
                # renpy.notify("Jump loop now")
                persistent.day += 1
                renpy.save_persistent()
                return "normal_0_dorkis"

        persistent.day += 1
        renpy.save_persistent()
        return "normal_0_dorkis"




# label after_load:
    
#     if persistent.chapter_actual >= 120 and not persistent.end_cap_120 == True:
#         $ persistent.actived_cap_120 = True
#     if persistent.end_cap_120:
#         $ persistent.actived_cap_120 = False

    # play sound transition_sound
    # scene white with Dissolve(.65)
    # $ renpy.pause(.75, hard=True)
    # play sound reloj_sound_normal
    # $ reset_name_characters()
    # show reloj_tic_tac
    # show background_pink_blur:
    #     pause 0.6
    #     easeout 2.0 alpha 0.4
    # show cubes_red_background:
    #     subpixel True
    #     yoffset 100
    #     ease 1.2 yoffset -600
    #     easeout 2.7 yoffset 600  
    # with Dissolve(.2)   

    # show layer master at shake_try(r=6)
    # $ renpy.pause(3.2, hard=True)
    # stop sound fadeout 1.7
    # scene black with Dissolve(.6)
    # play sound transition_sound
    # pause 0.1
    # $ jump_label = get_jump_label()
    # show layer master
    # $ renpy.pause(predict=True)
    # jump expression jump_label



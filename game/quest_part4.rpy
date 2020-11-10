init:



    $ candy_colleted = 0
    $ key_garage_colleted = 0
    $ part4_bonusanim = False






define qustion1 = False
define qustion2 = False
define qustion3 = False
define qustion4 = False
define qustion4_close = False
define qustion5 = False
default KeyGarage1 = False
default Candy1 = False
default Candy1_collected = False
default Candy2 = False
default Candy2_collected = False
default Candy3 = False
default Candy3_collected = False
default Candy4 = False
default Candy4_collected = False
default Candy5 = False
default Candy5_collected = False
default Candy6 = False
default Candy6_collected = False




label quest_1:

    jump koridor1

label quest_part4_end:

    hide screen mirage_score_1
    scene black with d
    pause
    $ part4_bonusanim = True
    jump angel_sex_1




transform map_arrow_anim:
    subpixel True
    on idle:
        block:
            linear 0.1 rotate 0
    on hover:

        block:
            linear 0.1 rotate 20
            linear 0.1 rotate 0
            linear 0.1 rotate -20
            linear 0.1 rotate 0

label part4_info:

    scene part4_info

    $ renpy.block_rollback()
    call screen part4_info

label tualet1:

    scene tualet2

    $ renpy.block_rollback()
    show screen mirage_score_1
    call screen tualet1




label garag1:

    $ renpy.block_rollback()
    show screen mirage_score_1
    scene garag
    call screen garag1

label garag2:

    $ renpy.block_rollback()
    show screen mirage_score_1
    scene garag2
    call screen garag2

label koridor1:

    $ renpy.block_rollback()
    show screen mirage_score_1
    scene koridor
    call screen koridor1


label krylco1:

    $ renpy.block_rollback()
    show screen mirage_score_1
    scene krylco
    call screen krylco1

label stena1:

    $ renpy.block_rollback()
    show screen mirage_score_1
    scene stena
    call screen stena1




label menu_mike_1:


    menu:

        "Ask for the garage key." if qustion4 == True and qustion5 == False:

            bigmaike "It's somewhere in the yard."
            $ qustion5 = True
            jump tualet1

        "Ask for the garage key." if qustion4 == True and qustion5 == True:

            s "You have already asked for it."
            jump tualet1


label menu_tim_1:



    menu:



            "Ask for a dose of Mirage." if qustion1 == False:

                f "Can I have a dose?"
                tim "There should be one on Elsa's bed."
                $ qustion1 = True
                $ Candy1 = True
                jump room1

            "Ask for another dose." if candy_colleted == 1 and qustion2 == False:

                tim "It's somewhere around here. Why don't you look for it?"
                $ qustion2 = True
                $ Candy2 = True


                jump room1

            "Ask where another dose could be." if candy_colleted == 2 and qustion3 == False:


                tim "Check out the garage."
                $ qustion3 = True
                $ qustion4 = True
                $ Candy3 = True
                jump room1








label room1:

    $ renpy.block_rollback()
    show screen mirage_score_1
    scene room1


    if Candy1 == False:

        call screen room1

    elif Candy1 == True and Candy1_collected == False:

        call screen room1_2

    elif Candy1 == True and Candy1_collected == True:

        call screen room1_3



label room2:

    $ renpy.block_rollback()
    show screen mirage_score_1
    scene room2
    call screen room2

screen part4_info():

    $ clickable = True

    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action [Jump("koridor1")]


    imagebutton auto "gui/AngelQuestHelp_%s.png" xcenter 0.5 yalign 0.99 focus_mask True  action OpenURL("https://www.patreon.com/posts/28566360")



screen room1():

    $ clickable = True



    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action [Jump("koridor1")]



    if Candy1 == True:

        imagebutton:

            at map_arrow_anim
            xalign 0.0
            yalign 0.5
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

            if clickable == True:
                action [Jump("room2")]


    imagebutton:

        at map_arrow_anim
        xpos 1000
        ypos 500
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )

        if Candy1 == False:
            action [Jump("menu_tim_1")]


screen room1_2():

    $ clickable = True



    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action [Jump("koridor1")]



    if Candy1 == True:

        imagebutton:

            at map_arrow_anim
            xalign 0.0
            yalign 0.5
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

            if clickable == True:
                action [Jump("room2")]




    imagebutton:

        at map_arrow_anim
        xpos 1000
        ypos 500
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )

        if Candy1 == True:
            action [Jump("menu_tim_1")]

screen room1_3():

    $ clickable = True



    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action Jump("koridor1")



    if Candy1 == True:

        imagebutton:

            at map_arrow_anim
            xalign 0.0
            yalign 0.5
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

            if clickable == True:
                action Jump("room2")



    imagebutton:

        at map_arrow_anim
        xpos 1000
        ypos 500
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )

        if Candy1 == True:
            action [Jump("menu_tim_1")]


screen room2():

    $ clickable = True




    imagebutton:

        at map_arrow_anim
        xpos 930
        ypos 950
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

        if clickable == True:
            action Jump("room1")


    if Candy1 == True and Candy1_collected == False:

        imagebutton:

            xpos 1100
            ypos 650
            focus_mask True
            idle "gui/D1.png"
            hover "gui/D1_hover.png"
            if clickable == True:
                action [Play ("sound", "music/C_click.wav"), SetVariable("Candy1_collected", True), SetVariable("candy_colleted", candy_colleted + 1)]






screen mirage_score_1():

    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.01
    imagebutton:
        idle "drug1" hover "btn_m" xalign 0.01 yalign 0.01 action ShowMenu("save")
    text "6/[candy_colleted]" xalign 0.045 yalign 0.02

    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.1
    imagebutton:
        idle "key1" hover "btn_k" xalign 0.01 yalign 0.1 action ShowMenu("save")
    text "1/[key_garage_colleted]" xalign 0.045 yalign 0.11




screen stena1():

    $ clickable = True






    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action Jump("krylco1")




    if Candy3 == True and Candy3_collected == False:

        imagebutton:

            xpos 1395
            ypos 835
            focus_mask True
            idle "gui/D2.png"
            hover "gui/D2_hover.png"
            if clickable == True:
                action [Play ("sound", "music/C_click.wav"),SetVariable("Candy3_collected", True),SetVariable("candy_colleted", candy_colleted + 1)]






screen krylco1():

    $ clickable = True


    if qustion2 == True:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 1.0
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

            if clickable == True:
                action Jump("garag2")





    imagebutton:

        at map_arrow_anim
        xalign 0.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action Jump("stena1")



    imagebutton:

        at map_arrow_anim
        xpos 710
        ypos 50
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 90, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 90, zoom = 0.8 )

        if clickable == True:
            action Jump("koridor1")



    if Candy2 == True and Candy2_collected == False:

        imagebutton:

            xpos 1495
            ypos 635
            focus_mask True
            idle "gui/D1.png"
            hover "gui/D1_hover.png"
            if clickable == True:
                action [Play ("sound", "music/C_click.wav"),SetVariable("Candy2_collected", True),SetVariable("candy_colleted", candy_colleted + 1)]

    if qustion5 == True and KeyGarage1 == False:

        imagebutton:

            xpos 800
            ypos 200
            focus_mask True
            idle "gui/Key_garage.png"
            hover "gui/Key_garage_hover.png"
            if clickable == True:
                action [Play ("sound", "music/C_click.wav"),SetVariable("KeyGarage1", True),SetVariable("key_garage_colleted", key_garage_colleted + 1)]




screen tualet1():

    $ clickable = True




    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action Jump("koridor1")


    imagebutton:

        at map_arrow_anim
        xpos 1000
        ypos 500
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action [Jump("menu_mike_1")]





screen garag1():

    $ clickable = True



    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 1.0
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

        if clickable == True:
            action Jump("garag2")



    if Candy4 == False and Candy4_collected == False:

        imagebutton:

            xpos 500
            ypos 835
            focus_mask True
            idle "gui/D2.png"
            hover "gui/D2_hover.png"
            if clickable == True:
                action [Play ("sound", "music/C_click.wav"),SetVariable("Candy4_collected", True),SetVariable("candy_colleted", candy_colleted + 1)]

    if Candy5 == False and Candy5_collected == False:

        imagebutton:

            xpos 1800
            ypos 495
            focus_mask True
            idle "gui/D2.png"
            hover "gui/D2_hover.png"
            if clickable == True:
                action [Play ("sound", "music/C_click.wav"),SetVariable("Candy5_collected", True),SetVariable("candy_colleted", candy_colleted + 1)]

    if Candy6 == False and Candy6_collected == False:

        imagebutton:

            xpos 670
            ypos 300
            focus_mask True
            idle "gui/D3.png"
            hover "gui/D3_hover.png"
            if clickable == True:
                action [Play ("sound", "music/C_click.wav"),SetVariable("Candy6_collected", True),SetVariable("candy_colleted", candy_colleted + 1)]




screen garag2():

    $ clickable = True





    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 1.0
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

        if clickable == True:
            action Jump("krylco1")



    if KeyGarage1 == True and candy_colleted >= 3:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.2
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 90, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 90, zoom = 0.8 )

            if clickable == True:
                action Jump("garag1")



    if KeyGarage1 == False and candy_colleted <= 3:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.2
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 90, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 90, zoom = 0.8 )

            if clickable == True:
                action Show("Need_key")
                unhovered Hide("Need_key")

    elif KeyGarage1 == True and candy_colleted < 3:


        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.2
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 90, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 90, zoom = 0.8 )

            if clickable == True:
                action Show("Need_key")
                unhovered Hide("Need_key")






screen koridor1():

    $ clickable = True


    imagebutton:

        at map_arrow_anim
        xalign 0.005
        yalign 0.15
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action [Jump("part4_info")]


    if qustion4 == True and KeyGarage1 == False:

        imagebutton:

            at map_arrow_anim
            xalign 0.0
            yalign 0.5
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

            if clickable == True:
                action Jump("tualet1")

    else:

        imagebutton:

            at map_arrow_anim
            xalign 0.0
            yalign 0.5
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )



    if candy_colleted  == 6:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.5
            focus_mask True
            idle Transform("gui/questiongreen.png", rotate = 0, zoom = 0.8)
            hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )

            if clickable == True:
                action [Play ("sound", "music/C_click.wav"),Jump("quest_part4_end")]









    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 0.2
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 90, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 90, zoom = 0.8 )

        if clickable == True:
            action Jump("krylco1")


    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 1.0
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

        if clickable == True:
            action Jump("room1")


    imagebutton:

        at map_arrow_anim
        xalign 0.1
        ypos 10
        focus_mask True
        idle Transform("gui/skip_quest_part4.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/skip_quest_part4_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action Jump("angel_sex_1")





label menu_quest_1:

    menu:

        "Play Quest (Bonus animation)":

            jump quest_1

        "Fuck off Quest.":

            jump angel_sex_1

screen angel_quest_help():

    $ clickable = True


    imagebutton:

        at map_arrow_anim
        xalign 0.005
        yalign 0.15
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )


        if clickable == True:
            action Show("displayTextScreen")
            unhovered Hide("displayTextScreen")

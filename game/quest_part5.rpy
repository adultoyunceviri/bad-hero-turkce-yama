label part5_quest1:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1456
    call screen part5_quest_bedkate

label part5_quest1_2:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1460 with d
    pause
    scene 1461 with d
    call screen part5_quest_bedkate_2

label part5_quest1_3:

    $ renpy.block_rollback()
    call screen part5_quest_bedkate_3



label part5_quest2:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1457
    call screen part5_quest_table

label part5_quest2_2:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1463
    pause
    jump part5_quest2

label part5_quest2_3:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1464
    pause
    jump part5_quest2

label part5_quest2_4:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1465
    pause
    jump part5_quest2

label part5_quest3:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1458
    call screen part5_quest_closet

label part5_quest3_2:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1467b
    call screen part5_quest_closet2

label part5_quest3_3:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1468
    pause
    jump part5_quest3

label part5_quest4:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1459
    call screen part5_quest_bedchelsey

label part5_quest4_2:

    $ renpy.block_rollback()
    show screen part5_key_score
    scene 1469
    call screen part5_quest_bedchelsey_2

label part5_quest4_3:

    $ renpy.block_rollback()
    show screen part5_key_score
    call screen part5_quest_bedchelsey_3

label part5_quest_end:

    $ renpy.block_rollback()
    hide screen part5_key_score
    scene 1462 with d
    pause
    $ part5_bonusanim1 = True
    jump part5_game2

label part5_info:

    scene 1457d

    $ renpy.block_rollback()
    call screen part5_info


screen part5_info():

    $ clickable = True

    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest2")



screen part5_quest_bedkate():

    $ clickable = True

    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest2")


    imagebutton:

        at map_arrow_anim
        xpos 1000
        ypos 800
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )
        action [Jump("part5_quest1_2")]


screen part5_quest_bedkate_2():

    $ clickable = True



    imagebutton:

        at map_arrow_anim
        xpos 800
        ypos 600
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )
        action [Jump("part5_quest1_3")]

    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 1.0
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest1")




screen part5_quest_bedkate_3():

    $ clickable = True

    imagemap:

        ground "images/part5/1461b.jpg"
        idle "images/part5/1461d.jpg"
        hover "images/part5/1461d_hover.jpg"


        if part5_ch1 == False:

            hotspot (380, 375, 445, 200) action [SetVariable("part5_ch1", True), Play("sound", "music/C_click.wav")]

        if part5_ch2 == False:

            hotspot (310, 605, 180, 200) action  [SetVariable("part5_ch2", True), Play("sound", "music/C_click.wav")]

        if part5_ch3 == False:

            hotspot (600, 585, 220, 220) action  [SetVariable("part5_ch3", True), Play("sound", "music/C_click.wav")]

        if part5_ch4 == False:

            hotspot (1030, 330, 200, 235) action  [SetVariable("part5_ch4", True), Play("sound", "music/C_click.wav")]

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 1.0
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

            if clickable == True:
                action Jump("part5_quest1")


        imagebutton:
            idle "p progress1" xalign 0.025 yalign 0.01
        imagebutton:
            idle "key1" hover "btn_k" xalign 0.01 yalign 0.01 action ShowMenu("save")
        text " 1/[part5_quest_key_score1]" xalign 0.040 yalign 0.02









screen part5_quest_table():

    $ clickable = True

    imagemap:

        ground "images/part5/1457.jpg"
        idle "images/part5/1457b.jpg"
        hover "images/part5/1457b_hover.jpg"

        if part5_quest_key == False:
            hotspot (580, 700, 60, 20) action  Play ("sound", "music/C_click.wav")
        else:
            hotspot (580, 700, 60, 20) action  [Jump("part5_quest_end"), Play ("sound", "music/C_click.wav")]

        if part5_ch8 == False:

            hotspot (150, 565, 292, 80) action [SetVariable("part5_ch8", True), Play("sound", "music/C_click.wav")]


        if part5_ch9 == False:

            hotspot (520, 565, 185, 80) action [SetVariable("part5_ch9", True), Play("sound", "music/C_click.wav")]

        if part5_ch10 == False:

            hotspot (1635, 590, 220, 80) action [SetVariable("part5_ch10", True), Play("sound", "music/C_click.wav")]

        if part5_ch11 == False:

            hotspot (1830, 50, 45, 80) action [SetVariable("part5_ch11", True), Play("sound", "music/C_click.wav")]


        hotspot (1721, 685, 200, 30) action [Jump("part5_quest2_4"),Play ("sound", "music/C_click.wav")]




    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest3")


    imagebutton:

        at map_arrow_anim
        xalign 0.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest1")


    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.01
    imagebutton:
        idle "key1" hover "btn_k" xalign 0.01 yalign 0.01 action ShowMenu("save")
    text " 1/[part5_quest_key_score1]" xalign 0.040 yalign 0.02



    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 0.15
        focus_mask True
        idle Transform("gui/QuestionGreen.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action [Jump("part5_info")]

screen part5_quest_closet():

    $ clickable = True

    imagemap:

        ground "images/part5/1466.jpg"
        idle "images/part5/1466.jpg"
        hover "images/part5/1466_hover.jpg"


        hotspot (844, 690, 350, 40) action  Jump("part5_quest3_3") hovered Play ("sound", "music/C_click.wav")

    imagebutton:

        at map_arrow_anim
        xalign 0.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest2")


    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest4")


    imagebutton:

        at map_arrow_anim
        xpos 620
        ypos 550
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )
        action [Jump("part5_quest3_2")]

    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.01
    imagebutton:
        idle "key1" hover "btn_k" xalign 0.01 yalign 0.01 action ShowMenu("save")
    text " 1/[part5_quest_key_score1]" xalign 0.040 yalign 0.02

screen part5_quest_closet2():

    $ clickable = True

    imagemap:

        ground "images/part5/1467.jpg"
        idle "images/part5/1467b.jpg"
        hover "images/part5/1467b_hover.jpg"

        if part5_ch12 == False:

            hotspot (330, 750, 100, 120) action [SetVariable("part5_ch12", True), Play("sound", "music/C_click.wav")]

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 1.0
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

            if clickable == True:
                action Jump("part5_quest3")


        imagebutton:
            idle "p progress1" xalign 0.025 yalign 0.01
        imagebutton:
            idle "key1" hover "btn_k" xalign 0.01 yalign 0.01 action ShowMenu("save")
        text " 1/[part5_quest_key_score1]" xalign 0.040 yalign 0.02


screen part5_quest_bedchelsey():

    $ clickable = True

    imagebutton:

        at map_arrow_anim
        xalign 0.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action Jump("part5_quest3")


    imagebutton:

        at map_arrow_anim
        xpos 150
        ypos 850
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )
        action [Jump("part5_quest4_2")]

screen part5_quest_bedchelsey_2():

    $ clickable = True


    imagebutton:

        at map_arrow_anim
        xpos 620
        ypos 450
        focus_mask True
        idle Transform("gui/question.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/question_hover.png", rotate = 0, zoom = 0.8 )
        action [Jump("part5_quest4_3")]

screen part5_quest_bedchelsey_3():

    $ clickable = True

    imagemap:

        ground "images/part5/1470.jpg"
        idle "images/part5/1470b.jpg"
        hover "images/part5/1470b_hover.jpg"


        if part5_ch5 == False:

            hotspot (370, 267, 606, 375) action [SetVariable("part5_ch5", True), Play("sound", "music/C_click.wav")]

        if part5_ch6 == False:

            hotspot (1020, 500, 315, 325) action  [SetVariable("part5_ch6", True), Play("sound", "music/C_click.wav")]

        if part5_ch7 == False:

            hotspot (1050, 300, 310, 180) action  [SetVariable("part5_ch7", True), SetVariable("part5_quest_key", True), Play("sound", "music/Level_Up.mp3"), SetVariable("part5_quest_key_score1", 1)]



        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 1.0
            focus_mask True
            idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
            hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

            if clickable == True:
                action Jump("part5_quest3")


        imagebutton:
            idle "p progress1" xalign 0.025 yalign 0.01
        imagebutton:
            idle "key1" hover "btn_k" xalign 0.01 yalign 0.01 action ShowMenu("save")
        text " 1/[part5_quest_key_score1]" xalign 0.040 yalign 0.02


label part5_minigame1_1:

    $ renpy.block_rollback()

    scene 1315
    call screen elsa_minigame1_1


label part5_minigame1:

    $ renpy.block_rollback()
    $ last_pressed = "a"
    scene 1315 with d
    call screen elsa_minigame1

label part5_minigame2_1:

    $ renpy.block_rollback()

    scene 1316
    call screen elsa_minigame2_1


label part5_minigame2:

    $ renpy.block_rollback()
    $ last_pressed = "a"
    scene 1316 with d
    call screen elsa_minigame2

label part5_minigame3_1:

    $ renpy.block_rollback()

    scene 1317
    call screen elsa_minigame3_1


label part5_minigame3:

    $ renpy.block_rollback()
    $ last_pressed = "a"
    scene 1317 with d
    call screen elsa_minigame3

label part5_minigame4_1:

    $ renpy.block_rollback()

    scene 1320
    call screen elsa_minigame4_1


label part5_minigame4:

    $ renpy.block_rollback()
    $ last_pressed = "a"
    scene black with d
    pause
    scene 1318 with d
    angel "I can see it all."
    scene 1319 with d
    elsa2 "But I can't reach from here."
    angel "Let me help you out."
    scene 1320 with d
    call screen elsa_minigame4

label part5_minigame5_1:

    $ renpy.block_rollback()

    scene 1326
    call screen elsa_minigame5_1


label part5_minigame5:

    $ renpy.block_rollback()
    $ last_pressed = "a"
    scene 1326
    call screen elsa_minigame5

label part5_minigame6_1:

    $ renpy.block_rollback()

    scene 1329
    call screen elsa_minigame6_1


label part5_minigame6:

    $ renpy.block_rollback()
    $ last_pressed = "a"
    scene 1329
    call screen elsa_minigame6











screen elsa_minigame1_1():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()

    add "1315"
    add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920


    imagebutton:


        xpos 1740
        ypos 760
        focus_mask True
        idle "images/pool_minigame/HUD/completed.png"
        hover "images/pool_minigame/HUD/completed_hover.png"
        if clickable == True:
            action Jump("angel_treining")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860


    text "10/" xpos 1750 ypos 870
    text "[elsa_minigame1_count]" xpos 1810 ypos 870

screen elsa_minigame1():

    $ clickable = True



    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()


    if last_pressed == "d" and elsa_minigame1_count < 10:

        key "mouseup_1" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame1_count", elsa_minigame1_count + 1), Play ("sound", "music/C_click.wav")]
        key "a" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame1_count", elsa_minigame1_count + 1)]
        key "mouseup_3" action NullAction()
    if last_pressed == "a" and elsa_minigame1_count < 10:
        key "mouseup_3" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame1_count", elsa_minigame1_count + 1), Play ("sound", "music/C_click.wav")]
        key "d" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame1_count", elsa_minigame1_count + 1)]

    if elsa_minigame1_count >=0.01 and elsa_minigame1_count < 10:
        timer 0.30 action SetVariable("elsa_minigame1_count", elsa_minigame1_count - 1) repeat True





    if clickable == True and last_pressed == "a":
        add "1315"
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954



    if clickable == True and last_pressed == "d":
        add "1315b"
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954

    if clickable == True and elsa_minigame1_count == 10:

        #key "mouseup_3" action NullAction()
        #key "game_menu" action NullAction()
        key "mouseup_1" action Jump("part5_minigame1_1")




    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860



    text "10/" xpos 1750 ypos 870
    text "[elsa_minigame1_count]" xpos 1810 ypos 870

screen elsa_minigame2_1():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()

    add "1316b"
    add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920


    imagebutton:


        xpos 1740
        ypos 760
        focus_mask True
        idle "images/pool_minigame/HUD/completed.png"
        hover "images/pool_minigame/HUD/completed_hover.png"
        if clickable == True:
            action Jump("angel_treining")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860
        #if elsa_minigame1_count >= 1:
            #text "[elsa_minigame1_count]" xpos 1800 ypos 870
            #text "0" xpos 1800 ypos 870
        #else:
            #text "[elsa_minigame1_count]" xpos 1800 ypos 870


    text "20/" xpos 1750 ypos 870
    text "[elsa_minigame2_count]" xpos 1810 ypos 870

screen elsa_minigame2():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()


    if last_pressed == "d" and elsa_minigame2_count < 20:

        key "mouseup_1" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame2_count", elsa_minigame2_count + 1), Play ("sound", "music/C_click.wav")]
        key "a" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame2_count", elsa_minigame2_count + 1)]
        key "mouseup_3" action NullAction()
    if last_pressed == "a" and elsa_minigame2_count < 20:
        key "mouseup_3" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame2_count", elsa_minigame2_count + 1), Play ("sound", "music/C_click.wav")]
        key "d" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame2_count", elsa_minigame2_count + 1)]

    if elsa_minigame2_count >=0.01 and elsa_minigame2_count < 20:
        timer 0.30 action SetVariable("elsa_minigame2_count", elsa_minigame2_count - 1) repeat True




    if clickable == True and last_pressed == "a":
        add "1316"
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954



    if clickable == True and last_pressed == "d":
        add "1316b"
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954

    if clickable == True and elsa_minigame2_count ==20:

        key "mouseup_1" action Jump("part5_minigame2_1")








    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860

        #if elsa_minigame2_count >= 1:
            #text "[elsa_minigame2_count]" xpos 1800 ypos 870
            #text "0" xpos 1800 ypos 870
        #else:
            #text "[elsa_minigame2_count]" xpos 1800 ypos 870


    text "20/" xpos 1750 ypos 870
    text "[elsa_minigame2_count]" xpos 1810 ypos 870

screen elsa_minigame3_1():

    $ clickable = True



    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()

    add "1317b"
    add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920


    imagebutton:


        xpos 1740
        ypos 760
        focus_mask True
        idle "images/pool_minigame/HUD/completed.png"
        hover "images/pool_minigame/HUD/completed_hover.png"
        if clickable == True:
            action Jump("part5_4")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860
        #if elsa_minigame1_count >= 1:
            #text "[elsa_minigame1_count]" xpos 1800 ypos 870
            #text "0" xpos 1800 ypos 870
        #else:
            #text "[elsa_minigame1_count]" xpos 1800 ypos 870


    text "10/" xpos 1750 ypos 870
    text "[elsa_minigame3_count]" xpos 1810 ypos 870

screen elsa_minigame3():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()


    if last_pressed == "d" and elsa_minigame3_count < 10:

        key "mouseup_1" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame3_count", elsa_minigame3_count + 1), Play ("sound", "music/C_click.wav")]
        key "a" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame3_count", elsa_minigame3_count + 1)]
        key "mouseup_3" action NullAction()
    if last_pressed == "a" and elsa_minigame3_count < 10:
        key "mouseup_3" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame3_count", elsa_minigame3_count + 1), Play ("sound", "music/C_click.wav")]
        key "d" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame3_count", elsa_minigame3_count + 1)]

    if elsa_minigame3_count >=0.01 and elsa_minigame3_count < 10:
        timer 0.30 action SetVariable("elsa_minigame3_count", elsa_minigame3_count - 1) repeat True




    if clickable == True and last_pressed == "a":
        add "1317"
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954



    if clickable == True and last_pressed == "d":
        add "1317b"
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954

    if clickable == True and elsa_minigame3_count ==10:

        key "mouseup_1" action Jump("part5_minigame3_1")








    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860

        #if elsa_minigame2_count >= 1:
            #text "[elsa_minigame2_count]" xpos 1800 ypos 870
            #text "0" xpos 1800 ypos 870
        #else:
            #text "[elsa_minigame2_count]" xpos 1800 ypos 870


    text "10/" xpos 1750 ypos 870
    text "[elsa_minigame3_count]" xpos 1810 ypos 870

screen elsa_minigame4_1():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()

    add "1320b"
    add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920


    imagebutton:


        xpos 1740
        ypos 760
        focus_mask True
        idle "images/pool_minigame/HUD/completed.png"
        hover "images/pool_minigame/HUD/completed_hover.png"
        if clickable == True:
            action Jump("part5_5")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860



    text "20/" xpos 1750 ypos 870
    text "[elsa_minigame4_count]" xpos 1810 ypos 870

screen elsa_minigame4():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()


    if last_pressed == "d" and elsa_minigame4_count < 20:

        key "mouseup_1" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame4_count", elsa_minigame4_count + 1), Play ("sound", "music/C_click.wav")]
        key "a" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame4_count", elsa_minigame4_count + 1)]
        key "mouseup_3" action NullAction()
    if last_pressed == "a" and elsa_minigame4_count < 20:
        key "mouseup_3" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame4_count", elsa_minigame4_count + 1), Play ("sound", "music/C_click.wav")]
        key "d" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame4_count", elsa_minigame4_count + 1)]

    if elsa_minigame4_count >=0.01 and elsa_minigame4_count < 20:
        timer 0.30 action SetVariable("elsa_minigame4_count", elsa_minigame4_count - 1) repeat True




    if clickable == True and last_pressed == "a":
        add "1320"
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954



    if clickable == True and last_pressed == "d":
        add "1320b"
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954

    if clickable == True and elsa_minigame4_count ==20:

        key "mouseup_1" action Jump("part5_minigame4_1")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860



    text "20/" xpos 1750 ypos 870
    text "[elsa_minigame4_count]" xpos 1810 ypos 870

screen elsa_minigame5_1():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()

    add "1326b"
    add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920


    imagebutton:


        xpos 1740
        ypos 760
        focus_mask True
        idle "images/pool_minigame/HUD/completed.png"
        hover "images/pool_minigame/HUD/completed_hover.png"
        if clickable == True and dildo_big_complete == True:
            action [SetVariable("part5_bonusanim2", True), Jump("part5_minigame_end")]
        elif clickable == True and dildo_big_complete == False:
            action Jump("part5_6")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860
        #if elsa_minigame1_count >= 1:
            #text "[elsa_minigame1_count]" xpos 1800 ypos 870
            #text "0" xpos 1800 ypos 870
        #else:
            #text "[elsa_minigame1_count]" xpos 1800 ypos 870


    text "30/" xpos 1750 ypos 870
    text "[elsa_minigame5_count]" xpos 1810 ypos 870

screen elsa_minigame5():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()


    if last_pressed == "d" and elsa_minigame5_count < 30:

        key "mouseup_1" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame5_count", elsa_minigame5_count + 1), Play ("sound", "music/C_click.wav")]
        key "a" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame5_count", elsa_minigame5_count + 1)]
        key "mouseup_3" action NullAction()
    if last_pressed == "a" and elsa_minigame5_count < 30:
        key "mouseup_3" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame5_count", elsa_minigame5_count + 1), Play ("sound", "music/C_click.wav")]
        key "d" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame5_count", elsa_minigame5_count + 1)]

    if elsa_minigame5_count >=0.01 and elsa_minigame5_count < 30:
        timer 0.30 action SetVariable("elsa_minigame5_count", elsa_minigame5_count - 1) repeat True




    if clickable == True and last_pressed == "a":
        add "1326"
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954



    if clickable == True and last_pressed == "d":
        add "1326b"
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954

    if clickable == True and elsa_minigame5_count ==30:

        key "mouseup_1" action Jump("part5_minigame5_1")




    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860




    text "30/" xpos 1750 ypos 870
    text "[elsa_minigame5_count]" xpos 1810 ypos 870

screen elsa_minigame6_1():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()

    add "1329b"
    add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920


    imagebutton:


        xpos 1740
        ypos 760
        focus_mask True
        idle "images/pool_minigame/HUD/completed.png"
        hover "images/pool_minigame/HUD/completed_hover.png"
        if clickable == True:
            action Jump("part5_7")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860



    text "10/" xpos 1750 ypos 870
    text "[elsa_minigame6_count]" xpos 1810 ypos 870

screen elsa_minigame6():

    $ clickable = True


    key "game_menu" action NullAction()
    if clickable == True:
        key "mouseup_3" action NullAction()


    if last_pressed == "d" and elsa_minigame6_count < 10:

        key "mouseup_1" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame6_count", elsa_minigame6_count + 1), Play ("sound", "music/C_click.wav")]
        key "a" action [SetVariable("last_pressed", "a"), SetVariable("elsa_minigame6_count", elsa_minigame6_count + 1)]
        key "mouseup_3" action NullAction()
    if last_pressed == "a" and elsa_minigame6_count < 10:
        key "mouseup_3" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame6_count", elsa_minigame6_count + 1), Play ("sound", "music/C_click.wav")]
        key "d" action [SetVariable("last_pressed", "d"), SetVariable("elsa_minigame6_count", elsa_minigame6_count + 1)]

    if elsa_minigame6_count >=0.01 and elsa_minigame6_count < 10:
        timer 0.30 action SetVariable("elsa_minigame6_count", elsa_minigame6_count - 1) repeat True




    if clickable == True and last_pressed == "a":
        add "1329"
        add "images/pool_minigame/HUD/Bd.png" xpos 1720 ypos 920
        text "{b}a{/b}" xpos 1767 ypos 954



    if clickable == True and last_pressed == "d":
        add "1329b"
        add "images/pool_minigame/HUD/Ba.png" xpos 1720 ypos 920
        text "{b}d{/b}" xpos 1810 ypos 954

    if clickable == True and elsa_minigame6_count ==10:

        key "mouseup_1" action Jump("part5_minigame6_1")

    imagebutton:

        idle "images/pool_minigame/HUD/Bc.png" xpos 1720 ypos 860




    text "10/" xpos 1750 ypos 870
    text "[elsa_minigame6_count]" xpos 1810 ypos 870




screen part5_dildo():

    imagemap:

        ground "images/part5/1325.jpg"
        idle "images/part5/1325.jpg"
        hover "images/part5/1325_hover.jpg"

        if dildo_big_complete == False and dildo_big == True:
            hotspot (560, 420, 300, 400) action [SetVariable("dildo_big_complete", True), Jump("part5_minigame5")] hovered Play ("sound", "music/C_click.wav")

        if dildo_big_complete == False and dildo_big == False:
            hotspot (560, 420, 300, 400) action Jump("part5_minigame5") hovered Play ("sound", "music/C_click.wav")

        if dildo_middle_complete == False:
            hotspot (860, 420, 200, 400) action Jump("part5_minigame3") hovered Play ("sound", "music/C_click.wav")

        if dildo_middle_complete == False and dildo_small_complete == True:
            hotspot (860, 420, 200, 400) action Jump("part5_minigame4") hovered Play ("sound", "music/C_click.wav")

        if dildo_small_complete == False:
            hotspot (1100, 420, 200, 400) action Jump("part5_minigame6")hovered Play ("sound", "music/C_click.wav")

screen part5_key_score():


    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.01
    imagebutton:
        idle "key1" hover "btn_k" xalign 0.01 yalign 0.01 action ShowMenu("save")
    text " 1/[part5_quest_key_score1]" xalign 0.040 yalign 0.02

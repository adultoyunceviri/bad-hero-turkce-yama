init:

    $ crismas_toy_colleted = 0
    $ analtoy_colleted = 0
    $ alltoys = 0


    $ anal_toy_1 = False
    $ anal_toy_2 = False
    $ anal_toy_3 = False
    $ anal_toy_4 = False
    $ anal_toy_5 = False
    $ anal_toy_6 = False
    $ anal_toy_7 = False
    $ anal_toy_8 = False
    $ anal_toy_9 = False

    $ crismas_toy_1 = False
    $ crismas_toy_2 = False
    $ crismas_toy_3 = False
    $ crismas_toy_4 = False





label part9_quest_start:

    $ crismas_toy_colleted = 0
    $ analtoy_colleted = 0
    $ alltoys = 0


    $ anal_toy_1 = False
    $ anal_toy_2 = False
    $ anal_toy_3 = False
    $ anal_toy_4 = False
    $ anal_toy_5 = False
    $ anal_toy_6 = False
    $ anal_toy_7 = False
    $ anal_toy_8 = False
    $ anal_toy_9 = False

    $ crismas_toy_1 = False
    $ crismas_toy_2 = False
    $ crismas_toy_3 = False
    $ crismas_toy_4 = False

    jump part9_quest1



label part9_quest1:


    $ renpy.block_rollback()
    show screen part9_tree1
    #scene 1456
    call screen part9_tree1

label part9_quest2:

    $ renpy.block_rollback()
    show screen part9_tree2
    #scene 1456
    call screen part9_tree2

label part9_quest3:

    $ renpy.block_rollback()
    show screen part9_tree3
    #scene 1456
    call screen part9_tree3










screen part9_tree1():



    $ clickable = True

    imagemap:

        ground "images/part9/quest/2497.jpg"
        idle "images/part9/quest/2497b.jpg"
        hover "images/part9/quest/2497_hover.jpg"



        if anal_toy_1 == False:

            hotspot (740, 30, 150, 250) action [SetVariable("anal_toy_1", True), SetVariable("analtoy_colleted", analtoy_colleted + 1), SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]


        if anal_toy_2 == False:

            hotspot (1150, 12, 150, 250) action [SetVariable("anal_toy_2", True), SetVariable("analtoy_colleted", analtoy_colleted + 1), SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]

        if anal_toy_3 == False:

            hotspot (1260, 400, 150, 300) action [SetVariable("anal_toy_3", True), SetVariable("analtoy_colleted", analtoy_colleted + 1), SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]

        if anal_toy_4 == False:

            hotspot (730, 490, 200, 370) action [SetVariable("anal_toy_4", True), SetVariable("analtoy_colleted", analtoy_colleted + 1), SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]

        if crismas_toy_1 == False:

            hotspot (945, 345, 150, 150) action [SetVariable("crismas_toy_1", True), SetVariable("crismas_toy_colleted", crismas_toy_colleted + 1), SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]






    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )


        if clickable == True:

            action Jump("part9_quest2")



    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 1.0
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )

        if clickable == True:

            action Jump("part9_quest3")


    if analtoy_colleted == 9 and crismas_toy_colleted == 0:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.5
            focus_mask True
            idle Transform("gui/end1.png", rotate = 0)
            hover Transform("gui/end1_hover.png", rotate = 0)

            if clickable == True:
                action Jump("quest_part9_end")


    if alltoys == 13:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.5
            focus_mask True
            idle Transform("gui/end2.png", rotate = 0)
            hover Transform("gui/end2_hover.png", rotate = 0)

            if clickable == True:
                action Jump("play_quest_part9_error")

    imagebutton:

        at map_arrow_anim
        xpos 10
        ypos 10
        focus_mask True
        idle Transform("gui/youtube.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/youtube_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action OpenURL("https://youtu.be/dbzSejdzg_g")







    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.01
    imagebutton:
        idle "toy1" hover "btn_a" xalign 0.01 yalign 0.01 action ShowMenu("save")
    text "  [alltoys]" xalign 0.040 yalign 0.02

    #text tt.value








screen part9_tree2():

    $ clickable = True

    imagemap:

        ground "images/part9/quest/2496.jpg"
        idle "images/part9/quest/2496b.jpg"
        hover "images/part9/quest/2496_hover.jpg"



        if anal_toy_5 == False:

            hotspot (660, 3, 150, 400) action [SetVariable("anal_toy_5", True),SetVariable("analtoy_colleted", analtoy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]


        if anal_toy_6 == False:

            hotspot (1066, 280, 150, 250) action [SetVariable("anal_toy_6", True),SetVariable("analtoy_colleted", analtoy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]

        if anal_toy_7 == False:

            hotspot (770, 630,150, 300) action [SetVariable("anal_toy_7", True),SetVariable("analtoy_colleted", analtoy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]

        if crismas_toy_2 == False:

            hotspot (380, 860, 150, 250) action [SetVariable("crismas_toy_2", True),SetVariable("crismas_toy_colleted", crismas_toy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]






    imagebutton:

        at map_arrow_anim
        xalign 0.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 0, zoom = 0.8 )


        if clickable == True:

            action Jump("part9_quest1")



    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 1.0
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 270, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 270, zoom = 0.8 )


        if clickable == True:

            action Jump("part9_quest3")


    if analtoy_colleted == 9 and crismas_toy_colleted == 0:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.5
            focus_mask True
            idle Transform("gui/end1.png", rotate = 0)
            hover Transform("gui/end1_hover.png", rotate = 0)

            if clickable == True:
                action Jump("quest_part9_end")


    if alltoys == 13:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.5
            focus_mask True
            idle Transform("gui/end2.png", rotate = 0)
            hover Transform("gui/end2_hover.png", rotate = 0)

            if clickable == True:
                action Jump("play_quest_part9_error")

    imagebutton:

        at map_arrow_anim
        xpos 10
        ypos 10
        focus_mask True
        idle Transform("gui/youtube.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/youtube_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action OpenURL("https://youtu.be/dbzSejdzg_g")


    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.01
    imagebutton:
        idle "toy1" hover "btn_a" xalign 0.01 yalign 0.01 action ShowMenu("save")
    text "  [alltoys]" xalign 0.040 yalign 0.02


screen part9_tree4():

    $ clickable = True

    imagemap:

        ground "images/part9/quest/2498.jpg"
        idle "images/part9/quest/2498b.jpg"
        hover "images/part9/quest/2498_hover.jpg"

        if anal_toy_8 == False:

            hotspot (717, 315, 250, 470) action [SetVariable("anal_toy_8", True),SetVariable("analtoy_colleted", analtoy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]



        if anal_toy_9 == False:

            hotspot (1000, 490, 150, 200) action [SetVariable("anal_toy_9", True),SetVariable("analtoy_colleted", analtoy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]


        if crismas_toy_3 == False:

            hotspot (350, 488, 370, 370) action [SetVariable("crismas_toy_3", True),SetVariable("crismas_toy_colleted", crismas_toy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]

        if crismas_toy_4 == False:

            hotspot (1170, 418, 370, 370) action [SetVariable("crismas_toy_4", True),SetVariable("crismas_toy_colleted", crismas_toy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]


screen part9_tree3():

    $ clickable = True

    imagemap:

        ground "images/part9/quest/2498.jpg"
        idle "images/part9/quest/2498b.jpg"
        hover "images/part9/quest/2498_hover.jpg"

        if anal_toy_8 == False:

            hotspot (717, 315, 250, 470) action [SetVariable("anal_toy_8", True),SetVariable("analtoy_colleted", analtoy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]



        if anal_toy_9 == False:

            hotspot (1000, 490, 150, 200) action [SetVariable("anal_toy_9", True),SetVariable("analtoy_colleted", analtoy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]


        if crismas_toy_3 == False:

            hotspot (350, 488, 370, 370) action [SetVariable("crismas_toy_3", True),SetVariable("crismas_toy_colleted", crismas_toy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]

        if crismas_toy_4 == False:

            hotspot (1170, 418, 370, 370) action [SetVariable("crismas_toy_4", True),SetVariable("crismas_toy_colleted", crismas_toy_colleted + 1),SetVariable("alltoys", alltoys + 1), Play("sound", "music/C_click.wav")]






    imagebutton:

        at map_arrow_anim
        xalign 0.5
        yalign 0.0
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 90, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 90, zoom = 0.8 )

        if clickable == True:

            action Jump("part9_quest1")



    imagebutton:

        at map_arrow_anim
        xalign 1.0
        yalign 0.5
        focus_mask True
        idle Transform("gui/map_arrow.png", rotate = 180, zoom = 0.8 )
        hover Transform("gui/map_arrow_hover.png", rotate = 180, zoom = 0.8 )


        if clickable == True:

            action Jump("part9_quest2")


    if analtoy_colleted == 9 and crismas_toy_colleted == 0:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.5
            focus_mask True
            idle Transform("gui/end1.png", rotate = 0)
            hover Transform("gui/end1_hover.png", rotate = 0)

            if clickable == True:
                action Jump("quest_part9_end")


    if alltoys == 13:

        imagebutton:

            at map_arrow_anim
            xalign 0.5
            yalign 0.5
            focus_mask True
            idle Transform("gui/end2.png", rotate = 0)
            hover Transform("gui/end2_hover.png", rotate = 0)

            if clickable == True:
                action Jump("play_quest_part9_error")

    imagebutton:

        at map_arrow_anim
        xpos 10
        ypos 10
        focus_mask True
        idle Transform("gui/youtube.png", rotate = 0, zoom = 0.8 )
        hover Transform("gui/youtube_hover.png", rotate = 0, zoom = 0.8 )

        if clickable == True:
            action OpenURL("https://youtu.be/dbzSejdzg_g")


    imagebutton:
        idle "p progress1" xalign 0.025 yalign 0.01
    imagebutton:
        idle "toy1" hover "btn_a" xalign 0.01 yalign 0.01 action ShowMenu("save")
    text "  [alltoys]" xalign 0.040 yalign 0.02

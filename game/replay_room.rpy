init -2:
    $ x = ui.adjustment()
    $ y = ui.adjustment()

label replay_room:
    $ x.value = 0
    $ y.value = 0
    call screen replay_room(x,y)

screen replay_room(x,y):
    tag menu

    frame:

        add "black"

        viewport:


            xadjustment x
            yadjustment y
            scrollbars "vertical"
            mousewheel True
            draggable True


            vbox:



                #xminimum 1000 xmaximum 1000
                #align(0.5,0.5)
                #xpos 0.232
                #xalign 0.5
                #yalign 1.0
                spacing 10
                #xfill True


                textbutton "Animasyon Part 1-3" action Replay("anim_part1_3", locked=False)
                textbutton "Animasyon Part 4" action Replay("anim_part4", locked=False)
                textbutton "Animasyon Part 5" action Replay("anim_part5", locked=False)
                textbutton "Animasyon Part 6" action Replay("anim_part6", locked=False)
                textbutton "Animasyon Part 7" action Replay("anim_part7", locked=False)
                textbutton "Animasyon Part 8" action Replay("anim_part8", locked=False)
                textbutton "Animasyon Part 9" action Replay("anim_part9", locked=False)
                textbutton "Animasyon Part 10" action Replay("anim_part10", locked=False)
                textbutton "Animasyon Part 11" action Replay("anim_part11", locked=False)
                textbutton "Main Menu" action ShowMenu("main_menu")

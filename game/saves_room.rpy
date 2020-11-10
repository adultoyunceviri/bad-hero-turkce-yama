

init -2:
    $ x = ui.adjustment()
    $ y = ui.adjustment()

label saves_room:


    $ x.value = 500
    $ y.value = 0
    call screen saves_room(x,y)

screen saves_room(x,y):
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



                textbutton "Main Menu" action ShowMenu("main_menu")
                textbutton "Kayıt sorunu yaşıyorsanız Discord sunucumuzdan yardım alabilirsiniz." action OpenURL("https://discord.com/invite/XsKNAub")

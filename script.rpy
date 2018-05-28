## The script of the game goes in this file.
#For multipersistent only
#init:
#    $ mp = MultiPersistent("demo.renpy.org")
## Declare characters used by this game. The color argument colorizes the name
## of the character.
#image mc_plain = im.Scale("/images/1488296822494.JPEG", 275, 500)
define y = Character('You') #nick smallcat
define sa = Character('Sarah') #nick flowerbush
define ev = Character('Evan') #nick dangomasta
define g = Character('Gwen') #nick ignitionkick
define si = Character('Silo') #nick dake
define sys = Character('System') #nick system

image phone = "images/chatbackground.png"
image mainmenu = im.Scale("images/mainlayout.png", 1280, 720)
image evan-kere = im.FactorScale("/images/evan-kere.png", 0.15, 0.15)
image sarah-good = im.FactorScale("/images/sarah-good.png", 0.2, 0.2)
image father = im.FactorScale("/images/father-sprite.png", 0.35, 0.35)
image mother = im.FactorScale("/images/mother-sprite.png", 0.35, 0.35)
init:
    image cg1 = "CG dega-proto.jpg"
    image cg2 = "CG gwen-proto.jpg"

## The game starts here.
transform phone_pickup:
    yalign 0.9 xalign 0.5
    yoffset 500
    easein 0.3 yoffset 150

    on hide:
        easeout 0.2 yoffset 400

transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1
    
transform phone_message_bubble_tip2:
    xoffset 0
    yoffset 1

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0
        
transform sysnotice:
    yoffset 100
    xalign 2.9
    yalign 0.16
    alpha 0
    parallel:
        easein 0.3 alpha 1
    parallel:
        easein 0.2 yoffset 0

transform incoming_message:
    yoffset 100
    yalign 0.2
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message

transform incoming_message2:
    yoffset 150
    yalign 0.4
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0
    
    on hide:
        scrolling_out_message
        
transform incoming_message3:
    yoffset 200
    yalign 0.6
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0
    
    on hide:
        scrolling_out_message

transform incoming_message4:
    yoffset 250
    yalign 0.8
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0
    
    on hide:
        scrolling_out_message
#$ enpos = Position(xpos = .18, xanchor = 0, ypos = .35, yanchor = 0)

    

label start:
    $ mainCharaFemale = 0
    jump intro
    ev "Time to check out my phone!"
    
    ## Add cellphone screen here
    show phone at phone_pickup


    window hide
    $ renpy.pause(0.2)
    show screen phone_message("Evan", "I got the power now so no thanks")# at incoming_message
    $ renpy.pause()
    #show screen phone_pic("Evan", im.FactorScale("/images/evan-kere.png", 0.2, 0.2))
    show evan-kere at Position(xalign=0.08, yalign=0.35)
    $ renpy.pause()
    
    #call screen phone_reply("umm no","nobreakfast","totally!","yesbreakfast")
    

label yesbreakfast:
    #hide screen phone_message
    #hide evan-kere
    $ renpy.pause(0.1)
    
    show screen player_phone_message2("Me", "yes hahaha, lol") #at incoming_message2
    $ renpy.pause()

    #hide screen player_phone_message2
    #$ renpy.pause()

    show screen phone_message3("evan", "good!!")
    $ renpy.pause(0)

    hide screen phone_message
    hide phone

    $renpy.pause(0.2)
    jump continues
    
label nobreakfast:
    #hide screen phone_message
    #hide evan-kere
    $ renpy.pause(0.1)
    show screen player_phone_message2("Me", "haha no i havent  lol")
    $ renpy.pause()

    #hide screen phone_message2
    #$ renpy.pause(0.1)

    show screen phone_message3("mom", "ok. well eat some then")
    $ renpy.pause()

    hide screen phone_message
    hide phone

    $renpy.pause(0.2)
    jump continues  
        
    $ mainCharaFemale = 0
    
    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    #scene bg room

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    #show eileen happy

    ## These display lines of dialogue.

    #"Hello, world."

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    ## This ends the game.

    jump intro

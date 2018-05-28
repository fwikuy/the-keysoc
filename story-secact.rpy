label secact:
    show black
    "Father is home. Better greet him before I can invoke another phase of his wrath."
    "Let's meet up with him."
    "Father" "\"There you are.\""
    show father at center
    with dissolve
    "He said it as if he has been expecting me."
    "You" "\"Hello, Father.\""
    "He nodded."
    "Our awkward conversation before still linger in his mind, must be that."
    "Father" "\"You'd do well listening to your parents.\""
    hide father
    with dissolve
    "And he walked away again."
    "..."
    "As angry as I could be, I should never try to vent it to him anymore."
    "I must keep this story about the open community chat a secret."
    "Now, breath... Let all your anger quenched in the breath..."
    "... Right."
    "Time to think objectively."
    "What should I do now?"
    menu:
        "Check the phone.":
            pass
        "Talk to mother.":
            pass
    "Right, I forgot about mother."
    "It's not difficult to find her."
    "My father came home and get into bedroom, but mother should still be preparing for dinner."
    stop music
    play music "music/Blissful Ignorance.mp3"
    "You" "\"Mother.\""
    show mother at center
    with dissolve
    "Mother" "\"Dear me... I thought it was someone suspicious.\""
    "She is my mother."
    "The excessive overprotecting syndrome had taken a few toll on her."
    "One of them is her ability to perceive her surroundings accurately."
    "Mother" "\"It's unusual for you to be here now.\""
    "You" "\"Yes. I had this sudden urge to take a breath. I'm stuck on my math problems.\""
    "Lies."
    "I can't work on math if I get myself preoccupied with the chatroom."
    "Mother" "\"Ah, I get it. Is it one of those... what was it called again? Calciumus?\""
    "No, that's calculus."
    "Mother" "\"It must be one of those worms again.\""
    "Worms? Oh, she might have thought about integral equations."
    "You" "\"Yes. I find it quite difficult to solve.\""
    "Lies."
    "The tutor explained it splendidly to me."
    "I just don't have the tenacity to continue after being put in such stress from the previous conversation with father."
    "Mother" "\"My, my... Well, grab a drink. Anything from the fridge is good for your health. Do you mind some juice?\""
    "You" "\"No, I'll have some.\""
    hide mother
    with dissolve
    "She took a cup and poured orangish liquid from a container into it."
    show mother at center
    with dissolve
    "Mother" "\"Here goes. Drink up.\""
    "I take the glass and smell it."
    "You" "\"Another drink from Tropical Hills?\""
    "Tropical Hills is where my father works at."
    "He runs as marketing division of the company and plays major part at gaining their current portion of customer."
    "Mother" "\"Well, what can I say? Your father always bring one or two containers home every week. We just have to make sure that they are drunk.\""
    hide mother at center
    with dissolve
    "She continued her work at the kitchen."
    "You" "\"I will continue my studies. Please tell father that I'd like to give it an undivided attention.\""
    "Mother" "\"Sure, just make sure that you come down at dinner.\""
    "You" "\"I will.\""
    "I went back to my PC."
    "Dinner is just around the corner, so I'd better play it quick."
    show black
    show screen phone_message("SecretHush", "If you are interested in the continuation, please donate to SecretHush!")
    $ renpy.pause(1.7)
    show screen phone_message2("SecretHush", "We are on at Patreon, so click donate and help us finishing this project!")
    $ renpy.pause(1.5)
    show screen phone_message3("SecretHush", "Well, then, see you!")
    $ renpy.pause()
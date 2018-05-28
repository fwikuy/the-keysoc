label prolog:
    show black
    #test plan
    play music "music/Crisis Calls.mp3"
    
    "Father" "\"How awful.\""
    "Mother" "\"It is. I wonder what they think when trying to do that.\""
    "It was the news."
    "That day, a gang of underaged boys attempted to kidnap their schoolmate."
    "The attempt was half successful, the police caught them red-handed while they were trying to lock the poor soul in an abandoned house."
    "The news stated that the boys attempted such act because the schoolmate was not willing to help them cheating during an exam."
    "The statement might be fraud, of course. Mass media during those days were looking for senseless attention and popularity over the truth."
    "I hate such news."
    "No, I'm not a truth-seeker. I'm just your average schoolkid."
    "However, that news marked my last day at school."
    "My parents grew into paranoid couple."
    "Whenever I came home late, they threw dozens of questions, all filled with needless worry."
    "At first, they were asking about how my lunch was, then it escalated into how my friends treated me."
    "But at the very next day..."
    "Father" "\"Put down your bag and forget your uniform. I've hired a private tutor for you.\""
    "Mother" "\"Listen to your father, there will be no more school for you. They are unsafe.\""
    "As a kid I was, listening about not having to go to school put my mood in merry."
    "Well, kids tend to crave fun more than adults do and most schools provide more stress than fun."
    "But now..."
    y "\"That's just unfair!\""
    "I threw another tantrum."
    show father at center
    with dissolve
    "This is my father."
    "As you can see, he is already quite old but still as headstrong as he was before he married mother."
    "I know that it is not a good habit to speak ill about your parents, but he is asking for it."
    "Well, let's continue my tantrum."
    y "\"How am I supposed to learn socializing if I'm staying at home?\""
    "Father" "\"Well, that's what parents for. You can talk to us.\""
    "Talk to them? Oh, what am I? A baby? A kindergartener?"
    y "\"That's your role years ago! I eventually have to learn to understand people outside family too!\""
    "Father" "\"Does that really apply for everyone? Why do you suddenly talk about it anyway?\""
    "A cliche way to change the topic."
    y "\"...\""
    "Father" "\"Ah, of course! You have been watching television lately. What did you watch? Soap operas? Scripted reality shows? Well, no matter. I guess this is the last day for you to watch them.\""
    y "\"But I didn't --\""
    "Father" "\"No! No room for arguments. From today onwards, television channels for you are limited to child-safe channels only and that is final!\""
    menu:
        "\"But I am a teenage BOY!\"":
            $ mainCharaFemale = 0
        "\"But I am a teenage GIRL!\"":
            $ mainCharaFemale = 1
    "Father" "\"So what? You are not mature enough to be called an adult and that is all that matters.\""
    y "\"But I really am a teenager!\""
    "Father" "\"Grow up, Kid. Only children dare enough to throw tantrum at their parents.\""
    hide father
    with dissolve
    "And he walks away."
    y "\"How am I supposed to talk calmly if you never even try to listen!?\""
    # At this part, the main character attempts to find a way to amuse him/her self.
    # The main character accidentally found an open social media for students, he/she found that there are chatroom consisting of people around his/her neighbourhood
    # He/she signed up at the social media and joined a chatroom for people around his/her neighbourhood
    y "\"Augh, that's it! I'm fed up with him!\""
    "I hate him. No matter how childish it could be, I really hate him."
    "How did he change from an open-minded parent into a one-way selfish old man?"
    "Is it really that difficult to let go his only child?"
    y "\"...\""
    "There is no use thinking about it."
    "PLING!!"
    "That sound came from my phone, signaling an incoming e-mail."
    # Show the HTML Screenshot of an invitation to join student forum, look around to find the pattern and banners.
    # Don't forget to find the symbol.
    y "\"Oh, only an ad.\""
    y "\"Wait...\""
    y "\"An open community project dedicated to students who want to meet with each other from different school or academy.\""
    y "\"You only have to sign up using your e-mail and log-in. It's a free world for everyone!\""
    "Suspicious indeed."
    "However, the part \"meet with each other\" is especially hard to ignore."
    "What a fearsome power of marketing ability."
    y "\"Sign-up using e-mail. Isn't the app is too cheap? No routine fee? No ads?\""
    "Oh, forget it. Being paranoid will only make me grow into the same person as how my father is."
    y "\"Hello, open community, good-bye, golden cage!\""
    jump story1
label intro:
    python:
        if persistent.plays is None:
            persistent.plays = 1
        else:
            persistent.plays += 1
        
        if persistent.evan is None:
            persistent.evan = 0
        
        if persistent.sarah is None:
            persistent.sarah = 0
        
        if persistent.silo is None:
            persistent.silo = 0
            
        if persistent.dega is None:
            persistent.dega = 0
        
        if persistent.mia is None:
            persistent.mia = 0
            
        if persistent.gwen is None:
            persistent.gwen = 0
        
        if persistent.ide is None:
            persistent.ide = 1
        
        if persistent.fam is None:
            persistent.fam = 1
        
        if persistent.sch is None:
            persistent.sch = 1
        
        if persistent.act is None:
            persistent.act = 1
            
    $ evan = persistent.evan
    $ sarah = persistent.sarah
    $ silo = persistent.silo
    $ dega = persistent.dega
    $ mia = persistent.mia
    $ plays = persistent.plays
    $ gwen = persistent.gwen
    $ ide = persistent.ide
    $ fam = persistent.fam
    $ sch = persistent.sch
    $ act = persistent.act
    if persistent.plays == 1:
        jump prolog
    else:
        show black
        stop music
        play music "music/Blissful Ignorance.mp3"
        call screen phone_reply("Open the chat", "story1", "Reread prologue", "prolog", "Quit", "preend")
        
label story1:
    show mainmenu
    "I was surprised, indeed."
    "In a small app which was released only a few hours ago, at least a thousand new users dove in and signed up."
    "I guess the \"free\" word played a strong part in it. No students can resist the temptation of a free item when it comes to social media."
    "My first amusement found in this app is the capability to look at usernames of people signed up."
    "Students are amazing creatures with boundless imagination and it shows in how they name themselves in this forum."
    "Names related with foods, drinks, television programme, characters of a story, and some even included names from their favorite celebrity."
    y "\"Oh, look at this! dangoMasta? That's hilarious!\""
    "I continued my browsing attempt and discovered more unique names."
    y "\"exoticpaul, mariamMerriam, simsalabimsa... oh, wow! me.handsome!\""
    "Surely a unique way to show up."
    # A pop-up menu came, trying to inform you to join a chatroom
    "A chatroom? Why not!"
    # moves to another page, try to draw an interesting layout for chatroom selection.
    y "\"Ah, what is this?\""
    # You found a chatroom designated for your neighbourhood
    y "\"Pfft, a Lily Street Society?\""
    "I recalled that Lily Street is where my house is located."
    "However, I had never left my house unattended, I had no friends nearby."
    y "\"Can I really join them?\""
    "No, please, no more paranoid little worries!"
    with fade
    stop music
    play music "music/Pleasant Chat_v2.mp3"
    show phone at phone_pickup
    window hide
    # Show an animation of mouse clicking the join button
    # Then, show a confirmation page about your subscription and then hyperlink to the chatroom
    # Begin the chat layout of the game!!
    
    $ renpy.pause(0.1)
    show screen sysnotif("smallcat has joined the room")
    $ renpy.pause(1.1)
    hide screen sysnotif
    show screen phone_message("dangomasta", "Oh, a newcomer!")
    $ renpy.pause(1.4)
    show screen phone_message2("flowerbush", "Welcome!")
    $ renpy.pause(0.8)
    menu:
        "Say \"Hi!\"":
            jump story1_1a
        "*stay silent":
            jump story1_1b
    
label story1_1a:
    show screen player_phone_message3("smallcat", "Hi!")
    $ renpy.pause(2.1)
    show screen phone_message4("dangomasta", "Wow, you are energetic! I like that!")
    $ renpy.pause(1.8)
    hide screen phone_message
    hide screen phone_message2
    hide screen player_phone_message3
    hide screen phone_message4
    $ renpy.pause(1.4)
    show screen phone_message("flowerbush", "You like to befriend anyone, don't you?")
    $ renpy.pause(2)
    show screen phone_message2("dangomasta", "Isn't it good? That way, all people will like me as well.")
    $ renpy.pause(1.1)
    show screen phone_message3("flowerbush", "No, they will only think of you as a freak.")
    $ renpy.pause(1)
    menu:
        "Say \"He-he~\"":
            show screen player_phone_message4("smallcat", "He-he~")
            pass
        "Say \"I don't mind that.\"":
            show screen player_phone_message4("smallcat", "I don't mind that.")
            pass
    $ renpy.pause(1.4)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen player_phone_message4
    $ renpy.pause(1.3)
    show screen phone_message("dangomasta", "See? She agrees with me!")
    $ renpy.pause(1.7)
    show screen phone_message2("flowerbush", "Anyone can laugh it off, you know. Not minding doesn't necessarily mean she agreed to it!")
    $ renpy.pause(1.3)
    show screen phone_message3("flowerbush", "Moreover, we don't know whether it's a he or she!")
    # this game doesn't care whether you are a boy or girl, so take it easy.
    $ renpy.pause(1.4)
    show screen phone_message4("dangomasta", "No matter! Cat is usually used by females, right?")
    $ renpy.pause(1.3)
    jump story1_2
label story1_1b:
    $ renpy.pause(3)
    show screen phone_message3("dangomasta", "... The message is read by 2.")
    $ renpy.pause(1.4)
    show screen phone_message4("flowerbush", "Perhaps smallcat is a shy person.")
    $ renpy.pause(2.2)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(1.3)
    show screen phone_message("dangomasta", "A spy from CIA?")
    $ renpy.pause(1.4)
    show screen phone_message2("flowerbush", "Why would they join us here?")
    $ renpy.pause(1.7)
    show screen phone_message3("dangomasta", "Oh, c'mon, flowerbush!")
    $ renpy.pause(1.6)
    show screen phone_message4("flowerbush", "You and your weird ideas again.")
    $ renpy.pause(1.3)
    jump story1_2
label story1_2:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(1.4)
    if mainCharaFemale:
        show screen phone_message("dake", "It's a she.")
        pass
    else:
        show screen phone_message("dake", "It's a he.")
        pass
    $ renpy.pause(1.3)
    show screen phone_message2("dangomasta", "Welcome back! Where did you go?")
    $ renpy.pause(1.7)
    show screen phone_message3("dake", "There is this little cute cat near the window.")
    $ renpy.pause(0.4)
    show screen phone_message4("dake", "Tried catching it but he ran.")
    $ renpy.pause(2.3)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(0.3)
    show screen phone_message("flowerbush", "You sure are carefree.")
    $ renpy.pause(1.2)
    show screen phone_message2("dake", "That's just how I am.")
    $ renpy.pause(0.6)
    show screen phone_message3("flowerbush", "Also, sneaking a peek on other's profile is not good.")
    $ renpy.pause(0.9)
    show screen phone_message4("flowerbush", "It's a violation on privacy rights.")
    $ renpy.pause(2.1)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(0.7)
    show screen phone_message("dake", "I doubt it. Why would the app allow me to sneak peek then?")
    $ renpy.pause(1.6)
    show screen phone_message2("flowerbush", "That doesn't mean that you can see without permission.")
    $ renpy.pause(1.1)
    show screen phone_message3("dake", "Do I really have to?")
    $ renpy.pause(1.4)
    show screen phone_message4("flowerbush", "Well, duh, you DO have to ask.")
    $ renpy.pause(2.1)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(0.9)
    show screen phone_message("dake", "Really? He didn't ask any permission to join our chatroom.")
    $ renpy.pause(1)
    show screen phone_message2("dake", "We don't know his locations and origins.")
    $ renpy.pause(1.9)
    show screen phone_message3("flowerbush", "... I see your point.")
    $ renpy.pause(1.7)
    show screen phone_message4("dake", "Say, smallcat, which house do you live?")
    $ renpy.pause(1.3)
    menu:
        "Post a pic from neighbourhood.":
            jump story1_3a
        "I'm living at Lily Street no.19":
            jump story1_3b
label story1_3a:    
    $ renpy.pause(0.7)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(0.9)
    #You posted a pic, next chat starts at phone_message3
    show screen phone_message3("flowerbush", "Oh, that's dake's house.")
    jump story1_3
label story1_3b:
    $ renpy.pause(0.7)
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(0.9)
    show screen player_phone_message("smallcat", "I'm living at Lily Street no. 19")
    $ renpy.pause(1.4)
    show screen phone_message2("dake", "Oh, that's nearby.")
    $ renpy.pause(1.7)
    show screen phone_message3("flowerbush", "That's straight ahead your house, dake.")
    jump story1_3
label story1_3:
    $ renpy.pause(3.1)
    show screen phone_message4("dake", "Be right back.")
    $ renpy.pause(1.9)
    hide screen player_phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(1.1)
    if mainCharaFemale:
        show screen phone_message("dangomasta", "Eh, her house is in front of dake's house?")
        pass
    else:
        show screen phone_message("dangomasta", "Eh, his house is in front of dake's house?")
        pass
    $ renpy.pause(1.4)
    show screen phone_message2("flowerbush", "Where have you been?")
    $ renpy.pause(1.7)
    if mainCharaFemale:
        show screen phone_message3("dangomasta", "Someone threw my phone into a bush.")
        $ renpy.pause(1.8)
        show screen phone_message4("dangomasta", "She threw it saying that she had to protect innocent girls.")
        $ renpy.pause(2.3)
        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3
        hide screen phone_message4
        $ renpy.pause(1)
        show screen phone_message("flowerbush", "My, what are you talking about?")
        $ renpy.pause(1.2)
        show screen phone_message2("dangomasta", "Says the culprit.")
        $ renpy.pause(3.3)
        show screen phone_message3("flowerbush", "Oh. Looks like throwing is not enough. Should I wreck the whole stuff and throw it as far as the rooftop? Should I put the entire stuff in a cloth, set it ablaze, skin the entire cover, and throw it to your house instead? Will you be able to regain its original form after shredding it with claws of a cat?")
        $ renpy.pause(2.3)
        show screen phone_message4("dangomasta", "Have mercy! You are breaking the limits of your textbox and it's covering the previous message!")
        $ renpy.pause(2.5)
        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3
        hide screen phone_message4
        pass
    else:
        show screen phone_message3("dangomasta", "I've been sulking.")
        $ renpy.pause(1.1)
        show screen phone_message4("flowerbush", "Huh?")
        $ renpy.pause(2.1)
        hide screen phone_message
        hide screen phone_message2
        hide screen phone_message3
        hide screen phone_message4
        $ renpy.pause(1.7)
        show screen phone_message("dangomasta", "This chatroom is one step closer becoming a desert.")
        $ renpy.pause(1.3)
        menu:
            "I think I understand what you meant.":
                show screen player_phone_message2("smallcat", "I think I understand what you meant.")
                $ renpy.pause(1.4)
                show screen phone_message3("dangomasta", "Ah, how good it is to have a brother in arms! So beautiful~")
                $ renpy.pause(1.6)
                pass
            "My condolences.":
                show screen player_phone_message2("smallcat", "My condolences.")
                $ renpy.pause(1.3)
                show screen phone_message3("flowerbush", "What? What is it all about?")
                $ renpy.pause(1.4)
                pass
        menu:
            "Actually, I too don't understand.":
                show screen player_phone_message4("smallcat", "Actually, I too don't understand.")
                $ renpy.pause(1.8)
                pass
        hide screen phone_message
        hide screen player_phone_message2
        hide screen phone_message3
        hide screen player_phone_message4
        pass
    $ renpy.pause(1.3)
    show sarah-good at Position(xalign = 0.1, yalign = 0.17)
    with dissolve
    $ renpy.pause(1.4)
    show screen phone_message2("dangomasta", "Don't play a joke when it comes down to that thing!")
    $ renpy.pause(1.7)
    show screen phone_message3("flowerbush", "Your reactions are always priceless, dangomasta.")
    $ renpy.pause(1.4)
    show screen phone_message4("dangomasta", "Enough, I'm not visiting your house anymore, flowerbush!")
    $ renpy.pause(1.3)
    show screen sysnotif("dangomasta has left the chatroom")
    $ renpy.pause(1.4)
    hide screen sysnotif
    $ renpy.pause(0.2)
    hide sarah-good
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(1.7)
    show screen phone_message("flowerbush", "Ah, he ran.")
    $ renpy.pause(1.3)
    show screen phone_message2("dake", "Yo, I'm back. Why did dangomasta ran?")
    $ renpy.pause(1.4)
    show screen phone_message3("flowerbush", "Welcome, dake. Dunno, we were just teasing him a little.")
    $ renpy.pause(1.3)
    show screen phone_message4("dake", "How?")
    $ renpy.pause(1.2)
    if mainCharaFemale:
        menu:
            "We were talking about cats, fire, and throwing stuffs up.":
                hide screen phone_message
                hide screen phone_message2
                hide screen phone_message3
                hide screen phone_message4
                $ renpy.pause(1.4)
                jump story1_4a
            "You can read it if you touch the left side of your screen.":
                hide screen phone_message
                hide screen phone_message2
                hide screen phone_message3
                hide screen phone_message4
                $ renpy.pause(1.4)
                jump story1_4b
        pass
    else:
        menu:
            "We were talking about desert and stuffs.":
                hide screen phone_message
                hide screen phone_message2
                hide screen phone_message3
                hide screen phone_message4
                $ renpy.pause(1.4)
                jump story1_4a
            "You can read it if you touch the left side of your screen.":
                hide screen phone_message
                hide screen phone_message2
                hide screen phone_message3
                hide screen phone_message4
                $ renpy.pause(1.4)
                jump story1_4b
        pass
label story1_4a:
    if mainCharaFemale:
        show screen player_phone_message("smallcat", "We were talking about cats, fire, and throwing stuffs up.")
        $ renpy.pause(2.2)
        show screen phone_message2("dake", "Ah, more of flowerbush's sadistic nature.")
        $ renpy.pause(1.3)
        show screen phone_message3("dake", "Don't worry, she is actually a good girl.")
        $ renpy.pause(1.7)
        show screen phone_message4("flowerbush", "You made me heard like some delinquents.")
        $ renpy.pause(1.8)
        menu:
            "Are you a delinquent?":
                hide player_phone_message
                hide phone_message2
                hide phone_message3
                hide phone_message4
                $ renpy.pause(1.4)
                show screen player_phone_message("smallcat", "Are you a delinquent?")
                $ renpy.pause(1.2)
                show screen phone_message2("flowerbush", "Used to. I'm now a straight-laced diligent and cheery girl.")
                $ renpy.pause(1.4)
                show screen phone_message3("dake", "So much just to retain the image of a perfect girl.")
                $ renpy.pause(1.6)
                show screen phone_message4("flowerbush", "Oh, shut it.")
                $ renpy.pause(1.5)
                jump story1_4
            "*stay silent":
                hide player_phone_message
                hide phone_message2
                hide phone_message3
                hide phone_message4
                $ renpy.pause(1.4)
                show screen phone_message("dake", "Well, for sure you were a bad one.")
                $ renpy.pause(1.6)
                show screen phone_message2("flowerbush", "Oh, what might you be talking about, dake?")
                $ renpy.pause(1.2)
                show screen phone_message3("dake", "Just a little bit history between us.")
                $ renpy.pause(1.3)
                show screen phone_message4("flowerbush", "That's enough. We are not going to talk about that.")
                jump story1_4
        pass
    else:
        show screen player_phone_message("smallcat", "We were talking about desert and stuffs.")
        $ renpy.pause(1.4)
        show screen phone_message2("dake", "Ah, dangomasta's usual ramblings.")
        $ renpy.pause(1.7)
        show screen phone_message3("flowerbush", "Yep. We are lucky that his perversion is not contagious.")
        $ renpy.pause(1.3)
        show screen phone_message4("dake", "I don't think it's that bad. Want me to ring him?")
        $ renpy.pause(1.9)
        hide screen player_phone_message
        hide screen phone_message2
        hide screen phone_message3
        hide screen phone_message4
        $ renpy.pause(1.5)
        show screen phone_message("flowerbush", "No need. He'll come back later.")
        $ renpy.pause(1.6)
        show screen phone_message2("dake", "Really? If you say so.")
        $ renpy.pause(1.4)
        show screen phone_message3("flowerbush", "Hmm...")
        $ renpy.pause(1.6)
        show screen phone_message4("dake", "What?")
        jump story1_4
label story1_4b:
    show screen player_phone_message("smallcat", "You can read it if you touch the left side of your screen.")
    $ renpy.pause(1.3)
    show screen phone_message2("dake", "I'm using a laptop, and it is using a common screen.")
    $ renpy.pause(1.7)
    show screen phone_message3("flowerbush", "Why?")
    $ renpy.pause(1.4)
    show screen phone_message4("dake", "Meh, too lazy. I am not on my bike too, so why bother?")
    $ renpy.pause(1.8)
    menu:
        "A bike?":
            hide screen player_phone_message
            hide screen phone_message2
            hide screen phone_message3
            hide screen phone_message4
            $ renpy.pause(1.7)
            show screen player_phone_message("smallcat", "A bike?")
            $ renpy.pause(1.4)
            show screen phone_message2("flowerbush", "dake is commuting to school on motorbikes.")
            $ renpy.pause(1.3)
            show screen phone_message3("dake", "Yep, that's why using a smartphone is a no-go. Replying when me being on my bike is too much of a hassle as well.")
            $ renpy.pause(1.6)
            show screen phone_message4("flowerbush", "Ehh, why?")
            $ renpy.pause(1.5)
            pass
        "Don't you have a smartphone?":
            hide screen player_phone_message
            hide screen phone_message2
            hide screen phone_message3
            hide screen phone_message4
            $ renpy.pause(1.7)
            show screen player_phone_message("smallcat", "Don't you have a smartphone?")
            $ renpy.pause(1.5)
            show screen phone_message2("dake", "I have, but I rarely use it.")
            $ renpy.pause(1.3)
            show screen phone_message3("dake", "Besides, most games on smartphones are not entertaining. I still prefer the ones in laptops.")
            $ renpy.pause(1.6)
            show screen phone_message4("flowerbush", "Laptops are not only for gaming, you know.")
            $ renpy.pause(1.4)
            pass
    hide screen player_phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(1.3)
    show screen phone_message("dake", "Don't be such a sissies. It's pain in the &##.")
    $ renpy.pause(1.7)
    show screen phone_message2("flowerbush", "Hey, watch your words!")
    $ renpy.pause(1.4)
    show screen phone_message3("dake", "Ease up, lass. Can't have my way without bad words once in a while.")
    $ renpy.pause(1.8)
    show screen phone_message4("flowerbush", "Oh, fine, fine. Let's wrap about this badmouthing.")
    jump story1_4
label story1_4:
    $ renpy.pause(1.4)
    hide screen player_phone_message
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message4
    $ renpy.pause(1.5)
    show screen phone_message("flowerbush", "Oh, well, enough about us. Why don't you tell a story about yourself, smallcat?")
    $ renpy.pause(1.8)
    #sa "\"Oh, don't mind us, for now, why don't you tell us more about yourself?\""
    #From this point out, giving away one piece of information is considered as checkpoint.
    #For every one piece of information you gave, your relationship level with your target(s) will be raised by one point.
    #You can choose one information to gave among all four, each level will give bonus affection point to different characters.
    #Please plot it carefully because informations can only be given out at five chances.
    #For the current set of targets, missing the chance to give out all informations will end up at bad route.
    #In the future developments, some targets are even available without you trying to give any informations at all.
    #However, try to rule the balance among them so they will hold the same value as the story goes.
    #Future character development will be done according to the dates and the characters in the story will age to their college days.
    jump informationlist
label informationlist:
    #This stuff is where the game got tricky.
    #Not all people want to hear everyside of your life, so some things are best remained unsaid.
    #You can use this chance to immerse yourself with the protagonist character and clean out targets you don't want to end up with.
    #However, the most unwanted thing to be heard must be told as final piece of information to establish relationship with the chosen target.
    #This thing is important because establishing friendship means that you have to come out as what you are.
    #Without opening about yourself, the target will not disclose his/her truest self.
    #For the first targets, disclosing their truest selves becomes the main goal before the player can take part in events after them.
    menu:
        "Identity.":
            pass
        "Family situation.":
            pass
        "School.":
            pass
        "Favorite activities.":
            pass
        "Why don't you tell your stories instead?":
            pass
    "Oof, the time is close to when Father goes home."
    "Better stop the chat for a while."
    show screen player_phone_message2("smallcat", "Sorry, guys. Time up. I had something to do now.")
    $ renpy.pause(0.8)
    show screen player_phone_message3("smallcat", "I'll tell you my story later on. See you tomorrow!")
    $ renpy.pause(1.6)
    "That would do."
    "See you, free world! Hello again, golden cage."
    hide screen phone_message
    $ renpy.pause(1.1)
    hide screen player_phone_message2
    $ renpy.pause(0.3)
    hide screen player_phone_message3
    $ renpy.pause(0.7)
    hide mainmenu
    $ renpy.pause(0.4)
    stop music
    play music "music/Crisis Calls.mp3"
    jump secact
    show black
    show screen phone_message("SecretHush", "If you are interested in the continuation, please donate to SecretHush!")
    $ renpy.pause(1.7)
    show screen phone_message2("SecretHush", "We are on at Patreon, so click donate and help us finishing this project!")
    $ renpy.pause(1.5)
    show screen phone_message3("SecretHush", "Well, then, see you!")
    $ renpy.pause()
label preend:
    python:
        persistent.plays = plays
        persistent.silo = silo
        persistent.dega = dega
        persistent.mia = mia
        persistent.sarah = sarah
        persistent.evan = evan
        persistent.gwen = gwen
        persistent.ide = ide
        persistent.fam = fam
        persistent.sch = sch
        persistent.act = act
        
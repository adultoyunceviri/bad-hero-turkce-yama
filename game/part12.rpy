


label part12_info:

    scene warning with d
    show screen warningscreen
    pause
    scene frank_upgrade with d
    pause
    scene patrons with d
    pause
    scene saves with d
    pause
    #scene edit with d
    #pause
    #scene hardcore with d
    #pause
    hide screen warningscreen
    pause

label part12:





    scene black with d
    pause
    play music "music/city1.mp3"
    scene 3097 with d
    tim "This is it guys. We’re now cooking Mirage on our own."
    tim "Get out and start finding new customers."
    tim "We’re going to market this as the best product in town."
    tim "I’m not gonna lie, Marty really knows his stuff when it comes to drugs."





    scene black with d
    pause
    scene 3098 with d
    pause
    scene 3099 with d
    pause
    scene 3100 with d
    glen "Hey bro, you got any?"
    scene 3101 with d
    pause




    scene black with d
    pause
    scene 3102 with d
    pause
    scene 3103 with d
    pause
    scene 3104 with d
    jacob "You’re selling product on our territory. "
    jacob "And I know your gang, you aren’t supposed to be here."
    jacob "So, get lose or face the consequences."
    scene 3105 with d
    isaac "That’s a no from us, we’re going to be selling our product here."
    scene 3104 with d
    jacob "Not on our territory."
    play audio "music/punch.opus"
    scene 3106 with vpunch
    stop music
    pause





    scene black with d
    pause
    play music "music/Miami Viceroy.mp3"
    scene 3107 with d
    f "Hey."
    scene 3109 with d
    john "The hell do you want?!"
    scene 3108 with d
    f "Wait, do I know you?"
    f "Aren’t you that asshole that almost shot me?"
    scene 3109 with d
    john "You’re lucky Angel stopped me."
    scene 3108 with d
    f "I’m supposed to pay my taxes to the police today or something? A-ha-ha."
    scene 3109 with d
    john "Funny…. I’m here to see Angel."
    scene 3108 with d
    f "And here I thought one shouldn’t mix business with pleasure. "
    f "Never thought you’d be down for all that submissive bullshit."
    scene 3109 with d
    john "Fuck off! To me, she’s more than an escort."
    john "One day, I’m going to take her far away from this place."
    john "So she never has to deal with assholes and losers, like yourself."
    stop music


    scene black with d
    pause
    play music "music/Danger Storm.mp3"
    scene 3110 with d
    angel "So John, have you seen our new girl?"
    scene 3111 with d
    john "No, Mistress. I have not seen her, Mistress."
    scene 3110 with d
    angel "Her name’s Elsa."
    angel "That’s probably fake."
    angel "I need you to do a deep-dive into her background, I need to know everything about her."
    scene 3111 with d
    john "Yes, Mistress. Whatever you ask for, Mistress."
    scene 3110 with d
    angel "And don’t you dare say a word to anyone."
    angel "This is for my eyes only."
    scene 3111 with d
    john "Yes, Mistress."
    scene 3110 with d
    angel "Enough with this, let’s get to it. "
    scene 3111b with d
    pause
    scene 3111d with d
    angel "And this time, you’re going to work extra hard for me."
    jump part12_hardcore1





label part12_2:



    scene black with d
    pause
    play music "music/Sneaky Snitch.mp3"
    scene 3112 with d
    pause

    menu:

        "{color=#1BBB20} Take a closer look.":

            scene 3113 with d
            pause
            scene 3114 with d
            pause
            scene 3115 with d
            pause

    scene 3112 with d
    chelsey "*So, we couldn’t get the toy back."
    chelsey "*How the hell am I supposed to stretch my ass now. Shit."
    if renpy.loadable("patch.renpy"):

        chelsey "*Although, I think I saw something in Dad’s bag that could help."

    else:

        chelsey "*Although, I think I saw something in Frank’s bag that could help."


    scene 3116 with d
    pause
    scene 3117 with d
    pause

    menu:

        "{color=#1BBB20} Take a closer look.":

            scene 3118 with d
            pause
            scene 3119 with d
            pause

    if renpy.loadable("patch.renpy"):

        scene 3117 with d
        chelsey "*Wait a minute, wasn’t this mom’s?"
        chelsey "*Well damn, I know what I need to do now."
        scene 3117b with d
        chelsey "*Who knew, mom loved using her ass too."

    else:


        scene 3117 with d
        chelsey "*Well damn, I know what I need to do now."
        scene 3117b with d


    stop music



    scene black with d
    pause
    play music "music/Why_Did_You_Do_It_-_Everet_Almond.mp3"
    scene 3229 with d
    if renpy.loadable("patch.renpy"):

        chelsey "Hey sis."

    else:


        chelsey "Hey Kate."


    scene 3227 with d

    if renpy.loadable("patch.renpy"):

        chelsey "So I found this toy in Dad’s bag."

    else:

        chelsey "So I found this toy in Frank’s bag."


    scene 3230 with d
    chelsey "And I thought we can play with it like before."
    chelsey "And you can show me how to use this in my ass."
    scene 3228 with d
    kate "That’s not going to work for me."
    kate "It’s too small, way too small."
    kate "Guess you’re going to have to help yourself. Have fun though. He-he-hee."
    stop music



    scene black with d
    pause
    play music "music/Sneaky Snitch.mp3"
    scene 3120 with d
    chelsey "*So Kate’s being a bitch again."
    chelsey "*Nothing new."
    chelsey "*Guess I’ll have to go it alone then."
    scene 3121 with d
    pause
    scene 3122 with d
    pause
    scene 3123 with d
    pause
    scene 3124 with d
    pause
    scene 3125 with d
    chelsey "*Fuck. This really isn’t doing anything."
    chelsey "*Why did Kate have to be such a bitch earlier. Urgh."
    scene 2884 with d
    pause
    scene 2793 with d
    pause
    play music "music/classicals_breakfast.mp3"
    scene 3126 with d
    may "What they hell are you doing, Chelsey?!"
    scene 3135b
    pause
    scene 3133 with d
    chelsey "Nothing!"
    scene 3132 with d
    may "Really, nothing? I saw everything. "
    scene 3133 with d
    chelsey "Well why didn’t you knock before entering? You’re invading my privacy!"
    scene 3132 with d
    may "This is Frank’s room and Frank isn’t here, so why would I knock? In case you forgot, this isn’t your room."
    scene 3133 with d

    if renpy.loadable("patch.renpy"):

        chelsey "Well Dad lets me use his room whenever I want."

    else:


        chelsey "Well Frank lets me use his room whenever I want."


    scene 3132 with d
    may "I didn’t know, sorry then."
    may "But does Frank know what you’re really using his room for?"
    scene 3133 with d
    chelsey "Of course he does."
    scene 3132 with d
    may "Great! Then you won’t mind if I check with him when he returns?"
    scene 3133 with d
    chelsey "Wait! … Fine."
    chelsey "I’m still a virgin and Kate showed me how to pleasure myself."
    chelsey "But I can’t get it to work and I don’t feel anything."
    chelsey "I can’t get this toy to go deep enough."
    scene 3134 with d
    chelsey "Could you help me, please?"
    scene 3135 with d
    may "Okay, if that’s what you want."
    scene 3134 with d
    chelsey "Thanks."
    scene 3128 with d
    pause
    scene 3129 with d
    pause
    scene 3130 with d
    pause
    scene 3131 with d
    chelsey "Ouch!"
    scene 3193 with d
    chelsey "What the hell was that?!"
    chelsey "That hurt!"
    scene 3192 with d
    may "A-ha-ha. I’m sure it did, but now it’s all the way in."
    may "Just like you wanted."


    scene black with d
    pause
    play music "music/city1.mp3"
    scene 3136 with d
    pause
    scene 3137 with d
    tim "There they are. They beat our guy up and stole his supply."
    scene 3138 with d
    f "Do you know them?"
    scene 3137 with d
    tim "Yeah, they’re from William’s gang, used to buy Mirage from us."
    tim "We used to have joint control of this territory."
    tim "But since Jarred banned us, they’ve been forced to get their supply from another lab."
    tim "Their margins took a big hit, delivery expenses have gone through the roof."
    scene 3138 with d
    f "Alright, let’s see what they want."
    scene 3137 with d
    tim "Drive up, but slowly. We don’t want to spook them and get into a gun fight."
    tim "I know one of them, I’ll introduce you."
    tim "Our former boss used to work with, long-term basis."
    tim "We can get through this, without any violence. "
    scene 3138 with d
    f "We’ll see about that. Buckle up."
    play sound "music/Auto_Go.ogg"
    scene 3139 with d
    pause
    scene 3140 with d
    pause
    scene 3141 with d
    pause
    play sound "music/sound_cardriveby.mp3"
    scene 3142 with d
    pause
    scene 3139 with d
    pause
    scene 3143 with d
    pause
    scene 3144 with d
    pause
    scene 3142 with d
    pause
    scene 3145 with d
    pause
    scene 3144 with d
    pause
    play sound "music/sound_car.mp3"
    scene 3146 with d
    pause
    play audio "music/punch.opus"
    scene 3147 with vpunch
    pause
    scene 3148 with d
    pause
    play audio "music/punch.opus"
    scene 3149 with vpunch
    pause
    scene 3150 with d
    pause
    scene 3151 with d
    pause
    play audio "music/punch.opus"
    scene 3152 with vpunch
    pause
    scene 3154 with d
    pause
    play audio "music/punch.opus"
    scene 3155 with vpunch
    pause
    scene 3154 with d
    pause
    play audio "music/punch.opus"
    scene 3155 with vpunch
    pause

    scene black with d
    pause
    scene 3157 with d
    pause
    scene 3158 with d
    jacob "You’ll regret this!"
    jacob "See you this evening, our boss has been waiting to meet you."

    scene black with d
    pause
    scene 3159 with d
    tim "What the fuck! You two are fucking crazy."
    tim "They’re going to kill us tonight, and that’s it."
    tim "Who the fuck taught you how to handle negotiations, huh?!"
    scene 3160 with d
    f "The streets."
    stop music


    scene black with d
    s "*A couple of hours later."
    pause
    play music "music/Drive_Rock.mp3"
    scene 3161 with d
    pause
    scene 3162 with d
    pause
    scene 3163 with d
    pause
    scene 3164 with d
    pause
    scene 3165 with d
    william "Good evening, my name is William."
    william "You attack 2 of my men."
    william "Started selling product in our territory."
    william "One of my men is in a serious condition in hospital."
    scene 3164 with d
    f "Do you have anything to say for yourself?"
    f "I hate when someone comes between me and my cash."
    f "You beat one of my guys up and took his supply and started selling it for yourselves."
    scene 3165 with d
    william "But that’s our territory, you man wasn’t welcome there."
    william "You can’t just walk and take whatever you want, things don’t work that way."
    william "This city was divided between the different gangs a long time ago."
    scene 3164 with d
    f "I don’t care about that. You stopped buying from, that’s what I care about."
    f "We were forced to distribute ourselves."
    scene 3165 with d
    william "Jared introduced new rules, we had to comply."
    scene 3164 with d
    f "Yeah, I don’t give a fuck about this Jared guy."
    f "Just tell me how I can find him, and I’ll fix this."
    scene 3165 with d
    william "Jared’s a ghost. No one knows who are where he is."
    william "It’s how he keeps control of this city, anonymity is key. "
    scene 3164 with d
    f "A-ha-ha."
    f "So basically, you’re afraid of someone you’re never even seen?"
    f "Who knows, it could be some pathetic nerd pulling your strings."
    f "Back in my day, this shit wouldn’t fly."
    f "To me, you’re nothing. Just a gang of cowards. Beating guys up when they’re all alone. Shameful."
    scene 3165 with d
    william "Shut the hell up, we’re done here. You’re going to pay for what you’ve done."
    william "Jacob will easily put you down."
    scene 3167 with d
    jacob "Yeah, I’ll kick this shit out of you without breaking a sweat."
    scene 3168 with d
    pause
    scene 3169 with d
    f "Just a little bitch if you ask me."
    scene 3170 with d
    f "Really now? I bet she can take you, easily."
    scene 3171 with d
    pause
    scene 3172 with d
    may "What? Why me?!"
    scene 3173 with d
    f "You need to get some practice in for your MMA fights, remember."
    f "This would be unorthodox, but some really good practice, don’t you think?"
    scene 3172 with d
    may "Really Frank…"
    scene 3174 with d
    jacob "Alright then, I could do with a warm-up."
    jacob "First, I knock this bitch out, then I take you out."


    scene black with d
    pause
    scene 3185 with d
    pause
    play audio "music/swoosh.mp3"
    scene 3186 with vpunch
    pause


    scene black with d
    pause
    play music "music/Hitman.mp3"
    scene 3181d with d
    pause
    scene 3181b with d
    pause
    scene 3181 with d
    pause
    scene 3175 with d
    pause
    scene 3176 with d
    paul "Sir! Look, over there."
    scene 3177 with d
    pause
    scene 3178 with d
    william "*Fuck. The Night Dragons."
    william "*They can’t be backing Frank. Shit."
    william "*We’re going to be destroyed if they attack us."
    scene 3180 with d
    pause
    scene 3179 with d
    william "Jacob, enough."
    william "Fine. Frank, let’s make a deal."
    scene 3189 with d
    f "About damn time."
    f "So this is what’s going to happen, you’re going to start buying Mirage from us again and selling it on our streets."
    scene 3179 with d
    william "And what about Jared?"
    william "He controls the labs."
    scene 3189 with d
    f "We’ve dealt with that."
    f "We’re making our own supply of Mirage."
    scene 3179 with d
    william "Quality?"
    scene 3189 with d
    f "Fucking brilliant. Our cook is a goddamn professional."
    f "He also used to work in Jared’s labs. So he knows his stuff."
    f "Trust me, the product is brilliant."
    f "And I’ll give you a discount off the top."
    f "We are back to the good ol’ days."
    scene 3188 with d
    william "Fair enough, we’ve had a long history of working together."
    william "Honestly speaking, our profits have taken a hit after we stopped buying from you."
    william "That said, Jared won’t let this go."
    william "I need assurances that if anything were to happen, you would be there to help us."
    william "If you can agree to that, I’ll gladly agree and start buying from you again."
    scene 3189 with d
    f "We got your backs if anything happens."
    f "Let’s talk details."
    pause


    scene black with d
    pause
    play music "music/district-four.mp3"
    scene 3194 with d
    pause
    scene 3195 with d
    f "Good fucking job, Mike."
    f "These idiots couldn’t even tell you weren’t the real Night Dragons."
    scene 3197 with d
    may "If my father finds out you’ve been impersonating his Clan…"
    may "You will face a most painful death."
    may "I will deal with you later Maike."
    scene 3196 with d
    bigmaike "I love you too, sweety. A-ha-ha."
    stop music

    scene black with d
    pause
    play music "music/Sneaky Snitch.mp3"
    scene 3198 with d
    pause
    scene 3200 with d

    if renpy.loadable("patch.renpy"):


        chelsey "Hi Daddy."

    else:

        chelsey "Hi Frank."

    scene 3199 with d
    f "What are you doing here? "
    scene 3200 with d
    chelsey "I’ve been waiting for you to come back home."
    scene 3199 with d
    f "That smile on your face makes me worry."
    f "So tell me, what are you up to?"
    scene 3200 with d

    if renpy.loadable("patch.renpy"):


        chelsey "I want you to take my virginity, like you did for my sister."

    else:


        chelsey "I want you to take my virginity, like you did for Kate."

    scene 3199 with d
    f "No."
    f "That was a terrible mistake. "

    if renpy.loadable("patch.renpy"):


        f "I had no idea you two were my daughters. "

    scene 3200 with d

    if renpy.loadable("patch.renpy"):


        chelsey "But, Dad!"

    else:

        chelsey "But, Frank!"

    chelsey "Please, we won’t tell anyone."
    scene 3199 with d
    f "I said no. And that’s final."
    f "What we did with Kate wasn’t right."
    scene 3202 with d
    f "Where the hell did you get that?"
    f "Who said you can look through my personal things?"
    scene 3201 with d

    if renpy.loadable("patch.renpy"):


        chelsey "I know this belonged to my mom."


    chelsey "And I also know how it’s supposed to be used."
    chelsey "May even helped me with this."
    scene 3202 with d
    f "I going to talk to May about that."
    scene 3201 with d
    chelsey "But this toy is too small for me now."
    chelsey "If you’re not going to take my virginity, at least get me a bigger toy. I have needs you know."
    scene 3202 with d
    f "I’m not going to get you anything that might hurt you."
    f "You have a small ass, you can forget about big toys."
    scene 3201 with d

    if renpy.loadable("patch.renpy"):


        chelsey "Don’t worry Dad, I promise to be slow and gentle."

    else:

        chelsey "Don’t worry Frank, I promise to be slow and gentle."


    scene 3202 with d
    f "I said no."
    scene 3203 with d
    chelsey "We’ll see about that. "
    stop music

    scene black with d
    pause
    play music "music/Miami Viceroy.mp3"
    scene 2792b with d
    f "The hell were you thinking? Helping Chelsey with her toys."
    scene 2792 with d
    may "She’s grown up, Chelsey will do whatever she wants. No matter what you or I say."
    scene 2792b with d

    if renpy.loadable("patch.renpy"):


        f "Just because you like anal doesn’t mean that my daughter must  too."

    else:

        f "Just because you like anal doesn’t mean that Chelsey must too."


    scene 2792 with d
    may "I just showed her how to do it properly, now it’s up to her to continue or not."
    scene 2792b with d
    f "Well, now she’s asking me for a bigger toy."
    scene 2792 with d
    may "Oh, could you get me one too? I don’t know when I’ll be able to shop around the city again."
    scene 2792b with d
    f "Fuck you, May."


    if renpy.loadable("patch.renpy"):


        f "And from now on, please no helping or encouraging my daughters on exploring their body’s. I already have enough to deal with."

    else:


        f "And from now on, please no helping or encouraging the girls on exploring their body’s. I already have enough to deal with."


    stop music


    scene black with d
    pause
    play music "music/Miami Viceroy.mp3"
    scene 3204 with d
    pause

    menu:

        "{color=#1BBB20} Take a closer look":

            scene 3205 with d
            pause
            scene 3207 with d
            pause
            #scene 3207b with d
            #pause

    scene 3208 with d
    pause
    scene 3209 with d
    john "Hey! I’m John."
    scene 3210 with d
    elsa2 "I’m Elsa."
    scene 3209 with d
    john "Are you new around here?"
    scene 3210 with d
    elsa2 "Yeah, I’ve only started working here recently."
    scene 3209 with d
    john "What’s your real name?"
    scene 3210 with d
    elsa2 "Everyone here calls me Elsa."
    scene 3209 with d
    john "And your surname?"
    scene 3210 with d
    elsa2 "Honestly, I don’t remember."
    elsa2 "I’m sorry, I’ve been suffering from amnesia and don’t remember much about my past."
    scene 3209 with d
    john "Maybe I can help. Do you mind if I take a picture of you?"
    john "I could help you find out about your past, and your family."
    scene 3210 with d
    elsa2 "Yes please! I would like that."
    stop music



    scene black with d
    pause
    play music "music/Sneaky Snitch.mp3"
    scene 3211 with d
    chelsey "*Alright, let’s try something with my pussy."
    chelsey "*Kate said this is another way to have fun."
    scene 3212 with d
    pause
    scene 3212b with d
    pause
    chelsey "*Oooh, this feels good."
    scene 3213 with d
    chelsey "*I’m going to need to get rid of these shorts if I want to continue."
    scene 3214 with d
    pause

    menu:

        "{color=#1BBB20} Take a closer look":



            scene 3215 with d
            pause
            scene 3216 with d
            pause
            scene 3217 with d
            pause

    scene 3220 with d
    pause


    menu:


        "{color=#1BBB20} Watch":


            #scene a134 with fade
            #pause


            scene black with fade:
                "anim_134" with d
            pause


    chelsey "*Oh my God. This really hits the spot."

    if renpy.loadable("patch.renpy"):


        chelsey "What if I try mom’s toy though? She had it around for a reason, right? "


    scene 3218 with d
    pause


    menu:


        "{color=#1BBB20} Watch":


            #scene a125 with fade
            #pause


            scene black with fade:
                "anim_125" with d
            pause

    chelsey "*Oh wow, it way tighter that I though."
    pause

    scene black with d
    pause
    play sound "music/plastinka.mp3"
    scene 3225 with d
    f "Chelsey! What the hell are you doing here?!"
    scene 3226 with d
    chelsey "I can only do this in your room."
    chelsey "And you said I can come in here anytime I want to."
    scene 3225 with d
    f "Yes, but I never though you would be doing this in my room. "
    scene 3226 with d
    chelsey "I’m an adult now and I can do whatever I want to."
    chelsey "If you’re against this, fine. I can always find myself a boyfriend who will satisfy my need."
    scene 3225 with d
    f "No, you’re not getting a boyfriend."
    f "You’re way too naive, and you’ll be taken advantage of. "
    scene 3226 with d
    chelsey "Then how can you be mad at me if you’re denying me any use of alternatives."
    scene 3225 with d
    f "Fine. Urgh."
    f "You can explore yourself, but only when I’m not home. Okay?"
    scene 3226 with d


    if renpy.loadable("patch.renpy"):


        chelsey "Fine. But could you do me a favor, please Daddy?"

    else:

        chelsey "Fine. But could you do me a favor, please Frank?"

    scene 3225 with d
    f "Oh sure, I’ll step out while you wrap this up."
    scene 3226 with d
    chelsey "No, not that, I want you to help me with this, please. "
    chelsey "I can’t do it right by myself."
    chelsey "And Kate doesn’t want to help me. "
    chelsey "So, could you please push that toy deeper in my ass?"
    scene 3225 with d
    f "Hell no."
    scene 3226 with d
    chelsey "Fine, I’ll just get a boyfriend to take advantage of me and to use my body as he likes."
    scene 3225 with d
    f "Fuck me. Fiiine. But let’s make this quick."
    f "I don’t want anyone to see this."



    menu:


        "{color=#1BBB20} Watch":


            #scene a126 with fade
            #pause

            play music "music/Feelin Good.mp3"
            scene black with fade:
                "anim_126" with d
            pause



    if renpy.loadable("patch.renpy"):


        chelsey "Oh yes, Daddy!"

    else:

        chelsey "Oh yes, Frank!"


    chelsey "Deeper!"

    menu:


        "{color=#1BBB20} Watch":


            #scene a127 with fade
            #pause


            scene black with fade:
                "anim_127" with d
            pause


    scene black with d
    pause

    scene 3254 with d
    pause

    menu:

        "{color=#1BBB20} Take a closer look":

            scene 3256 with d
            pause
            scene 3255 with d
            pause


    scene 3253 with d
    chelsey "Look, this toy is too small for me, and the new one won’t be here soon."
    chelsey "So please, could you put your dick in my ass?"

    if renpy.loadable("patch.renpy"):


        chelsey "Sis said it was fun."

    else:


        chelsey "Kate said it was fun."


    scene 3252 with d
    f "What the hell do you mean? What does Kate know about this?"

    if renpy.loadable("patch.renpy"):

        f "I can’t do this with you, especially my own daughters."

    else:

        f "I can’t do this with you."




    scene 3253 with d

    if renpy.loadable("patch.renpy"):

        chelsey "Besides, I could help you get in touch with mom."

    else:


        chelsey "If you refuse, I’ll tell Mrs. Thompson everything."
        chelsey "And you’ll be lucky if you only get fired."


    scene 3252 with d

    if renpy.loadable("patch.renpy"):

        f "Also, how do you know where to find her?"

    else:


        f "Are you threatening me?"

    scene 3253 with d
    chelsey "I can’t wait. I’m horny and need this now!"
    chelsey "This can be our little secret."

    if renpy.loadable("patch.renpy"):

        chelsey "And of course I know where to find her."
        scene 3252 with d
        f "But your sister said she has no idea where her mom is."
        scene 3253 with d
        chelsey "She has no idea because mom loves me more than her."
        chelsey "She left me a phone number and an address."



    scene 3252 with d
    f "*Well shit. What do I do know?"

    if renpy.loadable("patch.renpy"):
        f "*I’ve made no progress whatsoever in finding Gloria."
        f "*Without this help, it could months, at least."
        f "*And I really need my money back. It’ll help me start making real business moves. "
        f "*All this Mirage hustle barely makes any money. "



    if renpy.loadable("patch.renpy"):


        f "*Would it really be that bad if it’s just a quickie with my own daughter? Fuck, am I really considering this."

    else:


        f "*Would it really be that bad if it’s just a quickie with Chelsey? Fuck, am I really considering this."
    f "*Besides, she promised to keep it a secret. So no one will know."
    if renpy.loadable("patch.renpy"):

        f "*With that money, everything will change. "
        f "*We can get real guns and control the streets."
        f "*Get some proper muscle and sell Mirage on our terms."
        f "*Eventually, Jared will go to war with us. And I don’t trust William yet."
        f "*We’ll be alone, with no one to back us up."
        f "*Elvira even told me about the insane profits her casino makes."
        f "*With this money, who knows, I could eventually open a casino. I guess this is it then."
    f "Fine. I’m in. We can do this."




    f "But only if you promise to not tell anyone."
    scene 3253 with d

    if renpy.loadable("patch.renpy"):


        chelsey "Of course, Daddy!"

    else:


        chelsey "Of course, Frank!"


    scene black with d
    pause
    scene 3257 with d

    if renpy.loadable("patch.renpy"):


        f "What are you doing, honey?"

    else:

        f "What are you doing, Chelsey?"

    scene 3259 with d
    chelsey "Is something wrong?"

    scene 3258 with d
    f "Your ass it too tight, I need my dick lubed so you don’t feel any pain."
    f "So, it’ll need to be wet first. Maybe lick it or something."
    scene 3259 with d
    chelsey "Lick your dick?!"
    scene 3258 with d
    f "Yes."

    scene 3259 with d

    if renpy.loadable("patch.renpy"):


        chelsey "Sis never said anything about this."

    else:


        chelsey "Kate never said anything about this."


    scene 3258 with d
    f "Don’t worry, everyone does this."
    scene 3259 with d
    chelsey "Okay, if you say so."
    scene 3260 with d
    pause


    menu:


        "{color=#1BBB20} Watch":


            #scene a133 with fade
            #pause


            scene black with fade:
                "anim_133" with d
            pause

    menu:


        "{color=#1BBB20} Watch":


            #scene a132 with fade
            #pause


            scene black with fade:
                "anim_132" with d
            pause

    scene 3264 with d

    if renpy.loadable("patch.renpy"):


        chelsey "Is this right, Daddy?"

    else:


        chelsey "Is this right, Frank?"


    scene 3263 with d
    f "Yes, sweetheart. "
    scene 3265 with d
    pause
    scene 3266 with d
    pause
    scene 3267 with d
    stop music
    jump part12_hardcore2



label part12_3:


    if renpy.loadable("patch.renpy"):

        scene black with d
        pause
        scene 3281 with d
        pause
        scene 3282 with d
        f "Okay, so you promised to tell me where I can find your mom."
        scene 3283 with d
        chelsey "I was just kidding, Daddy."
        chelsey "I have no idea where she is."
        scene 3284 with d
        f "This was a mistake."
        scene 3285 with d
        chelsey "I’m so sorry, Daddy."






    scene black with d
    pause
    play music "music/jack_the_lumberer.mp3"
    scene 3231 with d
    f "Marty, get off the phone. You’re here to cook, not talk."
    scene 3233 with d
    marty "Hey Frank!"
    scene 3232 with d
    f "We need to increase our Mirage output."
    f "William agreed to distribute our product. "
    scene 3233 with d
    marty "How the fuck did you get that right?"
    marty "Jared banned us. How did you convince William?"
    scene 3232 with d
    f "Let’s just say I’m a natural-born charmer. Ha-ha-haa."
    scene 3233 with d
    marty "Sounds great. Miranda and I can’t wait to get back to business."
    stop music

    scene black with d
    pause
    play music "music/Police_Office.mp3"
    scene 3234 with d
    pause
    scene 3235 with d
    john "Hey Bianca."
    scene 3236 with d
    bianca "How’s it going, John?"
    scene 3235 with d
    john "Can you help me with something? I need full background on this girl, I need anything and everything you can find on her."
    scene 3236 with d
    bianca "Aww, you fell in love and want to make sure she won’t hurt you. So sweet."
    bianca "And here I thought you were only into whores."
    scene 3235 with d
    john "Are you done?"
    scene 3237 with d
    pause
    scene 3238 with d
    bianca "I know her, I mean, I’ve heard of her."
    bianca "She’s the founder of an investment fund, lots of money involved."
    bianca "Her husband reported her missing recently."
    scene 3239 with d
    bianca "Any information on her current whereabouts?"
    scene 3240 with d
    john "Not yet, but I’m chasing down a few leads."
    stop music

    scene black with d
    pause
    play music "music/Danger Storm.mp3"
    scene 3248 with d
    pause
    scene 3250 with d
    angel "How’d it go?"
    angel "I’m sure Frank fucked it up and now you have no way to sell Mirage. Ha, idiots."
    scene 3249 with d
    tim "Everything went according to plan."
    tim "William is working with us again. "
    scene 3251 with d
    angel "*How the hell goes he keep doing it."
    angel "*Someone must be helping him, it’s the only way."
    stop music
    scene black with d
    pause
    play music "music/get_back.mp3"
    scene 3247 with d
    elvira "Hey, miss me yet?"
    scene 3246 with d
    f "Wouldn’t you like that."
    scene 3247 with d
    elvira "Vikki is out and wants to meet May."
    scene 3246 with d
    f "Looks like that concussion really hit her hard."
    scene 3247 with d
    elvira "Not at all. For once, you’ve got it wrong Frank."
    elvira "Vikki is certain your girl is the next big thing in the fighting industry."
    elvira "And she wants to be May’s coach and prepare her for upcoming fights."
    scene 3246 with d
    f "I’ll tell May what you told me."
    f "I’m sure she’ll find this hilarious too."
    f "Oh, and tell your husband I say hello."
    scene 3247 with d
    elvira "He says he never wants to see you ever again! Ha-ha-haa!"

    scene black with d
    pause
    play music "music/Danger Storm.mp3"
    scene 3245 with d
    angel "This is Angel."
    angel "William’s gang has agreed to buying Mirage from us again."
    angel "They’re working together like they used to."
    scene 3244 with d
    shadow "Thanks for the intel, whore. "
    stop music



    scene black with d
    pause
    play music "music/Battle.mp3"
    scene 2608 with d
    shadow "The whore told me that William is ignoring the ban and is back with Frank."
    shadow "Both gangs are teaming up against us."
    shadow "Also, apparently the Night Dragons’ princess brough some assassins with her from the Clan."
    shadow "We need to push back if we don’t want to lose control over that part of the city. "
    jared "That doesn’t sound right. The Nigh Dragons never side with anyone."
    jared "The deal in assassinations, not petty stand-offs between gangs."
    jared "We should distance ourselves from this."
    jared "Can have our fingerprints all over this. Let’s rather have Frank’s lab disrupted through official channels."
    jared "Get in touch with someone from the force. Get them to raid the place."
    jared "If they cook is out of the picture, the production immediately stops."
    jared "Violence isn’t always the answer."
    jared "Our city attracts tourists and addicts. "
    jared "We can’t ruin that reputation by making people think gang violence is prevalent in the city."
    jared "This isn’t back when we took this city by force."
    jared "But we need to make sure they remember who’s in charge. It’s time we make them remember."
    scene 2609 with d
    shadow "Got it, boss."
    stop music


    scene black with d
    pause
    play music "music/Battle.mp3"
    scene 3241 with d
    pause
    scene 3242 with d
    shadow "Jared needs something done."
    scene 3243 with d
    stella "What does he need?"
    scene 3242 with d
    shadow "There’s a new lab in your neighborhood."
    shadow "The lab needs to be raided and the cook detained."
    scene 3243 with d
    stella "That’s not so easy. We get a cut from them, so we turn a blind eye to the lab."
    scene 3242 with d
    shadow "Seems like you’re forgetting who runs this city and how much you owe Jared."
    shadow "That gang, Frank runs it."
    shadow "He’s opened a new lab and now they’re cooking their own Mirage."
    scene 3243 with d
    stella "Frank? Mmm, I know him."
    stella "I think it’s time I pay him a friendly visit. Tell Jared it’ll be handled."
    stop music

    jump end



label part12_hardcore1:

    menu:



        "{color=#1BBB20} Watch.":



            play sound "music/blowjob.mp3"
            scene black with fade:

                "anim_131" with d

            pause
    stop sound
    angel "You’re one of my favorite slaves."
    angel "Do you like me, slave?"
    scene 3111t with d
    john "Yes, Mistress. I like you very much, Mistress."

    menu:



        "{color=#1BBB20} Watch.":




            scene black with fade:

                "anim_135" with d

            pause


    jump part12_2




label part12_hardcore2:

    play music "music/Feelin Good.mp3"

    f "Now turn around and show me your ass."
    scene 3268 with d
    f "This is going to hurt."
    scene 3269 with d

    if renpy.loadable("patch.renpy"):


        chelsey "It’s okay Dad, I can take it."

    else:


        chelsey "It’s okay Frank, I can take it."


    scene 3270 with d
    pause
    scene 3271 with d
    pause
    scene 3270 with d
    pause
    scene 3272 with d
    pause
    scene 3268 with d
    pause
    scene 3274 with d
    pause
    chelsey "Ouch! It hurts!"
    scene 3273 with d
    f "Hold on, it’ll go away."
    scene 3275 with d



    menu:


        "{color=#1BBB20} Watch":


            #scene a129 with fade
            #pause


            scene black with fade:
                "anim_129" with d
            pause
            f "How’s it feeling? "
            chelsey "Better, but take it slow, please."
    menu:


        "{color=#1BBB20} Watch":


            #scene a128 with fade
            #pause

            scene black with fade:
                "anim_128" with d
            pause


    menu:


        "{color=#1BBB20} Watch":


            #scene a130 with fade
            #pause


            scene black with fade:
                "anim_130" with d
            pause



label part12_secret:

    f "I want you to face me, flip around."
    scene 3276 with d
    f "Remember asking me for a favor? I’m going to ask you for one now."
    scene 3277 with d

    if renpy.loadable("patch.renpy"):


        chelsey "I will do anything, Daddy."

    else:


        chelsey "I will do anything, Frank."

    scene 3276 with d
    f "I want to cum on your face."
    scene 3280 with d
    chelsey "On my face!?"
    chelsey "Could you cum anywhere else?"
    scene 3279 with d
    f "No, sweetheart. It has to be the face"
    scene 3286 with d


    menu:

        "{color=#1BBB20} Cum":

            pause
            scene 3287 with d
            pause
            scene 3288 with d
            pause
            scene 3289 with d
            pause


    jump part13_info

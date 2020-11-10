


label start: # 4 строка

    stop music fadeout 1.0
    #jump part12_info
    scene warning with d
    show screen warningscreen
    pause
    #scene writer with d
    #pause
    #scene hardcore with d
    #pause
    scene 2 with d
    pause

    AB "Hey guys, I am AB and if you want to see my list of mods or report any error do it here: {a=https://www.patreon.com/f95IAmAB}Patreon{/a} or {a=https://f95zone.to/members/iamab.1796945/}f95zone{/a}!"
    AB "Server on Discord {a=https://discord.com/invite/fwMgWnH}HERE!{/a}"
    AB "My user in Discord is IAmAB#1400"
    AB "Choices with {color=#1BBB20}this color are the best!"
    AB "{color=#E5170A} With this color are the worse!"
    AB "With no colors are the neutral or that have no future consequence. Gallery mod will be ready in the future. Enjoy!"
    f2 "Hey."
    pause

    #jump part4

    play music "music/Alarm_police.mp3" fadeout 1

    f2 "I'm Frank."
    f2 "I’ve served 18 years I prison."
    f2 "And today I’m meeting with an investigator."
    f2 "I wonder what he wants from me."
    f2 "Probably to add more time to my sentence."

    scene black with d
    play sound "music/Dver_Police.mp3" fadeout 1
    pause 1

    s "Cop arrives."
    play music "music/sexy.mp3" fadeout 1
    scene 11:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    scene 3 with d
    show screen topleftmenu1
    stop music
    Bianca "Who are you talking to?"

    scene 4 with d

    f2 "Nobody, ma'am."
    f2 "Just thinking out loud."
    #f2 "I’ve been alone for a long time now and I’ve missed talking to another real person."

    scene 6 with d
    Bianca "Don’t speak without my permission."
    Bianca "Understood?"



    f2 "Yes, ma'am "
    play music "music/Alarm_police.mp3" fadeout 1
    pause
    scene 8 with d

    f2 "*My God! I haven’t seen a woman’s breasts in ages."
    f2 "*Looks like she finds underwear optional. Can’t complain."
    f2 "*No bra in sight, that is for sure."
    f2 "*I wonder is her panties are also missing…"
    f2 "*Her boobs are stunning."
    f2 "*Wish I could grab them."
    scene 9 with d

    Bianca "Aye, the hell you staring at perv?"
    Bianca "Focus. My eyes are up here."
    f2 "That won't be easy, ma'am."
    Bianca "I dare you to keep staring. I promise you it will be the last thing you see in your pitiful life."
    f2 "I was just paying you a compliment, that’s all ma’am."
    Bianca "Hmm, if you say so."
    stop music fadeout 1
    menu:

        "{color=#E5170A} Your boobs are a dream come true. {color=#FF0000} (-1 Bianca's Point)":
            scene 9 with d
            pause
            show heart with moveintop:
                yalign 0.70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ bianca_score = change_stat(bianca_score,-1)
            hide heart

        "{color=#1BBB20} You look great in this uniform. {color=#FF0000} (+1 Bianca's Point)":
            scene 9 with d
            pause
            show heart with moveinbottom:
                yalign .10 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ bianca_score = change_stat(bianca_score,1)
            hide heart
            f2 "*I saw a smile on her face. Nice."
            f2 "*Her lips are full and gorgeous."
            f2 "*She shouldn’t be an officer."
            f2 "*Constantly around criminals who don’t truly appreciate her beauty."
            f2 "*She could easily fit in with elite escorts at a brothel."


        "{color=#E5170A} I want to take you right here! {color=#FF0000} (Game Over)":

            pause
            jump gameover

    Bianca "I don’t care what you think of me."
    Bianca "I can’t wait to send you back to your cell and forget you ever existed."
    f2 "You never know, you never know..."


    scene black with d
    play sound "music/Dver_Police.mp3"
    pause 1

    s "Someone else is coming."
    scene 13 with d
    pause
    scene 14 with d
    Detective "Well, hi Frank!"
    Detective "It has been a while."
    f2 "Detective, but not long enough."
    f2 "18 years to be precise."
    f2 "I see you haven’t changed."
    f2 "Same suit."
    f2 "Still no bribery hey?"
    Detective "Of course!"
    play music "music/Alarm_police.mp3" fadeout 1
    Detective "I don’t break the law, the law I swore to protect and defend."
    Detective "I could never stoop that low. My moral code will never allow such despicable acts."
    f2 "… Will never allow you to live in a big mansion with a gorgeous woman?"
    f2 "Will never allow you to drive the car of your dreams?"
    f2 "You have wasted a lucrative opportunity that’s been right in front of your eyes for years."
    Detective "I can't do it and you know it."
    f2 "Sure, if you say so."

    stop music fadeout 1
    f2 "So, what’s with today’s visit, detective?"
    f2 "What? Did you miss me that much that you need to apologize before you retire?"
    Detective "You wish. I’m here regarding your release."
    Detective "Officer, remove his cuffs please."
    scene 17 with d
    Bianca "But Sir. He still has 12 more years on his sentence."
    Detective "The times are changing. Money is power, and power is above all. And right now, someone powerful wants him out of prison. "
    Detective "The witness that came forward, recanted. The initial testimony is invalid. "
    Detective "His term was reduced by 20 years."
    Detective "Which means, we’re releasing you."
    f2 "Terrific news detective."
    Detective "I do believe they have no idea who you really are."
    Detective "And I had no say in this."
    Detective "To your advantage, Judge Olsen is unbeknownst to your “accomplishments”."
    Detective "He pretty much told me to ‘shut up’ when I tried to object."
    Detective "This city has gone to shit hey?"
    Detective "Get the release papers ready officer."
    Detective "I can only hope that you have changed so I don’t ever, and I mean ever, have to see you again."
    f2 "You and me both, detective."
    Detective "What was that Frank?"
    f2 "Don’t ever doubt me."
    play music "music/Alarm_police.mp3" fadeout 1
    f2 "*You bet I’ll return the favor."
    scene 3 with d
    f2 "Something on your mind officer? I’ve got places to be."
    Bianca "Stand up."
    stop music fadeout 1
    scene 25 with d
    pause
    #scene black with d
    Bianca "Remove your clothes."
    Bianca "Let’s see if you can back up that big mouth of yours."
    scene 27 with d
    Bianca "What the Fuck. It’s huge. I’ve never seen one this big before."
    Bianca "How long has it been out of use?"
    f2 "You don’t want to know."
    scene 30 with d
    Bianca "Does it still work?"
    f2 "Why don’t you find out?"
    Bianca "I don’t date inmates."
    f2 "I’m a free man, remember."
    Bianca "For how long?"
    f2 "I have changed. I swear."
    f2 "I’ve been here for a long time. A lot of time to reflect on my choices."
    f2 "I could knit you a cozy sweater if that’s enough to convince you."
    f2 "It’ll keep you warm throughout the cold winter nights as you reminisce about our time together."
    play music "music/Alarm_police.mp3" fadeout 1
    scene 33 with d
    f2 "What are you doing?"
    Bianca "Taking a photo."
    f2 "And what are you taking a photo?"
    Bianca "To help me reminisce about our time together (soft chuckle)."
    f2 "Ha ha haa. I knew you liked him. "
    f2 "You know, you don’t only need to look. You can touch too."
    Bianca "No thanks."
    stop music fadeout 1
    scene 34 with d
    Bianca "My friend needs to see it. Hahaha"
    Bianca "A selfie is the best way to show it off."
    Bianca "Now she can’t deny it. "
    Bianca "Brilliant picture."
    f2 "Glad I could be a part of it."
    f2 "*This lack of attention is becoming problematic"
    f2 "Are we done here?"
    f2 "Where’s my clothes? It’s time I leave this place."
    Bianca "Sure, I’ll get them now."
    scene 37 with d
    pause
    scene 38 with d
    f2 "*Now that is a nice ass!"
    f2 "*I want to rip her clothes apart."
    scene 38 with d

    menu:

        "{color=#E5170A} Grab officer's ass. {color=#FF0000} (-1 Bianca's Point/Game Over)":
            scene 120 with d
            pause
            scene 122 with d
            pause
            play audio "music/punch.opus"
            scene 124 with hpunch
            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ bianca_score = change_stat(bianca_score,-1)
            hide heart
            pause
            jump gameover



        "{color=#1BBB20} Make a compliment. {color=#FF0000} (+1 Bianca's Point)":
            scene 38 with d
            f2 "Your legs are exceptional."
            pause
            show heart with moveinbottom:
                yalign .10 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ bianca_score = change_stat(bianca_score,1)
            hide heart


        "Jerk off.":
            pause
            scene 39 with d
            pause
            scene 40 with d
            f2 "*My not-so-little guy is getting hard"
            f2 "Having a woman this close after such a long time..."

            f2 "That’s it, I can’t hold it any longer."
            window hide


    pause

    menu:


        "{color=#1BBB20} Nut all over her ass.":
            scene 40 with fade:
                "anim_3" with d
            pause


            f2 "*Just please don’t look back"
            f2 "*Wait for it…"
            pause
            scene 42
            with flash
            scene 42 with flash
            pause 0.3
            scene 42 with flash
            scene 42 with flash
            pause 2.0

            with d
            scene 43 with d
            f2 "*Aah yes, perfect."
            scene 44 with d
            Bianca "Aye, what’s going on back there?"
            scene 45 with d
            f2 "Nothing worth sharing, officer."
            f2 "*I hope she doesn’t find out what really happened."
            Bianca "*He appears to be staring at my ass."
            Bianca "*I was stupid to allow him that view of my ass."




    scene 48 with d
    Bianca "Try this."
    play music "music/Alarm_police.mp3" fadeout 1
    Bianca "Looks good."
    f "And where is my stuff?"
    Bianca "It was thrown out."
    Bianca "We assumed you’d never get released. Oh well."
    f "Fine, this will have to do."
    f "Just give me my cash and I’ll be gone."
    Bianca "Cash? What cash are you talking about?"
    f "I had a couple grand on me when I was arrested."
    Bianca "I have some bad news for you."
    Bianca "The feds seized it upon your arrest."
    f "What the hell am I supposed to do now?"
    Bianca "Find a job."

    f "You’re kidding right? I’ve never had a job before."
    Bianca "Well then, if you resort to your criminal ways, we’ll have to arrest you and bring you back here, for good this time."
    Bianca "We set up an employment office appointment for you."
    Bianca "Try it out. Who knows, you might find this ‘job’ that you have never tried before."
    stop music fadeout 1
    Bianca "A friend works there, Erin."
    Bianca "Tell her that I sent you."

    f "Fine. Thanks."
    Bianca "Remember, the straight and narrow this time."
    Bianca "And don’t try to run, it will be a waste of your time and ours."

    f "*Good thing I still have some cash stashed away at the country house."
    f "*Once I get that, they can forget about finding me again."
    f "*Need to get there ASAP."
    f "So, we done here?"

    Bianca "Yeah, think so."
    Bianca "Try to stay out of trouble, and please don’t come back."
    Bianca "See you never, I hope."
    f "*As hard as it may be, you won’t. Ha ha haa."


    scene black with d
    pause

    scene 170 with d
    pause

    play music "music/sexy.mp3" fadeout 1
    scene 142:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    scene 143:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    stop music fadeout 1
    scene 168 with d
    play music "music/battle.mp3"
    pause
    scene 156 with d
    Jared "Keep surveilling him."
    strip "Why? What’s in it for me?"
    pause
    scene 159 with d
    pause
    scene 161 with d
    stop music
    pause





    scene 51 with d
    f "Freedom! Here I come!"
    scene black with d
    pause
    play sound "music/action.mp3"
    scene 55 with d
    pause
    scene 56c with d
    pause
    scene 57 with d
    pause
    scene 58 with d
    s "What the hell, man!?"
    menu:
        "Apologize.":
            scene 58 with d
            pause
            scene 59 with d
            pause


        "{color=#1BBB20} Knock the bastard out. {color=#FF0000} (You're the BadHero, aren't you?)":
            scene 184 with d
            pause
            play audio "music/punch.opus"
            scene 185 with vpunch
            pause
            scene 186 with d
            pause
            scene 187 with d
            pause
            #scene 127 with d
            #pause
        "{color=#E5170A} Do nothing. {color=#FF0000} (Game Over)":

            pause
            play audio "music/punch.opus"
            scene 841 with vpunch
            pause
            jump gameover


    scene 60 with d
    pause
    scene 61 with d
    f "I need to get to the country house."
    f "I don’t even have the cash to take a cab."
    scene 89 with d
    pause
    scene 90 with d
    pause
    scene 91 with d
    pause
    scene 93 with d
    pause
    scene 94 with d

    f "Hmmpf. Looks like I’m all set."
    pause
    scene 62 with d
    pause
    play sound "music/Auto_sound.mp3"
    scene 63 with d
    stop sound
    pause
    scene 65 with d
    f "What's up. Nice car dude."
    Driver "Thanks man."
    f "I need to get to this address, mind helping me out?"
    Driver "Sure, no problem."
    play sound "music/Car_Sound.mp3"
    scene 66 with d
    stop sound
    scene 264 with d
    pause
    scene black with d
    play sound "music/Dver_Police.mp3"
    pause 1
    scene 265 with d
    pause
    play music "music/sexy.mp3" fadeout 1
    scene 277:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    stop music
    pause
    play music "music/Alarm_police.mp3" fadeout 1
    scene 272 with d
    Stella "What are you looking at?"
    Bianca "Eh, nothing."
    Bianca "Just scrolling through my gallery."
    scene 275 with d
    Bianca "Hey, it hurts!"
    Stella "Don't you dare lie to me Bianca."
    Bianca "Okay okay. I was just going to send a picture to my friend."
    Stella "I saw you taking those photos with him, forget we have cameras in here?"
    Bianca "It’s just for a friend, her name’s Erin."
    Stella "I’m your only friend, remember."
    Stella "Don’t you dare start thinking about anyone else while we are together."
    Stella "You forget we live together?"
    Stella "Seems like you have. Let’s see if this will jog your memory."
    scene 280 with d
    Stella "It was about this big, right?"
    Bianca "Don’t, please! Please stop!"
    Stella "How about it all inside you?"
    Stella "Since you can’t stop thinking about how big it is."
    Bianca "No! Please don't!!!"
    scene 282 with d
    Stella "I’m just kidding honey. You know I would never hurt you."
    Stella "I do have to discipline you. Let’s try a more hands-on approach."
    Stella "I guess spanking will have to do… for now."
    scene 284 with d
    pause
    menu:

        "{color=#1BBB20} Spank her":

            scene 284 with fade:
                "285" with d
                pause 1.5
                "284" with d
                pause 1.5
                repeat
    pause
    Bianca "mmm"
    scene 284 with d
    pause
    scene 285 with d
    Bianca "mmm"
    pause
    scene 291 with d
    Stella "You like that, huh?"
    Bianca "No, no, not at all. It hurts, it hurts a lot."
    Stella "Do you think I’m a fool?"
    Stella "That’s all, for now."
    Stella "I hope you’ve learned your lesson; I would hate to use more extreme tactics next time."
    Bianca "Yes, of course. It will never happen again."
    Stella "I’m glad."
    Stella "Anyways, what were you two talking about?"
    scene 293 with d
    Bianca "Information regarding his release."
    Stella "Don’t forget how dangerous he is. "
    Stella "Frank will be behind bars, sooner or later."
    Bianca "Well he looked pretty free to me."
    Stella "You truly have no idea what’s really going on."
    Stella "Just be careful around him."

    Stella "I’m gotta go."
    Stella "Chat later."
    scene 296 with d
    pause
    scene 299 with d
    stop music fadeout 1
    pause

    scene 563 with d
    play music "music/forest.mp3" fadeout 1
    pause
    f "This is where I hid my “in case of emergency” stash."
    scene 530 with d
    f "I hope no one followed me."
    stop music fadeout 1
    f "Oh, hello there, how I’ve missed you."
    f "I knew this would one day come in handy."
    scene 533 with d
    pause
    scene 534 with d
    pause

    scene 536 with d
    f "This is all I needed, now I can disappear for good."
    scene 537 with d
    pause
    scene 538 with d
    pause
    play sound "music/plastinka.mp3"
    scene black with d
    pause 2
    scene 539 with d
    f "Wait. Something isn’t right here."
    f "What? My money. Where is it?!"
    f "What’s this?"
    f "A letter. From who?"
    scene 540 with d
    Gloria "*H Frank. If you are reading this, it means you are out of prison."
    Gloria "*You’re a worthless old man with nothing to his name. How sad."
    Gloria "*I took your money, didn’t seem like you would need it."
    Gloria "*When the feds took you, they seized everything."
    Gloria "*I had to find a way to support myself and our two kids."
    Gloria "*Yes, 2 kids. When you were arrested, I was pregnant."
    Gloria "*So, by now, you are the father 2 girls."
    Gloria "*And no, I’m not going to share their identities with you."
    Gloria "*They don’t need a father like you in their lives."
    Gloria "*I know you’ll try to find me, but don’t, I’m long gone."
    Gloria "*New identities and everything. What can I say, I learned a thing or two over the years."
    Gloria "*And one last thing, I left you this toy as a souvenir. Something to remember me by."
    Gloria "*Remember when you got this for me."
    Gloria "*So I could use this, instead of finding other men to satisfy my needs."
    Gloria "*It was fun while it lasted, but I think you’ll need it more than me after your time in prison. Ha ha ha."
    Gloria "*All this cash, I’m sure I’ll find a way to satisfy my needs."
    Gloria "*You were really prepared for a rainy day. "
    Gloria "*I was surprised when I found this much cash."
    Gloria "*I’m going to be set for a long, long time."
    Gloria "*Yours truly, Gloria."
    f "*This bitch. She made me think she was sleeping when I dealt with the money. Shit."
    f "But, you did not anticipate my early release. "
    f "You may be far away, but not far enough. I will find you."
    scene 543 with d
    f "And you will regret trying to play me."
    f "‘Til we meet again, Gloria."
    f "I’ve got to give it to her, she played me well. Never expected her to be capable of something like this."
    scene 578 with d
    pause
    scene 65 with d
    play sound "music/Car_Sound.mp3"
    Driver "You aren’t from around here are you?"
    f "That obvious. It’s been a while since I’ve visited this place."
    Driver "Ha, now I remember, you served time hey. I picked you up near prison."
    f "Got me there. But we can keep this between us hey (soft chuckle)."
    f "What’s there do around here at night?"
    Driver "There’s a casino by the café."
    Driver "High stakes poker games, if you’re into that sort of thing."
    f "Back in the day, there never used to be a casino here. "
    Driver "Yeah. It all changed when that Jared guy showed up."
    Driver "Everyone works for him, he controls everything."
    Driver "He began establishing gambling in the city."
    Driver "Our city has become party central. "
    scene 70 with d
    Driver "We’re here. "
    Driver "Here you can get some food."
    Driver "Be careful though, this neighborhood is no joke. "
    f "Gotcha. Thanks man."
    f "How do I contact you?"
    Driver "You can usually find me by the casino."
    f "Sure. See you later man."
    stop sound fadeout 1
    scene 76 with d
    play music "music/piano.mp3"
    Waitress "Good evening sir, ready to order?"
    f "Whiskey, a bottle. And surprise me with something to eat."
    Waitress "Will do, sir. I’ll be back shortly with your order."
    f "*It’s a nice café – quiet and away from the busy city life."
    scene 79 with d
    Waitress "Here’s your order sir. Enjoy your meal and if you need anything just shout."
    f "Thank you. Looks delicious. It’s a nice place this, food looks good and the service is great."
    Waitress "It’s our job, sir. Nothing but the best for our customers."
    scene 80 with d
    stop music fadeout 1
    f "Whiskey. Oh, how I’ve missed you."
    f "Can’t wait to savor this heavenly elixir in peace. "
    play sound "music/Dver_Police.mp3"
    scene 81 with d
    pause
    scene black
    pause
    play music "music/sexy.mp3" fadeout 1
    scene 82:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    scene 83 with d
    stop music
    pause
    scene 84 with d
    play music "music/piano.mp3"
    pause
    scene 83 with d
    pause
    scene 84 with d
    pause
    scene 83 with d
    pause
    scene 85 with d
    pause
    scene 87 with d
    f "For fuck’s sake, who’s messing with the lights?"
    scene 101 with d
    pause
    scene 102 with d
    f "Oh, how I’ve missed the sight of a beautiful woman. "
    f "Prison truly deprives you of the good things in life."
    f "It’s time to get back in the game."
    scene 106 with d
    pause
    scene 109 with d
    pause
    scene 112 with d
    Waitress "Good day ma’am. Welcome to Albert’s Café."
    Waitress "Anything to drink?"
    Kori "Martini, olives on the side, please."
    Waitress "Anything else?"
    Kori "That’s all thanks."
    Waitress "I’ll be right back with your drink ma’am."
    scene 115 with d
    Waitress "One martini, with olives on the side. Enjoy ma’am."
    Kori "Thanks."
    scene 116 with d
    pause
    scene 117 with d
    f "*She’s staring. Seems like she wants more than that martini."
    f "*Let’s be patient. She could be waiting for someone. Let’s see what happens."
    #scene 118 with d
    scene 119 with d
    pause
    scene 300 with d
    pause
    scene 303 with d
    Kori "Excuse me, mind if I join you?"
    f "Not at all. Please, take a seat."
    scene 304
    Kori "I’m Kori, it’s a pleasure to meet you."
    scene 318 with d
    f "Frank. And please, the pleasure is mine."
    scene 304 with d
    Kori "I apologize for interrupting."
    Kori "I was supposed to meet a friend here, but she just said she can’t make it. "
    Kori "I ordered a drink, but don’t have any cash on me."
    Kori "If you could help me out, I’m there’s a way I could return the favor."
    scene 318 with d
    f "No problem, I’ve got you covered."
    f "*I’m running low on cash as it is, and now I need to cover her receipt."
    f "*Anyways, I’ll just have to make it work."
    scene 304 with d
    Kori "You aren’t from around here hey? "
    scene 318 with d
    f "Yeah, but I plan to stick around for a little while."
    scene 304 with d
    Kori "How about a toast – to new friendships."
    scene 318 with d
    f "Sounds good."
    scene 309 with d
    Kori "A bottle of wine, please."
    Waitress "Sure ma’am. I’ll be right back with your bottle."
    scene 305 with d
    f "*Shit. I didn’t know she meant the whole bottle. I’m definitely going to be short now."
    f "*Oh well, going to have to make it work somehow."
    scene 311 with d
    Waitress "Your wine, ma'am."
    Kori "Thank you."
    scene 312 with d
    Kori "To new friendships!"
    scene 313 with d
    f "Yes! To new friendships and new experiences!"
    scene 314 with d
    pause
    scene 304 with d
    Kori "I just recently broke up with my boyfriend. And I really wanted to chill with my friend and get over him."
    Kori "He was a real asshole. Always pick the bad ones."
    scene 318 with d
    f "Trust me, not all men are like that. Some of us don’t know how to appreciate a good woman."
    f "And I’m a great listener, by the way."
    Kori "Are you waiting for someone else?"
    scene 304 with d
    Kori "A friend? A girlfriend maybe?"
    scene 318 with d
    f "No, it’s just me. Here to start over. A fresh start."
    scene 304 with d
    Kori "Great! Let’s drink to new beginnings! Ha haa."
    f "Sure, why not!"
    scene 314 with d
    pause
    scene 313 with d
    pause
    scene 304 with d
    Kori "How come someone so handsome is here all by himself?"
    scene 318 with d
    f "*The wine is clearly starting to get to her. Let’s see where this line of questioning leads."
    f "Well, I’ve been away on holiday and never found someone I could connect with."
    scene 304 with d
    Kori "Ohh, interesting. Guess they never had what you wanted."
    Kori "My ex just used me for sex, you know how it is sometimes."
    f "Yeah, I’m sorry."
    scene 321 with d
    pause
    scene 325 with d
    pause
    scene 330 with d
    pause
    scene 331 with d
    Kori "Let’s drink to us."
    f "*Us? The hell does she mean ‘us’?"
    f "Maybe we should wait a little and drink more later?"
    Kori "No. I want to have this bottle now."
    f "Fine, let’s drink then."
    scene 314 with d
    pause
    scene 335 with d
    pause
    scene 337 with d
    pause
    scene 339 with d
    pause
    f "Woah. What’s this? Getting frisky are we."
    scene 340 with d
    pause
    scene 341 with d
    f "*Ha-ha. Seems like the alcohol is taking over."
    scene 342 with d
    f "*Woah girl, take it easy."
    scene 343 with d
    pause
    scene 332 with d
    Kori "Oh, I think the wine is getting to me. I’m starting to feel dizzy."
    Kori "Let’s go to your place and sober up?"
    scene 333 with d
    pause
    scene 334 with d
    f "*My place? I don’t even have enough cash for the drinks, let alone a place to stay."
    f "*What am I going to do. Need to find a way out of this one."
    scene 346 with d
    f "I’d love to, but I’m crashing at a friend’s place. And I doubt he would appreciate me bringing someone over."
    f "What about your place then?"
    scene 349 with d
    Kori "I have a roommate and she also won’t appreciate me bringing home a guy."
    f "Okay, we’ll figure it out."
    scene 351 with d
    pause
    scene 354 with d
    Kori "Settle the bill and we can decide."
    scene 355 with d
    f "One moment, need the restroom."
    scene 354 with d
    Kori "Make it quick."
    scene 353 with d
    Kori "And I’ll finish my glass."
    stop music fadeout 1
    scene 357 with d
    pause
    scene 359 with d
    pause
    scene 360 with d
    pause
    scene 361 with d
    pause
    scene 363 with d
    pause
    scene 365 with d
    pause
    scene 366 with d
    pause
    scene 367 with d
    pause
    scene 368 with d
    pause
    scene 369 with d
    pause
    scene 375 with d
    pause
    play audio "music/punch.opus"
    scene 372 with hpunch
    pause
    scene 376 with d
    pause
    scene 392 with d
    pause
    scene 389 with d
    pause
    scene 390 with d
    pause
    play audio "music/punch.opus"
    scene 391 with hpunch
    pause
    scene 377 with d
    pause
    scene 380 with d
    pause
    scene 383 with d
    f "Nice."
    f "Now I can cover the bill."
    scene 394 with d
    f "I'm back."
    f "Let me settle the bill and then we can get out of here."
    scene 396 with d
    pause
    scene 398 with d
    play music "music/city1.mp3" fadeout 1
    Kori "I think I had a little too much to drink."
    Kori "Do you mind holding me, pretty please?"
    scene 401 with d
    pause
    scene 403 with d
    pause
    scene 404 with d
    pause
    scene 411 with d
    Kori "Wait, I need to use the bathroom."
    f "Hold it, we’ll find a bar quickly."
    stop music fadeout 1
    pause
    play sound "music/bike1.mp3"
    Kori "No, sorry, but I can’t hold it anymore."
    scene 413 with d
    Kori "I’ll go here around the corner."
    scene 579 with d
    pause
    stop sound
    pause
    play music "music/city1.mp3" fadeout 1
    scene 416 with d
    pause
    scene 419 with d
    Kori "Mind helping me out?"
    f "Sure, no problem."
    scene 422 with d
    Kori "Let’s be honest, you know I didn’t need the bathroom."
    Kori "I want to pay you back for the drinks, but I don’t have money."
    Kori "But I think there’s another way I can make up for it…"
    f "I like where this is going."
    scene 424 with d
    pause
    scene 425 with d
    pause
    scene 428 with d
    Kori "Remove your pants Frank, it’s time to see what you’ve been hiding."
    scene 431 with d
    pause
    scene 432 with d
    pause
    scene 436 with d
    Kori "Shit. It’s huge Frank!"
    f "And it’s all yours to use."
    scene 438 with d
    Kori "But why is it still soft?"
    Kori "Don’t you find me attractive? Don’t I get you hard?"
    f "Of course you do. You just need to show it some attention and it will show you how appreciated he is."
    Kori "Alright then, what about this?"
    scene 440 with d
    pause

    menu:

        "{color=#1BBB20} Jerk off.":
             scene 442 with fade:

                "anim_4" with d

    pause
    scene 448 with d
    Kori "You were right Frank, all he needed was a little attention."


    menu:

        "{color=#1BBB20} Jerk off.":

            scene 448 with fade:
                "anim_5" with d
    pause
    scene 473 with d
    Oscar2 "Hey asshole, give me your money and your valuable now!"
    f "I don’t have anything. I used it all at the café."
    scene 474 with d
    pause
    scene 475 with d
    Kori "Give me your money now, or I’ll shoot your dick off."
    f "Oh, I see. Let me guess, this is your ‘ex-boyfriend’ Kori?"
    Kori "That’s none of your business asshole. Just give us your money and you won’t get hurt."

    menu:

        "{color=#1BBB20} Jerk off.":

            scene 476 with fade:
                "anim_6" with d
            Kori "The hell are you doing?"
            f "My apologies, I just couldn’t help myself."
    pause
    scene 480 with d
    pause
    scene 482 with d
    pause
    scene 483 with d
    Kori "He fucking blinded me!"
    Kori "He came right in my fucking eye."
    Kori "I can’t see shit. Oscar, help me!"
    scene 485 with d
    Oscar2 "What the fuck Kori! You just used my real name, stupid bitch."
    f "Too late, Kori and Oscar. I know your names and faces now."
    scene 487 with d
    stop music fadeout 1
    f "Cops! Over here."
    scene 488 with d
    Oscar2 "Where? "
    scene 489 with d
    play music "music/battle2.mp3"
    pause
    scene 498 with d
    pause
    scene 497 with d
    pause
    scene 499 with d
    pause

    scene 509 with d
    pause
    play audio "music/punch.opus"
    scene 510 with hpunch
    pause
    scene 513 with d
    pause
    scene 512 with d
    pause
    play audio "music/punch.opus"
    scene 514 with hpunch
    pause
    scene 523 with d
    pause
    play audio "music/punch.opus"
    scene 524 with hpunch
    pause
    scene 525 with d
    pause
    scene 515 with d
    pause
    scene 517 with d
    pause
    scene 526 with d
    Kori "*Take this, Frank."
    scene 527 with d
    pause
    scene 546 with d
    Kori "Get him, Oscar."
    pause
    scene 547 with d
    pause
    play audio "music/punch.opus"
    scene 548 with hpunch
    pause
    play audio "music/punch.opus"
    scene 549 with hpunch
    pause
    play audio "music/punch.opus"
    scene 550 with hpunch
    pause
    scene 553 with d
    pause
    scene 554 with d
    pause
    play audio "music/punch.opus"
    scene 555 with hpunch
    pause
    scene 556 with d
    pause
    scene 557 with d
    pause
    scene 559 with d
    pause
    scene 560 with d
    pause
    play audio "music/punch.opus"
    scene 561 with hpunch
    pause
    scene 562 with d
    pause
    scene 564 with d
    f "Mask off, Mr ‘ex-boyfriend’ Oscar."
    stop music fadeout 1
    scene 565 with d
    f "You choose. Who dies first?"
    scene 567 with d
    Kori "Please, Frank, don't kill me."
    Oscar "He’s bluffing. Not everyone can take a life with their own hands."
    Oscar "He’s just some regular family guy who doesn’t want trouble or know how to kill. "
    Oscar "Just let us go and you’ll never see us again."
    f "See that’s what you think. I just got out. Yes, of prison."
    f "18 years. 18 long, grueling years."
    f "And now that I’m out, I have nothing to lose. I hope you’re ready to meet your maker."
    scene 569 with d
    Oscar "Seriously Kori! You really couldn’t tell he was a criminal and not some tourist?"
    Oscar "Look at him. He looks like he has no money."
    Kori "Fuck you, next time you try and find the target."
    Kori "You were the one a gun."
    Kori "And even with the gun you were totally useless. What a waste."
    Oscar "He caught me off guard!"
    scene 571 with d
    Kori "Just kill him Frank. And then we can continue what we started."
    Oscar "Look at this bitch. You know how many times I’ve saved your ass and this is the thank you I get?"
    Kori "I do all the heavy lifting here, all you do is take the money."
    Oscar "Well you know what, your blowjobs are terrible. I would rather use my hand."
    Kori "Don’t listen to him Frank, he’s just jealous and a real piece of shit."
    Kori "I swear to God I’m gonna kill you! Aaaah!"
    scene 572 with d
    f "Dear God, can you two just shut the fuck up. You’re giving me a headache."
    scene 574 with d
    f "You weren’t that bad."
    f "From now on you work for me. Okay."
    f "I’ll give you assignments on upcoming jobs and you need to complete them. Perfectly."
    f "Agreed?"
    Oscar "Agreed. I’ll honestly do anything to not work with this bitch."
    Oscar "Finally, something good."
    f "And you Kori? You in?"
    Kori "Yes, I'm in."
    f "I’ll be taking your gun."
    f "Get yourself something else."
    f "I’ll find you when I need you. Later."
    scene 204 with d
    pause
    scene 208 with d
    pause
    scene 174 with d
    f "What a day."
    f "Time to rest. Hopefully turns out better."
    f "I hope the owner of this mattress doesn’t show up."
    f "I need to find a place to stay. "
    f "Nights are getting colder, need somewhere to warm up."
    scene 175 with d
    scene black with d

    s "*8 hours later."

    scene 176 with d
    pause
    scene 177 with d
    Bianca "Wake up, Frank."
    scene 178 with d
    f "Who is this? "
    Bianca "It’s me, Bianca."
    f "What are you doing here?"
    Bianca "I really liked you, so I needed to see you again."
    f "I knew you would want some more, I’m glad you came back."
    Bianca "Frank, Frank. Wake up."
    f "Wait, not yet. Let’s relax some more, I like lying in bed with you."
    Bianca "Wake up, asshole! Or your ass is about to get some action."
    play sound "music/plastinka.mp3"
    scene 178 with vpunch
    f "What!?"
    scene 181 with d
    pause
    scene 189 with d
    f "Who the hell are you? And what the hell are you doing here?"
    Marty "I’m Marty, and I’m homeless."
    f "And why are you here, next to me?"
    Marty "Well, it is my bed after all."
    Marty "I got back late last night, very drunk. Saw someone lying on the mattress, assumed it was another homeless guy."
    Marty "Didn’t feel like investigating, so here we are."
    Marty "It began to get cold, needed heat, so I went for a quick cuddle."
    f "Don’t ever fucking try this again."
    Marty "By the way, you don’t look homeless."
    f "I’m not, let’s just say I’m a temporary homeless resident. I’m Frank, by the way."
    Marty "We’re all temporary homeless residents man. Ha ha ha. If you’re going to be one of us, you better find your own mattress, I don’t share. "
    scene 193 with d
    Marty "How about a morning wake-up drink?"
    menu:
        "{color=#E5170A} Take a drink. {color=#FF0000} (Game Over)":
            f "Sure. I can skip work tomorrow."
            scene 212 with d
            pause
            scene black with d
            pause
            s "*You failed to find a job."
            jump gameover



        "{color=#1BBB20} Refuse.":
            scene 193 with d
            f "Can’t. Have an appointment at the employment office today."



    f "You got anything to eat around here?"
    Marty "Here, take some cash. You can pay me back later."
    scene 195 with d
    pause
    scene 197 with d
    pause
    scene 199 with d
    f "Look at this, a sweet. "
    Marty "Woah. Stop. Don’t eat that. It’s called ‘Mirage’."
    f "What’s Mirage?"
    Marty "A new designer drug."
    Marty "Manufactured in underground labs throughout the city."
    Marty "There’s been a spike in the number of local gangs that distribute Mirage. "
    Marty "Targeting random tourists and anyone wanting a good time."
    Marty "It’s all run by Jared. "
    f "How you know all this?"
    Marty "I used to work at one of the underground labs. I know how it all works."
    f "Alright. But I gotta go, looking for a job. See you later Marty."
    Marty "I’ll be here. Good luck. See you later."
    scene 130 with d
    f "*Time to find a job."
    f "*Bianca arranged an appointment for me. Let’s see how it goes. "
    f "*I hope they have something to offer me."

    f "Good day ma’am."
    pause
    play music "music/sexy.mp3" fadeout 1
    scene 131:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    hide screen topleftmenu1
    show screen topleftmenu2
    scene 134 with d
    stop music fadeout 1
    play music "music/office.mp3" fadeout 1
    f "I’m Frank. I’m for employment appointment. Bianca sent me. "
    Erin "Yes, of course. Please, take a seat. Bianca informed me about your visit."
    Erin "I must say, it’s the first time she’s done this for one of the inmates."
    Erin "I wonder what makes you so special?"
    scene 242 with d
    pause
    scene 215 with d
    Erin "I have some questions I need you to answer."
    f "Sure, fire away."
    Erin "Tell me about your previous jobs."
    scene 217 with d
    f "I’ve never had a job before."
    Erin "Any useful working skills? Your educational background?"
    f "I finished high school. Not college, don’t have a degree."
    f "Unfortunately, I don’t have any specific skills to the work environment."
    Erin "Oh. I won’t be easy to find a job for you, especially regarding your lack of skills."
    Erin "Please, fill out this form."
    Erin "I’ll look through available vacancies and see if anything sticks out."
    scene 242 with d
    pause
    scene 223 with d
    pause
    scene 228 with d
    pause
    f "Apologies, I dropped the pen. Let me get it."
    scene 231 with d
    pause
    scene 232 with d
    f "Wow, those are nice. Let me try and get a closer look before she realizes what I’m doing down here. "
    scene 233 with d
    pause
    menu:
        "{color=#E5170A} Spread her legs wide open. {color=#FF0000} (Game Over)":
            scene 234 with d
            pause
            scene 235 with d
            pause
            scene 238 with d
            pause
            play audio "music/punch.opus"
            scene 239 with hpunch
            pause
            jump gameover



        "{color=#1BBB20} Take a closer look. {color=#FF0000} (+1 Erin's Point)":

            pause
            show heart with moveinbottom:
                yalign .15 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ erin_score = change_stat(erin_score,1)
            hide heart


        "{color=#E5170A} Compliment {color=#FF0000} (-1 Erin's Point)":

            pause
            f "You have a great taste in underwear!"
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ erin_score = change_stat(erin_score,-1)
            hide heart
            pause


    scene 219 with d
    pause
    scene 220 with d
    pause
    scene 221 with d
    pause
    scene 240 with d
    Erin "What are you doing down there?"
    menu:

        "{color=#1BBB20} Apologize. {color=#FF0000} (+1 Erin's Point)":

            f "The pen rolled further in, had to move closer."
            pause
            show heart with moveinbottom:
                yalign .15 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ erin_score = change_stat(erin_score,1)
            hide heart

        "{color=#E5170A} Make a joke. {color=#FF0000} (-1 Erin's Point)":
            f "Admiring your panties, ma'am."
            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ erin_score = change_stat(erin_score,-1)
            hide heart
            pause

    Erin "It seems like that’s not the only reason you took so long."
    Erin "Go sit back in your seat. I think I’ve found a job for you."
    scene 242 with d
    Erin "Since you lack any specific skills, work experience and a degree."
    Erin "This is what I could find: Freight mover, Delivery guy, Mailman."
    Erin "Your choice."
    f "Those are all physical jobs."
    f "I’d prefer to be working smarter, rather than harder. "
    f "Is there anything available regarding that?"
    Erin "I’ll see. But tell me, why should I help you?"
    f "You’ll never find someone like me. I can be very persuasive."
    f "How about I take you out for dinner? Treat you right and we see what happens."
    f "Do you have a boyfriend?"
    Erin "Bianca mentioned your high self-confidence, but this is something else."
    Erin "I’m speechless."
    Erin "Ten minutes together and you’re already asking me out. "
    f "Please. I’ll do anything, just find me a decent job and I’ll make it worth your while."
    f "Trust me, you’ll want to see what I have in store for you."
    Erin "I'm married to Judge Olsen. Ever heard of him?"
    f "Yeah, I’ve heard of him. What about him?"

    menu:

        "{color=#1BBB20} Ask her out to dinner {color=#FF0000} (+1 Erin's Point)":

            f "But don’t worry, he won’t come between us and a friendly dinner."
            pause
            show heart with moveinbottom:
                yalign .15 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ erin_score = change_stat(erin_score,1)
            hide heart

        "{color=#E5170A} Do nothing. {color=#FF0000} (-1 Erin's Point)":

            scene 242 with d
            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ erin_score = change_stat(erin_score,-1)
            hide heart
            pause


    scene 244 with d
    Erin "Okay then. I found a job that fits your skills."
    Erin "I can’t directly recommend you because of your past."
    Erin "But here’s the time and address of the job interview."
    f "Thank you, what is it about?"
    Erin "A boarding school is looking for a staff member to escort the students around on field trips."
    Erin "Meet tomorrow at the local café. There will be other applicants though. "
    Erin "I’ll tell them to come an hour later, so use that time to win them over."
    scene 242 with d
    f "Thank you, I won’t let you down."
    scene 246 with d
    Erin "Bianca?! Who the fuck is this guy? I was barely able to find him a job."
    Erin "You better have a damn good reason for sending him to me."
    Bianca "I just sent you a pick. Check you email, you’ll understand why."
    Erin "Alright, let’s see what this reason is. "
    scene 248 with d
    Erin "Oh my. It’s huge! But why are you sending me this?"
    Erin "Where did you get this picture? The internet?"
    Bianca "It’s his. Trust me, he changed in front of me."
    Erin "Bianca, really. Why are you lying to me?"
    Bianca "I knew you won’t believe me, so I’m sending through another picture."
    Bianca "This one’s a selfie."
    scene 249 with d
    Erin "My God. It is real."
    Erin "But why are you sending me all of this?"
    Erin "You know I’m at work."
    Bianca "I know, I know. I was just having some fun. And besides, you asked why I sent him to you."
    Erin "And what am I supposed to do now?"
    Bianca "Oh, you know what to do. And there’s a little something in your desk drawer that might help you."
    Erin "Seriously Bianca. Digging in my drawers while I’m out?"
    Bianca "Oh, would you look at time, I’ve got to go. Enjoy the pics. Chat later."
    scene 246 with d
    pause
    scene 253 with d
    Erin "My, my, my. She’s not wrong, guess I’m going to have to use it now."
    Erin "What would I do without you?"
    scene 255 with d
    pause
    Erin "I hope the batteries aren’t flat."


    menu:

        "{color=#1BBB20} Turn the vibrator ON.":

            scene 258 with fade:
                "anim_13" with d
            pause
            scene 258 with fade:
                "anim_14" with d

    pause
    scene 261 with d
    Erin "Of course, they are."
    scene 262 with d
    Erin "Makes sense, I’ve been using it quite often."
    Erin "Guess I’ll have to wait ‘til tonight to relieve myself."
    pause
    stop music fadeout 1
    scene black with d
    pause


    play music "music/sexy.mp3"

    scene 522:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause


    scene 506 with d
    stop music
    pause

    menu:

        "{color=#1BBB20} Unzip her top":

            scene 505 with d
    pause

    menu:

        "{color=#1BBB20} Free the girls.":

            scene 508 with d
    pause
    Marty "Now this, this is amazing. Today is a good day."
    Marty "These nipples are just calling my name, guess I must play with them."
    menu:

        "{color=#1BBB20} Play with her nipples.":
            scene 520 with fade:
                "anim_7" with d


    pause
    scene 454 with d
    f "Woah, Marty what’s going on here?"
    scene 456 with d
    f "Find yourself a girl?"
    f "Guess it isn’t the best time. I’ll come by later, need to talk to you."
    Marty "Frank, that you? Wait, stay, I’m almost done here."
    scene 457 with d
    f "Marty, she’s gorgeous. Even I don’t often get girls like her."
    f "Another reason to join me as a permanent homeless resident. A-ha-ha."
    f "Where did you pick up?"
    #f "What did you do to her? Hypnosis? "
    #Marty "Found her not too far from here. "
    #Marty "Think she got some drugs from a local gang, but might have used a little too much."
    #Marty "Thought I bring her here, not safe on these streets. Thought I rescue her from the criminals here. "
    #f "Oh, aren’t you just a knight in shining armor. Ha ha haa."
    Marty "Come join me. We can both enjoy this moment."
    scene 459 with d
    f "Fine, just make space for me."

    pause
    menu:

        "{color=#1BBB20} Join up.":


            scene 459 with fade:
                "anim_9" with d
            pause
            f "What’s she doing with her head?"
            #Marty "It’s Mirage man. That shit ain’t no joke, she’s probably hallucinating some crazy shit."
            Marty "Just put your dick in her mouth Frank. "
            #f "No way! She’s on Mirage man, what it she bites it off?"
            f "Rather safe and have a dick. Than sorry and be without one."

    pause
    Marty "Fine, then let’s swap. I’m done back here."
    f "I’m good thanks. Not a big fan of STDs, especially one from you. "
    Marty "*cough* Bitch *cough*"
    scene 468 with d
    f "Anyways, Marty, I need your help."
    Marty "What’s up. What do you need?"
    f "I need some help landing a job tomorrow."
    f "I went to that Employment Office and they lined up an interview tomorrow."
    f "Basically, a chaperone for some boarding school."
    scene 469 with d
    Marty "Oh, looking for some teen-action aren’t we? Say no more."
    f "I just need this job so the cops can stop tailing me."
    f "We can’t be sharing this mattress forever now."
    Marty "Sure, I’m in."
    Marty "But in return, you gotta introduce me to one of your students."
    f "Marty, Marty, Marty. Can’t get enough can you? Ahahaha."
    scene 471 with d
    Marty "I mean, what about this ass right here?"
    Marty "This one is mine, and mine alone."
    f "What about me?"
    Marty "We’ll see. But I’ll be there tomorrow, no problem."
    pause

##############   PART 2   ########################################################

    scene black with d
    s "The next morning."
    scene 600 with d
    play music "music/Alarm_police.mp3" fadeout 1
    Stella "Where were we ordered in so early?"
    Stella "What’s the emergency?"
    Bianca "Detective said it was urgent, so we’re here."
    scene 602 with d
    Stella "How did you like last night?"
    scene 603 with d
    Stella "Maybe a little too rough for you?"
    scene 603 with d
    Bianca "Yeah, a little."
    Stella "Sorry, but your flirting with Frank has really gotten under my skin."
    pause
    menu:

        "{color=#1BBB20} Caress.":


            scene 604 with fade:
                "anim_15" with d
    pause
    scene 607 with d
    Stella "Do you like it?"
    Bianca "Oh, yes. Don’t stop."
    scene 609 with d
    Stella "What if the detective comes in and catches us, then what?"
    Bianca "So what. I’m sure he won’t mind joining in."
    Bianca "A threesome in the Police Department, that’s something he can never turn down."
    scene 608 with d
    Stella "Oh, you horny minx. I’m all "
    Stella "This is why I can’t keep my hands to myself. You have me craving you."
    scene 610 with d
    Detective "Good morning, officers."
    Bianca "Morning, detective. How you doing?"
    scene 613 with d
    Detective "I’ve had better mornings, to say the least."
    Bianca "What’s wrong sir?"
    Detective "These past couple of days have been terrible in our district. The Captain and the Chief is up my ass complaining. Let’s just move on."
    Bianca "Oh. Sorry… Oohh."

    Detective "What’s that Bianca?"
    scene 614 with d
    Bianca "No, nothing sir. "
    scene 615 with d
    pause
    scene 616 with d
    menu:

        "{color=#1BBB20} Caress.":


            scene 617 with fade:
                "616" with d
                pause 1.5
                "617" with d
                pause 1.5
                repeat
    pause
    Detective "Anyways, back to the matter at hand. Someone robbed a tourist at a café."
    Detective "The waitress identified Frank as being there at the time of the crime."
    Detective "He was seen having dinner with a girl at the time."
    Detective "We need to find out whether he was involved or not."
    scene 618 with d
    pause
    scene 619 with d
    Detective "Also, a female tourist was reported missing yesterday."
    Detective "Her husband provided us with a photo."
    Detective "We need to find her before the media gets wind of this."
    Detective "She’s the founder of a major private equity fund. And the Mayor said this needs to be dealt with quickly and with discretion."
    Detective "If she remains missing, the fund will deteriorate and that can’t happen."
    scene 620 with d
    Bianca "Roger that sir. We’ll do everything we can to bring her back safely."

    menu:

        "{color=#1BBB20} Caress.":


            scene 621 with fade:
                "622" with d
                pause 1.5
                "621" with d
                pause 1.5
                repeat
    pause
    Detective "This is a photo of her."
    scene 623 with d
    pause
    scene 622 with d
    pause
    scene 624 with d
    pause
    scene 625 with d
    Detective "Bianca, are you okay? Your face is all red."
    scene 626 with d
    Detective "What’s wrong?"
    Bianca "Nothing sir. I’m fine, thank you."
    Detective "Alright. Pick Frank up and find out what the hell he was doing at that café."
    Stella "With all due respect sir, let me deal with Frank. He’s been a thorn in our side for a while, and we can’t have anything go sideways, since there are powerful eyes on him."
    Stella "Let me bring him in, quickly and quietly."
    Detective "You’re right. Frank is all yours."
    Detective "Bianca, you’re dismissed. Stella, would you stay behind please."
    scene 628 with d
    pause
    scene 629 with d
    pause
    scene 630 with d
    Detective "I’m sure you’re aware of my imminent retirement. "
    Detective "Someone must take my place as detective."
    Detective "And I’d like you to be that candidate."
    Stella "Thank you, sir. I’ll do whatever needs to be done to be a great detective. "
    Detective "Now don’t rush or screw anything up. This is your promotion to lose."
    Stella "What do you mean?"
    Detective "Well, either I recommend you for the promotion, or someone else gets it. Do you understand?"
    Stella "I do. That’s why I’m asking what do you want? Money?"
    Detective "You know I’m against bribery."
    Stella "Then what?"
    Detective "Take a guess. Let’s say something along the lines of a nice gesture towards me."
    Stella "What. You want to go to the movies? (soft chuckle)"
    Detective "What about a massage?"
    Stella "I’m not that good at massages sir."
    scene 631 with d
    Stella "Oh. You mean that type of massage…"
    Stella "With all due respect, this is a sexual harassment case waiting to happen."
    Detective "You could report me, but then you won’t get the promotion and you’ll probably lose your job."
    Detective "Also, a certain video with you and Bianca will be leaked to the press. You wouldn’t want that now would you."
    Detective "Do you want everyone to know what you guys do in your spare time?"
    Detective "I bet HQ would love to see the video of it all going done."

    scene 632 with d
    Stella "*Fuck! I’ve wanted this promotion for the longest time now."
    Stella "*Fucking old bastard. You will regret this."
    Stella "*I really hope Bianca never finds out."
    scene 636 with d
    Detective "Remove your hat, it’s easier with it off."
    scene 638 with d
    pause
    Detective "Heh, whenever you’re ready."
    menu:
        "{color=#1BBB20} Jerk off.":

            scene 643 with fade:


                "anim_1" with d




    pause
    scene 644 with fade:

        "anim_2" with d
    Detective "Yes, yes. Faster, faster."
    scene 647 with flash
    scene 646 with flash
    pause 0.3
    scene 646 with flash
    scene 646 with flash
    with d
    scene 648 with d
    Detective "Trust me, that promotion is within your reach Stella, or should I say Detective. It will soon be yours."
    Detective "Go and clean and up continue with your duties."
    Detective "Oh and by the way, that massage was great. "

    stop music
    scene black with d
    pause
    play music "music/sexy.mp3"
    scene 582b:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    stop music

    scene 580 with d
    thompson "Yes, we’re here."
    scene 581 with d
    thompson "And no one is here for the interview."
    thompson "We’re out in the open, waiting and no one is showing up."
    scene 584 with d
    thompson "This is the last time I work with that employment office. "
    scene 586 with d
    pause
    scene 587 with d
    thompson "I don’t have time for this bullshit."
    thompson "This neighborhood is not at all safe for us to be standing all alone outside."
    play music "music/rocket.mp3"
    scene 588 with d
    pause
    scene 589 with d
    pause
    scene 590 with d
    pause
    scene 591 with d
    Marty "Hey, cuties! Wanna have some fun? I’ll show you a good time."
    scene 593 with d
    chelsey "Get your hands off me!"
    scene 595 with d
    Marty "C’mon now, we can get to know each other and have all kinds of fun."
    scene 596 with d
    pause
    scene 597 with d
    pause
    scene 598 with d
    pause



    scene 649 with d
    kate "Help! Help!"
    scene 651 with d
    chelsey "Mrs. Thompson! Help!"
    scene 653 with d
    thompson "What the hell do you think you’re doing!"
    thompson "Get your hand off them now!"
    Marty "And who might this be, your grandma?"
    Marty "Tell her you rather want to come with me."
    scene 654 with d
    thompson "Enough! If you don’t get your hands off her right now, I’m going to call the cops."
    scene 656 with d
    pause
    Marty "I wouldn’t do that if I were you. The cops and me have bad history, things will get ugly."
    thompson "What? Hey! Give me my phone back!"
    scene 658 with d
    f "Hey asshole! Get your hands off the ladies!"
    scene 660 with d
    thompson "Sir please. Help us."
    f "Step aside ma’am. I’ll deal with this."
    scene 661 with d
    #pause
    #scene 665 with d
    pause
    scene 668 with d
    f "How dare you grope this young woman."
    Marty "And who do you think you are, some knight in shining armor? Just step aside and you won’t get hurt."
    scene 669 with d
    pause
    scene 670 with d
    Marty "Hey, how was that? Was I convincing enough?"
    f "Brilliant. Now run, before someone actually calls the cops."
    Marty "Don’t have to tell me twice. And get that brunette’s number for me, she’s fine as hell."
    scene 671 with d
    Marty "Ah, get off me! It hurts, please!"
    scene 672 with d
    f "See you later, Marty. And thanks again."
    scene 674 with d
    play audio "music/punch.opus"
    scene 673 with hpunch
    pause
    scene 675 with d
    f "And don’t you dare come back!"
    scene 676 with d
    show screen topleftmenu4
    f "Ma’am, are you okay?"
    thompson "Yes, I am. Thank you."
    f "Don’t worry, he won’t be coming back."
    thompson "You handled him like he was nothing. "
    thompson "Many would have left us and walked away, but you, you helped us. Thank you."
    f "I’m a gentleman. I can’t stand by and do nothing when a lady is in trouble."
    thompson "You’re too kind. How could we ever repay you?"
    f "I don’t feel right to take advantage of this situation."
    f "But I’m currently unemployed and would be undeniably thankful for an opportunity."
    thompson "And by chance I am looking for someone. Luck is on your side."
    thompson "There’s a café nearby. Let’s go there and discuss this."
    thompson "How does that sound?"
    thompson "What do you think girls?"
    scene 677 with d
    chelsey "Sounds good!"
    kate "I agree!"
    thompson "Perfect, let’s go."
    scene 678 with d
    stop music fadeout 1
    pause
    scene 679 with d
    pause
    scene 680 with d
    f "*What a nice ass."
    menu:
        "{color=#E5170A} Smack it. {color=#FF0000} (Game Over)":

            scene 680 with d
            pause
            scene 715 with d
            pause
            scene 716
            play sound "music/shlepok.mp3"
            pause
            scene 717 with d
            pause
            scene 718 with d
            pause
            jump gameover


        "{color=#1BBB20} Take a closer look. {color=#FF0000} (+1 Chelsey's Point)":


            pause
            show heart with moveinbottom:
                yalign .25 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ chelsey_score = change_stat(chelsey_score,1)
            hide heart

        "{color=#E5170A} Make a compliment. {color=#FF0000} (-1 Chelsey's Point)":

            f "You have a nice ass."

            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ chelsey_score = change_stat(chelsey_score,-1)
            hide heart
            pause
    scene 681 with d
    pause
    scene 682 with d
    f "The older one has a nice ass too."
    f "Marty was right, she really is gorgeous."
    scene 683 with d
    play music "music/piano.mp3"
    pause
    scene 684 with d
    pause
    scene 685 with d
    thompson "Does our hero have a name?"
    f "My name is Frank, ma’am."
    thompson "I'm Mrs. Thompson."
    thompson "And this is Kate and Chelsey."
    thompson "They are studying at the boarding school in town."
    menu:

        "{color=#1BBB20} Compliment Chelsey. {color=#FF0000} (+1 Chelsey's Point)":

            scene 723 with d
            f "It’s a pleasure to meet you."
            f "You’re adorable."
            scene 724 with d
            chelsey "Thank you, sir."
            pause
            show heart with moveinbottom:
                yalign .25 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ chelsey_score = change_stat(chelsey_score,1)
            hide heart

        "{color=#1BBB20} Compliment Kate. {color=#FF0000} (+1 Kate's Point/I recommend you choose this option so you won't miss a scene later)":

            scene 721 with d
            f "It’s a pleasure to meet you."
            f "You were brave out there. Keep your head up."
            scene 722 with d
            kate "Thank you, sir."
            pause
            show heart with moveinbottom:
                yalign .25 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ kate_score = change_stat(kate_score,1)
            hide heart

        "{color=#E5170A} Compliment Mrs. Thompson. {color=#FF0000} (-1 Chelsey and Kate Point)":

            f "It’s a pleasure to meet you, ma’am."
            f "Kate and Chelsey are truly adorable."
            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ kate_score = change_stat(kate_score,-1)
            $ chelsey_score = change_stat(chelsey_score,-1)
            hide heart
            pause

    thompson "I’m extremely grateful you showed up and rescued up from that disgusting asshole."
    f "It was nothing. I could not let such vile acts go unnoticed."
    scene 684 with d
    thompson "You said you’re unemployed. How come?"
    f "I worked overseas for 18 years, trying to make a living for my family."
    f "And one day when I came home to surprise then, my wife took my two daughters and left. She took everything we had and ran away with another man. She left me with nothing."
    f "I couldn’t believe it. After everything I’ve done for them."
    f "I loved them with all my heart."
    scene 687 with d
    f "I had nothing, so I’ve come to the city looking for a job and a chance to rebuild my life."
    f "I’ve had trouble finding a job, it hasn’t been easy these past weeks."
    scene 688 with d
    chelsey "My God. I’m so sorry Mr Frank. Don’t cry, please don’t cry. "
    if renpy.loadable("patch.renpy"):
        chelsey "Our daddy also left us when we were little."
    chelsey "We understand what you are going through."
    if renpy.loadable("patch.renpy"):
        scene 689 with d
        f "*Hold up. Gloria said she has another daughter when I was in prison."
        f "*Did I just find my two daughters??"
        f "I’m sorry, it must’ve been hard on your mother. What’s her name by the way?"
        kate "Our mom’s name is Mary."
        scene 688 with d
        f "*Figured as much. That would have been too easy. But don’t worry, I’ll find you Gloria."
    scene 693 with d
    chelsey "We must help you Mr Frank."
    scene 694 with d
    chelsey "Can we please give Mr Frank the job Mrs. Thompson? Pleeeease."
    chelsey "We’re looking for a personal escort, a bodyguard for you two."
    scene 685 with d
    thompson "I don’t know if Mr Frank would be interested in this position."
    thompson "The students at the boarding school have limited contact with men."
    thompson "Therefore, our bodyguard needs to be responsible, trustworthy and have strong morals."
    scene 695 with d
    f "I fit the description you just mentioned ma’am."
    f "Trust me. I will treat and protect these girls as if they were my own."
    f "I’ll be the father they never had. I won’t let anything happen to them."
    scene 719 with d
    chelsey "I think he is the right man for the job, ma’am."
    scene 696 with d
    thompson "Fine. But you’re on a probationary period for now."
    thompson "I’ll give you our address, meet us here on Monday."
    scene 690 with d
    pause
    scene 692 with d
    pause
    scene 719 with d
    chelsey "I think I need to pee."
    chelsey "May I please go to the restroom with Kate?"
    scene 762 with d
    f "*You better move your hands, unless you want to feel something else. "
    pause
    scene 763 with d
    pause
    scene 721 with d
    thompson "Chelsey! A young lady does not say such things out loud, especially when in the company of a man."
    thompson "Fine, but be quick. We need to leave now."
    chelsey "Thank you. Be back now."
    scene 764 with d
    chelsey "Mr Frank, may I squeeze through please?"
    f "Of course."
    scene 765 with d
    pause
    scene 766 with d
    pause
    scene 767 with d
    pause
    scene 726 with d
    thompson "You know, these girls had it rough growing up."
    thompson "They were only babies when their father left them."
    thompson "They don’t even know how he looks."
    thompson "They’ve spent the majority of their lives at our boarding school. It’s truly sad."
    thompson "I beg you to please be understanding of their situation."
    thompson "They can’t spend their entire lives within the school. Or else they won’t be prepared for the real world."
    thompson "They need to be prepared for life when they leave school."
    thompson "And you are the one who is going to make sure they’re ready for life after school."
    f "I understand ma’am. I will do anything I can to help them."
    stop music fadeout 1
    scene 697 with d
    pause
    scene 698 with d
    pause
    scene 707 with d
    pause
    scene 709 with d
    pause
    scene 710 with d
    pause
    scene 701 with d
    pause
    scene 703 with d
    pause
    kate "What was all that about?"
    scene 700 with d
    chelsey "What do you mean?"
    scene 703 with d
    kate "Why did you help Mr Frank get the job?"
    scene 700 with d
    chelsey "His life story is heart-breaking, why shouldn’t we help him?"
    scene 703 with d
    kate "Sure, but that look on your face says something else. It’s the same one you had after we finished that movie with Di Matrio."
    kate "You wrote letters to him for weeks."
    kate "Oh, I know what it is. You like Mr Frank don’t you? You are falling for Mr Frank hey?"
    scene 706 with d
    chelsey "No, I’m not!"
    scene 703 with d
    kate "I’m going to tell Mrs Thompson and we’ll see what she has to say about this."
    scene 700 with d
    chelsey "If you do that, then I’ll tell her you like that homeless man that was groping you."
    scene 703 with d
    kate "And why would you say that?"
    scene 700 with d
    chelsey "Because I don’t remember you fighting back while he was touching you."
    scene 703 with d
    kate "I’ve never been touched by a man in that way before."
    kate "I felt these tingles inside me, and below my belly."
    scene 700 with d
    chelsey "I see. So, we can keep this between us."
    scene 703 with d
    kate "You done?"
    scene 702 with d
    chelsey "Yes. "
    scene 703 with d
    kate "Me too, let’s go."
    scene 714 with d
    pause
    scene 713 with d
    pause
    scene 712 with d
    pause
    hide screen topleftmenu4
    scene 711 with d
    pause

##############   PART 3.0   ########################################################




    scene 728 with d
    play music "music/city1.mp3"
    pause
    scene 730 with d
    f "Hey, where’s Marty?"
    scene 732 with d
    pause
    scene 734 with d
    pause
    show screen topleftmenu4
    pause
    scene 736 with d
    f "How's it going Marty."
    f "What you doing?"
    Marty "Looking through Mrs. Thompson's texts."
    f "Wait, you managed to get her phone?"
    f "Damn, you’re good."
    f "Anything interesting?"
    Marty "SShe’s in AA."
    Marty "Been clean 3 years now."
    f "What? How did she get this job then?"
    Marty "Same way as you did. Ha-ha-ha!"
    Marty "How’d it go, by the way?"
    f "Great. Starting Monday."
    Marty "Did you get that brunette's number?"
    f "Seriously?"
    Marty "Damn straight. Ha-Ha!"
    f "Fine. But not now, too soon. "
    f "Anyways, what’s the girl from yesterday doing here?"
    f "She fell in love with you?"
    f "Dropped it all to live her life on the streets with you? Ha."
    Marty "Ha. As it turns out, Mirage messed with her mind for good."
    Marty "Memory’s been wiped."
    Marty "Name, age, where she lived."
    Marty "She’s forgotten her previous life."
    Marty "So, I managed to get my hands on some drugs."
    Marty "Going to her on a low dose."
    Marty "Told her I was her husband, she believed me."
    Marty "Said that we’re going through a bad patch. Lost everything."
    Marty "And now we’re living on welfare."
    Marty "And that she decided to work the streets to support us financially."
    f "Ohh, I see what’s going on here."
    f "You’re using her to make you money hey?"
    Marty "Incredible. Just look how much she  made me today."
    Marty "Customer satisfaction is through the roof."
    Marty "They’re lining up to see her. Everyone wants her."
    f "Just don’t forget she’s missing. And soon enough, someone will start looking for her."
    Marty "Cops are rare around these parts."
    Marty "It’s going to be fine."
    f "Still, I’d suggest buying her some new clothes. Changing her look."
    f "Since you can afford it."
    Marty "Fine. But remember, her name is Elsa, and she’s my wife."
    f "Sure, I’ll play along."
    scene 738 with d
    Elsa "I’m done, Marty."
    scene 739 with d
    Elsa "Who’s this?"
    Marty "This is Frank."
    Marty "Could it be that you forgot Frank?"
    Elsa "I think so. Forgive me."
    Marty "He's a friend of mine."
    Elsa "Is Frank here to have some fun with me?"
    Marty "Oh, he has fun with us, but casually."
    scene 740 with d
    Elsa "Awesome."
    Elsa "I’m exhausted."
    Elsa "And it pains down there. "
    Elsa "You sure I worked the streets?"
    Marty "Yes honey."
    Marty "That’s how we made money."
    Elsa "Can I have a beer?"
    Marty "You shouldn't mix drugs with alcohol."
    Elsa "Wait, I'm doing drugs?"
    Marty "I was dead set against it."
    Marty "But you argued they helped you relax."
    scene 744 with d
    s "Are you working at the moment, Ms. Elsa?"
    Elsa "What can I do for you?"
    s "How much for a flash?"
    Elsa "Are you even 18? Ha ha!"
    s "Of course, ma’am."
    Elsa "Sure. $30, deal?"
    s "Yes ma'am."
    scene 745 with d
    pause
    scene 748 with d
    pause
    scene 749 with d
    pause
    menu:


        "{color=#1BBB20} Play with tits":
            scene 750 with fade:
                "anim_8" with d
    pause
    Elsa "Time's up!"
    s "Thank you, ma’am."
    s "You have sexy breasts, ma’am."
    scene 752 with d
    play sound "music/beer.mp3"
    f "Bottoms up to a prosperous business."
    Marty "Thanks Frank."
    stop music fadeout 1
    scene 753 with d
    play music "music/ston.mp3"
    pause
    scene 754 with d
    pause
    scene black with d
    pause
    menu:

        "{color=#1BBB20} Peek.":


            scene 755 with fade:

                "anim_10" with d
    pause
    scene 757 with d
    f "Aye, could you turn it down a bit. I have work in the morning."
    stop music fadeout 1.0
    Elsa "And? We don’t."
    Elsa "What’s with him?"
    Marty "He’s just jealous that he’s single. "
    Elsa "Fine, we'll try to be quiet."
    Elsa "Let’s switch positions. "

    menu:

        "{color=#1BBB20} Peek.":

            play music "music/blowjob.mp3"
            scene 760 with fade:

                "anim_11" with d





    pause

    menu:

        "{color=#1BBB20} Peek.":


            scene 760 with fade:
                "anim_12" with d



    pause
    scene black with d
    stop music fadeout 1
    s "8 hours later."
    play music "music/city1.mp3"
    scene 768 with d
    f "Look’s like I’m up first."
    f "Shit. These two must’ve gone at it all night. Kept me up all night."
    f "I could do with some quick fun."
    scene 771 with d
    menu:

        "{color=#1BBB20} Jerk off.":


            scene 773 with fade:
                "774" with d
                pause 1.5
                "773" with d
                pause 1.5
                repeat

    pause
    scene 775 with d
    with flash
    scene 776 with flash
    pause 0.3
    scene 776 with flash
    scene 776 with flash
    pause 2.0
    with d
    scene 777 with d
    pause
    scene 783 with d
    pause
    scene 786 with d
    pause
    scene 785 with d
    pause
    Elsa "Marty, you naughty boy."
    Elsa "Not the backdoor!"
    Elsa "I told you it hurts down there."
    Elsa "Let's play later, I didn't get much sleep."
    pause
    scene 787 with d
    f "*Oh, she thinks I’m Marty."
    f "*Her ass is indeed amazing."
    f "*I should go to work now."
    f "*Time for fun and games will have to wait."
    stop music fadeout 1
    pause


    scene black with d
    pause
    scene 790 with d
    pause
    scene 792 with d
    f "Is this the right place?"
    scene 793 with d
    play music "music/forest.mp3"
    f "Now this is what you call a house. It’s huge. It’s a mansion."
    f "Never been in a mansion."
    f "But, how do I get in though?"
    f "There’s no one in sight, and no way to contact the house."
    f "I don’t have time to wait, I’m already late. I’m gonna have to jump the wall."
    pause
    play sound "music/bike1.mp3"
    scene 796 with d
    pause
    scene 842 with d
    stop sound fadeout 3
    pause
    scene 797 with d
    f "Where’s everyone?"
    f "No one in sight, not even staff."
    f "How do they not get robbed…?"

    scene 798 with d
    pause
    scene 799 with d
    f "Ah!"
    scene 800 with d
    f "It’s got me by the balls. Fuck!"
    pause
    stop music fadeout 1
    scene 801 with d
    play sound "music/Dver_Police.mp3"
    pause 1
    s "Someone came."
    pause
    play music "music/sexy.mp3"
    scene 802:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    scene 815 with d
    pause
    scene 816 with d
    pause
    stop music fadeout 1
    scene 803 with d
    show screen topleftmenu5
    pause
    scene 804 with d
    play sound "music/dog.mp3"
    dog "GRRRR."
    f "Aye, easy boy. I’m not here to hurt you."
    f "I’m not here to break in."
    f "Let go! Please."
    scene 805 with d
    stop sound fadeout 1
    f "Thank God! My balls are safe."
    scene 808 with d

    menu:

        "{color=#E5170A} Insult her {color=#FF0000} (-1 May's Point)":

            f "Hey! Watch your dog, will 'ya!"
            f "Almost ripped my balls off!"
            f "I'm talking to you."
            f "Are you mute or something?"
            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ may_score = change_stat(may_score,-1)
            hide heart
            pause

        "{color=#E5170A} Show balls and insult her {color=#FF0000} (Game Over/You will literally lose your balls)":

            scene 838 with d
            f "Hey! Watch your dog, will 'ya!"
            scene 839 with d
            f "Almost ripped off my balls!"
            scene 840 with d
            pause
            jump gameover

        "{color=#1BBB20} Commend the dog. {color=#FF0000} (+1 May's Point)":

            f "That’s a good dog you have there."
            f "A true gatekeeper."
            pause
            show heart with moveinbottom:
                yalign .35 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ may_score = change_stat(may_score,1)
            hide heart

    scene 814 with d
    pause
    scene 808 with d

    f "I’m new here. My name’s Frank. "
    f "Mrs. Thompson should’ve mentioned I’m coming."
    scene 809 with d
    pause
    scene 810 with d
    f "The staff is pretty damn weird around here."
    f "Maybe I’m at the wrong place?"
    scene 817 with d
    chelsey "Mr. Frank?"
    kate "No one’s here."
    kate "Let’s check the front of the house."
    chelsey "Nah. Let’s just wait here."
    chelsey "I don’t feel like walking around."
    scene 818 with d
    chelsey "Check out this bed, it’s massive. Must be a king-size."
    chelsey "It could easily fit three people."
    chelsey "Have you been in this room before?"
    kate "This house has plenty of rooms, that’s no lie."
    kate "Many of them are locked, I wonder why…"
    kate "But no, I’ve never been to this room."
    chelsey "Let's check out how soft the bed is."
    kate "No, we shouldn’t. What if Mr. Frank comes in?"
    scene 819 with d
    chelsey "Look at me!"
    scene 820 with d
    pause
    scene 821 with d
    kate "Chelsey, get off the bed. It’s not even your bed."
    scene 823 with d
    chelsey "C’mon. It’s just so soft."
    chelsey "Come and join me, please."
    kate "No. You’re flashing for everyone to see."
    kate "And this isn’t some gynecology appointment."
    scene 824 with d
    chelsey "Don’t you like it when our doctor touches us with her fingers?"  ###
    scene 825 with d
    chelsey "Let's pay her another visit."
    chelsey "We could make up some excuse."
    kate "You can go without me."
    kate "I bet you she’ll figure out real quick your reason for being there."
    kate "Then she’ll flush your system with an enema bag, something you won’t like."
    kate "And that’ll hopefully set you straight."
    kate "Get up before someone sees you!"
    scene 826 with d
    chelsey "How about some role-play first?"
    kate "What are we gonna role-play?"
    chelsey "Doctor-patient, silly! Ha-ha-ha!"
    scene 826 with d
    kate "Fine."
    scene 827 with d
    kate "As your doctor, I order you to get off the bed."
    chelsey "Seriously, you’re no fun…"
    chelsey "Just lemme chill for a bit."
    chelsey "Look!"
    chelsey "There’s a bag behind you."
    scene 828 with d
    kate "Let’s see what’s inside."
    kate "This is Mr. Frank’s bag."
    kate "We can’t just look through his stuff. It’s rude!"
    chelsey "We’ll just open it. Just a quick look."
    chelsey "Bring the bag here, please."
    kate "Only if you promise we’ll go to the front of the house after."
    chelsey "Fine, I promise."
    scene 829 with d
    pause
    scene 837 with d
    kate "Nothing interesting."
    kate "Some T-shirts, a pack of smokes."
    chelsey "Check out the side-pocket. "
    kate "I’m not searching his bag."
    chelsey "Whatever, let’s see if there’s anything hidden here."
    scene 843 with d
    kate "Chelsey, what are you doing with the cigarettes?"
    kate "Put them back."
    scene 844 with d
    chelsey "Just smell this, it smells soo good."
    kate "Cigarettes are bad for you."
    chelsey "Well I don’t think so."
    chelsey "I really enjoy the smell."
    kate "Don't even think about taking a puff."
    kate "Mrs. Thompson will know, and I’ll tell her."
    scene 830 with d
    chelsey "Look, what’s this?"
    scene 831 with d
    chelsey "How's it used?"
    scene 832 with d
    kate "Wait, I’ve seen one of these before."
    scene 833 with d
    if renpy.loadable("patch.renpy"):
        chelsey "Remember."
        scene 834 with d
        chelsey "Mom had one just like this."
        chelsey "It was in her drawer, where she kept her clothes."
        kate "Yeah, I remember."
        scene 833 with d
        kate "I’ve always wondered what she uses it for."
        kate "I mean, it could be used as a back massager."
        chelsey "Or as a substitute for a carrot in decorating a snowman."
        chelsey "What do you think? Do I look like a snowman?"
        scene 835 with d
        pause
        scene 836 with d
        kate "Ha-ha!"
        kate "Can't stop you from shoving things down your throat..."
        kate "Alright, pack it all up and meet me in the front of the house."
    pause
    scene black with d
    pause
    scene 846 with d
    thompson "Morning Mr. Frank."
    thompson "To be honest, I wasn’t expecting you to show up."
    thompson "Working with our girls is a lot to ask for."
    f "Morning Mrs Thompson, I gave my word and so I’m here."
    f "By the way, what’s the deal with your staff member?"
    f "Couldn't get a single word from her."
    scene 847 with d
    thompson "Her name is May."
    scene 848 with d
    thompson "She comes from a complicated background."
    thompson "May got here after she was raped by three bastards."
    thompson "We found her one day in the yard."
    thompson "We nursed her back to health and offered a job here."
    thompson "She’s been suffering from PTSD ever since that dreadful night."
    thompson "This is whys she never speaks to anyone."
    scene 846 with d
    f "So, she can speak, she just chooses not to."
    f "*Damn, that’s messed up."
    scene 847 with d
    f "Your mansion is huge, yet no guards?"
    thompson "We’ve got Rex."
    thompson "I'm sure you've met him by now."
    thompson "May loves this dog."
    thompson "Those two are inseparable."

    menu:

        "{color=#1BBB20} Praise Rex {color=#FF0000} (+1 May's Point)":
            f "Yes, he’s a very good boy."

            pause
            show heart with moveinbottom:
                yalign .35 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ may_score = change_stat(may_score,1)
            hide heart

        "{color=#E5170A} Complain about Rex {color=#FF0000} (-1 May's Point)":
            f "He certainly is aggressive, he tried to rib my balls off earlier."

            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ may_score = change_stat(may_score,-1)
            hide heart
            pause



    thompson "Rex hates men."
    thompson "Just like May, those two are on the same wavelength! Ha, it’s crazy."
    scene 847b with d
    thompson "May, Mr Frank is our new employee."
    thompson "His job is to escort the girls around the city."
    thompson "Would you call the girls please."
    scene 849 with d
    f "Morning ladies, and please, call me Frank."
    pause
    menu:

        "{color=#1BBB20} Say hi to Chelsey. {color=#FF0000} (+1 Chelsey's Point)":

            f "Hi Chelsey."

            pause
            show heart with moveinbottom:
                yalign .25 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ chelsey_score = change_stat(chelsey_score,1)
            hide heart

        "{color=#1BBB20} Say hi to Kate. {color=#FF0000} (+1 Kate's Point/I recommend you choose this option so you won't miss a scene later)":

            f "Hi Kate."

            pause
            show heart with moveinbottom:
                yalign .25 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ kate_score = change_stat(kate_score,1)
            hide heart


    chelsey "Morning Mr. Frank."
    thompson "You shall take the girls shopping today Frank."
    thompson "You will accompany them while they look for one-piece swimsuits."
    scene 850 with d
    kate "But ma’am, why? Why a one-piece?"
    kate "And why do we need new swimsuits?"
    scene 847b with d
    thompson "It’s no more just women here, Frank will be around also."
    thompson "Frank will also be here when you are in the pool."
    thompson "And I don’t want any improper thoughts crossing his mind."
    scene 850b with d
    chelsey "Can’t we go shopping tomorrow, Mrs. Thompson?"
    chelsey "I can't make it today."
    scene 847 with d
    thompson "Cut it our Chelsey."
    thompson "You are going today, and that’s final."
    thompson "The girls need one-piece swimsuits, Frank."
    thompson "Don't let them talk you into anything else."
    f "Yes ma’am."
    scene black with d
    pause
    scene 851 with d
    pause
    scene 852 with d
    pause
    scene 853 with d
    pause
    scene 854 with d
    pause
    play sound "music/glock.mp3"
    scene 855 with d
    stop sound
    pause
    scene 855b with d
    pause
    scene black with d
    pause
    scene 856 with d
    f "Alright girls, this is our first trip to the city together."
    f "I hope it all goes well and everyone is on their best behavior."
    chelsey "We'll do our best, sir."
    f "Get in the cab."
    play sound "music/Auto_sound.mp3"
    scene 857 with d
    stop sound fadeout 1
    pause
    scene 858 with d
    play music "music/Car_Sound.mp3"
    f "What shop is it? "
    f "Have you been there before?"
    scene 859 with d
    chelsey "No, it's our first time."
    chelsey "No worries, shop assistants are always there to help."
    stop music fadeout 1
    scene 860 with d
    play sound "music/Auto_Go.ogg"
    pause
    scene 861 with d
    stop sound fadeout 1
    pause
    play music "music/sexy.mp3"
    scene 862:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    scene 863 with d
    stop music fadeout 1.0
    eva "Hi."
    eva "My name’s Eva."
    eva "How can I help you?"
    scene 864 with d
    f "Hi there."
    f "I'm Frank."
    f "This is Chelsey and Kate."
    f "We need some help picking one-piece swimsuits."
    scene 865 with d
    eva "Do you need one as well, sir?"
    f "Ha! Aren’t you funny."
    f "Swimsuits are for the girls."
    f "I don’t mind swimming naked. "
    f "I’ve got nothing to be ashamed of."
    eva "You’ve got a big mouth and a lot of confidence."
    eva "But I wonder if you can back it up."
    f "*She likes to get straight to the point."
    scene 864 with d
    eva "Girls, you two can go to the changing rooms."
    eva "Swimsuits are on their way."
    scene 866 with d
    f "Eva has a great body."
    f "Probably works out often."
    play music "music/roulette.mp3"
    scene 867 with d
    f "*Everyone is busy."
    f "*Time to check the register for some cash."
    scene 868 with d
    f "*Where the hell is the cash?"
    f "*I can’t find anything"
    stop music fadeout 1
    scene 869 with d
    play sound "music/plastinka.mp3"
    eva "Anything in particular that you’re looking for?"
    stop sound
    scene 868 with d
    f "*Shit."
    f "*I need to come up with something."
    scene 870 with d
    f "Was looking for your panties, Eva."
    scene 869 with d
    eva "You are a pervert, aren't you?"
    scene 870 with d
    f "No, I'm not."
    scene 869 with d
    eva "Yes you are, I can see it."
    eva "And those aren’t even mine."
    eva "They are for sale."
    eva "Hmm. What am I to do with you?"
    eva "..."
    eva "..."
    eva "You know what, you can keep those."
    eva "For your personal private pleasure."
    eva "But, you’ll have to make a big purchase today."
    eva "I need to make employee of the month."
    eva "So that bitch, Rose, can shut up for good."
    eva "I’ll damn-near do anything to make more sales than her."
    scene 870 with d
    f "Sounds like a deal."
    scene 871 with d
    eva "I’ll go and take my panties of quick."
    eva "Wait for me here, pervert."
    scene 873 with d
    f "Looks like Kate forgot to close her door."
    f "I could watch her change."
    pause

    menu:

        "{color=#1BBB20} Spy on Kate. {color=#FF0000} (You need two Kate's points so you won't miss the scene)":

            if kate_score >= 2:

                scene 872 with d
                play music "music/blues.mp3"
                f "Made it just in time."
                f "Kate is about to start changing."
                f "Can’t wait for this strip-tease to begin."
                f "There we go. First your clothes."
                scene 874 with d
                f "Then the bra."
                f "Oh, I see, saving the best for later."
                scene 876 with d
                f "Now the panties."
                f "My God, she’s really good at this."
                scene 877 with d
                f "Silky-smooth skin."
                f "Exquisite curves."
                f "I’m about to rip my pants off."


                menu:

                    "{color=#E5170A} Spy. {color=#FF0000} (Game Over)":
                        pause
                        scene 878 with d
                        pause
                        f "*Oh shit, she spotted me."
                        f "*It's time to bail."
                        $ kate_gameover = change_stat(kate_gameover,1)
                        scene 878b with d
                        f "I can't contain myself with such a huge boner."





                    "{color=#1BBB20} Get away.":

                        scene 878b with d
                        f "I can't contain myself with such a huge boner."



            else:
                scene points with d
                pause
                scene 878b with d

    pause

    stop music fadeout 1
    menu:

        "{color=#1BBB20} Spy on Eva":
            scene 879 with d

    pause
    scene 880 with d
    play sound "music/plastinka.mp3"
    f "Eva's ass is so tight."
    f "Now’s the time for some fun."
    stop sound
    scene 880b with d
    eva "Are you spying on me, perv?"
    eva "Wait for me outside, I'll be out soon."
    f "No, I want to watch you change."
    scene 881 with d
    eva "No, grab the panties and go."
    f "There’s no way I’m leaving."
    scene 894 with d
    f "I want more than just panties."
    eva "What do you want?"
    f "For starters, your clothes on the floor."
    scene 882 with d
    eva "What are you doing?"
    f "Helping you remove your clothing."
    eva "This is an unusual way to remove my clothes."
    scene 883b with d
    eva "Fine, you’ve seen it all."
    eva "Now leave."
    f "Your body is stunning."
    scene 883c with d
    pause
    scene 883b with d
    f "I definitely can’t leave now."
    f "My friend over her wants to meet you too."
    scene 884 with d
    eva "You perverts are real slick these days."
    eva "First you want my clothes off."
    eva "And now you want to get laid."
    eva "You’re lucky I haven’t had sex in 2 months."
    eva "Fuck it, let’s do this."
    scene 885 with d
    pause
    scene 886 with d
    pause

    menu:
        "{color=#1BBB20} Fuck Eva":

            play music "music/vagin.mp3"
            scene 886 with fade:
                "anim_16" with d
            pause
            eva "Fuck me, it’s huge."
            eva "This position isn’t working that well since it’s that big."
            eva "Hey, don’t you dare cum inside me!"

            pause
            stop music fadeout 1
            scene black with fade:
                "anim_17" with d
            pause
            eva "Cum on my belly."







    pause
    scene black with d
    pause
    scene 895 with d
    pause
    scene 896 with d
    pause
    scene 897 with d
    pause
    scene 897b with d
    eva "That's a lot of cum."
    eva "How am I going to clean all this up?"
    eva "You should've cum in my mouth."
    scene 897c with d
    eva "Hey, what are you doing? These are my panties." ####
    f "As I recall, you gave them to me."####
    scene black with d
    s "15 minutes later."
    scene 887 with d
    f "So, Eva, how was it?"
    eva "My God… It was just …."
    f "What?"
    eva "It ended way too quickly."
    eva "It seems like you haven’t practiced in a while."
    f "Give Chelsey your number. And maybe we can pick things up where we left off."
    eva "Ha! Now who’s the funny one."
    pause
    scene 888 with d
    kate "I wonder what Frank and Eva are talking about."
    scene 889 with d
    kate "Mr. Frank."
    kate "Frank, can you hear me?"
    scene 890 with d
    f "Yes, Kate. What is it?"
    kate "You can’t smoke in here."
    f "It’s fine, Eva said it’s okay."
    kate "What do you think of the swimsuit?"
    f "Great. I like it."
    f "Now look for something else, maybe a lightly-colored one."
    kate "But Mrs. Thompson said to only get one?"
    f "Don’t stress, I’ll work it out with her."
    scene 889 with d
    kate "Alright, I’ll try on another one."
    scene black with d
    s "10 minutes later."
    scene 891 with d
    kate "*These two are talking again."
    kate "*They’re barely noticing me."
    kate "*Forget it."
    scene 892 with d
    pause
    scene 893 with d
    f "You've picked your items already, Kate? "
    kate "Yes, sir."
    f "Perfect. Let's help Chelsey out. "
    kate "Sure."
    scene 898 with d
    f "Here she comes."
    scene 899 with d
    f "You picked a great swimsuit Chelsey."
    f "I love it."
    scene 900 with d
    chelsey "Thank you, sir. I did my best."
    chelsey "Is mine better than Kate’s?"
    scene 899 with d
    f "No offence to Kate, but I like yours more."
    scene 901 with d
    kate "*This little bitch. You think you know more than me when it comes to fashion. We’ll see about that."
    kate "*Let’s see what else you picked."
    scene 899 with d
    eva "Do you have another one to show us?"
    scene 900 with d
    chelsey "Yes, ma'am."
    scene black with d
    s "10 minutes later."
    scene 902 with d
    eva "It’s nice, but it’s similar to your skin tone."
    eva "It gives the illusion that you aren’t wearing anything."
    f "Eva’s right, Mrs. Thompson won’t approve of this swimsuit."
    f "Thanks for pointing it out."
    scene 899 with d
    eva "Would you rather like to try the other swimsuit I brought you?"
    chelsey "No thank you, ma’am. I think I’ll just take the first one."
    scene 901 with d
    kate "*This is the first time I’ve seen Chelsey turn down trying on clothes."
    kate "*Something isn’t right here. Time to see where this leads."
    kate "Chelsey please, try on another one for us."
    scene 902 with d
    chelsey "No. I don't want to."
    scene 899 with d
    f "Please. We all want to see you try it on."
    scene 902 with d
    chelsey "Alright."
    scene black with d
    s "10 minutes later."
    scene 910 with d
    eva "Wow, this is easily the best one."
    eva "Could you please move your hands to your sides."
    eva "We want to see the entire look of the swimsuit."
    scene 909 with d
    pause
    play sound "music/plastinka.mp3"
    scene 901b with d
    kate "A-ha-ha! Her bikini line isn’t groomed. It’s overgrown!"
    stop sound
    scene 904 with d
    pause
    scene 906 with d
    pause
    scene 905 with d
    pause
    scene 907 with d
    pause
    scene 908 with d
    f "Kate, how dare you say that."
    #f "She is your sister."
    f "And in public no less!"
    f "If I was your father."
    f "I would ground you."
    f "Look at me when I talk to you."
    scene 908b with d
    kate "You’re not my father."
    kate "So don’t you dare tell me what to do."
    f "I'll try to calm Chelsey down."
    f "And when I get back, I expect an apology from you."
    f "Are we clear?"
    kate "Yes, sir."
    scene 911 with d
    f "Chelsea, calm down, stop crying."
    scene 912 with d
    f "Kate just said that because she was jealous."
    chelsey "Kate purposefully did it."
    chelsey "I saw her grinning."
    f "I know, I talked to her."
    f "She’s going to apologize when we come out here."
    chelsey "Thank you, Mr. Frank."
    f "Come here, don’ cry, it’s going to be okay."
    scene 913 with d
    f "*How could one hurt this angel's feelings."
    f "*Such a cute face."
    f "*Petite yet still beautiful breasts."
    f "*If only I could remove that bra and see them clearly."
    f "*Shit, I shouldn’t be thinking like that."
    scene 914 with d
    f "*It feels like Chelsey is grabbing my ass."
    f "*Maybe it was an accident."
    f "*I won’t mention it. She’s already upset as it."
    scene 913 with d
    f "You can pick any swimsuit you like, darling."
    chelsey "Thank you, Frank."
    chelsey "You are just like a real father."
    chelsey "Always there when I need him most."
    scene 914b with d
    f "*Shit, I’m starting to get hard."
    f "*She is pressing herself against my body."
    f "*She must've felt it by now."
    scene 914a with d
    f "*It’s weird that she’s not saying anything."
    scene black with d
    pause
    scene 915 with d
    kate "I'm sorry Chelsey."
    scene 916 with d
    kate "I didn't mean to hurt your feelings."
    f "Great."
    f  "Now don’t do it again."
    f "I'll find Eva to pay for your swimsuits."
    scene 917 with d
    chelsey "Is he gone?"
    kate "Yes."
    chelsey "If you ever bad-mouth me in front of Mr. Frank again. "
    chelsey "I swear, I will hit you."
    kate "Sure. I’m soo scared, I’ve got shiver down my spine. Please, I’m not afraid of you."
    chelsey "Hmmf. Well, Frank and I cuddled in the fitting room. Jealous?"
    kate "That imagination of yours knows no limits hey."
    chelsey "You can deny it, but you know I’m telling the truth."
    chelsey "And it felt great."
    scene 918 with d
    stop music fadeout 1
    f "I’m sorry Eva, we didn’t get that many items."
    eva "You owe me one."
    f "Deal."
    f "Thanks for the helping hand."
    f "See you around."
    scene black with d
    s "In the mansion."
    scene 849 with d
    thompson "How was the trip Frank?"
    f "Everything went great."
    f "We picked beautiful swimsuits for the girls."
    thompson "Did you like going on a trip with Frank, Chelsea?"
    chelsey "Yes. He is a perfect match for the job."
    thompson "What do you think, Kate?"



    if kate_gameover >= 1:

        scene 850 with d
        kate "He was spying on me in the fitting room."
        scene 847 with d
        thompson "You are fired. Farewell."
        jump gameover
    else:

        scene 850 with d
        kate "Undecided."

    thompson "50/50"
    thompson "Girls, you are free to go."
    thompson "I need to have a word with Frank."
    scene 849b with d
    thompson "How was the trip?"
    thompson "Getting along with the girls?"
    f "To be honest, there was a fight between the girls."
    f "But I managed to defuse the situation."
    f "Chelsey and I are getting along well."      #####
    f "But I’m going to need more time to get through to Kate."
    scene 847 with d
    thompson "I see."
    thompson "I have a question, with regards to the receipt."
    thompson "I told you to purchase two swimsuits, not four."
    scene 849b with d
    f "I apologize for that. I wanted to develop a better relationship with the girls and told them they could get another one each."
    scene 847 with d
    thompson "I don’t like it when my orders aren’t followed."
    thompson "Therefore, this is your first strike."
    thompson "When you get three strikes."
    thompson "We part ways."
    scene 849b with d
    f "I understand, ma'am."
    f "My apologies, forgive me."
    scene 847 with d
    thompson "I called the store and spoke to the shop assistant."
    thompson "I enquired about your behavior in the store."
    scene 849b with d
    f "*I do hope Eva was satisfied. Ha!"
    scene 847 with d
    thompson "The shop assistant was pleased with you."
    thompson "She also noted, that if you come again."
    thompson "You’ll get a large discount."
    thompson "This is good, I like hearing good things."
    scene 849b with d
    f "Thank you, ma'am."
    f "*Eva backed me up."
    f "*I should pay her a visit."
    scene 847 with d
    thompson "Now, May will show you to your room."
    thompson "You are done for the day."
    thompson "Oh, and the taxi driver dropped your bag off."
    thompson "You left it in the car."
    scene 849b with d
    f "Thank you, ma'am."
    scene black with d
    s "Frank's room."
    scene 919 with d
    f "A nice room with a shower too. Nice."
    f "How can I contact you, May?"
    scene 920 with d
    pause
    f "Could you answer me, please?"
    f "I won’t tell anyone if you do."
    f "I guess that’s a no."
    f "I understand."
    f "I’ll find a way to contact you."
    scene 921 with d
    f "*Gotta take a shower while no one is around."
    play music "music/shower.mp3"
    scene 922 with d
    f "*This shower is relaxing. The hot water is amazing."
    f "*Wish the room had a tub."
    scene 923 with d
    f "*This room is incredible."
    f "*And two shower units. "
    f "*I could share this experience with a girl."
    scene 924 with d
    f "*Singing."
    scene 923 with d
    f "*I haven’t had a shower like this in ages."
    f "*Well, I'm done."
    stop music fadeout 1
    scene 925 with d
    f "*Wow, May even fetched me a towel."
    f "*Maybe if I give her a fright she’ll say something."
    scene black with d
    pause
    f "BOO!"
    scene 926 with d
    f "*Nothing. Damn, she’s good."
    f "*I’ll be more prepared next time."
    scene 927 with d
    f "*Shit, she saw my dick and got scared."
    f "*Probably thought back to when those guys wanted to rape her."
    f "*That’s unsettling, she thinks of me in that way."
    f "*Mrs. Thompson would fire me if I tried anything like that."
    f "*And I’d probably end up back in prison."
    scene 928 with d
    dog "Woof."
    play sound "music/dog.mp3"
    f "*Damn dog again."
    f "*I need to apologize again, or I might just loose my balls. "


    menu:

        "{color=#1BBB20} Apologize. {color=#FF0000} (+1 May's Point)":

            f "I’m sorry May, I didn’t hear you come in."
            pause
            pause
            show heart with moveinbottom:
                yalign .35 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ may_score = change_stat(may_score,1)
            hide heart

        "{color=#E5170A} Insult {color=#FF0000} (-1 May's Point)":

            f "Maybe if you knocked this wouldn’t have happened."
            pause
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ may_score = change_stat(may_score,-1)
            hide heart
            pause



    pause
    scene 929 with d
    f "*I hope that’s fine."
    stop sound fadeout 1
    scene 930 with d
    f "The evenings are my free time."
    f "The girls are going through a family feud."
    f "No point paying them a visit."
    f "I'll go see Marty."
    scene 931 with d
    f "Woah, there’s a porch here."

    menu:

        "{color=#1BBB20} Step outside":

            f "Let’s see it."

    pause
    scene 932 with d
    f "My room is on the first floor."
    f "So, no one will know if I sneak some girls in."
    f "But I’ll first need to gain the trust of the dog."
    scene black with d
    s "After 30 minutes."
    pause
    play music "music/Auto_sound.mp3"
    scene 933 with d
    scene black with d
    stop music fadeout 1
    scene 934 with d
    play music "music/city1.mp3"
    Elsa2 "Why did I marry you Marty?"
    Elsa2 "You are old and unemployed."
    Marty "I used to be very rich."
    Marty "I had a firm to my name and everything."
    Marty "But then everything went to shit."
    Marty "I went bankrupt."
    Elsa2 "So you say I was with you for your money?"
    Elsa2 "I'm such an opportunistic bitch."
    Marty "Yep. Looks like it. Ha-ha."
    scene 935 with d
    Elsa2 "Could you put another finger in my ass?"
    Marty "Sure sweetheart."
    scene 936 with d
    f "Hello there."
    f "Looking sexy Elsa."
    f "Where did you get the new clothes?"
    scene 935 with d
    Elsa2 "Credit goes to Marty."
    f "Should've asked me."
    f "I know an assistant at a fashion store."
    f "I can get you huge discount."
    Marty "Aha-ha-ha! I’m sure your huge dick had a role to play hey? Ha!"
    scene 935 with d
    Elsa2 "Congratulations Frank!"
    Elsa2 "You got yourself a girlfriend."
    scene 936 with d
    f "Kinda, I guess."
    f "By the way, what are you doing with Elsa?"
    scene 934 with d
    Marty "Stretching her ass."
    Marty "Clients are asking why anal isn’t on the menu."
    scene 935 with d
    Elsa2 "So if I worked as a prostitute before."
    Elsa2 "Then how come my ass isn’t stretched out?"
    #scene 936 with d
    #pause
    scene 937 with d
    f "Business is booming?"
    scene 936 with d
    Marty "So far, so good."
    #scene 936 with d
    #pause
    scene 935 with d
    Elsa2 "Try investing it."
    Elsa2 "So that your capital generates more capital."
    Elsa2 "How do I know these things...?"
    scene 936 with d
    f "That’s actually great advice, thanks Elsa."
    f "Marty, get some Mirage from a local gang."
    f "And then Elsa can distribute it when she’s with her clients."
    Marty "Sounds like a plan."
    Marty "Elsa knows how to make money."
    Marty "She is truly gifted."
    Marty "The way she gets her clients into parting with their money, just masterful."
    Marty "They always leave with empty wallets, among other things. He-he-he."
    scene 938 with d
    Marty "Here come your clients, Elsa."
    Marty "Time to make some more money."
    stop music fadeout 1
    scene black with d
    pause
    play music "music/sexy.mp3" fadeout 1
    scene 941:

       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0

    pause
    scene 939 with d
    stop music fadeout 1.0
    pause
    scene 940 with d
    f "I need to visit Erin."
    f "She helped me land that job."
    f "I should take her out for a coffee."
    f "She said she was married to Judge Olsen."
    f "Maybe I can find out who was involved in my early release."
    f "I don’t like owing someone, especially someone I don’t know."
    Marty "See you around Frank."
    scene black with d
    pause
    scene 942 with d
    play music "music/office.mp3" fadeout 1
    Erin "Another day is over."
    Erin "This job is so boring."
    Erin "Same shit, different day."
    Erin "I used to be an attorney back in the day."
    Erin "Every new case was a challenge, it gave me meaning and joy."
    Erin "But when I got married, everything changed."
    Erin "My husband insisted I get a new job."
    scene 943 with d
    Erin "Soon I’ll get back home, alone."
    Erin "My husband won’t be home, he often isn’t."
    Erin "He’s always out somewhere."
    Erin "A huge caseload is his common excuse."
    Erin "And that is his reason why he neglects our time together."
    Erin "He rarely satisfies me, if ever."
    Erin "I'm tired of all these sex toys."
    Erin "And I can’t find a lover."
    Erin "As soon as men figure out my husband is Judge Olsen..."
    Erin "… they cut all contact immediately."
    scene 945 with d
    f "Good day. I’m here in regard to a job."
    scene 943 with d
    Erin "It's already past business hours."
    Erin "Come back tomorrow."
    scene 945 with d
    f "It’s extremely urgent."
    scene 944 with d
    Erin "Frank! It’s you."
    Erin "How’s the job going?"
    scene 945 with d
    f "It’s going great, thank you."
    f "I’m currently on a probationary period."
    scene 944 with d
    Erin "I didn’t even know it was you."
    Erin "Good for you!"
    Erin "How can I help you?"
    scene 945 with d
    f "I promised you a cup of coffee, and I plan to deliver on that promise."
    f "I'm free and available this evening."
    f "We could leave right now."
    scene 944 with d
    Erin "You must've forgotten that I'm married to Judge Olsen."
    scene 945 with d
    f "I haven’t forgotten."
    f "I'm asking you out, not Judge Olsen."
    scene 944 with d
    Erin "*What shall I choose."
    Erin "*Kill time watching TV or go out with a stranger."
    Erin "*I haven’t been out in such a long time"
    Erin "..."
    Erin "..."
    Erin "*Very well. Coffee it is."
    Erin "*Gosh, I'm so reckless."
    Erin "I’m in. Let’s go."
    stop music fadeout 1
    scene 946 with d
    play music "music/city1.mp3"
    pause
    scene 947 with d
    Stella "We are about to apprehend a very dangerous criminal, Sergeant."
    john "Yes, ma'am."
    Stella "He might be armed."
    Stella "If he resists, you are free to open fire. Shoot to kill has been deemed necessary."
    john "I’m an experienced police officer ma’am."
    john "I'll deal with him even if he resists."
    Stella "In case you didn’t hear me. If he disobeys, shoot to kill and that is an order Sergeant."
    john "But ma'am."
    Stella "What's your name?"
    john "John."
    Stella "Get to the backseat John."
    scene 948 with d
    Stella "And take off your pants."
    john "Why ma'am?"
    Stella "Are you disobeying an order from a superior, Sergeant?"
    john "No ma'am."
    scene 949 with d
    pause
    scene 950 with d
    Stella "Wow. What a big cock you have John, and it’s already hard."
    Stella "Would you like me to jerk you off?"
    john "Yes, ma'am."

    menu:

        "{color=#1BBB20} Jerk off.":

            scene 950 with fade:
                "anim_18" with d
    pause


    scene 960
    with flash
    scene 960 with flash
    pause 0.3
    scene 960 with flash
    scene 960 with flash
    pause 2.0
    with d
    scene 959 with d
    pause
    Stella "I’ve been watching you for a while now."
    Stella "An I want to be with you."
    Stella "Do you want to be with me?"
    john "Yes, ma'am."
    Stella "Kill Frank and we'll be together."
    Stella "I'll give you head every night."
    john "Yes ma’am!"
    stop music fadeout 1
    scene 951 with d
    f "I've seen a nice cafe nearby."
    f "We could go there."
    Erin "Let’s stay outside, please."
    Erin "I’m always indoors, I’d like to be outside for a bit."
    f "Sure, whatever you want."
    scene 952 with d
    play music "music/police_siren.mp3" fadeout 1
    john "Mr. Frank."
    scene 953 with d
    f "What’s going on here?"
    john "You are under arrest for robbery."
    f "*What do I do now…"
    f "*I can’t go back."
    f "*I should never have stayed in this city."
    f "You are mistaken, I’m not Frank."
    john "Lying won’t help, I have confirmed your identity with a photo on record."
    scene 954 with d
    f "Fine, I’ll prove it to you. Let me just het my driver’s license."
    scene 955 with d
    john "Don’t do it. Freeze or I will shoot!"
    scene 957 with d
    pause
    play sound "music/fire.mp3"
    scene 956 with d
    stop music fadeout 1.0
    pause
    jump newyear2019
    hide screen topleftmenu5
    pause
    scene patrons with d
    pause




    pause










label warning:

    scene warning with d
    show screen warningscreen
    pause
    #scene writer with d
    #pause
    scene frank_upgrade with d
    pause
    hide screen warningscreen
    scene patrons with d
    pause


label tryagain:

    hide screen topleftmenu1
    hide screen topleftmenu2
    hide screen topleftmenu3
    hide screen topleftmenu4
    hide screen topleftmenu5
    scene tryagain with d
    pause
    return


label end:

    hide screen topleftmenu1
    hide screen topleftmenu2
    hide screen topleftmenu3
    hide screen topleftmenu4
    hide screen topleftmenu5
    scene patrons with d
    pause
    show screen warningscreen
    #scene writer with d
    #pause
    scene end with d
    pause
    #scene edit with d
    #pause
    #scene hardcore with d
    #pause
    show screen screenend
    pause
    hide screen screenend
    hide screen warningscreen
    return


label gameover:

    window hide
    hide screen topleftmenu1
    hide screen topleftmenu2
    hide screen topleftmenu3
    hide screen topleftmenu4
    scene gameover
    show gameover
    play music "music/smex.wav"
    pause
    return

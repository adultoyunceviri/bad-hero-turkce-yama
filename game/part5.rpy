


































default clean_bar_max = 1.5
default clean_bar_value = 0
define barxsize = 1000
define barysize = 30


#################################################################################

label part5:



    scene 1262 with d
    play music "music/battle.mp3"
    strip "We got a problem."
    jared "What is it?"
    strip "Frank..."
    strip "You ordered to me to trace him."
    jared "What is up with him?"
    strip "I got some intel from a hooker."
    strip "Now he is the boss of a local gang that distributes the product."
    strip "It's you who appoints the new boss usually, sir."
    strip "Let me end the guy."
    strip "Then we just penalize the gang and call it a day."
    jared "We should not intervene for now."
    jared "All gangs get their supplies of Mirage from our labs."
    jared "What you should do is raise the price for Frank's gang by 40 percent."
    jared "They will get rid of Frank themselves as soon as the profits take a hit."
    jared "You are not smart enough to come up with a plan like this."
    jared "Killing someone is the only thing you can think of."
    jared "Don't bother me over trifling matters."
    jared "Apply yourself once."
    strip "Roger that, sir."
    strip "I must apologize for troubling you."
    scene 1262b with d
    stop music fadeout 1
    pause
    scene black with d
    s "Franks' room."
    scene 1263 with d
    f "Good job, Rex."
    f "You saved my life today."
    f "I owe you one."
    f "Want to get a treat?"
    scene 1264 with d
    f "*May is here."
    f "*Looks like treats are off the table."
    f "*She must have been looking for Rex."
    f "*Now that's clearly a murder face she makes. A-ha-ha."
    scene 1265 with d
    pause
    scene 1264 with d
    f "Hope we don't have any bad blood between us, right?"
    f "I took Rex for a short walk."
    f "He got tired of being locked in your backyard."
    f "He was so happy to see the city."
    f "I'm in good mood."
    f "You can take Rex if you need him."
    scene 1264b with d
    f "But I want your word that I'm free to take him on for a walk."
    scene 1266 with d
    f "Anything else?"
    s "..."
    s "..."
    f "Ah, right, you would like your phone back. A-ha-ha."
    f "Hmm..."
    f "You know the rules."
    f "You will get it back as soon as you open your mouth."
    scene 1267 with d
    pause
    scene 1268 with d
    f "I actually expected a thank you for returning Rex."
    scene 1269 with d
    f "It's time I take a shower and go to bed."
    scene black with d
    s "Kate and Chelsey's room."
    play music "music/Feelin Good.mp3"
    scene 1270 with d
    pause
    scene 1271 with d
    play sound "music/cellphone_ring.ogg"
    pause
    scene 1272 with d
    stop sound fadeout 1
    kate "Hi, Eva."
    scene 1295 with d
    eva2 "Hey."
    scene 1272 with d
    eva2 "How is it going, Kate."
    kate "All good. Ready to fall asleep."
    eva2 "Looks like you forgot about me though."
    kate "How so?"
    scene 1295 with d
    eva2 "I got you a Christmas gift."
    eva2 "Remember?"
    scene 1272 with d
    kate "It totally slipped my memory."
    kate "Thanks for a reminder."
    eva2 "I knew it."
    kate "Give me a second, I will give it a shot."
    scene 1295 with d
    eva2 "I'm longing for a photo."
    kate "I haven't seen it in a while."
    kate "I bet it was Chelsey who stowed it away from me."
    stop music fadeout 1

    menu:

        "{color=#1BBB20} Look for the present.(Bonus animation)":


            jump part5_quest1

        "Do nothing.":

            pause
label part5_game2:

    $ renpy.block_rollback()
    play music "music/Feelin Good.mp3"
    scene 1273 with d
    kate "There we go."
    kate "Panties should be inside."
    kate "I can try it on since Chelsey is not here."
    scene 1274 with d
    kate "Oh God. These panties show too much."
    kate "This type of underwear is prohibited in our school."
    kate "It has to be a mistake on Eva's behalf."
    kate "I should give she a call."
    scene 1275 with d
    kate "You must have put a wrong set of panties in my box, Eva."
    eva2 "What do you mean?"
    kate "They are too revealing."
    kate "My whole butt is visible in those."
    scene 1295 with d
    eva2 "That is exactly what I intended."
    eva2 "It's high time you grew up and started wearing real underwear, like all your peers do."
    scene 1275 with d
    kate "But it's against the rules."
    scene 1295 with d
    eva2 "I see how it is, Kate."
    eva2 "You don't care about our friendship in the slightest."
    eva2 "This is sad to hear. Goodbye."
    scene 1275 with d
    kate "Wait, Eva!"
    kate "I have no friends except for you."
    kate "I guess you are right."
    kate "Since everyone is ok with this type of panties..."
    kate "Why should I be afraid to show a little bit more skin!"
    scene 1295 with d
    eva2 "Way to go, honey."
    eva2 "It's up to you and you only, don't let anyone influence your decisions."
    eva2 "Cherish that independence."
    scene 1277 with d
    kate "I have to put it on real quick and snap a picture."
    kate "But if anyone walks in."
    kate "I will get in real trouble."
    scene 1278 with d
    kate "I feel like I'm totally butt-naked."
    kate "Who do people wear undergarments like this one."
    scene 1279 with d
    kate "I shall snap a photo and take them off immediately."
    scene 1280 with d
    kate "I took a photo for you, Eva."
    scene 1296 with d
    eva2 "You shy away from these cute panties too much, I can see it."
    eva2 "I knew it would be like this."
    eva2 "Snap one from behind now, would you?"
    scene 1280 with d
    kate "Isn't one picture enough already?"
    scene 1296 with d
    eva2 "Oh, what a cowardly girl."
    eva2 "Are you scared of your own body?"
    eva2 "Snap me a new photo or I will take it personally."
    scene 1280 with d
    kate "You are teasing me."
    kate "I will show you that I have no fear."
    kate "You are about to get what you asked for."
    scene 1281 with d
    kate "Taking a picture of my behind is harder than I thought."
    stop music fadeout 1
    scene 1282 with d
    play music "music/social_wreck.mp3"
    kate "Called it! This photo is a mess."
    chelsey "*What is Kate doing?"
    chelsey "*Revealing panties are against the rules."
    chelsey "*It has to be Eva's gift"
    chelsey "*But how she managed to find it?"
    chelsey "*This is my payback time."
    scene 1283 with d
    chelsey "*Time for photo of my own."
    scene 1284 with d
    chelsey "Where you got these panties from?"
    kate "This is Eva's gift. "
    chelsey "Only a whore would wear something like this."
    chelsey "You should immediately trash them."
    kate "It's not your call to make."
    chelsey "This photo will go straight to Mrs. Thompson."
    kate "I'm not getting rid of my new underwear anyway."
    scene 1285 with d
    chelsey "I said take them off now."
    chelsey "Let me give you a hand."
    kate "It hurts! Let me go!"
    chelsey "Stay still or there will be more pain."
    scene 1286 with d
    chelsey "There we go."
    scene 1287 with d
    stop music fadeout 1
    menu:

        "{color=#1BBB20} Take a closer look.":

            play music "music/trow.mp3"
            scene 1287b with d
            pause
            scene 1287d with d
            pause
    scene 1287 with d
    kate "Eva!?"
    scene 1296 with d
    eva2 "Yes. I'm waiting for the follow up photo."
    scene 1287 with d
    kate "Just don't hang up on me."
    eva2 "What happened, Kate?"
    kate "When I was trying to take a picture."
    kate "Chelsey...she entered the room."
    kate "She ripped your gift off me and threw it out."
    kate "I could not do anything about it."
    kate "Trust me."
    scene 1296 with d
    eva2 "Are you crying?"
    scene 1287 with d
    kate "I'm so sorry for letting you down."
    scene 1296 with d
    eva2 "Don't be so upset, Kate."
    eva2 "I will get you some new panties."
    eva2 "Pay me a visit this weekend."
    eva2 "We will have a great time together."
    scene 1287 with d
    kate "But we are not allowed to leave the mansion."
    eva2 "How about I come by?"
    kate "I will consult Mrs. Thompson."
    kate "I don't think she will turn down the idea."
    scene 1296 with d
    eva2 "I will have a talk with Chelsey."
    eva2 "So this incident never repeats itself."
    eva2 "Goodnight."
    scene 1298 with d
    eva2 "Now this little bitch gets on the wrong side of Kate."
    eva2 "It's time to end this."
    eva2 "Too bad I never got the second picture."
    eva2 "Her butt is perfect."
    eva2 "I guess from this point my imagination will take the wheel."
    scene 1297 with d
    stop music fadeout 1
    menu:


        "{color=#1BBB20} Bonus animation (ON)." if part5_bonusanim1 == True:

            play music  "music/fingering.mp3"
            scene black with fade:
                "anim_45" with d
            pause
            eva2 "Oh-oh-oh!"
            pause
            stop music fadeout 1

        "Bonus animation (OFF)." if part5_bonusanim1 == False:

            pause


    scene black with d
    pause
    scene 1289 with d
    play music "music/Sneaky Snitch.mp3"
    chelsey "Nice panties."
    scene 1289b with d
    chelsey "They emphasize my ass like nothing else."
    scene 1288 with d
    chelsey "Kate is so dumb."
    chelsey "Taking advantage of her is a piece of cake."
    chelsey "Mr. Frank's jaw will drop when he sees me like this. A-ha-ha."
    stop music fadeout 1
    scene black with d
    pause
    scene 1290 with d
    thompson "What is it, Kate?"
    scene 1291 with d
    kate "Could you give my girlfriend a permission to come here?"
    thompson "You got yourself a friend!"
    thompson "Great. But your company should have integrity, you can't be friends with questionable people."
    thompson "Who is she?"
    scene 1290 with d
    kate "She is Mr. Frank's acquaintance."
    scene 1291 with d
    thompson "Alright, you have my permission to spend this weekend together."
    thompson "Chelsey and you will benefit from getting to know new people."
    scene black with d
    s "Police Department."
    play music "music/Police_Office.mp3"
    scene 1292 with d
    genry "How the search for my wife is going, officer?"
    detective "This case is on Bianca."
    scene 1293 with d
    bianca "So far we haven't managed to get her whereabouts."
    scene 1294 with d
    genry "Does it usually take so long to locate the body?"
    scene 1293 with d
    bianca "Why you assumed we were looking for the body?"
    bianca "Is your wife dead?"
    bianca "You know something we don't?"
    scene 1294 with d
    genry "Umhhh..."
    genry "That was a wild guess, nothing more."
    genry "Our fund desperately needs an executive director."
    genry "And if she is dead I need to have a confirmation."
    genry "In order to officially take reigns."
    scene 1293 with d
    bianca "We are working on it."
    bianca "The district in questions is riddled with crime."
    bianca "It's hard to find anyone willing to cooperate with the police."
    scene 1294 with d
    genry "Have you managed to drag anything to light?"
    scene 1293 with d
    bianca "Yes, a taxi-driver who saw her on the day she disappeared."
    scene 1294b with d
    genry "Do you know where that taxi driver is?"
    genry "..."
    genry "..."
    genry "What exactly he saw?"
    scene 1293 with d
    bianca "Your wife wasn't alone."
    bianca "A man accompanied her that day."
    bianca "They got out of the car in this neighborhood."
    bianca "Taxi driver has no clue where they were heading."
    bianca "Who could be that man?"
    scene 1294 with d
    genry "Unfortunately, we can only guess."
    scene 1293 with d
    bianca "Taxi driver was not able to identify her companion."
    bianca "He was wearing a hoody and shades."
    scene 1294 with d
    genry "I needed results yesterday."
    genry "Oh, and one more thing. Put a bra on for God's sake."
    genry "We are in Police Department, not a brothel."
    scene 1293 with d
    bianca "Criticism noted, sir."
    scene black with d
    pause
    scene 1293 with d
    bianca "Sir. I feel like he has something to hide."
    bianca "Have you seen his eyes when I mentioned the taxi driver?"
    scene 1301 with d
    detective "Yes, good catch. I noticed that too."
    detective "Keep searching for his wife."
    stop music fadeout 1
    scene black with d
    pause
    scene 1302 with d
    angel "Get up."
    scene 1303 with d
    angel "Clean yourself."
    angel "I don't want you to smell like this hobo."
    elsa2 "Yes, ma'am. "
    scene 1304 with d
    elsa2 "It's been a while since I took a bath."
    elsa2 "Street life is horrible."
    elsa2 "Maybe it's good that Frank ordered me to stay here."
    elsa2 "This deserves a gift for sure."
    scene 1305 with d
    angel "Are you done?"
    elsa2 "Yes, ma'am. It was amazing."
    angel "I was ordered to make a top-notch escort girl from you."
    elsa2 "Oh, I have already worked as one."
    angel "Whatever you've been doing on the streets..."
    angel "Just forget about it."
    angel "In order to get wealthy clients."
    angel "You have to do something beyond spreading your legs like a doll."
    angel "Put your arms above your head, let me take a look."
    scene 1306 with d
    angel "You got a nice body."
    angel "Boobs are on a smaller side, but we will turn it around."
    angel "I know one plastic surgeon."
    angel "Any tats on you?"
    elsa2 "No, ma'am."
    elsa2 "Well, you should have some."
    scene 1305 with d
    angel "Why are you always naked?"
    angel "Is this how you attract your clients?"
    scene 1306 with d
    elsa2 "I have nothing to put on, ma'am."
    scene 1305 with d
    angel "Give me a second, I'll get you something."
    pause
    play music "music/sexy.mp3" fadeout 1
    scene 1307:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    stop music fadeout 1
    angel "Now we are talking."
    scene 1308 with d
    play music "music/rocket.mp3"
    marty "Elsa? Are you in here?"
    scene 1305b with d
    angel "What?"
    scene 1308 with d
    marty "I need some money."
    marty "Have to quench my thirst, if you know what I mean."
    scene 1305b with d
    angel "You quenched your thirst on every bottle of alcohol there was in the house yesterday."
    angel "You want to say that wasn't enough for you?"
    scene 1308 with d
    marty "Oh, we are only getting started."
    marty "My friends will get here soon."
    scene 1309 with d
    elsa2 "I haven't managed to make any money yet, Marty."
    elsa2 "I got nothing."
    scene 1308 with d
    marty "Then get back to work."
    marty "No time to sit here idly."
    scene 1305b with d
    angel "Don't tell her what to do."
    angel "Who the hell are you to begin with?"
    angel "Are you her pimp?"
    scene 1308 with d
    marty "I am her husband and I need money. Now."
    marty "Come with me. "
    scene 1305b with d
    angel "She is not going anywhere."
    scene 1308 with d
    marty "Try and stop me. A-ha-ha."
    scene 1310 with d
    angel "This gun will stop you, not me."
    scene 1308 with d
    marty "Woah-woah. Take it easy, baby."
    marty "I just want to get my wife."
    scene 1310 with d
    angel "I don't want to see you in this house ever again."
    angel "You belong on the streets with your frined Frank, under a bridge or something."
    angel "Let's make a deal."
    angel "You will get booze allowance from what she makes."
    angel "Your side of the deal is leaving this house."
    angel "She will be making here far more than what she was making on the street, trust me."
    scene 1308 with d
    marty "Hmmm..."
    marty "..."
    marty "..."
    marty "Alright, damned wretch. Deal."
    marty "But if you lied - I will come back and no one will save you."
    scene 1305 with d
    angel "A whore with a husband, now that's something new."
    angel "If you want to know my opinion, I think he takes advantage of you."
    scene 1311 with d
    elsa2 "He used to be rich."
    elsa2 "But then..."
    scene 1305 with d
    angel "Sure, save me from these bedtime stories."
    scene 1308b with d
    marty "This whore showed me the door."
    marty "I will have my revenge."
    stop music fadeout 1
    scene 1305 with d
    angel "To become a resident in our house."
    angel "You will have to put twice as much work."
    angel "Do anything I say."
    elsa2 "I thought Frank was in charge here."
    angel "All whores are under my command."
    angel "All the money go through me."
    angel "I tell you what to do and when."
    angel "I keep all the books."
    angel "So, in case you want your life to turn into hell."
    angel "I could arrange that easily."
    angel "Frank is not here to stay."
    angel "Therefore, my advice for you is to make a good friend of me."
    scene 1311 with d
    menu:

        "{color=#1BBB20} Comply and follow orders. (Bonus animation.)":

            elsa2 "I will do anything you say."
            elsa2 "I really need money."

        "Comply without following orders.":

            elsa2 "I will do anything you say."
            elsa2 "I really need money."
            jump part5_minigame_end

    scene 1314 with d
    angel "Let's start."
    jump part5_chosedildo

label angel_buhgalter:

    $ renpy.block_rollback()
    scene black with d
    pause
    scene 1314 with d
    angel "I'm tired."
    angel "Take a look at our books for me."
    jump part5_minigame1

label angel_buhgalter_2:

    $ renpy.block_rollback()
    scene black with d
    pause
    scene 1314 with d
    angel "I'm tired."
    angel "Take a look at our books for me."
    jump part5_minigame2

label angel_treining:

    $ renpy.block_rollback()
    scene black with d
    pause
    scene 1314 with d
    angel "I want you to play with the toys."
    angel "This will be good for you."
    jump part5_chosedildo




label part5_2:

    $ renpy.block_rollback()
    $ elsa_minigame1_count = 0
    scene black with d
    pause
    scene 1316 with d
    pause
    jump part5_minigame2

label part5_3:

    $ renpy.block_rollback()
    scene 1315b with d
    pause
    scene 1304 with d
    jump part5_minigame3

label part5_4:

    $ renpy.block_rollback()
    $ elsa_minigame3_count = 0
    scene 1317b with d
    angel "You have to work on your ass gape rather than pleasure yourself."
    angel "I'm extremely dissatisfied with you."
    jump part5_chosedildo

label part5_5:

    $ renpy.block_rollback()
    $ dildo_middle_complete = True
    $ dildo_big = True
    scene 1320 with d
    angel "Way to go, girl."
    jump angel_buhgalter_2

label part5_6:

    $ renpy.block_rollback()
    scene black with d
    pause
    scene 1327 with d
    pause
    scene 1328 with d
    elsa2 "Help!"
    angel "You picked too big of a size."
    angel "Now it is stuck inside of you."
    jump tryagain


label part5_7:

    $ renpy.block_rollback()
    $ dildo_small_complete = True
    scene 1329 with d
    angel "Good girl, you picked the right size to start with."
    jump angel_buhgalter


label part5_chosedildo:

    $ renpy.block_rollback()
    scene black with d
    pause
    scene 1325 with d
    angel "Take a pick."
    angel "Apply your brain this time."
    angel "Your training depends on this choice."
    menu:

        "{color=#1BBB20} Pick a toy.{color=#0000ff} (Order: 3, 2 and 1)":

            call screen part5_dildo

label part5_minigame_end:

    $ renpy.block_rollback()
    scene black with d
    pause
    scene 1327 with d
    angel "Great. Our training sessions work wonders."

    menu:

        "{color=#1BBB20} Secret scene.":

            angel "You did good today, it's time to have some rest."
            scene 1471 with d
            angel "Come here, girl."
            angel "Do you like my pussy?"
            elsa2 "Yes, it is gorgeous."
            angel "You are free to touch it."
            scene 1472 with d
            angel "Don't be afraid."
            angel "Get your fingers in there."
            scene 1473 with d
            play music "music/sexmusic.mp3"
            angel "Oh yeah, baby."
            scene 1475 with d
            angel "You turn me on."
            angel "Work with your tongue now."
            elsa2 "Why? "
            angel "I want to see what you are capable of."
            scene 1474 with d
            pause
            scene 1322 with d
            angel "Let me stand up to give you an easier access."
            scene 1321 with d
            angel "Where you learned all this?"

            menu:


                        "{color=#1BBB20} Watch.":
                            scene 1323 with fade:
                                "anim_44" with d
                            pause
                            elsa2 "Slurp."
                            elsa2 "Slurp."
                            elsa2 "Slurp."
                            pause




            scene 1321 with d
            angel "Mmm..."
            angel "I can stay on my feet no longer."
            angel "My legs are trembling."
            pause

            scene 1332 with d
            angel "You are no doubt my best apprentice!"
            angel "Bringing me to an orgasm so fast."

            menu:

                "{color=#1BBB20} Masturbate.":


                    scene 1332 with fade:
                        "1332" with d
                        pause 0.5
                        "1333" with d
                        pause 0.5
                        repeat
                        pause 2

            pause
            scene 1331 with d
            pause
            scene 1330 with flash
            pause 0.3
            scene 1330 with flash
            scene 1330 with flash
            pause 2.0
            with d
            scene 1334 with d
            stop music fadeout 1
            pause



    scene 1357 with d
    angel "You did a great job today."
    angel " I had a ton of fun."
    angel "You can rest now."
    scene 1358 with d
    elsa2 "Finally I got a friend in this house."
    elsa2 " Now I have a job and a place to call home."
    scene black with d
    pause
    scene 1335 with d
    play music "music/Miami Viceroy.mp3"
    pause
    scene 1335b with d
    f "Hi, Mike."
    bigmaike "Hey, Frank."
    f "How is it going?"
    bigmaike "All good."
    bigmaike " Whore are working."
    bigmaike "The product sells well."
    bigmaike "All the usual business."
    f "I will go check up on Elsa."
    bigmaike " Wait a second."
    bigmaike "The cops are about to arrive."
    bigmaike "We bribe them so they leave us alone."
    bigmaike "They want to meet a new boss."
    bigmaike "Leave your guns here."
    f "Alright, I will go talk to them."
    scene black with d
    pause
    scene 1336 with d
    den "Why you called us?"
    angel "One prick crossed the line with me."
    angel "Help me out and I will pay you big time."
    den "Alright."
    den "What you want us to do?"
    angel "I need you to beat the shit out of him and humiliate him."
    den "Humiliate how?"
    angel "Take a piss on his head."
    angel "This should be enough."
    den "Your request is quite kinky."
    angel "I will pay. Just name the amount."
    angel "You will get our whores at a discounted price."
    den "A tempting offer to say the least."
    den "Who is the guy."
    angel "He is our client."
    den "Any weapons on him? "
    angel "He will be alone and without any weapons."
    angel "It will be a walk in the park for you guys."
    den "What is his name?"
    angel "Frank."
    den "Frank???"
    den "Never heard of him."
    den "We have a deal."
    scene black with d
    pause
    scene 1337 with d
    f "Hmm. These cops look suspicious as hell."
    f "They shouldn't walk around in casual clothes."
    f "Guess they are undercover or something."
    scene 1338 with d
    f "You wanted to have a word with me?"
    den "Your name is Frank, right?"
    f "Yes, correct."
    scene 1339 with hpunch
    play audio "music/punch.opus"
    pause
    scene 1340 with d
    f "What's the deal, officers?"
    den "You crossed the wrong person, pal."
    den "Today you will answer for it."
    scene 1352 with d
    bigmaike "What is going on over there?"
    bigmaike "He needs help."
    angel "Don't intervene."
    angel "He has to deal with this by himself."
    bigmaike "Then we will get in trouble."
    angel "That last time he got lucky, nothing more."
    angel "Let's take a look how he handles this one."
    scene 1341 with d
    den "Sit still and we won't hurt you."
    scene 1342 with d
    f "What are you trying to do?"
    den "Chill, just a quick golden shower."
    f "You are not cops?"
    den "Of course not."
    f "Should have told me that right off the bat."
    den "You think the whole thing would have played out differently?"
    stop music fadeout 1
    s "..."
    s "..."
    menu:

        "{color=#1BBB20} Strike the groin.":

            play music "music/district-four.mp3"
            pause
            scene 1343 with hpunch
            play audio "music/punch.opus"

        "Bargain.":

            scene 1343b with d
            f " Let's bargain, guys?"
            den "Give me head first, then we bargain. "
            jump tryagain


    pause
    scene 1344 with d
    pause
    scene 1344b with d
    pause
    scene 1345 with hpunch
    play audio "music/punch.opus"
    pause
    scene 1346 with d
    pause
    scene 1347 with d
    pause
    scene 1348 with hpunch
    play audio "music/punch.opus"
    pause
    scene 1349 with d
    f "Who are you working for, kid?"
    den "I am not a snitch."
    scene 1350 with d
    f "Alright, how about this? "
    stop music fadeout 1
    play music "music/Miami Viceroy.mp3"

    jump vbar1_1

label part5_8:


    #$ d20roll_2 = renpy.random.choice(['Шлюха', 'Блядь', 'Сучка'])

    den "Ok-ok, chill."
    den "Let me go."
    f "I'm not going to repeat it again. Who is your boss?"
    den "Angel."
    f "He mentioned that I'm the boss of this gang by any chance?"
    den "I'm sorry, sir. We had no idea."
    den "She said that a client caused mischief."
    scene 1351 with d
    den " What are you going to do with this?"
    f "We will call it reciprocal measures."
    f "Hold still, kid."
    den "Please don't."
    den "How will I roam the streets after what you are about to do."
    scene 1353 with d
    angel "Let him go, it's not his fault."
    angel "Don't you dare to piss on him, prick."
    f "I have no choice."
    scene 1354 with d
    angel " Then we shall take it together."
    f "Hmmm..."
    f "After I do this."
    f "No one will want to hook up with you."
    den "Please, show mercy."
    den "You can take my car."
    den " I'm begging you."
    f "..."
    f "..."
    f "Next time I won't be so merciful."
    den "Thank you, sir."
    f "I will talk to you later, Angel."
    scene 1355 with d
    f "Now I have to teach your friend a lesson."
    scene 1355b with d
    f "Hey, get back here!"
    scene 1415 with d
    angel "Hey, watch the hands, kid."
    den "I'm looking forward to having sex with you."
    angel "On what ground? "
    den "Well, we suffered injuries because of you."
    scene 1416 with d
    angel "Really? You both failed to deal with one guy."
    den "He caught us off guard."
    angel "Cut it off, I saw everything."
    angel "Should not have fallen in with you."
    angel "Now I have a serious conversation ahead of me."
    den "Could you jerk me off at least?"
    scene 1417 with d
    den "Ouch!"
    scene 1416 with d
    angel "Give me the car keys and get the fuck out of here."
    angel "Or I will call Mike, he will give you a boxing lesson. A-ha-ha."
    scene black with d
    pause
    scene 1356 with d
    f "You knew about this and kept silent!"
    bigmaike "I had no clue."
    bigmaike "Angel tricked me into this shit."
    bigmaike "I genuinely thought it was cops."
    f "Well, I have a feeling that you are not lying."
    f "She is totally capable of such a scheme. "
    bigmaike "Our former boss would not have let it slide."
    bigmaike "We should give her a good beating."
    f "I don't hit women."
    bigmaike "If you do nothing."
    bigmaike "She will keep going at you."
    bigmaike " I know her and I know what I'm talking about."
    f "I will keep this in mind."
    f "But for now I want to see how she behaves."
    f "Where is Elsa?"
    f "I want to see her."
    bigmaike "She is in Angel's room."
    stop music fadeout 1
    scene black with d
    pause
    play music "music/sexy.mp3" fadeout 1
    scene 1359:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    stop music fadeout 1
    scene 1362 with d
    #play music "music/" ###############################################################
    elsa2 "Hi, Frank."
    f "How is it going, Elsa."
    f "You look stunning today."
    elsa2 "I want to express my gratitude."
    f "For what?"
    elsa2 "You saved my life."
    f "Don't mention it. Ha-ha."
    elsa2 "I made some dessert."
    elsa2 "Take a bite, will you?"
    f "*Hope this shit ain't poisoned."
    f "Can't say no to a good dessert. Thanks."
    scene 1363 with d
    f "How you like it here?"
    f "No one is bothering you?"
    elsa2 "All good."
    elsa2 "Angel helps me to feel at home."
    elsa2 "And I help her out with bookkeeping."
    f "Where is Marty? "
    elsa2 "He is not living with us now."
    elsa2 "He made a decision to keep living under that bridge."
    f "I shall pay him a visit."
    f "The way you are looking at these strawberries."
    f "Why are you not eating with me?"
    f "Maybe that's because it's poisoned, huh? ha-ha."
    elsa2 "Of course not."
    elsa2 "I borrowed this dress from Angel."
    elsa2 "She will kill me, if I mess it up with food."
    f "I could feed you if you don't mind."
    elsa2 "I'd appreciate it, Frank."
    elsa2 "I looove strawberries."
    elsa2 "Just be careful."
    scene 1364 with d
    f "Bon appetité!"
    scene 1365 with d
    pause
    scene 1366 with d
    pause
    scene 1367 with d
    pause
    scene 1368 with d
    elsa2 "I will mess up the dress this way."
    elsa2 "I need to change into something more appropriate."
    stop music fadeout 1
    scene black with d
    pause
    play music "music/sexy.mp3" fadeout 1
    scene 1369:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    play music "music/sexy.mp3" fadeout 1
    elsa2 "Mind turning around?"

    menu:

        "{color=#1BBB20} Take a peek.":

            scene 1361:


               subpixel True
               yalign 1.0
               pause 1.5
               linear 7.0 yalign 0.0
            pause

    elsa2 "Are you peeking, Frank?"
    scene 1360:


       subpixel True
       yalign 1.0
       pause 1.5
       linear 7.0 yalign 0.0
    pause
    stop music fadeout 1
    elsa2 "Come on, I asked you nicely."
    #play music "music/"   333333333333333333333333333333333333333333333333333333333333333
    f "Sorry, could not help it."
    f "You can stay like this."
    f "We don't want you messing up your reserve dress too."
    elsa2 "I guess you are right, Frank."
    scene 1370 with d
    elsa2 "Could you not stare at my boobs?"
    elsa2 "You are making me uncomfortable."
    f "It looks more pulled up and buffed."
    f "I want to feel it."
    elsa2 "Cut it off or I will have to dress up again."
    scene 1370b with d
    f "Let's add some whipped cream."
    scene 1372 with d
    f "Take a bite now."
    scene 1371 with d
    elsa2 "Oh, I got some cream on me."
    f "Don't fret, Elsa. I will take care of this."
    scene 1373 with d
    pause
    scene 1374 with d
    elsa2 "Oooh. Please, stop."
    elsa2 "You just can't hold yourself, can you?"
    elsa2 "Turns out you go crazy on whipped cream too."
    f "Mmmmm. "
    f "Uh-hum."
    elsa2 "I could arrange a cute whipped cream show for you."
    elsa2 "But don't peek before I tell you."
    menu:
        "{color=#1BBB20} Accept.":
            pause 0.5
    scene black with d
    pause
    scene 1375 with d
    elsa2 "Whipped cream dessert is served."
    f "Oh, wow. Wasn't expected anything like this."
    scene 1376 with d
    elsa2 "Would you like to start from the bottom and move up?"
    elsa2 "Hmm. You are the boos."
    scene 1377 with d
    elsa2 "You lick the cream off in such a sexy manner."
    f "You like that?"
    elsa2 "Yes. Don't stop."
    scene 1378 with d
    elsa2 "You gravitate towards my boobs again. Ha-ha."
    elsa2 " I want some cream too."
    scene 1379 with d
    f "Go ahead."
    f "I'm not greedy."
    elsa2 "Uhhmmm."
    scene 1380 with d
    elsa2 "O god. You stained up my panties."
    elsa2 "I will get grounded now, that's for sure."
    f "Quickly take them off before we stain them more."
    scene 1381 with d
    elsa2 "I feel like you do this intentionally. Ha-ha."
    f "No, I mess up on accident, I swear."
    elsa2 "I don't believe you."
    elsa2 "You want me fully naked!"
    scene 1382 with d
    f "What is it up your ass?"
    scene 1382b with d
    elsa2 "Angel gave me this buttplug."
    elsa2 "Buttplug helps me practice taking it up my ass."
    scene 1383 with d
    elsa2 "I'm practically naked."
    elsa2 "I will blush now for sure."
    f "Give me a minute."
    scene 1384 with d
    f "Now you are not alone in your nakedness."
    elsa2 "Wow, this is the first time I see you naked."
    scene 1386 with d
    elsa2 "Why would you take your briefs off?"
    scene 1385 with d
    elsa2 "Oh...now I see."
    elsa2 "I'm just a regular whore."
    elsa2 "Give me a second, I'll start blowing you."
    s "..."
    s "..."
    f "You are not a whore."
    elsa2 "???"
    f "You are my favorite whore."
    scene 1386 with d
    f "And if you are not ready."
    f "I won't push you."
    elsa2 "Ok, let's not get ahead of ourselves."
    f "Whatever you say, baby."
    scene 1388 with d
    f "Your butt is so tight."
    elsa2 "Yeah? I have a special exercise routine."
    f "Can I feel it?"
    elsa2 "Yes, sure."
    scene 1389 with d
    pause
    scene 1387 with d
    elsa2 "Your fingers are far lower than where they are supposed to be, Frank."
    elsa2 "They are right in my pussy, to be precise."
    scene 1390 with d
    f "I want you to have fun."
    f "I loved this little surprise you arranged."
    f "But if you don't want me to..."
    elsa2 " Mmmmm..."
    elsa2 "Keep going."
    scene 1479 with d
    pause
    scene 1390 with d
    f "How you like it?"
    elsa2 "Your fingers are magical."
    elsa2 "There is a toy nearby. Grab it."
    scene 1393 with d
    f "Do you like this one more?"
    elsa2 "Oh yes!"
    scene 1392 with d
    elsa2 "Ohh..."
    elsa2 "It fills me up so well."
    f "It's time we play a little."
    stop music fadeout 1
    menu:


        "{color=#1BBB20} Start playing.":
            scene 1483 with fade:
                "anim_29" with d
            pause
    elsa2 "Mmmmm..."
    elsa2 "Stop teasing me."
    menu:


        "{color=#1BBB20} Start playing.":
            scene 1484 with fade:
                "anim_33" with d
            pause
    f "I feel like this toy is too small for you."
    f "May I enter you, Elsa?"
    elsa2 "Don't waste your time talking."
    elsa2 "I'm already warmed up."
    elsa2 "My pussy is ready for you."

    menu:


        "{color=#1BBB20} Start playing for real.":

            play music "music/Breathing.ogg"
            scene 1485 with fade:
                "anim_30" with d
            pause
    f "Hooo...!"
    f "Now we both are having fun."
    elsa2 "Mmmm..."
    elsa2 "Let's change positions."
    elsa2 "It goes all the way up."
    elsa2 "How about I ride you?"

    menu:

        "{color=#1BBB20} Change a position.":
            scene 1486 with fade:
                "anim_31" with d
            pause
    f "Take it easy, Elsa."
    f "You rush it like someone is after us."
    elsa2 "This is Wild West, Frank."
    elsa2 "No one rides slow in Wild West."
    elsa2 "Let me turn around and check if some is actually after us."
    menu:


        "{color=#1BBB20} Start pounding. Bonus animation" if part5_bonusanim2 == True:
            scene 1487 with fade:
                "anim_32" with d
            pause
            f "Oh yes!"
            f "I can play Wild West whole game."

        "{color=#1BBB20} Bonus animation. (OFF)" if part5_bonusanim2 == False:

            pause


    menu part5_elsa:


        "{color=#1BBB20} Watch.":

            scene black with fade:
                "anim_34" with d
            pause


            elsa2 "Mmmmm..."
            elsa2 "Mmmmm..."
            scene 1409 with d
            pause
            scene 1409b with flash
            pause 0.3
            scene 1409b with flash
            scene 1409b with flash
            pause 0.5
            #with d
            scene 1409d with d
    stop music fadeout 1
    pause
    elsa2 "I couldn't hold it back."
    elsa2 "Looks like I came all over you."
    f "This deserves a punishment."
    elsa2 "Yes. Yes! Punish me."
    elsa2 "I'm a bad girl."
    f "Did you do that on purpose!?"
    elsa2 "Perhaps."
    scene 1395 with d
    pause
    scene 1396 with d
    f "Your ass will pay for your wrongdoings."
    scene 1410 with d
    elsa2 "My ass can take it. Ha-ha-ha."
    f "You sure talk a lot lately."
    elsa2 "I'm..."
    scene 1411 with d
    elsa2 "Uhmhm..."
    f "Much better now. Ha-ha."
    f "On your knees."
    scene 1404d with d
    pause
    scene 1404 with d
    elsa2 "I'm supposed to be afraid, huh? Ha-ha."

    menu:

        "{color=#1BBB20} Intimidate.":

            scene 1405 with d:

                "anim_36"
                pause 1.01
                "1405b"
            f "Shut up, whore."
            scene 1404 with d
    elsa2 "This don't cut it."
    elsa2 "I've heard worse."
    scene 1404 with d

    menu:

        "{color=#1BBB20} Slap":

            scene 1404 with d:
                "anim_35"
                pause 1.01
                "1404b"
            play audio "music/shlepok.mp3"
            pause 0.3
            scene 1405d with d
    f "It's time I clean that dirty mouth of yours."

    menu:

        "{color=#1BBB20} Start.":

            play music "music/blowjob.mp3"
            scene 1489b with fade:
                "anim_38" with d
            pause
            elsa2 "Slurp."
            elsa2 "Slurp."
            elsa2 "Slurp."
            f " What were you trying to say?"
            elsa2 "Ummhh..."

    menu:

        "{color=#1BBB20} Watch.":

            scene 1489 with fade:
                "anim_37" with d
            pause
            stop music fadeout 1


    scene 1404 with d
    f "Get on the bed."
    scene 1408 with d
    elsa2 "Want to look at my butt?"
    elsa2 "Do you like it?"
    f "I have seen better. Ha-ha."

    menu:


        "{color=#1BBB20} Slap ass.":


            scene 1408 with d:
                "anim_39"
                pause 1.01
                "1408b"
            play audio "music/shlepok.mp3"
            pause 0.3
            scene 1408d with d
    pause
    scene 1476 with d
    f "I found another toy here."
    f "Don't be shy."
    f "A-ha-ha. I bet you tried it already."
    elsa2 "I have never seen it before."
    f "Your ass is about to meet a new friend."

    menu:

        "{color=#1BBB20} Start.":

            play music "music/aah.mp3"
            scene 1490 with fade:
                "anim_40" with d
            pause
            f "Do you like it? "
            elsa2 "Ummmh..."
            elsa2 "Hoooh..."
            stop music fadeout 1

    menu:

        "{color=#1BBB20} Watch.":

            play music "music/aah.mp3"
            scene 1490b with fade:
                "anim_43" with d
            pause
            stop music fadeout 1
            f "Great."
            f "I have something else for you."
            scene 1478 with d
            elsa2 "Oh, how cute."
            elsa2 "You want to give me some cream."
            elsa2 "I'm so happy that you are not thinking only of yourself."
            f "Well, not quite…"
            f "I want to give this cream to your asshole."
            scene 1477 with d
            elsa2 "What!?"

    menu:

        "{color=#1BBB20} Start.":

            play music "music/aah.mp3"
            scene 1491 with fade:
                "anim_41" with d
            pause
            elsa2 "Ah-ah-ah."
            f "Doesn't it hurt?"
            elsa2 "Mmmmm...."
            stop music fadeout 1

    menu:

        "{color=#1BBB20} Watch.":

            play music "music/aah.mp3"
            scene 1491 with fade:
                "anim_42" with d
            pause
            stop music fadeout 1

    scene 1404 with d
    #s "{color=#f00}{b}Menu box can also be hidden by pressing middle mouse button.{/b}{/color}"
    jump part5_12
label part5_9:

    menu:

        "Go":

            jump part5_10


        "{color=#1BBB20} Toy play.":
            scene 1484 with fade:
                "anim_33" with d
            pause
            jump part5_9

        "{color=#1BBB20} Side.":

            scene 1485 with d
            play music "music/Breathing.ogg"

            scene black with fade:
                "anim_30" with d
            pause

            stop music fadeout 1

            jump part5_9

        "{color=#1BBB20} Cowgirl.":

            scene 1486 with d
            play music "music/Breathing.ogg"

            scene black with fade:
                "anim_31" with d
            pause

            stop music fadeout 1

            jump part5_9

        "{color=#1BBB20} Cowgirl behind." if part5_bonusanim2 == True:

            scene 1487 with d
            play music "music/Breathing.ogg"

            scene black with fade:
                "anim_32" with d
            pause

            stop music fadeout 1

            jump part5_9

        "{color=#1BBB20} Masturbate.":

            scene 1488 with d
            play music "music/Breathing.ogg"

            label anim_34_mid:



                scene black with fade:
                    "anim_34" with d
                pause

            stop music fadeout 1

            jump part5_9







label part5_10:

    $ d20roll_2 = renpy.random.choice(['Slut', 'Hooker', 'Bitch'])

    menu:

        "Return.":

            jump part5_9

        "{color=#1BBB20} Go":

            jump part5_11

        "{color=#1BBB20} Intimidate.":

            scene 1405 with d:

                "anim_36"
                pause 1.01
                "1405b"
            f "[d20roll_2]"
            scene 1404 with d

            jump part5_10

        "Slap.":

            scene 1404 with d:
                "anim_35"
                pause 1.01
                "1404b"
            play audio "music/shlepok.mp3"
            pause 0.3
            scene 1405d with d
            jump part5_10

        "Deepthroat.":

            scene 1489b with d
            play music "music/blowjob.mp3"

            scene black with fade:
                "anim_38" with d
            pause
            stop music fadeout 1

            jump part5_10

        "Deepthroat 2.":

            scene 1489 with d
            play music "music/blowjob.mp3"

            scene black with fade:
                "anim_37" with d
            pause

            stop music fadeout 1
            jump part5_10



label part5_11:

    menu:

        "Return.":

            jump part5_10

        "{color=#1BBB20} CumShot.":
            jump part5_12


        "Slap ass.":


            scene 1408 with d:
                "anim_39"
                pause 1.01
                "1408b"
            play audio "music/shlepok.mp3"
            pause 0.3
            scene 1408d with d
            pause
            jump part5_11

        "Dildo.":

            scene 1490 with d
            play music "music/aah.mp3"

            scene black with fade:
                "anim_40" with d
            pause

            stop music fadeout 1

            jump part5_11

        "Crem.":

            scene 1491 with d
            play music "music/aah.mp3"

            scene black with fade:
                "anim_41" with d
            pause

            stop music fadeout 1

            jump part5_11

        "Crem 2.":

            scene 1491b with d
            play music "music/aah.mp3"

            scene black with fade:
                "anim_42" with d
            pause

            stop music fadeout 1

            jump part5_11



label part5_12:

    menu:

        #"Return.":

            #jump part5_11

        #"Go.":

            #pause

        "{color=#1BBB20} Cum Face.":

            scene 1428 with fade:
                "1429" with d
                pause 0.8
                "1428" with d
                pause 0.8
                repeat
            pause
            scene 1426
            with flash
            scene 1426 with flash
            pause 0.3
            scene 1426 with flash
            scene 1426 with flash
            pause 2.0
            scene 1427 with d
            pause
            #jump part5_12

        "Cum Belly.":

            scene 1424 with fade:
                "1425" with d
                pause 0.8
                "1424" with d
                pause 0.8
                repeat
            pause
            scene 1422
            with flash
            scene 1422 with flash
            pause 0.3
            scene 1422 with flash
            scene 1422 with flash
            pause 2.0
            scene 1423 with d
            pause
            #jump part5_12

        "Cum Back.":

            scene 1420 with fade:
                "1421" with d
                pause 0.8
                "1420" with d
                pause 0.8
                repeat
            pause
            scene 1418
            with flash
            scene 1418 with flash
            pause 0.3
            scene 1418 with flash
            scene 1418 with flash
            pause 2.0
            scene 1419 with d
            pause
            #jump part5_12

        "Cum Ass.":

            scene 1432 with fade:
                "1433" with d
                pause 0.8
                "1432" with d
                pause 0.8
                repeat
            pause
            scene 1430
            with flash
            scene 1430 with flash
            pause 0.3
            scene 1430 with flash
            scene 1430 with flash
            pause 2.0
            scene 1431 with d
            pause
            #jump part5_12









    scene 1434 with d
    elsa2 "Never thought you could use whipped cream like this."
    elsa2 "I think there is still cream inside of me."
    elsa2 "I feel I've deserved some incentive."
    f "I'm going to feed you now, Frank."
    elsa2 "Ha-ha. Just make it not like the last time."
    scene 1441 with d
    elsa2 "Hmm. We sure think the same."
    scene 1440 with d
    f "Remember you wanted some cream?"
    scene 1438 with d
    elsa2 "Wow, here comes the treat."
    play sound "music/cellphone_ring.ogg"
    scene 1443 with d
    pause
    scene 1444 with d
    show screen topleftmenu4
    f "Hey, Chelsey."
    scene 1455 with d
    chelsey "Where are you, Mr. Frank?"
    scene 1444 with d
    f "In the city."
    chelsey "When are you coming back?"
    f "Evening, probably."
    scene 1455 with d
    chelsey "What a pity, I wanted to watch a movie with you."
    scene 1444 with d
    menu:

        "{color=#1BBB20} Permit. {color=#FF0000} (+1 Chelsey's Point)":

            $ chelsey_part5_question = True
            f "You can watch it without me."
            f "You have my permission."
            pause
            show heart with moveinbottom:
                yalign .25 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ chelsey_score = change_stat(chelsey_score,1)
            hide heart
            scene 1455 with d
            chelsey "Thanks."

        "{color=#E5170A} Forbid. {color=#FF0000} (-1 Chelsey's Point)":

            f "You shouldn't be in my room when I'm not home."
            show heart with moveintop:
                yalign .70 subpixel True
                xalign .0125 subpixel True
            pause 0.5
            $ chelsey_score = change_stat(chelsey_score,-1)
            hide heart


    chelsey "What are you doing now?"
    scene 1438 with d
    f "..."
    f "..."
    f "I'm feeding a stray cat."
    scene 1455 with d
    chelsey "Oh, how cute."
    chelsey "I had no idea you loved animals."
    chelsey "Could you snap a photo for me?"
    scene 1442 with d
    pause
    scene 1439 with d
    pause
    scene 1445 with d
    pause
    scene 1445b with d
    pause
    elsa2 "Meow, meow, meow."
    scene 1455 with d
    chelsey "Oh. I can hear it purring."
    chelsey "It loves what you are doing."
    f "No doubt."
    chelsey "I'm going to tell Mrs. Thompson what a saint you are."
    f "Thank you, Chelsey. "
    f "See you later."
    hide screen topleftmenu4
    scene 1446 with d
    elsa2 "Who was it? Ha-ha."
    elsa2 "Another favorite whore of mine."
    elsa2 "Should I start getting jealous?"
    f "This is my fosterling. Chelsey."
    scene 1454 with d
    chelsey "I'm so unlucky."
    chelsey "And what am I supposed to do with these panties now."

    menu:

        "{color=#1BBB20} Secret scene.":

            scene 1492 with d
            pause
            scene 1480 with d
            elsa2 "Look, Frank. I got a dick too. Ha-ha."
            scene 1482 with d
            elsa2 "This is how you do it without a girl?"
            scene 1481 with d
            pause
            scene 1482 with d
            pause
            scene 1481 with d
            pause
            scene 1482 with d
            pause



    scene black with d
    pause
    play music "music/nightmare.mp3"
    scene 1397 with d
    angel "So, you had fun with her?"
    f "None of your business."
    angel "You occupied my room."
    angel "I have been waiting for you for an hour."
    scene 1398 with d
    angel "The keys are in ignition."
    angel "You can take the car and drive off."
    f "I think Elsa needs her own separate room."
    angel "All rooms are occupied."
    angel "Next time you will do her on this couch. A-ha-ha."
    scene 1399 with d
    angel "Alright, let's make it quick, ok?"
    f "What are you talking about?"
    angel "You already had sex, which means you will beat me up."
    angel "Our former boss was like this. "
    f " It's not in my code to hit a woman. Even a woman like you."
    angel "Then who will punish the whores?"
    angel "They will let loose and start stealing drugs and cash."
    angel "Our profits will tank."
    f "I have a different view."
    f "You are getting the very last warning."
    angel "There will be time when I'll sit on your face. Ha-ha-ha."
    f "What was it?"
    angel "Later..."
    scene 1399b with d
    angel "I was right. He doesn't belong here."
    angel "I will have to show the whores who's the boss."
    stop music fadeout 1

    scene black with d
    pause
    scene 1435 with d
    angel "You had fun?"
    elsa2 "Frank and I went crazy..."
    angel "Wean me off these nuances."
    angel "What is THIS!? "
    angel "You stained my favorite dress."
    elsa2 "Sorry. it was Frank who dropped some whipped cream on it."
    angel "I told you to be more careful."
    angel "I guess you don't give a shit about what I say."
    elsa2 "Of course I do."
    angel "Here come the real punishment."
    scene 1436 with d
    elsa2 "But I haven't done anything."
    elsa2 "Please, don't do it."
    scene 1437 with d
    play audio "music/shlepok.mp3"
    pause

    scene black with d
    pause
    play music "music/roadtrip.mp3"
    scene 1400 with d
    f "He-he. Now I got myself a ride."
    scene 1401 with d
    f "It's been a while since I was behind a wheel."
    f "Hope I won't run anyone over."
    f "Guess I'll go to Marty's."
    stop music fadeout 1
    scene black with d
    pause
    scene 1402 with d
    play music "music/city1.mp3"
    f "Hey there, old friend."
    f "Drinking high-end alcohol now?"
    scene 1403 with d
    marty "Elsa is making more money now."
    scene 1402 with d
    f "Why you left the house?"
    scene 1403 with d
    marty "That tatted whore showed me the door."
    f "Yeah, she can do that. Ha-ha."
    f "I can get you back in, if you want."
    marty "Nah, don't bother."
    marty "She promised to give me booze money."
    marty "I'm fine with this deal. "
    marty "Plus, I'm accustomed to living on the streets."
    marty "All my friends are here. Ha-ah."
    marty "Back in the house I had no drinking buddies."
    marty "Everyone is into Mirage."
    scene 1402 with d
    f "Today Angel almost set me up."
    marty "Have you punished her for it?"
    f "Well, I gave her a talk."
    marty "A-ha-ha."
    marty "She understands raw power rather than words."
    marty "Today she sets you up, the next day she shoots you in the back."
    marty "Drive her ass to me."
    marty "I can re-educate her."
    f "I hope you won't beat her, right?"
    marty "She hasn't worked the streets in a long time by the looks of it."
    marty "I shall remind you how it is around here."
    f "And then we see how she behaves."
    marty "Bottoms up?"
    f "No, I'm driving."
    marty "Ah, come on. Don't be a pussy."
    marty "Haven't been driving under the influence?"
    stop music fadeout 1
    menu:

        "{color=#1BBB20} Drink some booze. {color=#FF0000} (+1 Bianca's Point)":

            $ bianca_part5_question = True
            scene 1402b with d
            f " Persuasive. "

        "Say no.":
            pause


    scene 1412 with d
    pause
    scene 1413 with d
    pause
    scene 1414 with d
    pause
    stop music fadeout 1


    scene black with d
    pause
    play music "music/police_siren.mp3"
    scene 1447 with d
    f "Cops. Again."
    scene 1448 with d
    show screen topleftmenu4
    f "Are they following me or something?"
    scene 1449 with d
    stop music fadeout 1
    f "Good evening, officer."
    play music "music/city1.mp3"
    bianca "Hi, Frank."
    bianca "Where you got this car from?"
    f "My friend gave it to me for some time."
    bianca "This is how you call grand theft auto?"
    f "I have no clue what you are talking about."
    bianca "Give me a second. I will run it though our database."
    scene black with d
    pause
    scene 1449 with d
    bianca "Weird, but this car is not listed as hijacked."
    f "I never lie, ma'am."
    bianca "What is wrong with you?"
    bianca "Are you drunk?"

    if bianca_part5_question == True:

        f "I had a drink or two with a friend."
        bianca "You are under arrest for DUI."
        bianca "This means a night in Police Department."
        f "*I knew this was a bad idea."
        f "..."
        f "..."
        f "You want to spend a night with me, am I getting this right?"
        f "Put me in cuffs and ride me till the sunrise."
        f "Your apparel makes me so horny."
        f "Where is your baton?"
        bianca "Horny prick."
        bianca "I don't care about you in the slightest."
        bianca "It's your lucky day, since I'm on duty alone."
        bianca "I won't be able to tolerate this drunken nonsense all night long."
        f "*Ha-ha. It worked."
        show heart with moveinbottom:
            yalign .25 subpixel True
            xalign .0125 subpixel True
        pause 0.5
        $ bianca_score = change_stat(bianca_score,1)
        hide heart

    else:

        f "No, I wasn't."

    bianca "Why you missed your follow-up appointment?"
    f "I got a job and this totally slipped my mind."
    bianca "Erin told me about your new job."
    f "*They are talking about me."
    f "*Another thing points at the fact that they care about me."
    bianca "I was this close from listing you as a wanted man."
    bianca "I will keep you here no longer."
    bianca "Drive safe."
    f "Much appreciated."
    f "See you later, baby."
    bianca "Shut the hell up."
    bianca "I can easily change my mind."
    f "That's what I'm hoping for."
    hide screen topleftmenu4
    stop music fadeout 1


    scene black with d
    pause
    scene 1450 with d
    play music "music/Forest.mp3"
    f "You have been waiting for me, Chelsey?"
    chelsey "You purchased a car, Mr. Frank?"
    f "No, it was given to me for a couple of rides."
    chelsey "I want to learn how to drive so bad."
    f "Someday I will teach you."
    scene 1451 with d
    chelsey "Did you bring a photo of that kitty?"
    chelsey "I want to show May that you also love animals."
    chelsey "You can be good friends with her."
    chelsey "You have such a big heart, Mr.Frank."
    f "I am packing a lot of big stuff on me. A-ha-ha."
    chelsey "What are you talking about?"
    f "Kitty was too shy."
    f "It feel asleep as soon as I fed it."
    f "I didn't want to wake it up."
    chelsey " What a pity."
    menu:

        "{color=#1BBB20} Ask about May.":

            f "What May likes to do? Any hobbies?"

            if chelsey_part5_question == True:

                chelsey "She is really into video games."
                chelsey "We occasionally play together."
                f "Hmm. Nothing special."
                chelsey "She also loves running with Rex in the morning."
                f "*Running is good."
                f "*Means she has stamina to spare."
                f "*You can do a girl like that all night long."
                chelsey "Also..."
                f "Spill it out..."
                chelsey "Once, late at night."
                chelsey "I had trouble falling asleep and went to get some juice."
                chelsey "I was passing the gym."
                f "You got a gym?"
                chelsey "Yes, we do."
                chelsey "I heard someone exercising there."
                chelsey "I took a sneak peek."
                chelsey "May was inside."
                chelsey "She was...."
                f "What? Hardcore weight-lifting? Ha-ha."
                chelsey "You won't be laughing, if I tell you."
                chelsey "She knows some martial arts."
                chelsey "She practiced moves that I've only seen on TV."
                f "*Now this is getting interesting."
                f "*A rape victim knows how to fight."
                f " *I have to take a look at what she does at night."
            else:

                chelsey "I'm not allowed in your room..."
                chelsey "That made me sad."
                chelsey "You should ask her."

    f "Let's get inside, it's getting dark."

    stop music fadeout 1
    scene black with d
    s "Later."
    pause
    play music "music/deadly-roulette.mp3"
    scene 1452 with d
    pause
    scene 1453 with d
    s "Shhhhhhhhhhh"
    pause
    stop music fadeout 1
    jump part6



    return

label vbar1_1:
    $ renpy.block_rollback()
    call screen vbar1


screen vbar1():

    $ clickable == True

    if clean_bar_value < 0.5:

        add "1350b"
    elif clean_bar_value > 0.5 and clean_bar_value <= 1:
        add "1350"
    elif clean_bar_value > 1:
        add "1350d"

    vbar top_bar Frame("images/pool_minigame/top_bar.png", gui.vbar_borders, tile=gui.bar_tile) bottom_bar Frame("images/pool_minigame/top_bar1_2.png", gui.vbar_borders, tile=gui.bar_tile) range clean_bar_max value clean_bar_value xsize barysize ysize barxsize xpos 1880 ypos 40

    if clean_bar_value >=0.01:
        timer 0.15 action SetVariable("clean_bar_value", clean_bar_value - 0.05) repeat True

    imagebutton:



        xpos 1740
        ypos 760
        focus_mask True
        idle "images/pool_minigame/HUD/hit.png"
        hover "images/pool_minigame/HUD/hit_hover.png"

        if clickable == True:
            action SetVariable("clean_bar_value", clean_bar_value + 0.10)
    #if clickable == True:
        #action SetVariable("clean_bar_value", clean_bar_value + 0.30)

        if clickable == True and clean_bar_value > 1.35:

            action Jump("part5_8")

    #text "10/" xpos 1750 ypos 870
    #text "[clean_bar_value]" xpos 1810 ypos 870

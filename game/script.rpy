define n = Character("Nicolas", who_color="#ffffff")
define b = Character("Boss", who_color="#ffffff")

image blackness = "#000000"
image cutscene_intro = Movie(size=(1920,1080),channel="movie", play="cutscenes/promo.webm", loop= False, image="images/promo.jpg")
image cutscene_01 = Movie(size=(1920,1080),channel="movie", play="cutscenes/run.webm", loop= True)
image cutscene_02 = Movie(size=(1920,1080),channel="movie", play="cutscenes/corner.webm", loop= False, image= "images/corner.jpg")
image cutscene_03 = Movie(size=(1920,1080),channel="movie", play="cutscenes/die.webm", loop= False, image = "images/die.jpg")
image cutscene_04 = Movie(size=(1920,1080),channel="movie", play="cutscenes/fight.webm", loop= False, image = "images/fight.jpg")
image cutscene_05 = Movie(size=(1920,1080),channel="movie", play="cutscenes/lemtter.webm", loop= True)
image cutscene_06 = Movie(size=(1920,1080),channel="movie", play="cutscenes/breakout.webm", loop= True)
image cutscene_07 = Movie(size=(1920,1080),channel="movie", play="cutscenes/died.webm", loop= False, image= "images/died.png")
image cutscene_08 = Movie(size=(1920,1080),channel="movie", play="cutscenes/Survive.webm", loop= False, image = "images/survived.png")
image cutscene_09 = Movie(size=(1920,1080),channel="movie", play="cutscenes/stab.webm", loop= True)
image cutscene_10 = Movie(size=(1920,1080),channel="movie", play="cutscenes/lips.webm", loop= True)
image cutscene_11 = Movie(size=(1920,1080),channel="movie", play="cutscenes/somegirl.webm", loop= True)


label start:
    stop music fadeout 2
    play sound "audio/promo.mp3" fadein 1.0 fadeout 2.0
    show cutscene_intro
    pause 7.0
    scene bg_image_01 with dissolve
    play music "audio/bg_music.ogg" fadein 2.0
    "Your name is Nicolas. You have just started a new job as a security
    guard on the night shift at a local storage unit. "
    "Nothing interesting is stored there, mainly random bits not worth all that much. 
    It was supposed to be an easy shift, until strange things began to happen."

    scene bg_image_02 with dissolve
    play sound "<from 0 to 7.0>audio/Start_Bus.mp3" fadein 1.0 noloop 
    "Just your luck that the bus was running late on the night of your first shift."
    
    scene bg_image_03 with dissolve
    "The time is 21:56, not as early as you would have liked to have arrived."
    "You approach the staff entrance to the side of the building."

    scene bg_image_04 with dissolve
    "Your new boss is standing there, looking quite worried."
    "Would you like to start your shift?"
    n "Sure sir"
    jump intro_node
    return

label intro_node:
    scene blackness with dissolve
    "Ten minutes was all the time you needed for the training."
    
    scene bg_image_05 with dissolve
    "It was a simple job on paper."
    "Patrol the building."
    "Keep an eye on the locks & fire escapes."

    show cutscene_05
    "On his way out, the boss places a handwritten note in your hand."
    b "Please Nicolas, make sure you read this when I've left."

    scene bg_image_06 with dissolve
    play sound "audio/Intro_Door_Close.mp3"
    "He exits the door, locking it and making his way to his car."
    jump select_letter

menu select_letter:
    "Do you want to read the note?"
    "Yes":
        jump path_1
    "No":
        jump path_2
    

label path_1:
    play sound "audio/Path_1_Paper_Open.mp3"
    scene bg_image_07 with dissolve
    "You peel the note open."
    n "Why is there blood on it?"
    "The writing is barely legible, but you persevere."
    "Your face goes pale, your hairs stick up on your arms."

    scene bg_image_08 with dissolve
    "The note reads..."
    jump select_path_1
    return
    

menu select_path_1:
    "What would you like to do?"
    "Run to the door and try to get out.":
        jump path_1_a
    "Hide underneath the desk.":
        jump path_1_b
    "Make your way into the main storage halls.":
        jump path_1_c

label path_1_a:
    show cutscene_01  
    "You sprint to the exit."
    scene bg_image_09 with dissolve
    "While fumbling around trying to open the door,"
    play sound "audio/Path_1A_Monster.mp3" volume 3.0
    "You hear a guttural moan from down the hallway."
    play sound "audio/Path_1A_door.mp3"
    n "Why won't this damn door open?!"
    show cutscene_02
    play sound "audio/Intro_Footstep.mp3"
    "You begin to hear footsteps from around the corner."
    "Growing louder with each stride."
    "Then you remember, the boss locked the door..."
    "With seconds until whatever is approaching you appears, you must choose!"
    jump select_1_a
    return

menu select_1_a:
    "Smash through the glass.":
        jump path_1_a_1
    "Run back into the office and hide.":       
        jump path_1_a_2

label path_1_a_1:
    scene bg_image_10 with dissolve
    play sound "audio/Path_1A1_Glass.mp3"
    "You grab the fire extinguisher nearby and smash through the glass."

    scene bg_image_11 with dissolve
    "While crawling through, you turn around to see a pale gaunt girl peeking around the corner at you."

    show cutscene_03 
    play sound "audio/Path_1A1_Scream.mp3"
    "She lets out a bloodcurdling scream and charges."
    "You narrowly avoid her razor sharp nails and manage to crawl out."

    scene bg_image_12 with dissolve
    "Sprinting towards the main road, you flag down the bus."

    scene bg_image_13 with dissolve
    "Covered in sweat, you board and begin hyperventilating in front of the driver."

    scene bg_image_14 with dissolve
    play sound "audio/Path_1A1_Bus.mp3"
    n "DRIVE! SHE'S BEHIND ME!"
    "In a panic the driver puts his foot down, throwing you to the floor."

    scene bg_image_15 with dissolve
    "She stops chasing you and retreats back to the building."
    jump win_screen
    return

label path_1_a_2:
    scene bg_image_16 with dissolve
    play sound "audio/Path_1A2_Table.mp3"
    "You dart through the door back into the office."
    "Quickly diving under the desk, you knock over the desk chair."
    "You hear the girl panting in the doorway."

    show cutscene_04  
    play sound "audio/Path_2A1_Bone.mp3"
    "She begins pacing around the room, searching for you."
    "Suddenly the girl sends the desk flying, revealing you curled up on the floor."
    "She attacks you..."
    play sound "audio/Path_1A2_Blood.mp3"
    "Bleeding out, the girl stands over you licking her lips."

    scene missing with dissolve
    "Your body was never found."
    jump lose_screen
    return

label path_1_b:
    scene bg_image_16 with dissolve
    play sound "audio/Path_1A2_Table.mp3"
    "You dart underneath the desk out of sheer panic."
    "Could this be a cruel prank the boss is playing on you?"

    show cutscene_02
    play sound "audio/Path_1A_Monster.mp3" volume 3.0
    "Then you hear a guttural moan from down the hallway."
    play sound "audio/Intro_Footstep.mp3"
    "You begin to hear footsteps coming from the hall."
    # play sound "audio/Path_2A2_ScaryBG.mp3"
    "Growing louder with each stride, until you sense the presence of someone in the room with you."
    "Frantically scanning the area, you look for anything to use as protection."

    scene bg_image_22 with dissolve
    "You notice a letter opener, next to you. What a coincidence!"
    "Quickly, you have to do something!"
    jump select_1_b
    return

menu select_1_b:
    "Stay hidden, like the coward you are.":  
        jump path_1_b_1
    "Attack them with the letter opener.":
        jump path_1_b_2

label path_1_b_1:
    show cutscene_06 
    "You hide in the vent."
    "Suddenly the girl notices you curled up in the vent."
    show cutscene_04
    play sound "audio/Path_1A2_Blood.mp3"
    "She attacks you, severing your jugular vein."
    "Bleeding out, the girl stands over you licking her lips."

    scene missing with dissolve
    "Your body was never found."
    jump lose_screen
    return

label path_1_b_2:
    scene bg_image_22 with dissolve
    play sound "audio/Path_1A2_Table.mp3"
    "You grab the letter opener and flip the desk as you stand up."

    show cutscene_09
    play sound "audio/Path_1B2_Knife.mp3"
    "In a blind rage you lunge at the girl, plunging your knife into her belly."
    "She lets out a blood curdling scream which echoes throughout the building."

    scene bg_image_18 with dissolve
    play sound "audio/Path_1B2_Police.mp3"
    "You call the emergency services with the work phone."

    scene idcard with dissolve
    "She is pronounced dead at the scene."

    scene bg_image_19 with dissolve
    "After the police had finished their inspection of the building, they found evidence suggesting the girl was the boss's daughter."
    "He is eventually caught days later and arrested."
    "The nightmare is over!"
    jump win_screen
    return

label path_1_c:
    scene bg_image_20
    play sound "audio/Path_2B2_Tied.mp3" volume 3.0 
    "You make your way into the main halls, confused about the nature of the note."

    scene bg_image_08
    "Could this be a cruel prank the boss is playing on you?"

    show cutscene_02
    play sound "audio/Path_1A_Monster.mp3" volume 3.0
    "Then you hear a guttural moan from down the hallway."
    "You notice a pale gaunt girl peeking staring at you from the end of the hall."
    play sound "audio/Intro_Footstep.mp3"
    "You begin to approach her, she must be a customer that accidentally got locked in."

    show cutscene_03
    play sound "audio/Path_2A1_Scream.mp3"
    "Her behaviour is erratic, moaning constantly like she is in agony."
    "She charges at you!"

    
    "Quickly, you have to do something!"
    jump select_1_c
    return

menu select_1_c:
    "Run into the lock up to your left and trap her in.":
        jump path_1_c_1
    "Charge her, you are not scared!":   
        jump path_1_c_2

label path_1_c_1:
    show cutscene_06
    play sound "audio/Path_1A2_Table.mp3"
    "You dart into the vent on your left, it's full of old car parts."

    scene bg_image_23 with dissolve  
    "She slides around the corner and comes at you!"
    play sound "audio/Path_1C1_Hitting.mp3"

    show cutscene_09
    "You hit her in the belly with a knife you found."

    show cutscene_01
    "While she is dazed, you run for it."
    play sound "audio/Path_1B2_Police.mp3"

    scene bg_image_18 with dissolve
    "You call the emergency services with your mobile phone."

    scene bg_image_25 with dissolve
    "When they arrive, it takes 3 police officers to subdue her and put her in a secure van going to the police station."

    scene bg_image_19
    "After they had finished their inspection of the building, they found evidence suggesting the girl was the boss's daughter."
    "He is eventually caught days later and arrested."
    "The nightmare is over!"
    jump win_screen
    return

label path_1_c_2:
    scene bg_image_24 with dissolve
    play sound "audio/Path_1A1_Glass.mp3"
    "She charges at you, colliding with you and both of you are knocked to the floor."
    "She quickly picks herself up."

    show cutscene_04
    "With her razor sharp nails, she starts wildly attacking you."
    "Her strength is overwhelming for such a small thing."
    play sound "audio/Path_1A2_Blood.mp3"
    "One last violent swipe hits your neck, severing your jugular vein."
    "Bleeding out, the girl stands over you licking her lips."

    scene missing with dissolve
    "Your body was never found."
    jump lose_screen
    return

label path_2:
    scene bg_image_28 with dissolve
    play sound "audio/Path_2_Paper_Dustbin.mp3"
    "You throw the note in the bin, it couldn't have been that important."

    show cutscene_02
    play sound "audio/Path_2_Wood_Sound.mp3"
    "You sit there for a while and notice strange noises are coming from the hallway."
    "With everything going on in your life right now, you ignore them and take the time to relax."

    scene bg_image_29 with dissolve
    "After all, you chose this job because you can basically just sit down the entire shift and play video games."
    "You decide it is probably best to make a move, since you are supposed to be working."
    jump select_path_2
    return

menu select_path_2:
    "What would you like to do?"
    "Go and do your first patrol of the evening.":
        jump path_2_a
    "Boil the kettle, the boss has left some tea bags for you.":
        jump path_2_b

label path_2_a:
    scene bg_image_20 with dissolve
    play sound "audio/Path_2_Wood_Sound.mp3"
    "You grab your torch and make your way into the hallway."
    "The strange noises begin again."

    scene bg_image_07 with dissolve
    "You start getting freaked out, the building has a strange vibe to it at night."

    scene bg_image_30 with dissolve
    "Turning left, right then left again you notice one of the doors is slightly open."
    "A glowing red light can be seen in the crack of the door."
    jump select_2_a
    return

menu select_2_a:
    "What would you like to do?"
    "Lock it back up.":
        jump path_2_a_1
    "Open the door and investigate.":
        jump path_2_a_2

label path_2_a_1:
    scene bg_image_09 with dissolve
    "You grab the door handle."

    show cutscene_03
    play sound "audio/Path_1A2_Blood.mp3"
    "A hand with razor sharp nails grabs your arm, gashing you multiple times."
    "Lurching backwards, you kick the hand while trying to break free."

    scene bg_image_32 with dissolve
    play sound "audio/Path_2A1_Bone.mp3"
    "You hear the bones break in the legs."

    scene bg_image_20 with dissolve
    play sound "audio/Path_2A1_Scream.mp3"
    "A loud scream echoes through the hallway."
    "You manage to shut it while whatever is in there is dazed."

    scene bg_image_18 with dissolve
    play sound "audio/Path_1B2_Police.mp3"
    "You call the emergency services with your mobile phone."

    scene bg_image_19 with dissolve
    "When they arrive they are horrified to see that it was a pale gaunt girl."

    scene bg_image_21 with dissolve
    "It takes 3 police officers to subdue her and put her in a secure van going to the police station."

    scene idcardrize with dissolve
    "After they had finished their inspection of the building, they found evidence suggesting the girl was the boss's daughter."
    "He is eventually caught days later and arrested."
    "The nightmare is over!"
    jump win_screen
    return

label path_2_a_2:
    scene bg_image_09 with dissolve
    play sound "audio/Path_2A2_ScaryBG.mp3"
    "You open the door, the smell overwhelms you."

    scene bg_image_33 with dissolve
    "Blood is all over the walls and floor."
    "Body parts are strewn across the room, mostly half chewed."

    scene bg_image_34 with dissolve
    "You notice a pale gaunt girl crouched in the corner."

    show cutscene_04
    "With her razor sharp nails, she charges and starts wildly attacking you."
    play sound "audio/Path_1A2_Blood.mp3"
    "One violent swipe hits your neck, severing your jugular vein."
    "Bleeding out, the girl stands over you licking her lips."

    scene missing with dissolve
    "Your body was never found."
    jump lose_screen
    return

label path_2_b:
    scene bg_image_26 with dissolve
    play sound "audio/Path_2B_Kettle.mp3"
    "You boil the kettle and prepare your brew."
    "No sugar, you are already sweet enough."

    scene bg_image_35 with dissolve
    "You finish making the drink and sit down at your desk."

    scene bg_image_07 with dissolve
    play sound "audio/Path_2A2_ScaryBG.mp3"
    "Those strange noises from before start again."
    "You're beginning to get freaked out."
    jump select_2_b
    return

menu select_2_b:
    "What would you like to do?"
    "Investigate the noises coming from the hallway.":
        jump path_2_b_1
    "Stay and drink your brew, must be nothing anyway.":       
        jump path_2_b_2

label path_2_b_1:
    scene bg_image_20 with dissolve
    "You leave the brew and investigate the hallway."

    show cutscene_03
    play sound "audio/Path_1A1_Scream.mp3"
    "After turning the corner, you see a pale gaunt girl."
    "She lets out a bloodcurdling scream and charges."
    "You narrowly avoid her razor sharp nails."
    scene bg_image_10 with dissolve
    play sound "audio/Path_1A1_Glass.mp3"
    "While she is falling over, she smashes through the glass on the exit."
    "You throw her to the side and dart through the gap."
    scene bg_image_12 with dissolve
    "Sprinting towards the main road, you flag down the bus."

    scene bg_image_13 with dissolve
    "Covered in sweat, you board and begin hyperventilating in front of the driver."

    scene bg_image_14 with dissolve
    play sound "audio/Path_1A1_Bus.mp3"
    n "DRIVE! SHE'S BEHIND ME!"

    scene bg_image_15 with dissolve
    "In a panic the driver puts his foot down, throwing you to the floor."
    "She stops chasing you and retreats back to the building."
    jump win_screen
    return

label path_2_b_2:
    scene bg_image_35 with dissolve
    play sound "audio/Path_2B2_Sip.mp3"
    "You take a sip of your brew and begin to feel sick."

    scene blackness with dissolve
    play sound "audio/Path_2B2_Tied.mp3" volume 3.0
    "Moments later you black out."
    "You wake up some time later, it is now pitch black in the room."

    scene bg_image_36 with dissolve
    "You realise you are tied to the chair."

    show cutscene_10 
    "A pale gaunt girl stands in front of you licking her lips."
    n "Who are you? WHAT WAS IN THAT DRINK!?"

    show cutscene_11
    play sound "audio/Path_1A2_Blood.mp3"
    "With her razor sharp nails, she swipes your neck, severing your jugular vein."
    "You're bleeding out, all you can see is her beginning to eat away at your forearm."

    scene missing with dissolve
    "Your body was never found."
    jump lose_screen
    return


label win_screen:
    show cutscene_08
    pause 5
    show cutscene_08
    pause 5
    show cutscene_08
    pause 5
    return

label lose_screen:
    show cutscene_07
    pause 5
    show cutscene_07
    pause 5
    show cutscene_07
    pause 5
    return




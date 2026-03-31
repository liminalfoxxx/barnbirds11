default dove_soda_received = False
default dove_soda_thanked = False
default dove_asked_who = False
default dove_asked_doing = False
default dove_asked_kingsnakes = False
default dove_asked_blight = False
default dove_asked_soda = False
default dove_asked_chorus = False
default dove_starlight = False

default penguin_asked_here = False
default penguin_asked_blight = False
default penguin_asked_dying = False
default penguin_asked_dead = False
default penguin_asked_her = False
default penguin_asked_him = False
default penguin_asked_infected = False
default penguin_asked_toucan = False

default scarlet_still_alive = False
default scarlet_asked_dead = False
default scarlet_asked_aware = False
default scarlet_asked_blight = False
default scarlet_asked_survive = False

# Crow conversation flags
default crow_asked_who = False
default crow_asked_bird = False
default crow_asked_blight = False
default crow_asked_blushwood = False
default crow_asked_glamor = False
default crow_asked_kingsnakes = False

# Toucan conversation flags
default toucan_first = False
default toucan_asked_who = False
default toucan_asked_dying = False
default toucan_asked_scarlet = False
default toucan_asked_hummingbird = False
default toucan_asked_kingsnake = False
default toucan_asked_blight = False

# --- D O V E ---

label talk_dove_blushwood:
    $ quick_menu = False
    $ can_travel = False

    if dove_soda_received and not dove_soda_thanked:
        d "You bought this for me? OHMYGOSH, thank you for the apricot soda!! You're the sweetest!! (;w;)!!!"
        d "..."
        d "I feel her energy radiating all around me, everywhere, we are all starlight in motion."
        $ dove_soda_thanked = True
    else:
        d "Good evening, sister. Tread carefully, there is a terrible curse beyond these gates."
        $ dove_starlight = True

    label .dove_menu:
    menu:
        "Why do you like orange soda so much?" if dove_soda_received and not dove_asked_soda:
            d "It's made with oranges, and oranges carry the sun's blessing (^_^)☀︎"
            d "Exactly the kind of pick me up I need after spellcasting all day."
            $ dove_asked_soda = True
            jump .dove_menu

        "Who are you?" if not dove_asked_who:
            d "I am a ☀︎Life Cleric☀︎ Rejoice, sister, for the Moon's light is also His love."
            $ dove_asked_who = True
            jump .dove_menu

        "What are you doing?" if not dove_asked_doing:
            d "I am casting a spell to protect this forest from the Blight. It's too late for the Orchard, I fear."
            d "But at least I can try to keep it from going beyond this point. I don't enjoy quarantine tactics, but sometimes it's our only option."
            d "The sun is setting for today. I will be resting soon... then back to casting after the Dawn Chorus."
            $ dove_asked_doing = True
            jump .dove_menu

        "What is the Dawn Chorus?" if dove_asked_doing and not dove_asked_chorus:
            d "You're unfamiliar with the Dawn Chorus? I suppose it is considered a primal tradition, and likely not one practiced by Owls."
            d "But I can't imagine starting the day without singing to the sun."
            d "It's a song that is not mine alone. It is the sound air makes when God returns, I simply lend it my voice."
            d "We map out the world before the first light spills over the edge of everything."
            d "It is our way of honoring the Sun ☀︎"
            d "Between us... I think the Chorus keeps the Blight from finding a home in me."
            d "When you name the morning out loud, the Void has less room to argue."
            $ dove_asked_chorus = True
            jump .dove_menu

        "I'm here to investigate the Blight" if not dove_asked_kingsnakes:
            d "Oh, yes, you must be the Cleric. The Kingsnakes did tell me to expect you."
            d "Death always comes after Life (^_^)☀︎ Here's a key to the Orchard gates."
            $ inventory.add_item(item_db["sector_key"])
            $ dove_asked_kingsnakes = True
            jump .dove_menu

        "Ask about Blight" if not dove_asked_blight:
            d "From what I've seen, it appears to be some sort of Void magic..."
            d "I'm afraid I don't know much about it, even though I've been here casting my spell for 11 days now."
            d "I suppose that's why the Kingsnakes hired an expert on all things deadly, such as yourself (^_^)"

            menu:
                "You've been casting a spell for 11 days?":
                    d "Yes, and I've never felt better ☀︎"
                    jump .dove_menu
                "What do you mean 'expert on all things deadly'??":
                    d "..."
                    d "I know the nature of Humans. Please, don't be mad."
                    $ dove_asked_blight = True
                    jump .dove_menu

        "Who do you mean, 'Her'?" if dove_starlight = True
            d "Oh! Forgive me, I think spending two weeks out here has made me comfortable in my solitude."
            d "Though you're a Cleric, too, so maybe you'll understand."
            d "Most members of the Church refer to the Sun in a masculine sense. And it's true that scripture says the same thing."
            d "But in my own personal faith... the Sun is a woman to me. It just feels right."
        "(exit conversation)":
            if dove_moved_to_sanctum:
                d "I'll be heading to the Inner Sanctum in Sundapple Square soon. I hope to see you there, sister."
            else:
                d "I noticed a spirit lurking around here earlier. Maybe it knows something about the Blight?"
                d "As a Death Cleric, you should be well equipped for speaking with ghosts."
                d "Best of luck, sister."
            $ can_travel = True
            jump overworld_loop

            

# --- THE CIDER MILL INTERIOR ---

label talk_penguin:
    pen "If you're here to kill me, go ahead. Gun's empty."
    label .penguin_menu:
    menu:
        "What happened here?" if not penguin_asked_here:
            pen "I did my job. I killed an innocent woman for no good reason."
            pen "And then, society collapsed. We live in a new world now, one where money, time, and God all mean nothing."
            pen "Nothing. I killed her for absolutely nothing."
            $ penguin_asked_here = True
            jump .penguin_menu

        "Do you know anything about the Blight?" if not penguin_asked_blight:
            pen "It turns people into trees. At least... I think they're trees."
            pen "There's some around here. Dark, twisting branches with no leaves, and strange flickering colors. Reminds me of TV static."
            pen "You might find pieces of viscera on and around them. It's the only thing left of the person that they used to be. As far as I can tell."
            pen "..."
            pen "I guess it doesn't kill you. It convinces you to stay until you're a place no one visits anymore."
            pen "Came up here to try to get infected on purpose. I think it's working."
            $ penguin_asked_blight = True
            jump .penguin_menu

        "You tried to get infected by the Blight?" if penguin_asked_blight and not penguin_asked_infected:
            pen "Yeah. I deserve whatever's coming to me."
            pen "So I'm just sitting here, waiting to die."
            pen "Toucan might still be alive. Might even still have some booze. I left a key out by the cornfield. Take it... I don't need it anymore."
            $ penguin_asked_infected = True
            jump .penguin_menu

        "Who is Toucan?" if penguin_asked_infected and not penguin_asked_toucan:
            pen "An old associate. He runs the bar downstairs. Might ask you to play cards with him."
            pen "I think he likes to pretend that money still means something in this world."
            $ penguin_asked_toucan = True
            jump .penguin_menu

        "You're close to dying..." if not penguin_asked_dying:
            pen "Good. I owe the world at least that much."
            $ penguin_asked_dying = True
            jump .penguin_menu

        "Why do you think I'm here to kill you?" if penguin_asked_dying and not penguin_asked_dead:
            pen "That's usually how this goes..."
            $ penguin_asked_dead = True
            jump .penguin_menu

        "Who did you kill?" if penguin_asked_here and not penguin_asked_her:
            pen "Scarlet Tanager. Her bodyguard and I used to be besties, before I started killing for money."
            pen "I killed some people here, too... if they could still be called 'people'. They're trees."
            $ scarlet_still_alive = True
            $ penguin_asked_her = True
            jump .penguin_menu

        "(exit conversation)":
            $ can_travel = True
            jump overworld_loop

label heal_penguin:
    pen "..."
    pen "You shouldn't have wasted that on me."
    $ can_travel = True
    jump overworld_loop

# Vending machine
label vending_machine_mill:
    "RECREATIONAL CONSUMABLES UNIT SYS:FILTER"
    menu:
        "Insert 2 units: CIGARETTE":
            if inventory.has_money(2):
                $ inventory.money -= 2
                $ inventory.add_item(item_db["cigarette"])
                "A single cigarette dispenses from the tray."
            else:
                "INSUFFICIENT FUNDS."
        "Insert 5 units: CATNIP":
            if inventory.has_money(5):
                $ inventory.money -= 5
                $ inventory.add_item(item_db["catnip"])
                "A pre-rolled catnip joint dispenses from the tray."
            else:
                "INSUFFICIENT FUNDS."
        "LEAVE":
            jump overworld_loop
    jump overworld_loop

# --- OTHER BLUSHWOOD LABELS ---

label scarlet_gate:
    sca "Look at me. I survived the end of the world."
    label .scarlet_menu:
    menu:
        "What do you know about the Blight?" if not scarlet_asked_blight:
            sca "The world grew sick of maintaining the illusion. Everything’s breaking."
            $ scarlet_asked_blight = True
            jump .scarlet_menu

        "Are you aware that you're dead?" if not scarlet_asked_aware:
            sca "Probably. If that's what you need to call it."
            sca "The brand outlives the girl."
            $ scarlet_asked_aware = True
            jump .scarlet_menu

        "Did you know the man who killed you is still alive?" if scarlet_still_alive and not scarlet_asked_dead:
            sca "Of course he is. For men like him and women like me, survival is all we know how to do."
            $ scarlet_asked_dead = True
            jump .scarlet_menu

        "You didn't survive..." if scarlet_asked_dead and not scarlet_asked_survive:
            sca "..."
            sca "Didn't I, though? I'm a brand in a post-brand place. I'm the last of my kind."
            sca "That's right, we're living in a new world."
            sca "There is no more Hollywood, no more record labels, no more media industry. No television, no phones, no print. No more promised sky for stars to shine in."
            sca "..."
            sca "I've never felt more free in my life."
            $ scarlet_asked_survive = True
            jump .scarlet_menu

        "I read that you died in the newspaper. Look, it says right here":
            sca "..."
            sca "They'll print anything that people want to hear."
            sca "Same as it's always been."
            jump .scarlet_menu

        "(exit conversation)":
            jump overworld_loop


label talk_turkey:
    $ quick_menu = False
    $ can_travel = False
    
    turk "Attention all guests"
    turk "In observance of THE END TIMES, all facilities are currently closed."
    turk "We hope you have enjoyed your visit to the Blushwood Court :^)"
    
    $ quick_menu = True
    $ can_travel = True
    jump overworld_loop

label surge_turkey:
    turk "..."
    turk "HELLO OPERATOR, how may I be of service?"
    turk "..."
    $ can_travel = True
    jump overworld_loop

label enter_mill:
    $ current_room = "cider_mill_interior"
    $ current_target = None
    "The heavy oak door groans. You enter the dark interior of the Cider Mill."
    jump overworld_loop

label talk_cat:
    if not can_speak_with_animals:
        "The black cat sits perched on a candy pumpkin, watching you curiously."
        jump overworld_loop

    cat "Good evening, Cleric."
    cat "I see you've been making good use of your spellbook. Keep it up :3"
    label .cat_menu:
        menu:
            "Who are you?":
                cat "I'm a Familiar, here to guide you in magic :3"
                cat "I can teach you a spell, if you'd like! :3"
                jump .cat_menu

            "What do you know about the Blight?":
                cat "Oh, I cannot tell you that. I can only guide you in magic :3"
                jump .cat_menu

            "I'd like to learn a new spell":
                cat "What spell would you like to learn? :3"
                menu:
                    "Power Surge":
                        # TODO: teaching logic will go here
                        jump .cat_menu
                    "Death Sight":
                        # TODO: teaching logic will go here
                        jump .cat_menu

            "(pet the cat)":
                cat "purrr, purrrrr..."
                jump .cat_menu

            "(exit conversation)":
                cat "Don't forget that I love you forever, Human :3"
                jump overworld_loop

label talk_dog:
    if not can_speak_with_animals:
        "The dog barks playfully, wagging its tail."
        jump overworld_loop

    dog "Death Cleric have dead things? Cleric give dead things to me? :3"
    # TODO: if give bone
    dog "DEAD THINGS!!! YAYAYAYAYAYYY I LOVE YOU, CLERIC :3"

    label .dog_menu:
        dog "Arf arf! :3"
        menu:
            "Who are you?":
                dog "I'm doggy. And doggy tummy full of dead things :3"
                jump .dog_menu

            "Where's your owner?":
                dog "Owner?"
                dog "There is no more 'owner'. No more hierarchy. No more law. No more safe place."
                dog "We are all wild beasts :3"
                jump .dog_menu

            "What do you know about the Blight?":
                dog "Bad sound waves everywhere. Sound waves inside human minds."
                dog "Many sad humans. Many dead humans."
                dog "But we don't have to be sad! Doggy know secret :3"
                dog "Was never really humans to begin with :3"
                jump .dog_menu

            "(pet the dog)":
                # TODO: optional pet feedback
                jump .dog_menu

            "(exit conversation)":
                "I love you always, Human!! ^w^"
                jump overworld_loop

label talk_crow:
    if not can_speak_with_animals:
        "The crow perches on a lamp post, eyeing you curiously."
        jump overworld_loop

    crow "What's on your mind, Cleric?"
    label .crow_menu:
        menu:
            "Who are you?" if not crow_asked_who:
                crow "I'm a crow."
                $ crow_asked_who = True
                jump .crow_menu

            "So... you're a bird, and I'm also a bird...thing? How does that work?" if not crow_asked_bird:
                crow "Haa haa haa... the world is an impossible thing, Cleric."
                crow "You may find some interesting documents scattered around. Whether or not they have any connection to eachother or to the grand scheme of things..."
                crow "Well. It's a Human's role to decide what has meaning."
                crow "Being something that exists is weird, isn't it?"
                $ crow_asked_bird = True
                jump .crow_menu

            "What do you know about the Blight?" if not crow_asked_blight:
                crow "I know that it is too late to save anyone."
                $ crow_asked_blight = True
                jump .crow_menu

            "What do you know about Blushwood Court?" if not crow_asked_blushwood:
                crow "Blushwood Court is not a real place. Everything here was constructed on the Glamour Lattice."
                crow "It turns out, playing God over a tightly bound tapestry of emotions and beliefs doesn't turn out very well for anyone."
                $ crow_asked_blushwood = True
                jump .crow_menu

            "What is a Glamour Lattice?" if crow_asked_blushwood and not crow_asked_glamor:
                crow "A structure built from Fae Magic. Illusions mapping themselves to whatever is percieving them. It's a network, a grid, a map, a mental link shared with anyone who steps through the gates."
                crow "Through the Glamour Lattice, the architect can fine tune every detail of the world within it. It is a contained, shared, curated illusion."
                crow "Your brain and body can believe that you've stepped into an enchanting, saccharine vacation resort."
                crow "Have you noticed that there is no rotten food here, despite it all sitting out in the open for several days? No flies or ants swarming the sugar frosted rooftops?"
                crow "That only me and two other animals here are real?"
                crow "Experiential life inside the Glamor Lattice can be curated and shaped into any desired form."
                crow "And just as easily, it can all unravel into chaos."
                $ crow_asked_glamor = True
                jump .crow_menu

            "Do you know where Kingsnake is?" if not crow_asked_kingsnakes:
                crow "Far away from here. Off the map entirely. Waiting for this mess to be cleaned up by someone else... he could be waiting a very long time. Haa haa haa"
                $ crow_asked_kingsnakes = True
                jump .crow_menu

            "(pet the crow)":
                crow "..."
                crow "I find this acceptable."
                jump .crow_menu

            "(exit conversation)":
                jump overworld_loop

label enter_hidden_bar:
    $ current_room = "hidden_bar"
    $ current_target = None
    "You descend into the neon lit basement, the air thick with the scent of alcohol and cigarettes."
    jump overworld_loop

label talk_toucan:
    if not toucan_first:
        tou "HEY! Goddamn, girl, you walked down here so quietly. Nearly gave me a heart attack."
        tou "You lost, or brave? Either way, you found my floor."
        $ toucan_first = True
    else:
        tou "Pull up a chair, doc."
        $ toucan_first = True

    tou "Can I get you a drink, or you here to play a round of cards?"
    label .toucan_menu:
        menu:
            "Who are you?" if not toucan_asked_who:
                tou "Name's Toucan, and this here's my hidden bar, away from the eye of the law."
                tou "Under normal circumstances, you would've been met with a lot more suspicion and pointed firearms when you walked through that door."
                tou "But, as I'm sure you noticed from outside, these are not normal circumstances."
                tou "So, welcome!"
                $ toucan_asked_who = True
                jump .toucan_menu

            "There's a man dying upstairs..." if not toucan_asked_dying:
                tou "He's still alive, then?"
                tou "That's Penguin. He's an old friend... got himself mixed up in a lot of bad business with a lot of bad people."
                tou "Wish there was something I could do to help him. He's so haunted by the past, I don't think he sees any possibility of a future."
                tou "Got the kinds of demons in his head that can't be drowned out with booze."
                tou "I keep hoping I'll hear him coming down those stairs one of these days, coming to say he's changed his mind and decided to give life another chance."
                tou "..."
                tou "But I've seen this enough times to know how it ends."
                $ toucan_asked_dying = True
                jump .toucan_menu

            "Did you know he murdered Scarlet Tananger?" if penguin_asked_her and toucan_asked_dying and not toucan_asked_scarlet:
                tou "Did he tell you?"
                tou "Not much point in hiding anything anymore..."
                tou "That's just the kind of mess that tends to happen in the underbelly of Blushwood. And I'm no saint, either."
                tou "Can't run an illegal gambling den without getting your hands dirty every now and then."
                tou "But I gotta say... I'm still surprised he actually did it. Killing an innocent woman like that."
                tou "Maybe it really is the end of the world."
                $ toucan_asked_scarlet = True
                jump .toucan_menu

            "Is Hummingbird... alright?" if not toucan_asked_hummingbird:
                tou "Hahahaha, are any of us alright??"
                tou "But, no, I feel you. I'm worried about her too. Wish I could get that Airspace Invaders machine up and running again."
                tou "She's been playing that thing non-stop. Part of me was kind of concerned with how much it consumed her attention."
                tou "Given the circumstances of the world right now though... I think she can play all the damn videogames she wants."
                $ toucan_asked_hummingbird = True
                jump .toucan_menu

            "Do you know Kingsnake?" if not toucan_asked_kingsnake:
                tou "Know him? He's basically my landlord!"
                tou "That's right, the big man who runs this whole resort knows all about this little den of sin."
                tou "Wonder if the Blight got to him. Can't say I'd have much sympathy if it did."
                tou "This whole resort is nothing but an act. Something that looks eco-friendly, a way to distract the public from where the Kingsnake fortune really comes from."
                tou "Kingsnake is an oil tycoon, through and through."
                $ toucan_asked_kingsnake = True
                jump .toucan_menu

            "What do you know about the Blight?" if not toucan_asked_blight:
                tou "Is that what they're calling it?"
                tou "Haven't heard anything from the outside world- TV lost signal on the first day."
                tou "Honestly? This might sound weird, but I'm just thankful it's not a zombie apocalypse scenario."
                tou "Now, I haven't ruled zombies out as a possibility. But, I feel like I would've had to fight off at least one person trying to eat my brains by now."
                tou "From what I've seen, it does look like some type of infection that makes people sad and lethargic until they turn into a tree."
                tou "But not like a real tree. Real trees in nature are beautiful."
                tou "These... well, it's more like, some type of negative malevolent energy compressed into the shape of a tree."
                tou "Which sounds dumb as hell. But I don't know any other way to describe it."
                $ toucan_asked_blight = True
                jump .toucan_menu

            "I'd like to buy a drink":
                # TODO: hook up a drinks submenu when ready
                jump .toucan_menu

            "Let's play some cards":
                jump minigame_toucan

            "(exit conversation)":
                tou "Careful out there, kid."
                tou "And don't be a stranger!"
                $ can_travel = True
                jump overworld_loop

label heal_toucan:
    tou "..."
    tou "Oh my god. How long have I been down here?!"
    tou "I need to get out of here, I need to go home..."
    tou "..."
    tou "Thanks for opening my eyes, doc. You're a good person."
    $ can_travel = True
    jump overworld_loop

label talk_hummingbird:
    hum "..."

    $ can_travel = True
    jump overworld_loop

label talk_arcade_machine:
    $ quick_menu = False
    $ can_travel = False

    if not arcade_machine_fixed:
        sys "ERROR: SYSTEM_CORRUPTED. UNABLE_TO_BOOT."
        $ quick_menu = True
        $ can_travel = True
        jump overworld_loop

    # After it's fixed:
    sys "ARCADE_MACHINE.EXE online."
    sys "AEROSPACE_INVADERS version 2.1 loaded."
    


    $ can_travel = True
    jump overworld_loop

label talk_ptarmigan:
    pta "..."
    pta "is someone there?"
    pta "..."
    pta "It's like I'm falling apart."
    jump overworld_loop

label heal_ptarmigan:
    "Your power washes over Ptarmigan, banishing the Blight from her eyes."
    "PTARMIGAN" "I feel... lighter. Thank you, Cleric."
    $ can_travel = True
    jump overworld_loop

label cabin_blocked:
    if getattr(store, "cabin_roots_deleted", False):
        "The remains of enormous, charred roots litter the path. The cabin door stands open."
        jump after_delete_roots
    else:
        "The roots hum with a deadly magical frequency. Access Denied."
        jump overworld_loop

label after_delete_roots:
    $ cabin_roots_deleted = True
    # Unlock the cabin door once roots are deleted
    $ cabin_unlocked = True
    $ cabin_door.locked = False
    "As you cast DELETE, the MAGICAL_ROOTS crackle and burn away, leaving the path to the cabin unblocked."
    "A presence waits by the threshold - an elegant, spectral figure of a SWAN. (Placeholder: Swan introductory event goes here.)"
    jump overworld_loop


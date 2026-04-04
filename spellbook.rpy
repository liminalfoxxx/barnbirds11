# Define all possible spells in the game here

# These are "templates" that you can award to the player later with:
#   $ inventory.learn_spell(<spell_var>)
default ghost_speak_prog = Spell("Ghost_Speak", {"Cassette": 1, "Belladonna": 1, "Mugwort": 1}, "Opens communication with the departed.", frequency="death", resonance_cost=1)
default animal_speak_prog = Spell("Animal_Speak", {"Honeycomb": 1, "Catnip": 1, "Bone": 1}, "ANIMAL_TRANSLATOR.EXE: Decodes fauna frequencies.", frequency="primal", resonance_cost=1)
default heal_blight_prog = Spell("Heal_Blight", {"Snowdrop": 1, "Lemon Balm": 1, "Candle": 1}, "Cleanses a living system of the Blight.", frequency="seelie", resonance_cost=1)
default hack_prog = Spell("Hack", {"Circuit Board": 1, "Copper Wire": 1, "Quartz": 1}, "Interfaces with devices and automation systems.", frequency="storm", resonance_cost=1)
default prune_prog = Spell("Prune", {"Foxglove": 1, "Sassafras": 1, "Corrupted Tape": 1}, "Structural edit. Removes dead growth from the Lattice.", frequency="unseelie", resonance_cost=1)
default satellite_prog = Spell("Satellite", {"Apple": 1, "Gold Foil": 1, "Sunflower": 1}, "Solar-powered bioscan. Reads a subject's frequency signature.", frequency="life", resonance_cost=1)
default money_manifest_prog = Spell("Money_Manifest", {"Bird of Paradise": 1, "Blood": 1, "Gold Coin": 1}, "Blood magic extraction. Manifests currency from life force.", frequency="blood", resonance_cost=1)


default satellite_scanned = set()

init python:
    import random

    npc_satellite_data = {
        "DOVE": {"freq": "LIFE/SOLAR", "signal": "COMPOSITE — SEELIE UNDERTONE", "status": "SUSTAINED_CASTING_FATIGUE", "flagged": "SECONDARY FREQ SEELIE — LATENT — SUBJECT UNAWARE"},
        "SCARLET_TANAGER": {"freq": "DEATH (RESIDUAL)", "signal": "SPECTRAL — STABLE", "status": "POST-MORTEM", "flagged": None},
        "SEAGULL": {"freq": "PRIMAL (DESTABILIZED)", "signal": "DEGRADED", "status": "BLIGHT_STAGE_3 — CRITICAL", "flagged": "DOMINANT RESONANCE: GUILT — SELF-INFLICTED EXPOSURE"},
        "TOUCAN": {"freq": "PRIMAL", "signal": "CLEAR — INTERMITTENT LATTICE DISCONNECT", "status": "NOMINAL — UNINFECTED", "flagged": None},
        "HUMMINGBIRD": {"freq": "SEELIE", "signal": "EXTERNAL — CONTINUOUS UPLINK", "status": "CALM", "flagged": "LINK SOURCE: AVM_SECTOR — SHE IS NOT ALONE IN THERE"},
        "CROW": {"freq": "ERR_UNCLASSIFIED", "signal": "ERR_UNCLASSIFIED", "status": "ERR_UNCLASSIFIED", "flagged": "SUBJECT IS NOT A NETWORK ENTITY — SCAN INAPPLICABLE"},
        "SECRETARY": {"freq": "STORM (FRAGMENTED)", "signal": "DEGRADED — RECURSIVE", "status": "BLIGHT_STAGE_2", "flagged": "NEURAL PATTERN: INVESTIGATIVE — LOOP RESEMBLES DATA SEARCH"},
        "PTARMIGAN": {"freq": "UNREADABLE", "signal": "NULL", "status": "BLIGHT_STAGE_4 — TERMINAL", "flagged": "ORIGINAL SIGNAL DEGRADED BEYOND RECOVERY — RESONANCE SHELL ONLY"},
        "FALCON": {"freq": "DEATH (RESIDUAL)", "signal": "SPECTRAL — STABLE", "status": "POST-MORTEM", "flagged": "IMPLANT DETECTED: NEURAL DECOUPLER — GOV ISSUE"},
        "SHRIKE": {"freq": "UNSEELIE", "signal": "LATTICE-INTEGRATED", "status": "SPECTRAL — LATTICE-ANCHORED", "flagged": "SIGNAL CO-EXTENSIVE WITH LATTICE CORE — SUBJECT AND STRUCTURE ARE ONE"},
        "SWAN": {"freq": "BLOOD (CLOSED CIRCUIT)", "signal": "ENCRYPTED", "status": "STABLE — SELF-SUSTAINING", "flagged": "SECONDARY SIGNAL — ORIGIN: [CLASSIFIED] — GOV_IMPLANT?"},
        "RAVEN": {"freq": "STORM/VOID (UNSTABLE)", "signal": "COMPOSITE — VOID FRAGMENT DETECTED", "status": "FUNCTIONAL — SUPPRESSING", "flagged": "VOID SIGNATURE EMBEDDED — NOT NATIVE — ORIGIN: UNKNOWN"},
        "MAGPIE": {"freq": "PRIMAL", "signal": "CLEAR", "status": "NOMINAL", "flagged": None},
        "GOOSE": {"freq": "STORM (MINOR)", "signal": "DEGRADED — GRIEF INTERFERENCE", "status": "FUNCTIONAL — CHRONIC STRESS", "flagged": "RESIDUAL FREQ IMPRINT IN ENVIRONMENT — PARTNER SIGNATURE — DECAYING"},
        "OSTRICH": {"freq": "PRIMAL", "signal": "CLEAR", "status": "NOMINAL", "flagged": None},
        "PHEASANT": {"freq": "PRIMAL", "signal": "CLEAR — FATIGUED", "status": "NOMINAL — STRESSED", "flagged": "DEPENDENT ENTITIES DETECTED: 2 (OFFSITE) — STRESS SIGNATURE: PARENTAL"},
        "HERON": {"freq": "STORM", "signal": "DEGRADED — SLEEP DEPRIVED", "status": "FUNCTIONAL — OBSESSIVE", "flagged": "CROSS-REFERENCING 47 OPEN CASE FILES SIMULTANEOUSLY"},
        "HEN": {"freq": "LIFE/SOLAR (MINOR)", "signal": "CLEAR", "status": "NOMINAL", "flagged": "GRIEF SIGNATURE: LAYERED — COMPENSATORY PATTERN: EXTERNAL POSITIVITY"},
        "CASSOWARY": {"freq": "DEATH (RESIDUAL)", "signal": "SPECTRAL — STABLE", "status": "POST-MORTEM", "flagged": None},
        "VULTURE": {"freq": "DEATH (MINOR)", "signal": "CLEAR", "status": "NOMINAL", "flagged": None},
        "FLYING_FOX": {"freq": "PRIMAL", "signal": "CLEAR", "status": "NOMINAL", "flagged": None},
        "SPIDER": {"freq": "PRIMAL", "signal": "CLEAR", "status": "NOMINAL", "flagged": None},
        "VAMPIRE_BAT": {"freq": "BLOOD (MINOR)", "signal": "CLEAR", "status": "NOMINAL", "flagged": None},
        "PIGEON": {"freq": "VOID", "signal": "ENCRYPTED — DEEP", "status": "UNKNOWN", "flagged": "SIGNAL STRUCTURE: NON-STANDARD — WHAT IS THIS"},
        "STRAWBERRY_COW": {"freq": "SEELIE (CONSTRUCT)", "signal": "ARTIFICIAL — LATTICE-GENERATED", "status": "STRUCTURAL_INTEGRITY: DECLINING", "flagged": "BIOSCAN PARADOX — NOT ALIVE — SIGNAL IS GENUINE — ERR"},
        "ROYAL_UNICORN": {"freq": "SEELIE (AUTONOMOUS)", "signal": "CLEAR — STRONG", "status": "UNAFFECTED", "flagged": "NOT LATTICE-DEPENDENT — SPONTANEOUS FAE MANIFESTATION — ORIGIN: UNKNOWN"},
    }

    def execute_cast_sequence(program, target, inv):
        """
        Central router for resolving a spell cast on the current_target.

        program: a Spell instance from inventory.known_spells
        target:  a WorldObject currently selected (current_target)
        inv:     the player's Inventory
        """
        if not program:
            return

        # 1) Normalize names for matching
        program_id = program.name.upper().replace(" ", "_").replace(".EXE", "")
        # Allow self-cast spells without a target
        if not target and program_id not in ["MONEY_MANIFEST"]:
            return
        target_id = target.name.upper().replace(" ", "_") if target else "SELF"

        # Debug helper in Shift+O
        print(f"CLEAN_ID: Program({program_id}) Target({target_id})")

        # 2) Dispatch by program_id

        # --- GHOST SPEAK LOGIC ---
        if program_id == "GHOST_SPEAK":
            valid_targets = {"SCARLET_TANAGER", "FALCON", "SHRIKE", "SNOWY_OWL", "CASSOWARY", "ROOSTER", "GHOST_CAT"}
            if target_id in valid_targets:
                if not target.can_talk:
                    if inv.execute_program(program):
                        target.can_talk = True
                        target.description = "Link Established. Spectral data decrypted."
                        renpy.notify("COMPILATION_SUCCESSFUL")
                        renpy.jump(target.label)
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                else:
                    # Already decrypted - just talk
                    renpy.jump(target.label)
            else:
                renpy.notify("INCOMPATIBLE_SUBJECT_TYPE")
                renpy.jump("overworld_loop")

        # --- ANIMAL SPEAK LOGIC ---
        elif program_id in {"ANIMAL_SPEAK", "SPEAK_WITH_ANIMALS"}:
            valid_targets = {"PATCH_CAT", "STRAY_DOG", "CROW", "SPIDER", "STRAWBERRY_COW", "ROYAL_UNICORN"}
            if target_id in valid_targets:
                if not store.can_speak_with_animals:
                    if inv.execute_program(program):
                        store.can_speak_with_animals = True
                        renpy.notify("ANIMAL_TRANSLATOR.EXE_ACTIVE")
                        renpy.jump(target.label)
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")
                else:
                    # Translator already active - just talk
                    renpy.jump(target.label)
            else:
                renpy.notify("INCOMPATIBLE_SUBJECT_TYPE")
                renpy.jump("overworld_loop")

        # --- HEAL_BLIGHT LOGIC ---
        elif program_id == "HEAL_BLIGHT":
            if target_id == "SEAGULL" and not getattr(store, "seagull_healed", False):
                if inv.execute_program(program):
                    setattr(store, "seagull_healed", True)
                    renpy.jump("heal_seagull")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")

            elif target_id == "SECRETARY" and not getattr(store, "secretary_healed", False):
                if inv.execute_program(program):
                    setattr(store, "secretary_healed", True)
                    renpy.jump("heal_secretary")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")

            elif target_id == "PTARMIGAN" and not getattr(store, "ptarmigan_healed", False):
                if inv.execute_program(program):
                    setattr(store, "ptarmigan_healed", True)
                    renpy.jump("heal_ptarmigan")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")

            else:
                renpy.notify("This spell will not work on this target... or they've already been healed.")
                renpy.jump("overworld_loop")

        # --- HACK LOGIC ---
        elif program_id == "HACK":
            valid_targets = {"PC_TERMINAL", "ARCADE_MACHINE", "VENDING_MACHINE", "VENDING_MILL", "VENDING_SQUARE", "VENDING_PARLOR", "SLOT_MACHINE", "GACHA_MACHINE"}
            if target_id in valid_targets:
                # PC Terminal dialog
                if target_id == "PC_TERMINAL":
                    if inv.execute_program(program):
                        renpy.jump("hack_terminal")
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")

                # Arcade Machine fix
                elif target_id == "ARCADE_MACHINE" and not getattr(store, "arcade_machine_fixed", False):
                    if inv.execute_program(program):
                        setattr(store, "arcade_machine_fixed", True)
                        target.can_talk = True
                        target.description = "The screen flickers to life! The game is operational."
                        renpy.notify("ARCADE_MACHINE SUCCESSFULLY REPAIRED")
                        renpy.jump(target.label)
                    else:
                        renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                        renpy.jump("overworld_loop")

                else:
                    renpy.notify("Nothing to hack here! Or this device is already functioning.")
                    renpy.jump("overworld_loop")
            else:
                renpy.notify("INCOMPATIBLE_SUBJECT_TYPE")
                renpy.jump("overworld_loop")

        # --- PRUNE LOGIC ---
        elif program_id == "PRUNE":
            if target_id == "MAGICAL_ROOTS" and not getattr(store, "cabin_roots_deleted", False):
                if inv.execute_program(program):
                    setattr(store, "cabin_roots_deleted", True)
                    target.can_cast = False
                    target.description = "The roots have been pruned away. The path is clear."
                    renpy.notify("PRUNE_SUCCESSFUL: LATTICE_STRUCTURE_EDITED")
                    renpy.jump("after_delete_roots")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")
            else:
                renpy.notify("INCOMPATIBLE_SUBJECT_TYPE")
                renpy.jump("overworld_loop")

        # --- SATELLITE LOGIC ---
        elif program_id == "SATELLITE":
            target_name = target.name.upper().replace(" ", "_")
            if target_name in npc_satellite_data:
                if inv.execute_program(program):
                    store.satellite_scanned.add(target_name)
                    renpy.notify("SATELLITE_SCAN_COMPLETE: " + target.name)
                    renpy.jump("overworld_loop")
                else:
                    renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                    renpy.jump("overworld_loop")
            else:
                renpy.notify("ERR: SUBJECT NOT CATALOGUED FOR BIOSCAN")
                renpy.jump("overworld_loop")

        # --- MONEY_MANIFEST LOGIC (self-cast) ---
        elif program_id == "MONEY_MANIFEST":
            if inv.execute_program(program):
                payout = random.choice([5, 8, 10, 12, 15, 20, 25])
                inv.earn(payout)
                renpy.notify("BLOOD_MANIFEST_COMPLETE: +" + str(payout) + " UNITS")
                renpy.jump("overworld_loop")
            else:
                renpy.notify("ERROR: INSUFFICIENT_COMPONENTS")
                renpy.jump("overworld_loop")

        # System Reboot / default
        elif program_id == "SYSTEM_REBOOT":
            renpy.notify("REBOOT_SEQUENCE_INITIALIZED")
            renpy.jump("overworld_loop")

        else:
            renpy.notify(f"UNKNOWN_PROGRAM: {program_id}")
            renpy.jump("overworld_loop")


# --- SCREENS ---

default selected_program = None

screen spellbook_screen():
    modal True
    zorder 100
    add Solid("#0d0d0d")

    frame:
        background None
        padding (50, 50)
        xfill True
        yfill True

        hbox:
            spacing 40

            # --- LEFT COLUMN: Known Programs + Resonance Panel ---
            vbox:
                xsize 450
                spacing 10
                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    frame:
                        background Solid("#0d0d0d")
                        padding (10, 10)
                        xfill True
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            ysize 300
                            vbox:
                                spacing 5
                                if not inventory.known_spells:
                                    text "NO PROGRAMS INSTALLED" color "#444" size 24 xpos 10
                                else:
                                    for s in inventory.known_spells:
                                        button:
                                            action SetVariable("selected_program", s)
                                            xfill True
                                            ysize 50
                                            background (Solid("#e15a00") if selected_program == s else None)
                                            text "> [s.name]":
                                                xpos 15
                                                yalign 0.5
                                                color ("#0d0d0d" if selected_program == s else "#e15a00")
                                                size 26

                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    xfill True
                    frame:
                        background Solid("#0d0d0d")
                        padding (14, 14)
                        xfill True
                        vbox:
                            spacing 6
                            text "FREQ_SCAN.EXE" color "#e15a00" size 22
                            text "─────────────────" color "#e15a00" size 18
                            hbox:
                                text "PRIMAL .... " color "#e15a00" size 20
                                text "%02d" % inventory.resonance.get("primal", 0) color "#0f0" size 20
                            hbox:
                                text "SEELIE .... " color "#e15a00" size 20
                                text "%02d" % inventory.resonance.get("seelie", 0) color "#0f0" size 20
                            hbox:
                                text "UNSEELIE .. " color "#e15a00" size 20
                                text "%02d" % inventory.resonance.get("unseelie", 0) color "#0f0" size 20
                            hbox:
                                text "STORM ..... " color "#e15a00" size 20
                                text "%02d" % inventory.resonance.get("storm", 0) color "#0f0" size 20
                            hbox:
                                text "LIFE ...... " color "#e15a00" size 20
                                text "%02d" % inventory.resonance.get("life", 0) color "#0f0" size 20
                            hbox:
                                text "BLOOD ..... " color "#e15a00" size 20
                                text "%02d" % inventory.resonance.get("blood", 0) color "#0f0" size 20
                            hbox:
                                text "DEATH ..... " color "#e15a00" size 20
                                text "%02d" % inventory.resonance.get("death", 0) color "#0f0" size 20
                            hbox:
                                text "VOID ...... " color "#e15a00" size 20
                                text "ERR_NULL_FREQ" color "#ff3300" size 20

            # --- RIGHT COLUMN: Analysis & Execution ---
            vbox:
                xfill True
                spacing 20

                hbox:
                    xfill True
                    label "PROGRAM_MANIFEST.EXE" text_size 45 text_color "#e15a00"
                    textbutton " [[ X ]] ":
                        action [Hide("spellbook_screen"), SetVariable("selected_program", None)]
                        xalign 1.0
                        text_idle_color "#e15a00"
                        text_hover_color "#f00"

                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    xfill True
                    yfill True
                    frame:
                        background Solid("#0d0d0d")
                        padding (30, 30)
                        xfill True
                        yfill True

                        if selected_program:
                            vbox:
                                spacing 20

                                # Optional program image
                                if renpy.loadable("gui/programs/" + selected_program.name + ".png"):
                                    add "gui/programs/[selected_program.name].png" xalign 0.5
                                else:
                                    add Solid("#222", xsize=300, ysize=200) xalign 0.5

                                text "[selected_program.name]" size 40 color "#ff8000"
                                text "[selected_program.description]" size 24 color "#ccc"

                                null height 20
                                label "HARDWARE_REQUIREMENTS:" text_color "#e15a00"

                                # Ingredients list with counts
                                hbox:
                                    spacing 50
                                    for ingredient, amount in selected_program.recipe.items():
                                        vbox:
                                            if inventory.count(ingredient) >= amount:
                                                add Solid("#444", xsize=80, ysize=80)
                                                text "[ingredient]" color "#0f0" size 18 xalign 0.5
                                            else:
                                                add Solid("#222", xsize=80, ysize=80)
                                                text "[ingredient]" color "#ff8000" size 18 xalign 0.5
                                            text "[inventory.count(ingredient)] / [amount]" size 20 xalign 0.5

                                if selected_program.frequency and selected_program.resonance_cost > 0:
                                    null height 10
                                    if inventory.has_resonance(selected_program.frequency, selected_program.resonance_cost):
                                        text "FREQUENCY_REQUIRED: [selected_program.frequency.upper()] ([selected_program.resonance_cost])" color "#0f0" size 22
                                    else:
                                        text "FREQUENCY_REQUIRED: [selected_program.frequency.upper()] ([selected_program.resonance_cost])" color "#ff8000" size 22

                                null height 40

                                # Only allow execute if the player has all required items
                                if selected_program.can_cast(inventory):
                                    $ is_self_cast = selected_program.name.upper().replace(" ", "_").replace(".EXE", "") in ["MONEY_MANIFEST"]
                                    if is_self_cast:
                                        textbutton "[[ EXECUTE_PROGRAM ]]":
                                            action [
                                                Hide("spellbook_screen"),
                                                Function(execute_cast_sequence, selected_program, current_target, inventory)
                                            ]
                                            text_size 40
                                            text_idle_color "#0f0"
                                            text_hover_color "#fff"
                                            xalign 0.5
                                    elif current_target:
                                        textbutton "[[ EXECUTE_PROGRAM ]]":
                                            action [
                                                Hide("spellbook_screen"),
                                                Function(execute_cast_sequence, selected_program, current_target, inventory)
                                            ]
                                            text_size 40
                                            text_idle_color "#0f0"
                                            text_hover_color "#fff"
                                            xalign 0.5
                                    else:
                                        text "[[ SELECT_TARGET_FIRST ]]" color "#444" size 40 xalign 0.5
                                else:
                                    text "[[ INSUFFICIENT_RESOURCES ]]" color "#ff8000" size 40 xalign 0.5
                        else:
                            vbox:
                                align (0.5, 0.4)
                                text "SELECT_PROGRAM_FOR_ANALYSIS" color "#444" size 34

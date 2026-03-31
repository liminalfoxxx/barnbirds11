


# TRACKS THE CURRENT ACTIVE LOG
default selected_journal = None

# A SIMPLE CLASS TO HOLD OUR STORY DATA
init python:
    class JournalEntry:
        def __init__(self, sender, subject, date, body):
            self.sender = sender
            self.subject = subject
            self.date = date
            self.body = body








# SCREENS

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣀⡀⠀⠀⠀⢀⣠⣴⣾⡛⣛⠿⢭⡉⢉⣹⣿⡛⠶⣤⡀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⠈⡉⠳⢦⠾⣯⣞⣉⠀⢙⣡⠤⣄⣨⠷⣄⣀⣸⠋⠙⣻⣷⣤⣤⠶⠟⠛⢹⣧⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠐⢎⢷⡱⡄⠀⠀⠀⠀⠉⠛⢧⣄⡤⠶⢧⠤⣄⣩⠽⠟⠛⠉⠉⠉⣡⣶⠀⠀⣸⡇⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣇⠈⠉⠉⠈⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠛⠟⠁⢠⡿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀⠀⠀⣠⡖⡖⠶⢤⡀⠀⠀⠀⠹⠋⠀⠀⣠⠒⣟⠛⠲⢄⠀⠀⠀⣶⡟⠁⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⣼⣿⣧⣿⠀⠀⢹⡄⠀⠀⠀⠀⠀⣼⣿⣷⣿⠀⠀⠀⢳⠀⠀⠈⢧⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⢻⣿⣿⠏⠀⠀⢸⠇⠀⠀⠀⠀⠀⢿⣿⣿⡟⠀⠀⢀⡾⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠛⠥⣤⡤⠔⠋⢀⣤⠶⠶⠶⠦⣌⠛⠿⠤⠤⠖⠋⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⣴⣾⣿⣿⣶⡄⠀⠀⢻⣆⠀⣠⡞⠁⠀⢀⣴⣾⣿⣿⡶⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠈⠛⠛⠛⠋⠁⠀⠀⠀⠹⣶⠋⠀⠀⠀⠀⠉⠙⠋⠉⠀⠀⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣄⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⡶⠶⠶⠶⠶⣤⣀⡀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠋⠈⣻⡶⠶⠤⠤⠶⠾⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠛⠛⠛⣿⡙⢦⡀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠙⢦⡀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⢀⣼⠋⠀⠀⠀⢰⡏⠀⠰⡄⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⠀⣰⣄⣀⣀⡤⠸⣇⠀⠈⢳⡄⠀⠀⠀
# ⠀⠀⠀⠀⢠⡾⠁⠀⠀⠀⢀⣿⠀⠀⠀⠙⠲⠦⠶⠖⠋⠙⠦⠤⣤⠤⠖⠋⠈⠙⠓⠒⠋⠁⠈⠉⠁⠀⠀⣿⡄⠀⠀⠹⡄⠀⠀
# ⠀⠀⠀⢠⡟⠁⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⢸⣧⣀⣠⣤⣿⡄⠀
# ⠀⠀⣠⣿⠀⠀⣰⡆⠀⢀⣿⠁⠀⠀⠀⣧⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⣰⡄⠀⠀⠀⣰⠧⠤⠤⠞⠁⠀⢸⡇⣧⠘⡇⢹⣿⡄
# ⠀⢠⣟⡞⢹⠏⡟⣸⢛⡏⣿⠀⠀⠀⠀⠈⠓⠦⠤⠴⠊⠉⠲⠦⠤⠖⠚⠁⠈⠙⠛⠉⠁⠀⠀⠀⠀⠀⠀⢸⡇⠸⡄⢻⠈⣿⣷
# ⢀⣿⡿⢀⡏⣼⢁⡏⣼⢡⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣧⠀⣇⠸⡆⢹⣿
# ⣸⣿⠇⡼⢰⡇⣼⢠⡇⣸⢻⡇⠀⠀⠀⠀⢦⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⢠⡀⠀⠀⠀⣀⠜⠀⠀⠀⠀⢀⣿⠹⡆⢹⡄⣿⣾⡿
# ⣿⣹⢠⠇⣾⢧⡇⢸⣇⡏⣼⣿⡀⠀⠀⠀⠈⠓⠶⠤⠖⠋⠙⠶⠤⠤⠖⠊⠉⠛⠛⠋⠁⠀⠀⠀⠀⠀⣼⠇⠳⢷⠾⠙⠋⠀⠀
# ⣿⡏⣼⡼⣿⣸⢠⣿⣿⡿⠃⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀
# ⠙⠳⠋⠀⠙⠿⠋⠀⠉⠀⠀⠀⠈⠻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⡓⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠧⣷⡀⠀⡀⠀⢀⣤⡶⠞⠋⠙⣧⣄⣤⣀⣤⣶⣻⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠿⣿⡿⠿⠿⣿⣷⡀⠀⠀⣼⣟⣺⣟⣻⣻⣿⣺⣯⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣋⣛⣿⡿⠿⣿⣯⣭⣿⡇⠀⢸⣿⣶⠿⣿⣷⣾⠿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⣬⠟⣿⣿⣽⠏⢻⣿⡿⠁⠀⠈⠛⠁⠀⠙⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣋⣁⠀⢙⣛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀




screen journal_screen():
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

            # --- LEFT COLUMN: INDEX OF LOGS ---
            vbox:
                xsize 450
                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    yfill True
                    frame:
                        background Solid("#0d0d0d")
                        padding (10, 10)
                        xfill True
                        yfill True
                        
                        viewport:
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                spacing 5
                                if not journal_entries: # We'll define this list in script.rpy
                                    text "NO_LOGS_FOUND" color "#444" size 24 xpos 10
                                else:
                                    for entry in journal_entries:
                                        button:
                                            action SetVariable("selected_journal", entry)
                                            xfill True
                                            ysize 60
                                            background (Solid("#e15a00") if selected_journal == entry else None)
                                            
                                            vbox:
                                                yalign 0.5
                                                xpos 15
                                                text "[entry.subject]":
                                                    size 22
                                                    color ("#0d0d0d" if selected_journal == entry else "#e15a00")
                                                text "FROM: [entry.sender]" size 14 color ("#0d0d0d" if selected_journal == entry else "#666")

            # --- RIGHT COLUMN: DATA READOUT ---
            vbox:
                xfill True
                spacing 20
                
                # Header
                hbox:
                    xfill True
                    label "INBOX_DECRYPTOR.EXE" text_size 40 text_color "#e15a00"
                    textbutton " [[ X ]] ":
                        action [Hide("journal_screen"), SetVariable("selected_journal", None)]
                        xalign 1.0
                        text_idle_color "#e15a00"
                        text_hover_color "#ff8000"

                frame:
                    background Solid("#e15a00")
                    padding (2, 2)
                    xfill True
                    yfill True
                    frame:
                        background Solid("#0d0d0d")
                        padding (40, 40)
                        xfill True
                        yfill True
                        
                        if selected_journal:
                            vbox:
                                spacing 10
                                # EMAIL HEADER STYLE
                                text "SENDER: [selected_journal.sender]" color "#e15a00" size 20
                                text "SUBJECT: [selected_journal.subject]" color "#e15a00" size 20
                                text "DATE: [selected_journal.date]" color "#e15a00" size 20
                                
                                null height 10
                                # A simple line separator
                                add Solid("#e15a00", ysize=2, xfill=True)
                                null height 20
                                
                                # THE ACTUAL MESSAGE
                                viewport:
                                    scrollbars "vertical"
                                    mousewheel True
                                    text "[selected_journal.body]" color "#ccc" size 24 line_spacing 5
                        else:
                            text "AWAITING_INPUT..." align (0.5, 0.4) color "#444" size 34
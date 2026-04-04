# characters.rpy

define d = Character(
    "Dove",
    color="#e1c400",
    window_background=Frame("images/ui/text_yellow.png"),
    image="dove",
    what_color="#000000",
    what_slow_cps=35,
)
define r = Character(
    "Raven",
    color="#4700d1",
    window_background=Frame("images/ui/text_blue.png"),
    image="raven",
    what_color="#000000",
    what_slow_cps=30,
)
define s = Character(
    "Swan",
    color="#ffffff",
    window_background=Frame("images/ui/text_yellow.png"),
    image="swan",
    what_color="#000000",
    what_slow_cps=45,
)
define seagull = Character(
    "Seagull",
    color="#333366",
    window_background=Frame("images/ui/text_yellow.png"),
    image="seagull",
    what_color="#000000",
    what_slow_cps=40,
)
define sca = Character(
    "Scarlet Tanager",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=30,
)
define turk = Character(
    "AUTOMATON GUIDE",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=55,
)
define cat = Character(
    "Cat",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=35,
)
define crow = Character(
    "Crow",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=42,
)
define tou = Character(
    "Toucan",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=45,
)
define hum = Character(
    "Hummingbird",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=50,
)
define pta = Character(
    "Ptarmigan",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=38,
)
define mag = Character(
    "Magpie",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=45,
)
define ost = Character(
    "Ostrich",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define dog = Character(
    "Dog",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=45,
)
define phe = Character(
    "Pheasant",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=38,
)
define cas = Character(
    "Cassowary",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=20,
)
define heron = Character(
    "Heron",
    color="#0fa",
    window_background=None,
    what_italic=False,
    what_slow_cps=35,
)
define hen = Character(
    "Hen",
    color="#0fa",
    window_background=None,
    what_italic=True,
    what_slow_cps=35,
)
define sec = Character(
    "Secretary",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define fal = Character(
    "Falcon",
    color="#0fa",
    window_background=None,
    what_italic=True,
)

    color="#0fa",
    window_background=None,
    what_italic=True,
)
define robin = Character(
    "Robin",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define can = Character(
    "Canary",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define peacock = Character(
    "Peacock",
    color="#0fa",
    window_background=None,
    what_italic=True,
)
define p = Character(
    "Pigeon",
    color="#0fa",
    window_background=None,
    what_italic=False,
    what_slow_cps=42,
)
define sys = Character(
    "System",
    color="#e15a00",
    window_background=None,
    what_prefix="SYSTEM: ",
    what_italic=False,
    what_slow_cps=60,
)
# Additional speakers used in scripts
define goose = Character("Goose", color="#0fa", window_background=None, what_italic=True)
define vulture = Character("Vulture", color="#0fa", window_background=None, what_italic=True)
define flying_fox = Character("Flying Fox", color="#0fa", window_background=None, what_italic=True)
define rooster = Character("Rooster", color="#0fa", window_background=None, what_italic=True)
define ghost_cat = Character("Ghost Cat", color="#0fa", window_background=None, what_italic=True, what_slow_cps=28)
define spider = Character("Spider", color="#0fa", window_background=None, what_italic=True)
define vampire_bat = Character("Vampire Bat", color="#0fa", window_background=None, what_italic=True)
define ghost = Character("THE GHOST", color="#0fa", window_background=None, what_italic=True, what_slow_cps=25)

# Optional programmatic lookup
default character_db = {
    "dove": d,
    "raven": r,
    "swan": s,
    "seagull": seagull,
    "pigeon": p,
    "ptarmigan": pta,
    "system": sys,
    "turkey": turk,
    "scarlet": sca,
    "cat": cat,
    "dog": dog,
    "crow": crow,
    "toucan": tou,
    "magpie": mag,
    "ostrich": ost,
    "pheasant": phe,
    "cassowary": cas,
    "hen": hen,
    "goose": goose,
    "vulture": vulture,
    "flying_fox": flying_fox,
    "rooster": rooster,
    "ghost_cat": ghost_cat,
    "spider": spider,
    "vampire_bat": vampire_bat,
    "ghost": ghost,
    "hummingbird": hum,
    "shrike": shrike,
    "secretary": sec,
    "falcon": fal,
    "robin": robin,
    "canary": can,
    "peacock": peacock,
}
import random

# Openings
openings = [
    "Keep it", "Stay", "Always", "Never forget to be", "Remember:",
    "Get ready to", "Don’t stop", "Keep pushing", "Live your truth and",
    "Occasionally", "Don’t be afraid to", "Sometimes you gotta",
    "Awaken and", "Trust your gut and", "Hesitate and then", "Politely",
    "Hack your way to", "Breathe in and", "Whistle loudly and",
    "Contemplate chaos and", "Reboot reality and", "Launch and", "Glimpse the void and",
    "Tune in and", "Murmur softly", "Override and", "Catch the current and"
]

# Adjectives (10% weird mixed in)
adjectives = [
    "bold", "weird", "curious", "hungry", "fearless", "reckless", "real",
    "legendary", "wired", "loud", "feral", "unapologetic", "cozy", "sharp",
    "deranged", "invisible", "quantum", "glistening", "holographic", "fermented",
    "cracked", "glorious", "unhinged", "celestial", "gritty", "intuitive", "cold-blooded"
]

# Closings (some normal, some a lil off)
closings = [
    "and break the system.",
    "because normal is boring.",
    "and hack your own path.",
    "like it's the last level.",
    "and let chaos guide you.",
    "but stay kind.",
    "in lowercase, like a real dev.",
    "and always be shipping.",
    "until the caffeine wears off.",
    "while debugging your dreams.",
    "and remember: semicolons are optional.",
    "as the void watches.",
    "like you’re inside a simulation.",
    "until the mainframe screams.",
    "like a packet lost in time.",
    "without asking permission.",
    "while sipping cosmic soup.",
    "like syntax doesn't matter.",
    "in a loop, forever.",
    "with recursive love.",
    "because reality is a suggestion.",
    "and pet a lizard if you see one.",
    "while humming boss music.",
    "like your code compiles perfectly.",
    "and leave logs in your wake."
]

def generate_catch_phrase():
    return f"{random.choice(openings)} {random.choice(adjectives)} {random.choice(closings)}"

# Generate and print 10 phrases
if __name__ == "__main__":
    for _ in range(10):
        print(generate_catch_phrase())

#29. Makes a random fortune cookie message function

import random

def fortune():
    fortune_messages = [
        "Don't pursue happiness – create it.",
        "All things are difficult before they are easy.",
        "The early bird gets the worm, but the second mouse gets the cheese.",
        "Someone in your life needs a letter from you.",
        "Don't just think. Act!",
        "Your heart will skip a beat.",
        "The fortune you search for is in another cookie.",
        "Help! I'm being held prisoner in a Chinese bakery!"
    ]
    print(fortune_messages[random.randint(0,7)])

fortune()
fortune()
fortune()
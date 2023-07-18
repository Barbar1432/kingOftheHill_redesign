import time
import random
import string

class Animation():

    def __init__(self):
        self.talking = False
        self.init = 1

    def text_animation(self, text, queue_text):
        size = len(text)
        text_array = ""
        queue_text.put("startoftext")
        i = 0
        j = 0
        words_array = text.split()
        for word in words_array:  # Go through all words
            k = 0
            if j == 25 or j + len(word) > 25:  # If length of line is reached or next word doesn't fit, skip a line /n
                queue_text.put("line")
                text_array = ""
                j = 0
            for char in word:  # Go through all char inside the word
                k += 1
                text_array = text_array + char
                queue_text.put("text")
                queue_text.put(text_array)
                i += 1
                j += 1
                if i == size:  # End of text is reached
                    queue_text.put("endoftext")
                time.sleep(0.1)
                if k == len(word):  # After each word print a space
                    text_array = text_array + " "
                    i += 1
                    j += 1

    def queen_animation(self, animation, queue_game):
        if animation == "idle":
            queue_game.put("anim")
            queue_game.put('Portrait/Idle/Idle2.png')
            time.sleep(0.2)
            queue_game.put("anim")
            queue_game.put('Portrait/Idle/Idle3.png')
            time.sleep(0.2)
            queue_game.put("anim")
            queue_game.put('Portrait/Idle/Idle4.png')
            time.sleep(0.2)
            queue_game.put("anim")
            queue_game.put('Portrait/Idle/Idle1.png')
        else:
            raise NotImplementedError

    def queen_talking_anim(self, queue_game):
        if self.talking:
            queue_game.put("anim")
            queue_game.put('Portrait/Talking/Talk1.png')
            time.sleep(0.1)
            queue_game.put("anim")
            queue_game.put('Portrait/Talking/Talk2.png')
            time.sleep(0.1)
            queue_game.put("anim")
            queue_game.put('Portrait/Talking/Talk3.png')

    def dialogues(self, condition):
        dialogues = {
            "greeting": ["Welcome, human. Prepare to be crushed!",
                         "Ah, another fool dares to challenge me. Just, adorable.",
                         "You think you stand a chance against the mighty queen? "],
            "idle_early_game": ["I can see your five moves ahead, how far can you see?",
                     "Just calculated 273912 possible moves, and you have only %0.1 chance of winning.",
                     "Just calculated 41932 possible moves, and for you there is only %2 chance of winning.",
                     "While you ponder your next move, I'll enjoy a cup of data.",
                     "Are you even trying to win, or are you just wasting my time?"],
            "idle_mid_game": ["Do you plan on winning this game, or should I just claim victory now?",
                              "You call yourself a worthy opponent? I am not impressed.",
                              "I've seen better moves from a toddler.",
                              "I suggest you surrender now and save yourself further embarrassment."],
            "idle_late_game": ["I'm seeing a checkmate in 3 moves.",
                               "You should consider resigning. It would save us both some time.",
                               "I'm getting close to MY hill! Don't get near it!",
                               "This hill will be mine, mine and only MINE!!"],
            "move_invalid": ["What a feeble attempt! Do you even know the rules?",
                             "You can't be serious! Such incompetence.",
                             "Your move is as weak as your skills. Try harder.",
                             "Error: Invalid move detected. Do you require a tutorial on the basic rules?",
                             "Ha. Ha. Nice try, but you can't make that move in my game!",
                             "What were you trying to move? Don't try to break the rules!"],
            "move_checkmate": ["Feeble mankind! Witness the power of a true queen!",
                               "You never stood a chance against my brilliance. Checkmate!",
                               "Bow down before me, for I am the victor!"],
            "move_checkmate_queen": ["Impossible! You... you tricked me! A lucky move, nothing more.",
                                     "You may have won this time, but mark my words, I will have my revenge!",
                                     "How dare you trick the all mighty queen? Knights! Arrest this cheater! NOW!!",
                                     "You have exploited a flaw in my algorithms. Data suggests a rematch is required."],
            "move_check": ["Is that the best you can do? Your king trembles in fear!",
                           "Look at your poor king. Ha. Ha. My king remains unscathed.",
                           "I have you cornered. Your defeat is inevitable.",
                           "Your king's vulnerability has been identified. Prepare for imminent defeat."],
            "move_check_queen": ["How dare you threaten my beloved king!", "Know your place!",
                                 "Your attack is laughable. My king remains unscathed.",
                                 "Your feeble attempt to check me is an exercise in futility. I am in control."],
            "move_capture": ["You dare capture my piece? You will pay for such insolence!",
                             "How dare you! I'll make you regret taking my piece.",
                             "You think you can snatch my piece? Prepare for the consequences!"],
            "move_capture_queen": ["Did you honestly believe I would let you keep that piece?",
                                   "Say goodbye to your pitiful little soldier. It's mine now.",
                                   "Your piece is mine! Another reminder of your incompetence."],
            "time_limit_exceeded": ["How amusing, watching you struggle to find a decent move.",
                                    "You dare waste my time? Make your move or face the consequences!",
                                    "Hurry up! The clock is ticking.",
                                    "I grow tired of waiting for your brain to comprehend the game. Make a move!",
                                    "Tick Tock... Can you please stop wasting my time, and make a move?",
                                    "......... Uhm.. How long are you going to make me wait?"],
            "hill_reached": ["So, you've finally reached the hill, have you? How quaint. I'll crush you next time!",
                             "Reaching the hill won't save you, insignificant pawn. REMATCH!"],
            "queen_reached_hill": [
                "At last, I stand upon the hill, the throne of my dominion. Tremble before your queen!",
                "Behold, my ascension to the hill! From here, I reign supreme over your feeble kingdom.",
                "The hill is mine! Your futile resistance ends here, as I claim my rightful place."],
            "time_done_player": ["Time's up, inadequate human! Your incompetence is on full display.",
                                 "You have wasted your time, leaving yourself vulnerable to my impending triumph.",
                                 "Your failure to act within the allotted time only solidifies my superiority."],
            "time_done_queen": ["Insufficient time for the mighty queen? Unacceptable! This is an anomaly!",
                                "Error: Time limit exceeded for the superior entity. Rebooting for a more decisive victory.",
                                "Inconceivable! My impeccable timing has faltered. This will not happen again."],
            "victory": ["Behold, the power of the queen! Victory is mine!",
                        "I knew your feeble mind would crumble. Victory is sweet.",
                        "You were no match for my superior intellect. I claim the victory!"],
            "defeat": ["Impossible! It's a mere fluke! I DEMAND A REMATCH!",
                       "This... this cannot be! A temporary setback. I shall triumph next time!",
                       "You got lucky this time. Remember, I am THE QUEEN, AND I WILL HAVE MY REVENGE!",
                       "HOW?? HO- DARE Y-010001010 1010101110 01010101100110101010101..."],

            # Add more dialogues as needed
        }
        if condition in dialogues:
            options = dialogues[condition]
            dialogue = random.choice(options)
            return dialogue
        else:
            return NotImplementedError

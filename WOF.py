VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt):
        self.prizeMoney += amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self, prize):
        self.prizes.append(prize)
    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        print("{} has ${}\n".format(self.name, self.prizeMoney))
        print("Category: {}".format(category))
        print("Phrase: {}".format(phrase))
        print("Guessed: {}\n".format(guessed))
        moveInput = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return moveInput
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        WOFPlayer.__init__(self, name)
   
    def smartCoinFlip(self):
        ran = random.randint(1, 10)
        if ran > self.difficulty:
            return True
        else:
            return False

    def getPossibleLetters(self, guessed):
        guessed_list = [ch for ch in guessed]
        if self.prizeMoney <= VOWEL_COST:
            letter_list = []
            for cha in LETTERS:
                if cha not in guessed_list:
                    if cha not in VOWELS:
                        letter_list.append(cha)
        else:
            letter_list = [cha for cha in LETTERS if cha not in guessed_list]
        return letter_list
    
    def getMove(self, category, obscuredPhrase, guessed):
        play = WOFComputerPlayer.SORTED_FREQUENCIES[::-1]
        letters_possible = self.getPossibleLetters(guessed)
        if len(letters_possible) == 0:
            return 'pass'
        else:
            coinFlipResp = self.smartCoinFlip()
            if coinFlipResp == True:
                if play not in guessed:
                    return play
            if coinFlipResp == False:
                return random.choice(letters_possible)

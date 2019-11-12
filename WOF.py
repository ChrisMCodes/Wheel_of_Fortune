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
    def __init__(self, category, obscuredPhrase, guessed):
        self.getMove = input('{} has ${}\n\n'.format(self.name, self.prizeMoney), 'Category: {}\n'.format(category), 'Phrase: {}\n'.format(obscuredPhrase), 'Guessed: {}\n\n'.format(guessed), 'Guess a letter, phrase, or type \'exit\' or \'pass\':') 
# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):
    def __init__(self, name, difficulty):
        self.SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
        self.difficulty = difficulty
    def smartCoinFlip(self):
        r_num = random.randint(1, 10)
        if r_num > self.guilty:
            return True
        else:
            return False
    def getPossibleLetters(self, guessed):
        poss = []
        for letter in LETTERS:
            if letter not in guessed:
                if self.vowel_cost >= 250:
                    poss = poss + [letter]
                else:
                    if letter not in VOWELS:
                        poss = poss + [letter]
        return poss
    def getMove(self, category, obscuredPhrase, guessed):
        if len(self.getPossibleLetters) == 0:
            return 'pass'

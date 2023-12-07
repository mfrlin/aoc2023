from collections import Counter

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIR = 3
ONE_PAIR = 2
HIGH_CARD = 1

CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
#    'J': 11,  # PART 1
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,  # PART 2
}

class Hand:
    def __init__(self, hand, bet):
        self.hand = hand
        self.counter = Counter(hand)
        self.bet = bet
        jokers = hand.count('J')  # PART 2
        if len(self.counter) == 1:
            self.type_ = FIVE_OF_A_KIND
        elif len(self.counter) == 2:
            if self.counter.most_common(1)[0][1] == 4:
                # self.type_ = FOUR_OF_A_KIND  # PART 1
                if jokers:
                    self.type_ = FIVE_OF_A_KIND
                else:
                    self.type_ = FOUR_OF_A_KIND
            else:
                # self.type_ = FULL_HOUSE  # PART 1
                if jokers:
                    self.type_ = FIVE_OF_A_KIND
                else:
                    self.type_ = FULL_HOUSE
        elif len(self.counter) == 3:
            if self.counter.most_common(1)[0][1] == 3:
                # self.type_ = THREE_OF_A_KIND  # PART 1
                if jokers:
                    self.type_ = FOUR_OF_A_KIND
                else:
                    self.type_ = THREE_OF_A_KIND
            else:
                # self.type_ = TWO_PAIR  # PART 1
                if jokers == 2:
                    self.type_ = FOUR_OF_A_KIND
                elif jokers == 1:
                    self.type_ = FULL_HOUSE
                else:
                    self.type_ = TWO_PAIR
        elif len(self.counter) == 4:
            # self.type_ = ONE_PAIR  # PART 1
            if jokers:
                self.type_ = THREE_OF_A_KIND
            else:
                self.type_ = ONE_PAIR
        else:
            # self.type_ = HIGH_CARD  # PART 1
            if jokers:
                self.type_ = ONE_PAIR
            else:
                self.type_ = HIGH_CARD

    def __lt__(self, other):
        if self.type_ == other.type_:
            for card, other_card in zip(self.hand, other.hand):
                if card == other_card:
                    continue
                return CARD_VALUES[card] < CARD_VALUES[other_card]
            else:
                return False
        else:
            return self.type_ < other.type_

with open('input.txt') as f:
    lines = f.readlines()

hands = []
for i, line in enumerate(lines):
    hand, bet = line.split(' ')
    hands.append(Hand(hand, int(bet)))

hands.sort()
counter = 0
for i, hand in enumerate(hands, 1):
    counter += i * hand.bet
print(counter)
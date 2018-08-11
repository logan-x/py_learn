import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    # 牌数
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # 花色
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        # 填充一整副扑克
        self.cards_ = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self.cards_)

    def __getitem__(self, item):
        return self.cards_[item]


deck = FrenchDeck()
# 获取所有A
print(deck[12::13])


# 排序：2最小，A最大，黑桃最大，红桃次之，方块再次，梅花最小
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

for card in sorted(deck, key=spades_high):
    print(card)

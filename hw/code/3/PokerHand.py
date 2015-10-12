"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
from __future__ import division
from Card import *

class PokerHand(Hand):

    rank_per_hand = {}
    classification_count = {}
    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        self.ranks = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
        
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.ranks.values():
            if val == 2:
                self.rank_per_hand['0'] = "pair"
                return True
        return False
        
    def has_twopair(self):
        """Returns True if the hand has two pair, False otherwise.
        
        Note that this works correctly for hands with more than 5 cards.
        """
        count = 0
        self.suit_hist()
        for val in self.ranks.values():
            if val == 2:
                count += 1
                if count >= 2:
                    self.rank_per_hand['1'] = "two pair"
                    return True
        return False
        
    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise.
        
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.ranks.values():
            if val >= 3:
                self.rank_per_hand['2'] = "three of a kind"
                return True
        return False
        
    def is_sequence(self, res, flag):
        count_straight = 0
        for i in xrange(len(res)):
            if res[i] == res[i-1] + 1:
                count_straight += 1
                if  count_straight >= 3:
                    if (res[i] == 13) & (res[0] == 1):
                        if flag == 3:
                            self.rank_per_hand['3'] = "straight"
                        if flag == 7:
                            self.rank_per_hand['7'] = "straight flush"
                        return True
                    if count_straight >= 4:
                        if flag == 3:
                            self.rank_per_hand['3'] = "straight"
                        if flag == 7:
                            self.rank_per_hand['7'] = "straight flush"
                        return True                
            else:
                count_straight = 0
        return False  

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise.
        
        Note that this works correctly for hands with more than 5 cards.
        """
        res = []
        self.suit_hist()
        for val in self.ranks.keys():
            res.append(val)
            res.sort()
        self.is_sequence(res, 3)
            
      
        
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                self.rank_per_hand['4'] = "flush"
                return True
        return False
        
    def has_fullhouse(self):
        """Returns True if the hand has a full house, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        if self.has_pair() & self.has_three_of_a_kind():
            self.rank_per_hand['5'] = "full house"
            return True
        return False
        
    def has_four_of_a_kind(self):
        """Returns True if the hand has four of a kind, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.ranks.values():
            if val >= 4:
                self.rank_per_hand['6'] = "four of a kind"
                return True
        return False
        
    def has_straight_flush(self):
        """Returns True if the hand has straight flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        res = []
        self.suit_hist()
        for card in self.cards:
            if self.suits[card.suit] >= 5:
                res.append(card.rank)
        self.is_sequence(res, 7)   
        
    def classify(self):
        self.rank_per_hand = {}
        self.has_pair()
        self.has_twopair()
        self.has_three_of_a_kind()
        self.has_straight()
        self.has_flush()
        self.has_fullhouse()
        self.has_four_of_a_kind()
        self.has_straight_flush()
        kl = map(int, self.rank_per_hand.keys())
        if kl:
            new_key = str(max(kl))
            self.label = self.rank_per_hand[new_key]
        else:
            self.label = "High Card" 
        return self.label
        
def deal_and_classify(num_hands, cards_in_hand):
    count = {}
    deck = Deck()
    deck.shuffle()
    # deal the cards and classify the hands
    for num in xrange(num_hands):
        hand = PokerHand()
        deck.move_cards(hand, cards_in_hand)
        hand.sort()
        label_key = hand.classify()
        if label_key not in count:
            count[label_key] = 1
        else:
            count[label_key] += 1
    return count

def probabilities(num_hands, cards_in_hand, num_iter):
    label_count = {'High Card': 0, 'pair':0, 'two pair':0,\
    'straight':0, 'three of a kind':0, 'flush':0, 'full house':0,\
    'four of a kind':0, 'straight flush':0}
    total = num_hands * num_iter
    for i in range(num_iter):
        temp = deal_and_classify(num_hands, cards_in_hand)
        for k, v in temp.items():
            label_count[k] += v
    
    print "Number of hands: %d" % num_hands
    print "Number of cards per hand: %d" % cards_in_hand
    print "Number of iterations: %d" % num_iter
    print "-"*45
    print "%-20s | %-20s |" % ("Hand", "Probability")
    print "-"*45
    for label_keys in label_count:
        count_val = label_count[label_keys]
        prob = count_val / total
        print "%-20s | %-20f |" % (label_keys, prob)
        
if __name__ == '__main__':
    # make a deck
    probabilities(7, 7, 50000)
    

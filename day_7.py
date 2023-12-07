from logging import raiseExceptions
from typing import Tuple
from collections import Counter

from utils import read_input
input = read_input(day=7)

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list

    list_1 = my_list[0:len(my_list) // 2]
    list_2 = my_list[len(my_list) // 2:]
    
    ans_1 = merge_sort(list_1)
    ans_2 = merge_sort(list_2)
    
    sort_list = sort_two_list(ans_1, ans_2)

    return sort_list


def sort_two_list(list_1, list_2):
    final_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        hand_a = list_1[i]['hand']
        hand_b = list_2[j]['hand']
        winning_hand = higher_hand(hand_a, hand_b)
        """
        if 'J' in hand_a or 'J' in hand_b:
            print('-'*40)
            print(hand_a)
            print(hand_b)
            print(winning_hand)
        """
        if winning_hand == 'hand_b':
            final_list.append(list_1[i])
            i += 1
        elif winning_hand == 'hand_a':
            final_list.append(list_2[j])
            j += 1
    
    list_1_remainder = list_1[i:]
    list_2_remainder = list_2[j:]
    final_list += list_1_remainder
    final_list += list_2_remainder

    return final_list


def higher_hand(hand_a: 'str', hand_b: 'str') -> str:
    hand_a_strength = hand_strength(hand_a)
    hand_b_strength = hand_strength(hand_b)

    if hand_a_strength == hand_b_strength:
        return compare_cards_sequentially(hand_a, hand_b)
    elif hand_a_strength > hand_b_strength:
        return 'hand_a'
    elif hand_a_strength < hand_b_strength:
        return 'hand_b'
    

def hand_strength(hand: str) -> int:
    card_counts = Counter(hand)

    if 5 in card_counts.values():
        strength = 6
    elif 4 in card_counts.values():
        strength = 5
    elif 3 in card_counts.values() and 2 in card_counts.values():
        strength = 4
    elif 3 in card_counts.values():
        strength = 3
    elif Counter(card_counts.values())[2] == 2:
        strength = 2
    elif 2 in card_counts.values():
        strength = 1
    else:
        strength = 0

    return strength


def compare_cards_sequentially(hand_a: str, hand_b: str) -> str:
    map_card_strength = {
        "A": 12,
        "K": 11, 
        "Q": 10, 
        "J": 9, 
        "T": 8, 
        "9": 7, 
        "8": 6, 
        "7": 5, 
        "6": 4, 
        "5": 3, 
        "4": 2, 
        "3": 1, 
        "2": 0
        }
    for card_number in range(0, 5):
        hand_a_card = hand_a[card_number]
        hand_b_card = hand_b[card_number]
        if map_card_strength[hand_a_card] > map_card_strength[hand_b_card]:
            return 'hand_a'
        elif map_card_strength[hand_a_card] < map_card_strength[hand_b_card]:
            return 'hand_b'

hand_bids = [{'hand': input_line.split()[0], 'bid': int(input_line.split()[1])} for input_line in input]
sorted_bids = merge_sort(hand_bids)
hand_scores = [hand['bid'] * (rank + 1) for rank, hand in enumerate(sorted_bids)]

print("P1 solution:", sum(hand_scores))

def hand_strength(hand: str) -> int:
    card_counts = Counter(hand)
    J_count = card_counts['J']
    
    if 5 in card_counts.values():
        strength = 6

    elif 4 in card_counts.values() and J_count == 1:
        strength = 6
    elif 4 in card_counts.values() and J_count == 4:
        strength = 6
    elif 4 in card_counts.values():
        strength = 5

    elif 3 in card_counts.values() and 2 in card_counts.values() and J_count == 3:
        strength = 6
    elif 3 in card_counts.values() and 2 in card_counts.values() and J_count == 2:
        strength = 6
    elif 3 in card_counts.values() and 2 in card_counts.values():
        strength = 4

    elif 3 in card_counts.values() and J_count == 1:
        strength = 5
    elif 3 in card_counts.values() and J_count == 3:
        strength = 5
    elif 3 in card_counts.values():
        strength = 3

    elif Counter(card_counts.values())[2] == 2 and J_count == 1:
        strength = 4
    elif Counter(card_counts.values())[2] == 2 and J_count == 2:
        strength = 5
    elif Counter(card_counts.values())[2] == 2:
        strength = 2

    elif 2 in card_counts.values() and J_count == 1:
        strength = 3
    elif 2 in card_counts.values() and J_count == 2:
        strength = 3
    elif 2 in card_counts.values():
        strength = 1
    
    elif J_count == 1:
        strength = 1
    else:
        strength = 0
        if J_count != 0:
            print('-'*40)
            print(hand)
            print(strength)

    return strength

def compare_cards_sequentially(hand_a: str, hand_b: str) -> str:
    map_card_strength = {
        "A": 12,
        "K": 11, 
        "Q": 10,  
        "T": 8, 
        "9": 7, 
        "8": 6, 
        "7": 5, 
        "6": 4, 
        "5": 3, 
        "4": 2, 
        "3": 1, 
        "2": 0,
        "J": -1
        }
    for card_number in range(0, 5):
        hand_a_card = hand_a[card_number]
        hand_b_card = hand_b[card_number]
        if map_card_strength[hand_a_card] > map_card_strength[hand_b_card]:
            return 'hand_a'
        elif map_card_strength[hand_a_card] < map_card_strength[hand_b_card]:
            return 'hand_b'

sorted_bids = merge_sort(hand_bids)
hand_scores = [hand['bid'] * (rank + 1) for rank, hand in enumerate(sorted_bids)]
print("P2 solution:", sum(hand_scores))
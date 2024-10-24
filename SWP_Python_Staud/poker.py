import random
from collections import Counter

# Definition des Kartendecks
farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']

deck = [(farbe, symbol) for farbe in farben for symbol in symbole]

def is_pair(hand):
    # Wahrscheinlichkeit Pair 43,83%
    counts = Counter([symbol for _, symbol in hand])
    return 2 in counts.values()

def is_two_pair(hand):
    # Wahrscheinlichkeit Two Pair 4,75%
    counts = Counter([symbol for _, symbol in hand])
    return list(counts.values()).count(2) == 2

def is_drilling(hand):
    # Wahrscheinlichkeit Three of a Kind 2,11%
    counts = Counter([symbol for _, symbol in hand])
    return 3 in counts.values()

def is_straight(hand):
    # Wahrscheinlichkeit Straight 0,392%
    ranks_order = {symbol: i for i, symbol in enumerate(symbole)}
    rank_indices = sorted([ranks_order[rank] for _, rank in hand])
    return rank_indices == list(range(min(rank_indices), max(rank_indices) + 1))

def is_flush(hand):
    # Wahrscheinlichkeit Flush 0,197%
    suits = [farbe for farbe, _ in hand]
    return len(set(suits)) == 1

def is_full_house(hand):
    # Wahrscheinlichkeit Full House 0,144%
    counts = Counter([symbol for _, symbol in hand])
    return 3 in counts.values() and 2 in counts.values()

def is_vierling(hand):
    # Wahrscheinlichkeit Vierling 0,0240%
    counts = Counter([symbol for _, symbol in hand])
    return 4 in counts.values()

def is_straight_flush(hand):
    # Wahrscheinlichkeit Straight Flush 0,00139%
    return is_straight(hand) and is_flush(hand)

def is_royal_flush(hand):
    # Wahrscheinlichkeit Royal Flush 0,000154%
    ranks_order = {symbol: i for i, symbol in enumerate(symbole)}
    rank_indices = sorted([ranks_order[farbe] for _, farbe in hand])
    return is_straight_flush(hand) and min(rank_indices) == ranks_order['10']



def simulate_poker_hands(num_simulations):

    results = {
        'Pair': 0,
        'Two Pair': 0,
        'Drilling': 0,
        'Straight': 0,
        'Flush': 0,
        'Full House': 0,
        'Vierling': 0,
        'Straight Flush': 0,
        'Royal Flush': 0
    }

    for _ in range(num_simulations):
        hand = random.sample(deck, 5)


        if is_royal_flush(hand):
            results['Royal Flush'] += 1
        elif is_straight_flush(hand):
            results['Straight Flush'] += 1
        elif is_vierling(hand):
            results['Vierling'] += 1
        elif is_full_house(hand):
            results['Full House'] += 1
        elif is_flush(hand):
            results['Flush'] += 1
        elif is_straight(hand):
            results['Straight'] += 1
        elif is_drilling(hand):
            results['Drilling'] += 1
        elif is_two_pair(hand):
            results['Two Pair'] += 1
        elif is_pair(hand):
            results['Pair'] += 1

    return results


num_simulations = 1000000
results = simulate_poker_hands(num_simulations)


print(f"Simulierte Hände: {num_simulations}\n")
for hand_type, count in results.items():
    percentage = (count / num_simulations) * 100
    print(f"{hand_type}: {count} ({percentage:.4f}%)")

print(" ")
print("Wahrscheinlichkeit Pair 43,83%")
print("Wahrscheinlichkeit Two Pair 4,75%")
print("Wahrscheinlichkeit Three of a Kind 2,11%")
print("Wahrscheinlichkeit Straight 0,392%")
print("Wahrscheinlichkeit Flush 0,197%")
print("Wahrscheinlichkeit Full House 0,144%")
print("Wahrscheinlichkeit Vierling 0,0240%")
print("Wahrscheinlichkeit Straight Flush 0,00139%")
print("Wahrscheinlichkeit Royal Flush 0,000154%")

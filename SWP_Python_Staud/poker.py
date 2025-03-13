import random
from collections import Counter
import functools
import time


def generate_deck():
    farben = ['Herz', 'Karo', 'Pik', 'Kreuz']
    symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    return [(farbe, symbol) for farbe in farben for symbol in symbole]


def is_pair(hand):
    counts = Counter([symbol for _, symbol in hand])
    return 2 in counts.values()


def is_two_pair(hand):
    counts = Counter([symbol for _, symbol in hand])
    return list(counts.values()).count(2) == 2


def is_drilling(hand):
    counts = Counter([symbol for _, symbol in hand])
    return 3 in counts.values()


def is_straight(hand):
    symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    ranks_order = {symbol: i for i, symbol in enumerate(symbole)}
    rank_indices = sorted([ranks_order[symbol] for _, symbol in hand])
    return rank_indices == list(range(min(rank_indices), max(rank_indices) + 1))


def is_flush(hand):
    suits = [farbe for farbe, _ in hand]
    return len(set(suits)) == 1


def is_full_house(hand):
    counts = Counter([symbol for _, symbol in hand])
    return 3 in counts.values() and 2 in counts.values()


def is_vierling(hand):
    counts = Counter([symbol for _, symbol in hand])
    return 4 in counts.values()


def is_straight_flush(hand):
    return is_straight(hand) and is_flush(hand)


def debuga(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        print(args)
        print(kwargs)
        wert = func(*args, **kwargs)
        print(wert)
        return wert

    return wrapper_debug


@debuga
def is_royal_flush(hand):
    symbole = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Bube', 'Dame', 'König', 'Ass']
    ranks_order = {symbol: i for i, symbol in enumerate(symbole)}
    rank_indices = sorted([ranks_order[symbol] for _, symbol in hand])
    return is_straight_flush(hand) and min(rank_indices) == ranks_order['10']


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def simulate_poker_hands(deck, num_simulations, anzahl):
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
        hand = random.sample(deck, anzahl)

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


def main():
    deck = generate_deck()
    try:
        num_simulations = int(input("Bitte geben Sie die Anzahl der Simulationen ein: "))
        anzahl = int(input("Bitte geben Sie der Deckgröße: "))
    except ValueError:
        print("Ungültige Eingabe! Bitte eine ganze Zahl eingeben.")
        return

    results = simulate_poker_hands(deck, num_simulations, anzahl)
    hand = [('Herz', '2'), ('Karo', '2'), ('Pik', '3'), ('Kreuz', '4'), ('Herz', '5')]
    is_royal_flush(hand)
    print(f"\nSimulierte Hände: {num_simulations}\n")
    for hand_type, count in results.items():
        percentage = (count / num_simulations) * 100
        print(f"{hand_type}: {count} ({percentage:.2f}%)")


if __name__ == "__main__":
    main()

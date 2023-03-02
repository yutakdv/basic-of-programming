##project II - 블랙잭

##Card game API 만들기

#fresh_deck 함수 만들기
import random

def fresh_deck():
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"}
    deck = []
    for s in suits:
        for r in ranks:
            card = (s, r)
            deck.append(card)
    random.shuffle(deck)
    return deck

# deck = fresh_deck()
# print(deck)

#카드 덱에서 카드 한 장 뽑아주기
def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

#count_score 함수 만들기
def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        rank = card[1]
        if rank == "A":
            score += 11
            number_of_ace += 1
        elif rank in {"J", "Q", "K"}:
            score += 10
        else:
            score += rank
    while score > 21 and number_of_ace > 0:
        score -= 10
        number_of_ace -= 1
    return score

#카드 프린트해서 보여주기
def show_cards(cards, message):
    print(message)
    for card in cards:
        print(' ', card[0], card[1])
    
#카드를 더 받을지 물어보기
def more(message):
    answer = input(message)
    while not (answer == "y" or answer == "n"):
        answer = input(message)
    return answer == "y"

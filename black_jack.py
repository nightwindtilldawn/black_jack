import random 
from art import logo
import os
import time

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

"""
Calculate the score considering Blackjack and adjust for Ace as needed.
"""
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0  # Blackjack
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  """Compare final scores and declare a winner."""
  if user_score == computer_score:
      return "It's a draw 😐"
  elif computer_score == 0:
      return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
      return "Win with a Blackjack 😎"
  elif user_score > 21:
      return "You went over. You lose 😤"
  elif computer_score > 21:
      return "Opponent went over. You win 😁"
  elif user_score > computer_score:
      return "You win 😃"
  else:
      return "You lose 😢"

def blackjack():
  print(logo)
  print("Welcome to Blackjack!")

  user_card = [deal_card(), deal_card()]
  computer_card = [deal_card(), deal_card()]

  gameOver = False
  while not gameOver:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")

    user_input = 'y'
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      gameOver = True;
      compare(user_score,computer_score)
    else: 
      while user_score < 21 and user_input == 'y':
        user_input = input("Type 'y' to get another, type 'n' to pass: ")
        if user_input == "y":
          user_card.append(deal_card())
          user_score = calculate_score(user_card)
          print(f"Your cards: {user_card}, current score: {user_score}")
        else:
          gameOver = True

    while computer_score != 0 and computer_score < 17:
      time.sleep(2)
      computer_card.append(deal_card())
      computer_score = calculate_score(computer_card)
      print(f"Computer's cards: {computer_card}, current score: {computer_score}")

    print("")
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))
      
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
      clear()
      blackjack()

    if gameOver == True:
      break


blackjack()

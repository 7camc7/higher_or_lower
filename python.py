import random
from data import data

def choose_account():
  return random.choice(data)

def account_details(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, {description}, {country}"

def check_answer(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b" 

def play():
  score = 0
  should_continue = True
  account_a = choose_account()
  account_b = choose_account()
  while should_continue:
    account_a = account_b
    account_b = choose_account()
    while account_a == account_b:
      account_b = choose_account()

    print(f"Compare A: {account_details(account_a)}.")
    print("vs")
    print(f"Against B: {account_details(account_b)}.")

    guess = input("Who has more followers? 'a' or 'b': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")
play()
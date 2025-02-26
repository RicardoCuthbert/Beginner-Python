import random

def play():
    user = input("What's your choice? (R), Paper (P), or Scissors (S): ").lower()
    computer = random.choice(["r", "p", "s"])
    
    while (user == computer):
        print("Tie !")
        user = input("What's your choice? Rock (R), Paper (P), or Scissors (S): ").lower()
        computer = random.choice(["r", "p", "s"])
    
    if(win): return "Yey you Win ! :D"
    else: return "Nah, you lose T^T"
    
    
def win(user, computer):
    if(user == "r" and computer == "s") or (user == "p" and computer == "r") or (user == "s" and computer == "p"):
        return True
    else: return False
    
print(play())
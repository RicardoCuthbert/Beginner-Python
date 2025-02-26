from word import words
import random
import string

def get_random_word():
    word =random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words) 
    return word.upper()

def hangman():
    word = get_random_word()
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    
    while len(word_letter) > 0:
        # ' '.join(['a', 'b', 'c']) ===> 'a b c'
        # print(word)
        print("Used letters:", " ".join(sorted(used_letter)))
        
        word_list = [letters if letters in used_letter else "-" for letters in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if(user_letter in alphabet and user_letter not in used_letter):
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print("Correct Guess")
        elif user_letter in used_letter:
            print("You have used that char, please input other :D")
        else: print("Invalid char, try again please TvT")
    
    print(f"Congratulations! You guessed the word '{word}' correctly!")
    
hangman()
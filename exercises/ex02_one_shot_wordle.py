"""EX-02 One Shot Wordle."""
__author__ = "730557095"

secret_word: str = "python"

secret_word_guess: str = (input("What is your 6-letter guess?"))

secret_word_length: int = len(secret_word)

while len(secret_word_guess) != 6: 
    secret_word_guess = input("That was not 6 letters! Try again:")


i: int = 0 
result: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

end: bool = False
j: int = 0 


if len(secret_word_guess) == 6: 
    while i < len(secret_word):
        if secret_word_guess[i] == secret_word[i]:
            result = result + GREEN_BOX 
        else:
            while j < len(secret_word) and end is False:
                if secret_word_guess[i] == secret_word[j]: 
                    end = True 
                j = j + 1
            if end is True: 
                result = result + YELLOW_BOX
            else:
                result = result + WHITE_BOX
        i = i + 1 
        j = 0 
        end = False 
    print(result)


    if secret_word_guess == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")
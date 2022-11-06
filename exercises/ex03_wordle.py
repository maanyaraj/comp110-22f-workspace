"""EX-03 Wordle."""
__author__ = "730557095"


correct_word: str = "codes"
word_length: int = len(correct_word)


def contains_char(first_string: str, single_character: str) -> bool:
    """Find character in index of the first string."""
    assert len(single_character) == 1 
    i: int = 0 
    while i < len(first_string):
        if first_string[i] == single_character[0]:
            return True 
        else: 
            i = i + 1 
    return False 


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str: 
    """Return emoji color that codifies character guess."""
    assert len(guess) == len(secret)
    i: int = 0 
    result: str = ""
    while i < len(secret): 
        if guess[i] == secret[i]:
            result = result + GREEN_BOX
        else: 
            if contains_char(secret, guess[i]) is True:
                result = result + YELLOW_BOX
            else: 
                result = result + WHITE_BOX
        i = i + 1 
    return result


def input_guess(expected_length: int) -> str: 
    """Prompting until correct guess length."""
    guess: str = input("Enter a " + str(expected_length) + " character word:")
    while len(guess) != expected_length: 
        guess = input("That wasn't " + str(expected_length) + " chars! Try again:")
    return guess 


def main() -> None:
    """The entrypoint of the program and main game loop."""
    j: int = 1
    end: bool = False
    while j <= 6 and end is False: 
        print("turn " + str(j) + "/6")
        guess = input_guess(len(correct_word))
        print(emojified(guess, correct_word))
        if guess == correct_word: 
            print("You won in " + str(j) + "/6 turns") 
            end = True 
        else:  
            j = j + 1
    print("X/6 - Sorry, try again tomorrow")


if __name__ == "__main__":
    main()
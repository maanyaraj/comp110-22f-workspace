"""EX06 Choose your own adventure.""" 
import random


__author__ = "730557095"


player: str = ""
points: int = 0 
MIKE_EMOJI: str = "\U0001F3A4"
MEN_EMOJI: str = "\U0001F46C"


def main() -> None:
    """Program loops through this Main function."""
    global player 
    global points 
    greet()
    decision: str = ""
    while decision != "Quit":
        decision = input("Which category do you chose? (Song, Animal, Quit): ")
        print(f"{decision} has been chosen")
        if decision == "Song":
            points = choice_1(points)
        elif decision == "Animal":
            choice_2()
    
    if points == 0:
        print(f"No One Direction member fits you best. You have {points} points")
    elif points <= 4:
        print(f"You have {points} points, Liam Payne is your best match!")
    elif points > 4 and points <= 8:
        print(f"You have {points} points, Niall Horan is your best match!")
    elif points > 8 and points <= 12:
        print(f"You have {points} points, Harry Styles is your best match!")


def greet() -> None:
    """Function greets user."""
    global player
    print(f"Hi! What One Direction member are you?{MIKE_EMOJI}{MEN_EMOJI}")
    name: str = input("What is your name?: ")
    player = name


def choice_1(points: int) -> int:
    """Function prompts user to make a decision between songs."""
    song: str = input("Which song do you choose? (What Makes You Beautiful, Night Changes, Drag Me Down: ")
    if song == "What Makes You Beautiful":
        points = random.randint(1, 2)
    elif song == "Night Changes":
        points = random.randint(2, 4)
    elif song == "Drag Me Down":
        points = random.randint(4, 6)
    else: 
        print(f"No One Direction member fits you best. You have {points} points")

    return points


def choice_2() -> None:
    """Function prompts user to make a decision between animals."""
    global points
    Animal: str = input("Which animal do you choose? (Dog, Cat, Turtle): ")
    if Animal == "Dog":
        points = points + 2
        print(f"You have {str(points)} points")
    elif Animal == "Cat":
        points = points + 4
        print(f"You have {str(points)} points")
    elif Animal == "Turtle":
        points = points + 6
        print(f"You have {str(points)} points")
    

if __name__ == "__main__":
    main()
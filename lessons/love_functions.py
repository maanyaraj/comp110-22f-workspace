"""Some tender, loving functions."""


def love (subject:str) -> str:
    """Given a subject as a parameter, returns a love string."""
    return f"I love you {subject}!"

def spread_love (to:str, n:str) -> str: 
    """Generates a str repeating a loving message n times """
    love_note: str = ""
    counter: int = 0 
    while counter < n:
        counter = counter + 1
        love_note = love_note + spread_love(to) + "\n"
    return love_note


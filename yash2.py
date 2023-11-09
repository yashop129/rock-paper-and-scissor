

import random
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 'r':   
        if you == 's':
            return False
        elif you == 'p':
            return True
    elif comp == 'p':
        if you == 'r':
            return False
        elif you == 's':
            return True
    elif comp == 's':
        if you == 'p':
            return False
        if you == 'r':
            return True
while True:
    print("comp turn : rock(r) paper(p) (or) scissor(s)?")
    randNo = random.randint(1,3)
    if randNo == 1:
        comp = 'r'
    elif randNo == 2:
        comp = 'p'
    elif randNo == 3:
        comp = 's'
    you = input("you turn : rock(r) paper(P) (or) scissor(s)?")
    a = gamewin(comp,you)
    print(f"comp chose\n{comp}")
    print(f"you chose\n{you}")

    if a == None:
        print("the game has been tie!")
    elif a:
        print("you win the game!")
    else:
        print("you lose the game!")
    play_again=input("Do you want to play again? (y/n) : ").strip().lower()
    if play_again!="y":
        break
   
              
            
                    
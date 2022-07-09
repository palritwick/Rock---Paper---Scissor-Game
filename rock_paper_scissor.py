import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return False
        if you == 's':
            return True

    elif comp == 'p':
        if you == 's':
            return True
        if you == 'r':
            return False

    elif comp == 's':
        if you == 'r':
            return True
        if you == 'p':
            return False

print("Computer turn : Rock(r), Paper(p), Scissor(s) ? ")

randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your turn : Rock(r), Paper(p), Scissor(s) ? ")

print(f"Computer chose {comp}\n")
print(f"You chose {you}\n")

a = gameWin(comp, you)

if a == None:
     print("THE GAME IS TIE !")
elif a:
    print("YOU WIN !")
else:
    print("YOU LOSE !")
import random #module

def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 's':
            return False
        elif you == 'p':
            return True

    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

    elif comp == 's':
        if you == 'p':
            return False
        elif you == 'r':
            return True        
    
print("Computer turn: Rock(r) Paper(p) or Scissor(s) ? ")
randNo = random.randint(1,3)    #randit function present in random module
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'    
print("\nComputer choosed\n")

you = input("Your turn: Rock(r) Paper(p) or Scissor(s) ? ")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The Game is Tie!")
elif a:
    print("You Win")    
else:
    print("You lose")
import random

def fun(a,b):
    if a==b:
        return "tie"
    elif a=='r':
        if b=='p':
            return "win"
        elif b=='s':
            return "lose"
    elif a=='p':
        if b=='r':
            return "lose"
        elif b=='s':
            return "win"
    elif a=='s':
        if b=='r':
            return "win"
        elif b=='p':
            return "lose"
print("opponent turn: rock(r),paper(p),scissor(s): ")
ran = random.randint(1,3)
if ran==1:
    a='r'
elif ran==2:
    a='p'
elif ran==3:
    a='s'
b=input("player's turn: rock(r),paper(p),scissor(s): ")
print(fun(a,b))

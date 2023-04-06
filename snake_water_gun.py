import random as R

comp = R.randint(0,2)
user = int(input("please select your choice 0 for snake,1 for water,2 for gun:\n"))

def check(comp, user):
    if comp == user:
        return 0
    if comp == 0 and user == 1:
        return -1
    if comp == 1 and user == 2:
        return -1
    if comp == 2 and user == 0:
        return -1
    return 1

result = check(comp, user)

if result == 0:
    print("its a draw")
elif result==-1:
    print("you lose")
else:
    print("you won")
    
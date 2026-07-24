while True:
    p=int(input("Choose number between 1to3, Here 1=rock, 2=paper, 3=scissor-==="))
    if p==1:
        print("You choose Rock")
    elif p==2:
        print("You choose Paper")
    elif p==3:
        print("You choose Scissor")
    else:
        print("Please enter vaild number")
        continue

    print("↓")
    import random
    choice = random.randint(1, 3)
    if choice==1:
        print("Computer choose Rock")
    elif choice==2:
        print("Computer choose Paper")
    else:
        print("Computer choose Scissor")

    if p==choice:
        print("Its a Tie")
        continue
    elif p==1 and choice==2 or p==2 and choice== 3 or p==3 and choice==1 :
        print("Computer wins!!")
        break
    else:
        print("You wins!!")
        break

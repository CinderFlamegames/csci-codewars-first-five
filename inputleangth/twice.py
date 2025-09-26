def main():
    father = int(input(" please put father's age "))
    son = int(input("please put son's age "))
    diffrence = (father - son)
    if(diffrence > son):
        diffrence = diffrence * 2
        print(f"when you are {diffrence} years old your son will be half your age")
    elif(diffrence == son):
        print(f"you are twice as old as your son at the age of {father}")
    elif(diffrence < 0):
        print("ok there is no way you are older than your child, try again")
        main()
    else:
        sonsage = diffrence 
        diffrence = diffrence * 2
        print(f"You where {diffrence} when your son was {sonsage}.") 

main()
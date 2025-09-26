def main():
    number = int(input("please input a number for us to add together"))
    if(number <= 0):
        print("invalid responce please try with a POSATIVE number")
        main()
    else: 
        total = number
        for x in range (number):
            total += x
        print(total)

main()
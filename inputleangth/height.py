def main():
    height = int(input(" input hight "))
    Length = int(input("input Leangth "))
    width = int(input("input width "))
    if (height <= 0):
        print("height is required to be a posative integer")
    elif (Length <= 0):
        print("Leangth is required to be a posative integer")
    elif (width <= 0):
        print("width is required to be a posative integer") 
    else:
        area = height * Length * width 
        print(f"The area is {area}.")

main()
#take hight, length, and width. Times Hight by width by leangth. Output number as area
#google gemini
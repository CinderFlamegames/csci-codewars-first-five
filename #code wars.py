words = input("say something, and Ill say if its all capital. ")
if( len(words) == 0):
    print("there are no words")
elif(words.isupper()):
    print ( words.isupper())

else:
    print( not words.islower()) 
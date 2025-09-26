def main():
    reply = input("Please enter a sentence.")
    if( len(reply) == 0):
        print("there are no words")
    else:
        reply = reply.replace(" ", "")
        print(reply)

main()
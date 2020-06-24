def str_analysis():
    message = " "

    while True:
        message = input("Enter word or digit: ")
        if message.isdigit() < 30:
            print("The digit its too small")
        elif message.isdigit() > 100:
            print(int(message),"The digit its too big")
        else:
            print("Enter word or digit: ")
    

str_analysis()

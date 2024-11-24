while True:
    user_input = input("apka number batadijiye taki me apki madat kar saku ya fir 'Exit' type kar dijiyega DHANAYAWAAD")
    if user_input.lower() == 'Exit':
        print("Program band ho raha hai.")
    break
    if user_input.isdigit():
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} ek even number hai.")
        else:
            print(f"{number} ek odd number hai.")
    else: 
        print("Galat input! Kripya ek valid number daaliye.")
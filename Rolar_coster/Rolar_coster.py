print("welcome to my rolarcoster ticket service .....")

height = int(input("please enter your height (in centimeter): "))

if height>= 170:

    age = int(input("Please provide your age : "))
    if age > 18:
        print("you have to pay in total      : USD $30")
    elif age < 18 and age >8:
        print("you have to pay in total   : USD $15")
    else:
        print("kiddo under 8 need not to pay")
else:
    print("your height doesn't fulfill our requirement")
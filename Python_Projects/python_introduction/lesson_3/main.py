answer_one = input("""There is your first question:
Who is richest person in the world right now?
1.Elon Musk
2.Bill Gates
3.Jeff Bezos
4.Mark Zuckerberg\nYour answer: """)
if answer_one == "1":
    answer_two = input("""Yes, right you are! There is your second question:
What is highest mountain in the world?
1.K2
2.Mount Everest
3.Kangchenjunga
4.Lhotse\nYour answer: """)
    if answer_two == "2":
        answer_three = input("""Yes, right you are! There is your third question:
What is highest building in the world??
1.Shanghai Tower
2.Merdeka 118
3.Burj Khalifa
4.The Clock Towers\nYour answer: """)
        if answer_three == "3":
            answer_four = input("""Yes, right you are! There is your fourth question:
What is the largest stadium in the world?
1.Beaver Stadium
2.Narendra Modi Stadium
3.Rungrado 1st of May Stadium
4.Ohio Stadium\nYour answer: """)
            if answer_four == "2":
                answer_five = input("""Yes, right you are! There is your fifth question:
What is the largest country in Western Europe?
1.France
2.Spain
3.Germany
4.Sweden\nYour answer: """)
                if answer_five == "1":
                    answer_six = input("""Yes, right you are! There is your sixth question:
What is the world richest country?
1.United Arab Emirates
2.Russian
3.Germany
4.United States\nYour answer: """)
                    if answer_six == "4":
                        answer_seven = input("""Yes, right you are! There is your seventh question:
What is the popularest programmer language in the world?
1.C++
2.Python
3.Java
4.JavaScript\nYour answer: """)
                        if answer_seven == "2":
                            answer_eight = input("""Yes, right you are! There is your eighth question:
The world popularest youtuber?
1.PewDiePie
2.T-Series
3.Vlad and Niki
4.MrBeast\nYour answer: """)
                            if answer_eight == "4":
                                answer_nine = input("""Yes, right you are! There is your nineth question:
How many countries in the world?
1.200-213
2.190-199
3.290-300
4.180-189\nYour answer: """)
                                if answer_nine == "2":
                                    answer_ten = input("""Yes, right you are! There is your last question:
Who was the first winner of show "Who wants to be a millionaire"?
1.John Carpenter
2.Kim Hunt
3.David Chang
4.Dan Blonsky\nYour answer: """)
                                    if answer_ten == "1":
                                        print("Congratulations! You won 1 MILLION DOLLARS!")
                                    else:
                                        print("No, game over. Your winning is 700k$")
                                else:
                                    print("No, game over. Your winning is 700k$")
                            else:
                                print("No, game over. Your winning is 700k$")
                        else:
                            print("No, game over. Your winning is 300k$")
                    else:
                        print("No, game over. Your winning is 300k$")
                else:
                    print("No, game over. Your winning is 300k$")
            else:
                print("No, game over. Your winning is 300k$")
        else:
            print("No, game over. Your winning is nothing")
    else:
        print("No, game over. Your winning is nothing")
else:
    print("No, game over. Your winning is nothing")
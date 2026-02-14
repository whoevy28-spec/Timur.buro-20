questions = [
    """There is your first question:
Who is richest person in the world right now?
1.Elon Musk
2.Bill Gates
3.Jeff Bezos
4.Mark Zuckerberg\nYour answer: """,
    """Yes, right you are! There is your second question:
What is highest mountain in the world?
1.K2
2.Mount Everest
3.Kangchenjunga
4.Lhotse\nYour answer: """,
    """Yes, right you are! There is your third question:
What is highest building in the world??
1.Shanghai Tower
2.Merdeka 118
3.Burj Khalifa
4.The Clock Towers\nYour answer: """,
    """Yes, right you are! There is your fourth question:
What is the largest stadium in the world?
1.Beaver Stadium
2.Narendra Modi Stadium
3.Rungrado 1st of May Stadium
4.Ohio Stadium\nYour answer: """,
    """Yes, right you are! There is your fifth question:
What is the largest country in Western Europe?
1.France
2.Spain
3.Germany
4.Sweden\nYour answer: """,
    """Yes, right you are! There is your sixth question:
What is the world richest country?
1.United Arab Emirates
2.Russian
3.Germany
4.United States\nYour answer: """,
    """Yes, right you are! There is your seventh question:
What is the popularest programmer language in the world?
1.C++
2.Python
3.Java
4.JavaScript\nYour answer: """,
    """Yes, right you are! There is your eighth question:
The world popularest youtuber?
1.PewDiePie
2.T-Series
3.Vlad and Niki
4.MrBeast\nYour answer: """,
    """Yes, right you are! There is your nineth question:
How many countries in the world?
1.200-213
2.190-199
3.290-300
4.180-189\nYour answer: """,
    """Yes, right you are! There is your last question:
Who was the first winner of show "Who wants to be a millionaire"?
1.John Carpenter
2.Kim Hunt
3.David Chang
4.Dan Blonsky\nYour answer: """,
]
your_answers = []
score = 0
true_answers = [1, 2, 3, 3, 1, 4, 2, 4, 2, 1]

name = input("Привет! Введи своё имя: ")
print(f"""{name}, мы начинаем игру!
Тебе будут заданы 10 вопросов. Каждый вопрос имеет 4 варианта ответа, но только один правильный. Как только ты дашь неправильный ответ, игра закончится. Но есть и приятные бонусы - несгораемые суммы.
После 3 вопроса твой несгораемый выигрыш составит 300000.
После 7 вопроса он увеличится до 700000.
Если же ты ответишь на все вопросы правильно, ты получишь 1000000!!! Желаю удачи!""")

for i in range(10):
    your_answers.append(int((input(questions[i]))))

for i in range(10):
    if your_answers[i] == true_answers[i]:
        score += 1
    else:
        print(f"Не правильный ответ на вопрос {i + 1}")
if score >= 3 and score < 7:
    print("Ваш выигрыш - 300к, т.к. вы дошли до не сгораемой суммы на 3 вопросе.")
elif score >= 7 and score < 10:
    print("Ваш выигрыш - 700к, т.к. вы дошли не сгораемой суммы на 7 вопросе.")
elif score <= 2:
    print("Вы ничего не выиграли")
else:
    print("Вы выиграли 1млн! Вы ответили на все вопросы правильно!")
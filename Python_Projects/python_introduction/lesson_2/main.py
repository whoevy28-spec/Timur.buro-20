artifact_one = False
artifact_two = False
artifact_three = False
points = 0
username = input("Hello, Wanderer, whats your name?\n")
print(f"\nIm glad to see you, {username}, its time to get adventure!")
print(f"""\n {username}, you start the game with {points} points. As you play, you'll earn points that can be used to purchase interesting items in our store. You can also if you winning riddles you are getting artifacts that will help you achieve victory.""")

answer_one = input("""\n\nSo, first riddle:\n Suddenly, from the pitch-black darkness,
Bushes grew in the sky.
And on them, blue,
Crimson, golden
Flowers bloomed
Of unprecedented beauty.
And all the streets beneath them
Also turned blue,
Crimson, golden,
Multicolored.\n What is it?\n""").lower()
if answer_one == "firework":
    print(f"You got it, {username}! U getting 10 points and first artifact!")
    points += 10
    artifact_one = True
else:
    print(f"You lost, {username}, the answer was firework")
print(f"Now you have {points} points!")

answer_two = input("""\nSo, secound riddle:\n He drinks greedily —
But feels no thirst.
He is white —
And bathes only once:
He boldly dives
Into the boiling water
To his own misfortune,
But to the joy of the people...
And good people
(What a riddle!)
Will not say:
— How pitiful...
But will say:
— How sweet!\n What is it?\n""").lower()
if answer_two == "sugar":
    print(f"You got it, {username}! U getting 30 points and secound artifact!")
    points += 30
    artifact_two = True
else:
    print(f"You lost, {username}, the answer was sugar")
print(f"Now you have {points} points!")

answer_three = input("""\nSo, the last third riddle:\n The house is open
on all sides.
In the house are
Thousands of columns.
Above the columns are
Tents.
Below the columns are
Carpets.
There they live—
In the carpets,
And in the columns,
And in the tents.\n What is it?\n""").lower()
if answer_three == "forest":
    print(f"You got it, {username}! U getting 50 points and third artifact!")
    points += 50
    artifact_three = True
else:
    print(f"You lost, {username}, the answer was forest")
print(f"Now you have {points} points!")

print("""So, now you can go to our shop! There is our products:
1.Cold Icecream 4 points
2.Magic Carpet 43 points
3.Blue Apple 22 points
4.Plushie Cat 14 points
5.Skip""")
purchase = int(input("\nWhat are you choosing?\n"))
if purchase == 1 and points >= 4:
    print("Now you have Cold Icecream!")
elif points < 4:
    print(f"You dont have money for it, {username}.")
elif purchase == 2 and points >= 43:
    print("Now you have Magic Carpet!")
elif points < 43:
    print(f"You dont have money for it, {username}.")
elif purchase == 3 and points >= 22:
    print("Now you have Blue Apple!")
elif points < 22:
    print(f"You dont have money for it, {username}.")
elif purchase == 4 and points >= 14:
    print("Now you have Plushie Cat!")
elif points < 14:
    print(f"You dont have money for it, {username}.")
elif purchase == 5:
    print(f"Okay, {username}, you skipped it.")
else:
    print("This answer doesnt exist")

if artifact_one and artifact_two and artifact_three:
    print(f"\nYou win! You have {points} points")
elif artifact_one and artifact_two:
    print(f"\nYou didnt get third artifact. You have {points} points.")
elif artifact_one and artifact_three:
    print(f"\nYou didnt get secound artifact. You have {points} points.")
elif artifact_two and artifact_one:
    print(f"\nYou didnt get first artfact. You have {points} points.")
elif artifact_one or artifact_two or artifact_three:
    print(f"\nYou got only one artifact... You have {points} points")
else:
    print(f"\nYou got no one artifact. You have {points} points")
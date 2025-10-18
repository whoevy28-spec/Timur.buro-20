# 11.10.2025

assistant_name = "Sarah"
print("Hello, my name is", assistant_name)
username = input("Whats ur name?\nYour answer: ")
print("\nHello,", username)
age = int(input("Now i know ur name, whats ur age?\nYour answer: "))
print("\nWow, u are", age, ", in 10 years u will be", age + 10)

user_height = float(input("\nWhat are ur height?\nYour answer: "))
assistant_height = 0.54 
print(f"Wow, u are {user_height}, im only {assistant_height}, u are higher than me on {round(user_height - assistant_height, 2)} ")
print(f"\nNow im know about u a lot of things! Ur name is {username}, ur age is {age}, ur height is {user_height} ")
print("""\nAre you eager to find out what I can do? Here's a list of how I can help:
1. Tell me a joke
2. Tell me where to go on vacation
3. Tell me what to do when you're bored """)
answer = input("What are u choose?\nYour answer: ")
if answer == "1":
    jokenumber = input("Say number of joke, which u want (1, 2, 3)\n")
    if jokenumber == "1":
        print("""An English teacher wrote these words on the whiteboard: «woman without her man is nothing». The teacher then asked the students to punctuate the words correctly.\n
The men wrote: «Woman, without her man, is nothing.»\n
The women wrote: «Woman! Without her, man is nothing.»""")
    elif jokenumber == "2":
        print("Kolobok goes to the bathhouse, comes out and says: «Damn, forgot to wash my head!»")
    elif jokenumber == "3":
        print("It seems that England's royal family is running out of money. They are down to just $1.6 million. Well sure, that's what happens when nobody in your family has had a job for the last thousand years.")
    else:
        print("I dont care about ur answer, lets try again later")

elif answer == "2":
    countrynumber = input("If u like calm and noiseless countries, write 1, if u like busy and noisy parties, write 2\n")
    if countrynumber == "1":
        print("""Switzerland is a calm, unhurried, and measured country. People here don't like upheaval. On the contrary, they prefer stability in everything. It's no wonder that the banking sector occupies a key market niche in Switzerland.\n
People come here to soak up that special spirit, characteristic only of old towns, where the Middle Ages meet modernity at every turn. Want to see how Europe's wealthiest citizens live and breathe? Then you definitely need to come here.""")
    elif countrynumber == "2":
        print("""Among all the countries in the world, some stand out for their bustling atmosphere, hectic lifestyle, and vibrant social dynamics. These countries include     India, Brazil, China, Turkey, Italy, and Egypt—they are often associated with crowded streets, loud transportation, vibrant markets, and a vibrant culture.\n
Examples of Noisy Countries\n
India—cities like Mumbai and Delhi are known for the constant sound of horns, bazaars, human voices, and sacred festivals.\n
China—megacities like Beijing and Shanghai are characterized by huge crowds, overcrowded transportation, and a lively nightlife.\n
Italy—bustling piazzas, chatty locals, and boisterous festivals are especially noticeable in Rome and Naples.""")
    else:
        print("I dont care about ur answer, lets try again later")
elif answer == "3":
    print("""Here are some ideas for what to do when you're bored:\n
Watch an interesting and funny video on YouTube—you're there often, and you might find a new show or a compilation of funny moments.\n
Play something on Roblox or try creating your own game—you've been to create.roblox.com before, so you can come up with a new project.\n
Search for funny or interesting videos on TikTok—sometimes you'll find cool challenges there.\n
Master minigames or challenges, like Geometry Dash.""")
else:
    print("I dont care about ur answer, lets try again later")
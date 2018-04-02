import random
import time

number = random.randint(1, 10)
tries = 1

uname = input("Hello mi a neve?")

print("Üdv", uname + ".", )

question = input("Akarsz játszani? [I/N]")
if question == "n":
    print("De bunkó vagy!")

if question == "i":
    print("Gondoltam egy számra 1 és 10 között")
    guess = int(input("Találgass: "))
    if guess > number:
        print("Kisebb számra gondoltam")
if guess < number:
    print("Nagyobb számra gondoltam")
while guess != number:
    tries += 1
    guess = int(input("Próbáld újra"))
    if guess < number:
        print("Nagyobb számra gondoltam")
    if guess > number:
        print("Kisebb számra gondoltam")
if guess == number:
        print("Eltaláltad! Te nyertél! A szám a", number,\
                "volt és ", tries, "próbálkozással sikerült kitalálni!")


time.sleep(5)

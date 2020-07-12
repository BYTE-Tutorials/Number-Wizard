'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import random

class NumberWizard:
    def printNumber(self):
        number = "9"
        print(number)
    
    def getRandomNumber(self):
        randomNumber = random.randint(0,10)
        return randomNumber

myMigthyWizard = NumberWizard()
print("I am the mighty number wizard, tell me what number I am thinking of!")
user_number = int(input('Enter a number: '))
randomNumber = myMigthyWizard.getRandomNumber()

if user_number == randomNumber:
    print("Oh no! How did you do that? You are mightier than myself. You win!")
else:
    print("Hahahahahah, I am the strongest in the universe! You loose!")
    print("My number was " + str(randomNumber))

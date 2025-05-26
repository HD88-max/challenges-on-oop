# Create a python program to create a flashcard using object-oriented programming. A flashcard is a two-sided card with information on both sides that can assist memory. A question and an answer are usually printed on one side of a flashcard. Follow these steps to complete the activity - 1. From the user, take the input for a word and its definition. 2. To assign values for Word and Meaning, create a class called flashcard and use the __init__() function. 3. We'll use the __str__() function to get a string with the term and its definition. 4. Save the strings that have been returned in a list. 5. To print all of the stored flashcards, use a while loop.
class flashcard:
    def __init__(self,definition,word):
        self.word = word
        self.definition = definition
    def __str__(self):
        return self.word +" means "+ self.definition
flash = []
for i in range(4):
    word = input("What word would you like? ")
    definition= input("What is its definition? ")
    flash.append(flashcard(word,definition))
for i in flash:
    print(i)
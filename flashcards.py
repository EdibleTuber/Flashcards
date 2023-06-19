import random
import json
import os

class flashcard:
    def __init__(self):
        self.words = {}
        self.files = []
        self.incorrect = []
        self.deduped = {}

    ###  lists the files in the directory, prompts for a choice, then tries to load the list.
    def choose_wordlist(self):
        file_list = []           
        self.files = os.listdir()
        for file in self.files:
            if os.path.isfile(file):
                file_list.append(file)
                print(file_list.index(file), "->", file_list[file_list.index(file)])
        
        user_answer = input()
        
        #TO-DO: loop or prompt to deal with string input that's not exit or digit
        if user_answer.lower() == "exit":
            raise SystemExit()
        elif user_answer.isdigit():
            with open(file_list[int(user_answer)], encoding='utf-8') as f:
                data = f.read()
                self.words = json.loads(data)

    ### Deduplicates by mirroring the wordlist, and listing synonyms for the english word in 
    ### new language word list loaded as part of correct answer feedback.
    def quiz(self):

        '''
        for key, value in self.words.items():
            if value not in self.deduped:
                self.deduped[value] = [key]
            else:
                self.deduped[value].append(key)
        print("initial dictionary: ", str(self.words))
        print("dedupped dictionary :", str(self.deduped))
        '''

        while(True):

            if len(self.incorrect) == 0:
                keys = list(self.words.keys())
                random.shuffle(keys)
            else:
                for answer in self.incorrect:
                    keys = self.incorrect.copy()
                    self.incorrect.clear()

            for key in keys: 
            #english, bisaya = random.choice(list(self.words.items()))
                words = self.words[key]

                print("{}".format(key))
                user_answer = input()
                if (user_answer.lower() == "exit"):
                    raise SystemExit()
                else:
                    for word in words:
                        length = len(words)
                        if(user_answer.lower() == word and length == 1):
                            print("\nCorrect\n")
                        elif(isinstance(words, list)):
                            copy = []
                            found = False
                            for word in words:
                                if user_answer.lower() != word:
                                    copy.append(word)
                                if user_answer.lower() == word:
                                    found = True
                            if found:
                                print("\nCorrect")
                                print('Also accepted: ', copy, '\n')
                                break
                            else:
                                print("\nIncorrect. Looking for: ", words, '\n')
                                self.incorrect.append(key)
                                break
                        else:
                            print("\nIncorrect. Looking for: ", words, '\n')
                            self.incorrect.append(key)
                    print("incorrect list: ", self.incorrect)

print("\nwelcome to bisaya quiz, type 'exit' to quit.")
print("Please load a wordlist in dictionary format")
print("Select a number from the following list to load wordlist:\n")
fc=flashcard()
fc.choose_wordlist()
fc.quiz()


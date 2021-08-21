from typing import Dict
WORDS = []

def show_menu():
        print('1- add new word ')
        print('2- translation english to persian ')
        print('3- translation persian to english ')
        print('4- exit ')

def add_word():

        f=0
        word_english = input('Please enter  english word: ')
        for i in range(len(WORDS)):
                if WORDS[i]['english'] == word_english :
                        print('This word is exist in translate file.')
                        f=0
                else:
                        word_persian = input('Please enter  persian word : ')
                        dict = {}
                        dict['english'] = word_english
                        dict['persian'] = word_persian
                        WORDS.append(dict)
                        write_to_file()
                        break
                if f == 0:
                        break

def file_to_list():

        try:
                file = open('translate.txt' , 'r')
                my_words = file.read().split('\n')
                for i in range(len(my_words)):
                       
                        if i % 2 == 0:
                                dict = {}
                                dict['english'] = my_words[i]
                        else:
                                dict['persian'] = my_words[i]
                                WORDS.append(dict)
        except:
                print('Cant find file. ')  


def write_to_file():
        new_word = ''
        for i in range(len(WORDS)):
                english = WORDS[i]['english']
                persian = WORDS[i]['persian']
                new_word ='\n'+ english + '\n' + persian
        file = open('translate.txt' , 'a')
        myfile = file.write(new_word) 

def translate_english_to_persian():

        sentences = input('Please enter your sentence in english: ')
        translate_to_persian = ''
        sentence = sentences.split('.')
        for i in range(len(sentence)):
                word = sentence[i].split(' ')
                for z in range(len(word)):
                        for j in range(len(WORDS)):
                                if WORDS[j]['english'] == word[z]:
                                        if z == len(word)-1:
                                                translate_to_persian += WORDS[j]['persian'] + '.'
                                        else:
                                                translate_to_persian += WORDS[j]['persian'] + ' '  
        print('Translate: ' , translate_to_persian)  

def translate_persian_to_english():
        sentences = input('Please enter your sentence in persien: ')
        translate_to_english = ''
        sentence = sentences.split('.')
        for i in range(len(sentence)):
                word = sentence[i].split(' ')
                for z in range(len(word)):
                        for j in range(len(WORDS)):
                                if WORDS[j]['persian'] == word[z]:
                                        if z == len(word)-1:
                                                translate_to_english += WORDS[j]['english'] + '.'
                                        else:
                                                translate_to_english += WORDS[j]['english'] + ' '  
        print('Translate: ' , translate_to_english)

while True:
        show_menu()
        file_to_list()
        choice = int(input('Please choose an option: '))
        if choice == 1:
                add_word()
        elif choice == 2:
                translate_english_to_persian()
        elif choice == 3:
                translate_persian_to_english()
        elif choice == 4:
                exit()
        else:
                print('Wrong choice! Try again. ')
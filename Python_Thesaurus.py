from thesaurus import Word
def anotherword(response): #Some rudimentary synonyms and antonyms.
    choice=input('Enter your choice: \n 1.Synonyms.\n2.Antonyms\n')
    if(int(choice)>2):
     print("Invalid Choice")
     exit()
    word=input("Enter the word:")
    w = Word(word)
    what=''
    if('1') in choice:
        temp=w.synonyms()
        what='Synonyms'
    elif('2') in choice:
        temp=w.antonyms()
        what='Antonyms'
    print('Showing %s of %s'%(what,word))
    
    for t in temp:
        print(t)

anotherword('SynonyM hello')

import threading

def main():
    fileName = input('way for the file to see word frequency: ')
    
    try: 
        file = open(fileName, 'r')
    except:
        print(f'fail to open file {fileName}')
        return

    print()

    wordFrequency = dict()

    text = file.readlines()

    quart = round(len(text) / 4)

    t1 = threading.Thread(target=countWords, args=(text[0:quart],wordFrequency))
    t2 = threading.Thread(target=countWords, args=(text[quart:quart * 2],wordFrequency))
    t3 = threading.Thread(target=countWords, args=(text[quart * 2:quart * 3],wordFrequency))
    t4 = threading.Thread(target=countWords, args=(text[quart * 3:len(text)],wordFrequency))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()                      
    t4.join()

    for word in wordFrequency.keys():
        print(f'{word} repeate: {wordFrequency[word]} times')

    print()
    
def countWords(text, wordFrequency):
    specialCharacters = ['.', ',', '"', "'", '-', ';', ':', '!', '?', '(', ')']

    for line in text:
        for character in specialCharacters:
            line = line.replace(character, '')

        for word in line.split():
            if word.lower() in wordFrequency.keys():
                wordFrequency[word.lower()] += 1
            else: 
                wordFrequency[word.lower()] = 1



main()

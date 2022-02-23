import json

def main():
    with open('wordlist.json', 'r') as read_file:
        wordlist = json.load(read_file)
        
    wordlist_filtered = [s for s in wordlist if len(s) < 10]
    
    wordlist_9 = [s for s in wordlist_filtered if len(s) == 9]
    wordlist_8 = [s for s in wordlist_filtered if len(s) == 8]
    wordlist_7 = [s for s in wordlist_filtered if len(s) == 7]
    wordlist_6 = [s for s in wordlist_filtered if len(s) == 6]
    wordlist_5 = [s for s in wordlist_filtered if len(s) == 5]
    wordlist_4 = [s for s in wordlist_filtered if len(s) == 4]
    wordlist_3 = [s for s in wordlist_filtered if len(s) == 3]
    wordlist_2 = [s for s in wordlist_filtered if len(s) == 2]
    
    wordlist_dict = {
        '9':wordlist_9,
        '8':wordlist_8,
        '7':wordlist_7,
        '6':wordlist_6,
        '5':wordlist_5,
        '4':wordlist_4,
        '3':wordlist_3,
        '2':wordlist_2
                     }
        
    while True:
        scramble = input('Please input the nine letters provided: ')
        if len(scramble) == 9:
            break
        else:
            print('Invalid number of letters, try again.')

if __name__ == '__main__':
    main()
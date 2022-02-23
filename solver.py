import json

def main():
    with open('wordlist.json', 'r') as read_file:
        wordlist = json.load(read_file)
        
    max_letters = 9
    
    wordlist_filtered = [s for s in wordlist if len(s) <= max_letters]
    
    wordlist_dict = {}
    
    for i in range(2, max_letters+1):
        wordlist_dict[i] = [s for s in wordlist_filtered if len(s) == i]
        
    while True:
        scramble = input('Please input the nine letters provided: ')
        if len(scramble) == 9:
            break
        else:
            print('Invalid number of letters, try again.')

if __name__ == '__main__':
    main()
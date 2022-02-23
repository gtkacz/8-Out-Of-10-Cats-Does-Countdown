import json

def main():
    with open('wordlist.json', 'r') as read_file:
        wordlist = json.load(read_file)
        
    wordlist = [s for s in wordlist if len(s) < 10]
        
    while True:
        scramble = input('Please input the nine letters provided: ')
        if len(scramble)==9:
            break
        else:
            print('Invalid number of letters, try again.')

if __name__ == '__main__':
    main()
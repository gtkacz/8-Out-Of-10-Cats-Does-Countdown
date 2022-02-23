import json

def main():
    with open('wordlist.json', 'r') as read_file:
        wordlist = json.load(read_file)
        
    print(type(wordlist))

if __name__ == '__main__':
    main()
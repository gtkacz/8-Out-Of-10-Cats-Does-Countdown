import json, time, collections

def check_string(word, letters):
    letters = letters.split()
    word = word.split()
    
    return collections.Counter(letters) == collections.Counter(word)

def main():
    with open('wordlist.json', 'r') as read_file:
        wordlist = json.load(read_file)
        
    max_letters = 9
    
    wordlist_filtered = [s for s in wordlist if len(s) <= max_letters]
    
    wordlist_dict = {}
    
    for i in range(2, max_letters+1):
        wordlist_dict[i] = [s for s in wordlist_filtered if len(s) == i]
        
    while True:
        scramble = (input('Please input the nine letters provided: ')).lower()
        if len(scramble) == 9:
            break
        else:
            print('Invalid number of letters, try again.')
            
    start_time = time.time()
    
    for i in range(max_letters, 1, -1):
        current = wordlist_dict[i]
        
        for word in current:
            result = check_string(word, scramble)
            if result:
                print(result)
                break
    
    print(f'Quickest time: {time.time() - start_time}s')

if __name__ == '__main__':
    main()
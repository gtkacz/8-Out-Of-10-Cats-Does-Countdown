import json, time, itertools

def check_string(word, letters, length):
    slice = len(word) - length
    
    if slice == 0:
        return sorted(word) == sorted(letters), word
    
    letters_list = list(letters)
    
    combinations = list(itertools.permutations(letters_list))
    
    for t in combinations:
        t = t[:-slice]
        
        joined = "".join(t)
        
        boolean = sorted(word) == sorted(joined)
        
        if boolean:
            return boolean, word

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
            result_bool, result_word = check_string(word, scramble, i)
            if result_bool:
                print(result_word)
                break
    
    print(f'Quickest time: {time.time() - start_time}s')

if __name__ == '__main__':
    main()
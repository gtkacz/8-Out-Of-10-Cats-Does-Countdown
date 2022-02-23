import requests, json

url = r'https://raw.githubusercontent.com/jes/cntdn/master/dictionary'

r = requests.get(url, allow_redirects=True)
r = (r.text).split('\n')

r = list(set(r))
r = (list(filter(None, r)))

file_str = json.dumps(r)
with open('wordlist.json', 'w') as f:
    f.write(file_str)
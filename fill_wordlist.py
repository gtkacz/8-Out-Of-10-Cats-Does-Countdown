import re, warnings, json
from tqdm import tqdm
from bs4 import BeautifulSoup
from pathlib import Path
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

def tag_cleanup(html):
    html = str(html)
    cleanr = re.compile('<.*?>')
    string = (re.sub(cleanr, '', html))
    string = string.replace('\n', '')
    string = string.replace('\t', '')
    return string

def main():
    warnings.filterwarnings('ignore')
    
    url = r'https://www.oxfordlearnersdictionaries.com/us/wordlists/oxford3000-5000'
    
    CUR_DIR = Path(__file__).parent
    PROGRAM = 'chromedriver.exe'
    PATH = CUR_DIR / PROGRAM
    
    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument('--headless')
    
    try:
        browser = webdriver.Chrome(PATH, options=OPTIONS)
        
    except WebDriverException:
        BINARY = 'D:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        # BINARY = askopenfilename()
        OPTIONS.binary_location = BINARY
        OPTIONS.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(PATH, options=OPTIONS)
        
    try:
        browser.get(url)
        WebDriverWait(browser, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'top-g')))
        source = browser.page_source
        browser.quit()
        
        soup = BeautifulSoup(source, 'html.parser')
        wordlist = []
        
        table = soup.find_all('ul', class_ = 'top-g')[0]
        
        for row in tqdm(table.find_all('li')):
            for word in row.find_all('a', href = True):
                wordlist.append(tag_cleanup(word))
                
        file_str = json.dumps(wordlist)
        with open('wordlist.json', 'w') as f:
            f.write(file_str)
    
    except TimeoutException:
        try:
            browser.quit()
        finally:
            print('Site too long to respond.')
    
if __name__ == '__main__':
    main()
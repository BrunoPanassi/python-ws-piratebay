from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import json

movie = None
while movie is None:
    try:
        movie = str(input('Type a movie: '))
    except:
        print('Type a movie name!')

binary = FirefoxBinary(r'C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
firefox = webdriver.Firefox(firefox_binary=binary, executable_path = r'F:\\Bruno\\Projects\\Python\\web_scrapping_dio\\python_ws_piratebay\\geckodriver\\geckodriver.exe')
firefox.get('https://thepiratebay.org/index.html')

try:
    searchMovie = WebDriverWait(firefox, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'input'))
    )
except:
    print('Could not find tag - input')

if searchMovie is not None:
    searchMovie.send_keys(movie)
    searchMovie.send_keys(Keys.ENTER)

    firefox.implicitly_wait(20)
    itemTitle = firefox.find_elements_by_css_selector('span.item-title')

    qualities = ['720p', '1080p', '2160p']
    notQualities = ['HD-TS', 'HDTS', 'HDCAM']
    movies_in_HD = []
    
    for item in itemTitle:
        tag_a = item.find_element_by_tag_name('a')
        movie_title = tag_a.text
        haveQuality = False

        for quality in qualities:
            if (quality in movie_title):
                haveQuality = True
            
        for notQuality in notQualities:
            if (notQuality in movie_title):
                haveQuality = False 

        if haveQuality and len(movies_in_HD) <= 4:
                movies_in_HD.append(
                    {
                        'title':movie_title,
                        'link':tag_a.get_attribute('href')
                    }
                )

    with open('piratebay_links.json', 'w', encoding='utf-8') as json_file:
        json.dump(movies_in_HD, json_file, ensure_ascii=False)
    


    
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

movie = None
while movie is None:
    try:
        movie = str(input('Type a movie: '))
    except:
        print('Type a movie name!')

firefox = webdriver.Firefox(executable_path = 'F:\Bruno\Projects\Python\web_scrapping_dio\python_ws_piratebay\geckodriver\geckodriver.exe')
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
    item_title = firefox.find_elements_by_css_selector('span.item-title')

    qualities = ['720p', '1080p', '2160p']
    movies_in_HD = []
    
    for item in item_title:
        tag_a = item.find_element_by_tag_name('a')
        movie_title = tag_a.text

        for quality in qualities:
            if (quality in movie_title) and (movie_title not in movies_in_HD):
                if len(movies_in_HD) <= 4:
                    movies_in_HD.append(
                        {
                            'title':movie_title,
                            'link':tag_a.get_attribute('href')
                        }
                    )
                else:
                    break
    
    for movie in movies_in_HD:
        for index, value in movie.items():
            print(index)
            print(value)
            print('')


    
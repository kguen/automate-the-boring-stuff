import random, pyinputplus as pyip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome() 
keys = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT] # game control keys

# open 2048 page
browser.get('https://play2048.co')
htmlElem = browser.find_element_by_tag_name('html')

# game loop
while True:
    move = random.randint(0, 3) # random move
    htmlElem.send_keys(keys[move])
    # if game over
    if len(browser.find_elements_by_class_name('game-over')) > 0:
        restart = pyip.inputYesNo('Try again? ')
        if restart == 'yes':
            browser.find_element_by_class_name('retry-button').click()
        else: break
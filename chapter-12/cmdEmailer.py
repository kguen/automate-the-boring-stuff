from selenium import webdriver
browser = webdriver.Chrome()

# open gmail page
browser.get('https://gmail.com')

# enter email
email = input('Enter your email:\n')
emailElem = browser.find_element_by_css_selector('input[type="email"]')
emailElem.send_keys(email)

# go to password page
spanElems = browser.find_elements_by_tag_name('span')
for item in spanElems:
    # find submit button
    if item.text == 'Tiếp theo':
        item.click()

# gmail tự động chặn selenium
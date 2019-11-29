    import pyautogui
    import random
    import string
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time

    err_pct_start = 0
    err_pct_end = 0
    RAND_ERR = list(range(err_pct_end, err_pct_start)) #percent random errors
    RAND_ERR.reverse() # Get better over time

    ######### Open website, size window
    url = 'https://www.keybr.com/login/voNk9utBn7' # -- psantos.stomboli 13qe!#QE
    print('webdriver')
    browser = webdriver.Chrome('c:/bin/chromedriver.exe')
    browser.set_window_size(1580,800)
    print('open website')
    browser.get(url)
    block_name = 'TextInput'

    pyautogui.PAUSE = 0.077 #149 wpm


    # Get HTML
    def get_html(err):
        html = browser.page_source
        bs = BeautifulSoup(html, 'html.parser')
        charList = [];

        count = 0
        namelist = bs.findAll('span', {'class':'TextInput-item'})
        for name in namelist:
            # print('Getting text for ', name)
            txt = name.get_text()
            if txt == chr(9251):
                charList.append('space')
            else:
                charList.append(txt)
            count = count + 1

        # Insert Errors
        num_errs = round(count * err/100)
        error_indices = random.sample(list(range(1, count)), num_errs)

        for x in error_indices: # change index
            new_char = random.choice(string.ascii_letters + string.digits)
            charList.insert(x, new_char)
            charList[x] = random.choice(string.ascii_letters + string.digits)
        print('Number of errors = ', num_errs)
        print('Number of Characters = ', count)
        ##################
        return charList


    # Typing function
    def typeaway(character_list):
        print('get html')
        for char in character_list:
            pyautogui.press(char)


    # Main
    for i in range(1,30): #RAND_ERR:
        print('Pause between keystrokes = ', pause_val)
        characters = get_html(0)
        pyautogui.PAUSE = pause_val
        typeaway(characters)
        time.sleep(2)
        #pause_val = pause_val - 0.001



import requests, time, random
import pyautogui as pag
from bs4 import BeautifulSoup

# 10ff.net
def write3():
    t = random.uniform(0.05, 0.1)
    html = str(input('''input html: '''))
    soup = BeautifulSoup(html, 'html.parser')
    words = [span.text for span in soup.find_all('span')]
    for i in range(random.randint(3, 15)):
        words.insert(random.randint(0, len(words)-1), 'jk') # typing the wrong words intentionally
    os.system('clear')
    time.sleep(2)
    for word in words:
        pag.write(word)
        pag.press('space')
        time.sleep(t)
    print('done')


while True:
    write3()

# example html
'''
<div class="place" style="top: 4px;"><span class="highlight">like</span><span class="">mountain</span><span
        class="">good</span><span class="">group</span><span class="">who</span><span class="">let</span><span
        class="">even</span><span class="">young</span><span class="">us</span><span class="">not</span><span
        class="">by</span><span class="">from</span><span class="">only</span><span class="">along</span><span
        class="">word</span><span class="">went</span><span class="">as</span><span class="">come</span><span
        class="">far</span><span class="">sound</span><span class="">river</span><span class="">many</span><span
        class="">one</span><span class="">is</span><span class="">that</span><span class="">are</span><span
        class="">must</span><span class="">side</span><span class="">its</span><span class="">head</span><span
        class="">leave</span><span class="">too</span><span class="">where</span><span class="">car</span><span
        class="">before</span><span class="">eat</span><span class="">do</span><span class="">came</span><span
        class="">mother</span><span class="">my</span><span class="">only</span><span class="">mile</span><span
        class="">man</span><span class="">want</span><span class="">be</span><span class="">do</span><span
        class="">tell</span><span class="">would</span><span class="">most</span><span class="">down</span><span
        class="">form</span><span class="">left</span><span class="">way</span><span class="">very</span><span
        class="">above</span><span class="">line</span><span class="">see</span><span class="">time</span><span
        class="">if</span><span class="">these</span><span class="">its</span><span class="">food</span><span
        class="">left</span><span class="">another</span><span class="">in</span><span class="">thing</span><span
        class="">let</span><span class="">go</span><span class="">were</span><span class="">must</span><span
        class="">plant</span><span class="">form</span><span class="">state</span><span class="">right</span><span
        class="">our</span><span class="">eat</span><span class="">near</span><span class="">look</span><span
        class="">like</span></div>
'''

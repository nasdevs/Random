from time import sleep
import keyboard as key
import pyautogui as pag
import re

# web = str(input('Input web : '))
web = 'https://komiku.id/ch/reincarnation-of-the-suicidal-battle-god-chapter-'
    
def chapter(n):
    pag.hotkey('ctrl', 'l')
    pag.write(web + str(n))
    pag.press('enter')

class Ads:
    # komikindo.id
    def ads_1():
        pag.click(870, 617)
        sleep(1)
        pag.hotkey('ctrl', 'w')
    
    # 1stkissmanga.io
    def ads_2():
        pag.click(24, 912)

if __name__ == '__main__':
    print('running...')
    C = int(input('Input chapter : '))

    # scroll
    key.add_hotkey('j', lambda: key.press('pagedown'))
    key.add_hotkey('k', lambda: key.press('pageup'))

    # remove ads
    key.add_hotkey('1', lambda: Ads.ads_1())
    key.add_hotkey('2', lambda: Ads.ads_2())

    while True:
        # next and previously chapter
        if key.read_key() == 'n':
            print('n is pressed')
            C+=1
            chapter(C)
        if key.read_key() == 'p':
            print('p is pressed')
            C-=1
            chapter(C)

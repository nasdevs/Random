# created : 21.7.2022

# modules
import re # for find all spesific from a string
import os # clear terminal

n = int(input('input number of line : '))
lyric = [str(input(f'input line {i+1}: ')) for i in range(n)]

# convert letter to emoji
let_to_emoji = {
    'a': '😲',
    'i': '😬',
    'u': '😗',
    'e': '😦',
    'o': '😮',
}

# clear terminal
os.system('clear')
print('------result------')

# get line by line from lyric list
for words in lyric:
    # find all letter a i u e o and space for condition space between words
    letters = re.findall('[aiueo ]', words)
    
    # get letter by letter from letters list
    for let in letters:
        # convert letter to emoji using dictonary
        print(let_to_emoji[let.lower()] if let != ' ' else ' ', end='')
    
    print(f'\n({words})\n')

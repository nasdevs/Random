'''
@name : Typing Test
@version : 0.1.0
@upgrade to speed typing test : coming soon
'''

text = str(input('Input text : '))
text = text.split()

score = 0

for i in text:
    print('->', i)
    N = str(input())
    if N == i:
        score += 1

print(f'''
-----------SCORE-----------
Correct words : {score}
Total words   : {len(text)}
''')

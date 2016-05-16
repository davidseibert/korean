# coding 'utf-8'

with open ('freq', 'rb') as f:
    lines = f.readlines()



print lines
num_lines = len(lines)
num_words = num_lines / 3
print num_lines
print num_words
words = []

def get_words():
    i = 0
    while i < len(lines) - 3:
        words.append((lines[i], lines[i+1].decode('utf-8'), lines[i+2]))
        i += 3


get_words()
print words[0][1]

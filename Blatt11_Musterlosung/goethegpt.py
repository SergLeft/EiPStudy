import random
import string

punctuation = list(string.punctuation)

def train():
    successors = {}
    file = open('faust.txt', 'r', encoding='utf-8')
    text = file.read()
    text = text.replace('\n', ' ')
    for p in punctuation:
        text = text.replace(p, '')
    text = text.lower()
    words = text.split()
    for i in range(len(words) - 1):
        w = words[i]
        if w not in successors:
            successors[w] = []
        successors[w].append(words[i + 1])
    file.close()
    return successors

def generate(successors, start, n):
    result = [start]
    for i in range(n):
        if start in successors:
            start = random.choice(successors[start])
            result.append(start)
        else:
            break
    s = ""
    for word in result:
        s += word + " "
    return s

successors = train()
print(generate(successors, 'faust', 10))

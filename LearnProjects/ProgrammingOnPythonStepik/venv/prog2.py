# подсчёт количества слов в тексте

inputText = [str(i.lower()) for i in input().split()]
outputText = {}
for i in inputText:
    if i not in outputText:
        outputText[i] = inputText.count(i)
    else:
        continue
for key, object in outputText.items():
    print(key, object)
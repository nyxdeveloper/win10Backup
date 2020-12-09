# самое частое слово в тексте

inputFile = open('text.txt', 'r')
text = inputFile.read().lower().split()
inputFile.close()
count = 0
word = str()
for i in text:
    if count < text.count(i):
        count = text.count(i)
        word = i

outputFile = open('text.txt', 'w')
outputFile.write(word+' '+str(count))
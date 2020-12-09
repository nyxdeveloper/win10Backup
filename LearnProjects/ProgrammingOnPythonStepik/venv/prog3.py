# декодирование генома

inputFile = open('coded_genome.txt', 'r')
codedGenome = inputFile.readline()
inputFile.close()
decodedGenome = ''
counts = []
items = []
number = ''
codedGenome+='a'
for i in codedGenome:
    if i < 'A':
        number+=i
    else:
        if number=='':
            continue
        else:
            counts.append(number)
            number = ''
codedGenome = codedGenome[0:-1]
for i in codedGenome:
    if i >= 'A':
        items.append(i)

print(counts)
print(items)


outputFile = open('decoded_genome.txt', 'w')
for i in range(len(items)):
    outputFile.write(items[i]*int(counts[i]))
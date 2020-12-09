# кодирование генома

genome = input()
genome = genome.lower()
genome=genome+'.'
counter = 1
sgenome =''
for i in range(len(genome)-1):
    if genome[i]==genome[i+1]:
        counter+=1
    else:
        sgenome+=genome[i]+str(counter)
        counter=1
print(sgenome)
# электронный дневник

iFile = open('text.txt', 'r', encoding='utf-8')
rf = iFile.read().split('\n')
iFile.close()
assessments = []
totalPoints = []

for i in rf:
    assessments.append(i.split(';'))

for i in assessments:
    del i[0]

for i in assessments:
    j = (int(i[0])+int(i[1])+int(i[2]))/3
    totalPoints.append(j)

firstTheme = []
secondTheme = []
thirdTheme = []

for i in assessments:
    firstTheme.append(i[0])
    secondTheme.append(i[1])
    thirdTheme.append(i[2])

sumPoints = 0

for i in firstTheme:
    sumPoints+=int(i)

sumPoints = sumPoints/len(firstTheme)
firstTheme.clear()
firstTheme.append(sumPoints)
sumPoints = 0

for i in secondTheme:
    sumPoints+=int(i)

sumPoints = sumPoints/len(secondTheme)
secondTheme.clear()
secondTheme.append(sumPoints)

sumPoints = 0

for i in thirdTheme:
    sumPoints+=int(i)

sumPoints = sumPoints/len(thirdTheme)
thirdTheme.clear()
thirdTheme.append(sumPoints)

totalStats = str(str(firstTheme[0])+' '+str(secondTheme[0])+' '+str(thirdTheme[0]))

totalPoints.append(totalStats)

oFile = open('total_points.txt', 'w')

for point in totalPoints:
    oFile.write(str(point)+'\n')
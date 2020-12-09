# навигатор
n = int(input())
north = 0
east = 0
for i in range(n):
        s = input().split(' ')
        if s[0] == 'юг':
            north += -int(s[1])
        elif s[0] == 'север':
            north += int(s[1])
        elif s[0] == 'запад':
            east += -int(s[1])
        elif s[0] == 'восток':
            east += int(s[1])
print(east, north)
# поисковик по пространствам имён
class nmspc(list):
    names = {"global": ["None"],"None":[]}
    def create(self, space, parent):
        self.names[parent].append(space)
        self.names[space] = [parent]
    def add(self, space, var):
        self.names[space].append(var)
    def get(self, space, var):
        if space == "None":
            return
        if var in self.names[space]:
            print(space)
            return
        elif self.names[space][0] != "None":
            self.get(self.names[space][0], var)
            return
        else:
            print("None")
        return
a = nmspc()
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == "add":
        a.add(s[1], s[2])
    elif s[0] == "create":
        a.create(s[1], s[2])
    else:
        a.get(s[1], s[2])
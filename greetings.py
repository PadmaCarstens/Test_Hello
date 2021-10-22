class article:
    def _init_(self,name,number):
        self._name=name 
        self._number=number

    def getname(self):
        return self._name

    def getarticlenum(self):
        return self._number

    def printart(self):
        print("article name is"+str(self))

    def _str_(self):
        return self._name+","+self._number

articles= [ article("brown", "123"), article("riley", "456") ]

for article in articles:
    article.getarticlenum()

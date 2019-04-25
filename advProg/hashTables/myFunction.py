class HashTable:

    def __init__(self,L):
        self.buckets = [''] * L
        self.things = 0.0

    def assign(self,val,rawKey):
        self.buckets[self.getKey(rawKey)] = val
        self.things += 1
        self.resizeCheck()
        print 'Done!'

    def retrieve(self,rawKey):
        return self.buckets[self.getKey(rawKey)]

    def getKey(self,rawKey):
        key = 0
        for letter in rawKey:
            key *= ord(letter)
        return key % len(self.buckets)

    def resizeCheck(self):
        while self.things / len(self.buckets) > 0.07:
            for i in range(len(self.buckets)):
                self.buckets.append([''])
            print 'needed to resize. new length:',len(self.buckets)


hs = HashTable(input('Enter initial length: '))

hs.assign(raw_input('Enter a new value: '),raw_input('Enter a new key: '))

print hs.retrieve(raw_input('Enter pre-existing key: '))

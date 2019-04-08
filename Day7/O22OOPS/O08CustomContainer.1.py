class pythonDictionary:
    def __init__(self):
        self.pairs = {}

    def add(self, val):
        self.pairs[val.lower()] = self.pairs.get(val.lower(), 0)+1

    def __iter__(self):
        return iter(self.pairs.items())

    def __getitem__(self, val):
        return self.pairs.get(val.lower(), 0)

    def __setitem__(self, val, count):
        self.pairs[val.lower()] = count

    def __len__(self):
        return len(self.pairs)


python = pythonDictionary()
python.add('python')
python.add('python')
python.add('python')
python.add('python')


for i in python:
    print(i)

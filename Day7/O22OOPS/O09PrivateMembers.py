'''
__var - private member
_var - static member
outside method inside class - Class variable
inside method - instance variable
'''


class pythonDictionary:
    def __init__(self):
        self.__pairs = {}
        self.name = "python"
        self.partner = "language"

    def add(self, val):
        self.__pairs[val.lower()] = self.__pairs.get(val.lower(), 0)+1

    def __iter__(self):
        return iter(self.__pairs.items())

    def __getitem__(self, val):
        return self.__pairs.get(val.lower(), 0)

    def __setitem__(self, val, count):
        self.__pairs[val.lower()] = count

    def __len__(self):
        return len(self.__pairs)


python = pythonDictionary()
print(python.__dict__)
print(python._pythonDictionary__pairs)

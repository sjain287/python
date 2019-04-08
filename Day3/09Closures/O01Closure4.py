def greet(msg):
    def separator(sep):
        def person(name):
            print(f'{msg}{sep}{name}')
        return person
    return separator


# currying
greet("Welcome")("-->")("Rajni")
greet("Welcome")("-->")("Shivaji")

print("_" * 30)
name_fun = greet("Namaskaram")(":")
name_fun("Guru")
name_fun("Shankar Guru")
name_fun("Guru Shishyan")

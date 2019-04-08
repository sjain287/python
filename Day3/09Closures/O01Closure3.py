def greet(msg):
    grt_msg = msg

    def person(name):
        per_name = name
        print(f'{grt_msg}: Mr.{per_name}')

    return person


# Curring
greet("Hello")("Rajni")  # Greet is returning person
greet("Hello")("Shivaji Rao")
greet("Hello")("Super Star")
greet("Hello")("Rajni Saar")

print("_"*30)
per_fun = greet("Welcome")
per_fun("Sachin")
per_fun("Saurav")
per_fun("Rahul")
per_fun("VVS")

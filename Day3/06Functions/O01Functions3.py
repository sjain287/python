
def greet(first_name, last_name="Tendulkar"):
    print(f"Hello Mr.{first_name}")
    print(f"Welcome Mr.{last_name}")
    print("Here we are.............")


greet("Sachin")

print("_" * 30)
greet("Sachin", "Ramesh")
print("_" * 30)

greet("Ramesh", "Sachin")
print("_" * 30)
greet(last_name="Ramesh", first_name="Sachin")

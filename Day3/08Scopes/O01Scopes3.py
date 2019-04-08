# nested functions
name = "Shiv"


def college():
    name = "Shankar"

    def room():
        nonlocal name  # refer the variable which is not local but available in parent
        name = "Param"
        print("room", name)
    room()
    print("College", name)


college()
print("Main", name)

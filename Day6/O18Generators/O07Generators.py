def hold_client(name):
    yield f"hello {name} !! you will bw connected to our officer"
    yield f"Dear {name}!!! Please wait they are busy"
    yield f"{name}: We play some music for you"
    yield f"{name} : Your call is important to us!"


for msg in hold_client("sachin"):
    print(msg)

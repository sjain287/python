info = "Agra's Taj Mahal in Agra a white marble monument Agra"
print(info)
print(info.center(80))
print(info.center(60, "*"))

print(info.find("Taj"))
print(info.find("Mahal"))
print(info.find("mozument"))
print(info.find("Agra"))
print(info.find("Agra", 1))
print(info.find("Agra", info.find("Agra")+1))
print(info.find("Agra", 1, 25))
print("End of find".center(40, "-"))


val = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(val))
dirs = 'c:', 'program files', '.net 4.0', 'tools'
print('\\'.join(dirs))


string_val = '\\'.join(dirs)
print(string_val)

print(string_val.split('\\'))
print(".".join(string_val.split('\\')))

print(" ".join(reversed(string_val.split('\\'))))

info = 'life like music'
print(" ".join(reversed(info.split(' '))))


table = str.maketrans('ls', 'Wz')
print(info.translate(table))

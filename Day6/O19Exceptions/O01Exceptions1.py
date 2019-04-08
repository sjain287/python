#num = 2
import sys
num = 0
inv = 0
try:
    print("Apple")
    print("Orange")
    inv = 1/num
    print("Pine")
except:
    print('Exception'.center(30, '*'))
    print(f'haaaaa {sys.exc_info()[0].__name__} happened')
    print('Handled'.center(30, '*'))

print("Prunes")
print(inv)
print("Mango")


print("_" * 50)

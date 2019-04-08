import sys
num = '2'
# num = 0
inv = 0
try:
    print("Apple")
    print("Orange")
    inv = 1/num
    print("Pine")
except ValueError:
    print('Value Error'.center(30, '*'))
    print('Error handled'.center(30, '*'))
except (TypeError, ZeroDivisionError):
    print('Division Error'.center(30, '*'))
    print('Error handled'.center(30, '*'))
except:
    print('Exception'.center(30, '*'))
    print(f'haaaaa {sys.exc_info()[0].__name__} happened')
    print('Handled'.center(30, '*'))
finally:
    print("Finally always excutes")

print("Prunes")
print(inv)
print("Mango")


print("_" * 50)

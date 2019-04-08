from math import pi, e

name = "Sachin"
fame = "cricket"
print("{nm}\t{}\t{fm}\t{}".format(pi, e, nm=name, fm=fame))
print("{nm}\t{1}\t{fm}\t{0}".format(pi, e, nm=name, fm=fame))

my_name = ["Ilayaraja", "Maestro"]
print(my_name[1])
print(my_name[0])

print("Mr.{nm[0]}".format(nm=my_name))


print("{pi!s} {pi!r} {pi!a}".format(pi="A"))

print("{num} {num:f} {num:b}".format(num=10))
print("{num:10} {num:5} {num:2}".format(num=10))
print("{num:-10} {num:-5} {num:-2}".format(num=10))

print("{pi:1.2f}".format(pi=pi))
print("{pi:2.3f}".format(pi=pi))
print("{pi:3.5f}".format(pi=pi))
print("{pi:10.6f}".format(pi=pi))


print("{:.5}".format("Sachin"))
print("One googol is {}".format(10**100))
print("One googol is {:,}".format(10 ** 100))

print("*"*30)
print("{0:.012f}".format(123.342))
print("{0:.<01212.4f}".format(123.342))
print("{0:.^01212.4f}".format(123.342))
print("{0:>012.4f}".format(123.342))
print("*" * 30)

# augment
print("{0:$<12.3f}".format(123.432))
print("{0:*^12.3f}".format(123.432))
print("{0:&>12.3f}".format(123.432))

print("*" * 30)
print("{0:10.2f}\n{1:10.2f}".format(pi, -pi))
print("{0:10.2f}\n{1:=10.2f}".format(pi, -pi))
#print("{0:10.2f}\n{1:$10.2f}".format(pi, -pi))

print("*" * 30)

# print("{0:.2f}\n{1:2f}".format(124.432))

print("{:b}".format(10))
print("{:#b}".format(10))
print("{:o}".format(10))
print("{:#o}".format(10))
print("{:x}".format(10))
print("{:#x}".format(10))
print("{:g}".format(10))  # decimal
print("{:#g}".format(10))

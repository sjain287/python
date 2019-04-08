print(1 + 2)
print('1' + '2')

'''
isnumeric()
isdigit
isdecimal()
...
'''

var1 = "dac123"
var2 = "123"
var3 = "123.54"

print(var1.isnumeric())
print(var2.isnumeric())
print(var3.isdecimal())
# print(type(var1))
# print(type(var2))
# print(type(var3))

#print("Hello %s,you scored %s out of %i" % ("Sachin", var2, 100))
print("_"*50)
print("Hello %s,you scored %s out of %i" % ("Sachin", var2, 100))

print("Hello" +

      "CDAC")
print(1 + 2
      + 3
      + 5)

print("c:\nowhere")
print("c:\\nowhere")
print(r"c:\nowhere")
print(r"c:\abc\dog\buffalo\nowhere")
print("This is a cat \N{Cat}".encode("UTF-32"))

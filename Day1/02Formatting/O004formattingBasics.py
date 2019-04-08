# 1 classical printf emulate
frm_str = "Hello Mr.%s %s talented Guy"
val_info = ('Scahin', "Super")

print(frm_str % val_info)
val_info = ('Scahin', 1000)  # 1000 convered as string
print(frm_str % val_info)

frm_str = "Hello Mr.%s %.3f talented Guy"
val_info = ('Scahin', 1000)  # 1000 taken as float
print(frm_str % val_info)

# Key value argument (kwargs)
def Get_Info(**info):
    print(info)
    print(info['three'])


Get_Info(one=10, two=20, three=30)

import random
list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',1,2,3,4,5,6,7,8,9,0]
for h in range(2000000000000):
    for i in range(3):
        a=random.sample(list,5)
        b=random.sample(list,5)
        c=random.sample(list,5)
        str=[]
        str+=a
        str+="-"
        str+=b
        str+="-"
        str+=c


        for j in range(17):
            print(str[j],end="")
        print("")
        




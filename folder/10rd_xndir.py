#2rd tarberaki 10y

def duplicate(string):
    datark=""
    for x in string:
        if x not in datark:
            datark+=x
    return datark
print(duplicate("lavutyun"))

#1in tarberaki 10y
def zuyg(listt):
    b=[]
    for x in listt:
        if x%2==0:
            b.append(x)
    return b
print(zuyg([1,2,3,4,5,6,7,8,9,10]))

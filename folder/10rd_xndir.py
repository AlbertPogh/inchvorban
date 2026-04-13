def duplicate(string):
    datark=""
    for x in string:
        if x not in datark:
            datark+=x
    return datark
print(duplicate("lavutyun"))

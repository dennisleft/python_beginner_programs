
##st = str([1,21,31,41,51,61,71,81,91])

#### rd = all numbers ending with 3 apart from 13
##number_list_1=[]
##user_input = int(input('Enter number: '))

##for i in range(9):
##    for x in range(1,10):
##        number=x*100+st[i]
##        number_list_1.append(number)
##
##
##if user_input in number_list_1 or st:
##    print(str(user_input)+'st')
##else:
##    print('not working')


##slicing


def suffix():
    user_input = int(input('Enter number: '))##object
    sliced_input_2=str(user_input)[-2:] ##common
    sliced_input_1=str(user_input)[-1] ##common
    if sliced_input_1==str(1): ##1 and 11, 2 and 12, 3 and 13, rest
        if sliced_input_2==str(11):
            return str(user_input)+'th'
        else:
            return str(user_input)+'st'
    elif sliced_input_1==str(2):
        if sliced_input_2==str(12):
            return str(user_input)+'th'
        else:
            return str(user_input)+'nd'
    elif sliced_input_1==str(3):
        if sliced_input_2==str(13):
            return str(user_input)+'th'
        else:
            return str(user_input)+'rd'
    else:
        return str(user_input)+'th'
for i in range(5):
    print(suffix())
####################################################







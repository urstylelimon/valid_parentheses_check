s = "{(})"
list = []
flag = False

opening_bracket = ['(','{','[']
closing_brackets = [')','}',']']
map = {
    ')' : '(',
    '}' : '{',
    ']' : '['
}

for i in s:
    if i in opening_bracket:
        list.append(i)

    if i in closing_brackets:
        if map[i] not in list:
            flag = False
            break

        if len(list) == 0:
            flag = False
            break
        if len(list) != 0 and list[-1] == map[i]:
            flag = True
            list.pop()




if len(list) > 0 :
    flag = False

if flag :
    print("True")

else:
    print("False")



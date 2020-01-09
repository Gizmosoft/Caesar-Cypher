new_inp = ""
while new_inp != "end":
    new_inp = input("")
    # print(type(new_inp)) --> str
    key = input('Enter the key size:  ')
    l = len(new_inp)
    inp = list(new_inp)
    # print(type(inp))
    # print("length of list: "+ str(len(inp))) -----> 5 w+o+r+d+s
    result = []
    for i in range(l):
         result.append(chr(ord(inp[i])+int(key)))
    result = ''.join(map(str, result))
    print(result)

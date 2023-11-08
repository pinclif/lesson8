def gai_ylii_cezar(move,step):
    move += 1
    code = ''
    for i in step:
        if i.isalpha():
            code += chr(ord(i)+move)
        else:
            code += i
    return code
with open('hello.txt') as fil:
    for move,step in enumerate(fil.readlines()):
        print(gai_ylii_cezar(move,step))
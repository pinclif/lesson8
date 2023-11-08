with open('stop_words.txt','r') as stop, open('original.txt','r') as trans:
    f = stop.read().split()
    d = trans.read().split()
    for i in d:
        z, k = 0, 0
        for j in f:
            if j in i.lower():
                while i[0].lower() !=j[z]:
                    z += 1
                p = i[z:len(j)]
                k = 1
        print(len(p) * '*' + i[len(p):]if k == 1 else i, end= ' ')
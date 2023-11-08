with open ('text.txt','r') as f:
    s = list(map(lambda i:i.strip('.,!?'),f.read().lower().split()))
    m = max(sorted(s), key = lambda j: s.count(j))
    print(f'Word',m,f'meets',s.count (m),f'times')
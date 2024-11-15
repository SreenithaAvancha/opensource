n=int(input())
k=int(input())
a=str(bin(n))[2:]
if k<=len(a) and a[-k]=='1':
    print('true')
else:
    print('false')

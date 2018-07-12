import sys
S = sys.stdin.read()
S = S.split()
S = [int(i) for i in S]
a = S[0]
b = S[1]
c = S[2]
if a>b and a>c :
	print(a)
elif(b>c):
	print(b)
else:
	print(c)
	

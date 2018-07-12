s=input("")
l=['a','e','i','o','u','A','E','I','O','U']
if((s>='a'and s<='z') or (s>='A'and s<='Z')):
	if s in l:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")

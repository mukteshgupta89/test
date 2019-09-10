import re
import string
word="hello inr1,364.08 ebit on debited card xx7000 on 26-may-19.info:godaddi india.avbl lmt:inr94,351.09.ca"
word = word.lower()
x=
re.sub('[^0-9]', '', x)
if "debit" in word or "debited" in word:
	print("HA ruko 1 min")

'''
#hogeya ab haa
thik hai
#mere pass 85,000 sms aageya hai abhi isko banake batata hun
ek aur dikkat hai abhi aage bataunga
7919 hai srif 7 utha raha
tume jo change kiya tha code usme
'''
'''

singles = [word.split()]
print(' '.join(singles))
	
if (any('debit' in s for s in singles) or any('txn' in s for s in singles) or any('use' in s for s in singles) or any('w/d' in s for s in singles)or any('withdrawn' in s for s in singles)or any('spent' in s for s in singles)):
 print("inside")
 
 haa ruko
 '''
from nltk.stem.porter import *
import json
import datetime
import re



header = []
sms = []
time = []
unique_bank=[]
unique_arr = []
final_3c_arr=[[]]
actual_mapping_arr = []
count_actual_mapping=0
count_unique_mapping=0
count_3c_arr=0
debit_msg_inside=0
credit_msg_inside=0
extra_msg_inside=0
extra_outside_loop=0

re_pattern_for_account_no_search=r"\bXX+[0-9]{3,}|\bX+[0-9]{3,}|\bxx+[0-9]{2,}|Txn#[0-9]{3,}|A/c ending+ [0-9]{3,}|a/cx+[0-9]{2,}$"

file1 = open("main_file_output.txt","w", encoding="utf-8-sig")

with open('muktesh_sms.json', encoding="utf-8-sig") as json_file:  			#input file Json and appending in 3 array header sms time
    data = json.load(json_file)
    for p in data['data']:
        header.append(p['contact_no'])
        sms.append('hello '+p['sms'])
        time.append((datetime.datetime.fromtimestamp(float(p['sms_time']) / 1e3)).strftime("%H:%M:%S.%f - %b %d %Y"))
		
for i in range(len(sms)):
	stemmer = PorterStemmer()
	singles = [stemmer.stem(word) for word in sms[i].split()]
	print(' '.join(singles))
	
	if (any('debit' in s for s in singles) or any('txn' in s for s in singles) or any('use' in s for s in singles) or any('w/d' in s for s in singles)or any('withdrawn' in s for s in singles)or any('spent' in s for s in singles)):
		
		acc = re.findall(re_pattern_for_account_no_search,sms[i])
		for j in range(len(acc)):
			if(acc[j]!=''):
				print("acc = "+str(acc[j]))       # we found account no in sample space step 1
				actual_mapping_arr.append(acc[j])  					
				if(acc[j] not in unique_arr):
					unique_arr.append(acc[j])
					
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, 1\n")		#1 for debit
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, 1\n")		#1 for debit
						break

	elif any('credit' in s for s in singles):
		acc = re.findall(re_pattern_for_account_no_search,sms[i])
		for j in range(len(acc)):
			if(acc[j]!=''):
				print("acc = "+str(acc[j]))       # we found account no in sample space step 1
				actual_mapping_arr.append(acc[j])  					
				if(acc[j] not in unique_arr):
					unique_arr.append(acc[j])
					
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for credit ", matchObj.group(8))
						credit_msg_inside=credit_msg_inside+1
						file1.write(sms[i]+"\, 2\n")		#2 for debit
						continue
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for credit ", matchObj.group(8))
						credit_msg_inside=credit_msg_inside+1
						file1.write(sms[i]+"\, 2\n")		#1 for debit
						continue
	
	else:
		extra_outside_loop=extra_outside_loop+1
		extra_msg_inside=extra_msg_inside+1
		file1.write(sms[i]+"\, 0\n")
print("Debit Msg are " +str(debit_msg_inside))
print("credit_msg_inside "+str(credit_msg_inside))
print("extra_msg_inside "+str(extra_msg_inside))



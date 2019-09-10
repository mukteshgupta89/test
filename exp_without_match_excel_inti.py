from nltk.stem.porter import *
import json
import datetime
import re
import array
from xlwt import Workbook
import xlrd
wb=Workbook()
sheet1=wb.add_sheet('sheet1')
#sheet1.write(0,0,'this is sheet one')


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
excel_count=0
sheet1.col(0).width=1000
sheet1.col(1).width=7000
sheet1.col(2).width=4000
sheet1.col(3).width=4000
sheet1.col(4).width=4000
sheet1.col(6).width=50000
sheet1.write(0,0,'S.no')
sheet1.write(0,1,'Date')
sheet1.write(0,2,'Tag_Name')
sheet1.write(0,3,'Account Detected')
sheet1.write(0,4,'Debit Detected')
sheet1.write(0,5,'Credit Detected')
sheet1.write(0,6,'SMS')
#re_pattern_for_account_no_search=r"\bXX+[0-9]{3,}|\bX+[0-9]{3,}|\bxx+[0-9]{2,}|Txn#[0-9]{3,}|A/c ending+ [0-9]{3,}|a/cx+[0-9]{2,}$"

file1 = open("main_file_output.txt","w", encoding="utf-8-sig")
######################Main Input Scouce File#################
'''
with open('Test_input.json', encoding="utf-8-sig") as json_file:  			#input file Json and appending in 3 array header sms time
    data = json.load(json_file)
    for p in data['data']:
        header.append(p['contact_no'])
        sms.append('hello '+p['sms'])
        time.append((datetime.datetime.fromtimestamp(float(p['sms_time']) / 1e3)).strftime("%H:%M:%S.%f - %b %d %Y"))

'''
'''
with open('80K_users_sms.json', encoding="utf-8-sig") as json_file: #input file Json and appending in 3 array header sms time
	data = json.load(json_file)
	for p in data['data']:
		header.append(p['contact_no'])
		sms.append('hello '+p['sms'].lower())
		time_date.append((datetime.datetime.fromtimestamp(float(p['sms_time']) / 1e3)).strftime("%d"))
		time_month.append((datetime.datetime.fromtimestamp(float(p['sms_time']) / 1e3)).strftime("%b"))
		time_year.append((datetime.datetime.fromtimestamp(float(p['sms_time']) / 1e3)).strftime("%Y"))
'''        
		
        

######################Testing JSON RUN#######################
with open('sms 15-08-2019 (contact no 10 & all unique sms).json', encoding="utf-8-sig") as json_file: #input file Json and appending in 3 array header sms time
    data = json.load(json_file)
    for p in data['data']:
        header.append(p['contact_no'])
		#p[sms]=p[sms].lower()
        sms.append('hello '+p['sms'].lower())
        time.append((datetime.datetime.fromtimestamp(float(p['sms_time']) / 1e3)).strftime("%H:%M:%S.%f - %b %d %Y"))


######################When input in array######################
'''
txtfile = open("two_debit.txt", 'r', encoding="utf-8-sig")
for line in txtfile.readlines():
    sms.append(line.rstrip().lower())
txtfile.close()
'''

for i in range(len(sms)):
	
	if ("debit" in sms[i] or "debited" in sms[i] or "use" in sms[i] or "used" in sms[i] or "spent" in sms[i]or "internet banking" in sms[i])and "card" not in sms[i]:
		print("###inside debit or debited or use or used or spent or internet banking&&&")
		acc = re.findall(r"\bXX+[0-9]{3,}|\bX+[0-9]{3,}|\bxx+[0-9]{2,}|a/c\b..+[0-9]{2,}|A/c ending+ [0-9]{3,}|a/cx+[0-9]{2,}$",sms[i])
		if acc:
			acc = re.findall('[0-9]*', acc[0]) #Extracting only numbers from account found in  acc also extracting only acc[0]
		for j in range(len(acc)):
			if(acc[j]!=''):
				print("acc = "+str(acc[j]))       # we found account no. 
				actual_mapping_arr.append(acc[j])  					
				if(acc[j] not in unique_arr):
					unique_arr.append(acc[j])
					
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						
						break
	
	
	elif "w/d@" in sms[i] or "withdrawn" in sms[i] or "ATM" in sms[i] or "used" in sms[i] or "spent" in sms[i]:
	#if (any('w/d@' in s for s in singles)or any('withdrawn' in s for s in singles) or any('ATM' in s for s in singles)or any('atm' in s for s in singles)):
		print("##########################inside ATM Withdar m,awal&&&&&&&&&&&&&&&&&&&&&&")
		acc = re.findall(r'x+[0-9]{3,}',sms[i])
		if acc:
			acc = re.findall('[0-9]*', acc[0])
		print(sms[i]) 
		
		
		if acc:
			print (acc[0])
		for j in range(len(acc)):
			print("inside j")
			if(acc[j]!=''):
				print("acc = "+str(acc[j]))       # we found account no in sample space step 1
				actual_mapping_arr.append(acc[j])  					
				if(acc[j] not in unique_arr):
					unique_arr.append(acc[j])
					
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						
						break
	
	elif (("txn" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i] or "Txn" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i]))and "card" not in sms[i] :
	#elif (any('txn of rs' in s for s in singles)):
		print("##########################inside internet banking&&&&&&&&&&&&&&&&&&&&&&")
		print(sms[i])
		acc = re.findall(r"x+[0-9]+|\bX+[0-9]{3,}",sms[i])
		print(acc)
		if acc:
			acc = re.findall('[0-9]*', acc[0])
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
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						
						break
	elif "sent" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i] :
	
		print("##########################inside sent &&&&&&&&&&&&&&&&&&&&&&")
		print(sms[i])
		acc = re.findall(r"x+[0-9]+|\bX+[0-9]{3,}",sms[i])
		print(acc)
		if acc:
			acc = re.findall('[0-9]*', acc[0])
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
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						
						break
	
	elif "card" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i] or "CARD" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i]  :
	
		print("##########################Card payments &&&&&&&&&&&&&&&&&&&&&&")
		print(sms[i])
		acc = re.findall(r"card [0-9]{3,}|Card [0-9]{3,}| +x+[0-9]+|\bX+[0-9]{3,}",sms[i])
		print(acc)
		print("ert")
		if acc:
			acc = re.findall('[0-9]*', acc[0])
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
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for debit ", matchObj.group(8))
						debit_msg_inside=debit_msg_inside+1
						file1.write(sms[i]+"\, D\n")		#1 for debit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,4,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						
						break
	
	
	
	
	
	elif "credit" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i] or "deposited" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i] :
	#elif (any('txn of rs' in s for s in singles)):
		print("##########################inside Credit and deposited &&&&&&&&&&&&&&&&&&&&&&")
		acc = re.findall(r"\bXX+[0-9]{3,}|\bX+[0-9]{3,}|\bxx+[0-9]{2,}|a/c\b..+[0-9]{2,}|A/c ending+ [0-9]{3,}|a/cx+[0-9]{2,}$",sms[i])
		if acc:
			acc = re.findall('[0-9]*', acc[0])
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
						file1.write(sms[i]+"\, C\n")		#2 for credit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,5,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for credit ", matchObj.group(8))
						credit_msg_inside=credit_msg_inside+1
						file1.write(sms[i]+"\, C\n")		#1 for credit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,5,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						
						break
	
	elif "chq" in sms[i] and "declined " not in sms[i] and "otp" not in sms[i] :
	
		print("##########################Cheque detection &&&&&&&&&&&&&&&&&&&&&&")
		acc = re.findall(r"\bXX+[0-9]{3,}|\bX+[0-9]{3,}|\bxx+[0-9]{2,}|A/c ending+ [0-9]{3,}|a/cx+[0-9]{2,}$",sms[i])
		if acc:
			acc = re.findall('[0-9]*', acc[0])
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
						file1.write(sms[i]+"\, C\n")		#2 for credit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,5,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						break
				else:
					matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',sms[i], re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
					if matchObj:         
						print ("matchObj.group(1) : for credit ", matchObj.group(8))
						credit_msg_inside=credit_msg_inside+1
						file1.write(sms[i]+"\, C\n")		#1 for credit
						excel_count=excel_count+1
						sheet1.write(excel_count,0,excel_count)
						sheet1.write(excel_count,1,time[i])
						sheet1.write(excel_count,2,header[i])
						sheet1.write(excel_count,3,acc[j])
						sheet1.write(excel_count,5,matchObj.group(8))
						sheet1.write(excel_count,6,sms[i])
						
						break
	
	
	
	
	
	
					
	
	else:
		extra_outside_loop=extra_outside_loop+1
		extra_msg_inside=extra_msg_inside+1
		file1.write(sms[i]+"\, other\n")
	

print("Debit Msg are " +str(debit_msg_inside))
print("credit_msg_inside "+str(credit_msg_inside))
print("extra_msg_inside "+str(extra_msg_inside))

###########Now Playing with info stored in excel file###########


wb.save('xlwt example.xls')
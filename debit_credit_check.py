import re
from money_parser import price_str
'''
row=[]

for line in txtfile.readlines():
    row.append(line.rstrip())
txtfile.close()

'''

#i="An amount of 200 INR has been debited to A/c no XXXXXXX1042545 by EFT Transfer on 07-MAY-19 00:15:40 For Account balance send SMS ACBAL ac?no to 9915622622\, 0"
#i = "Dear Customer your Account XX1009 has been credited with INR 5000.00 on 08-Feb-19. Info: BIL*INFT*001638443660*Family. The Available Balance is INR 9762.91"
i="Rs5000 w/d@SBI ATM S1BW000478027 fm A/cx2091 on02Jun19Txn#507Avl bal Rs30107 If not w/d by u,frwd this SMS to 9223008333 or call1800111109 to block ur card\, 0"
i= "Hello "+i
matchObj = re.match( r'(.*?)?(\s*)(inr|INR|Rs|rs|RS|inr.|INR.|Rs.|rs.|RS.|(amount(\s*)of)(\s*))(\s*)( *[0-9]+.?(\s*)[0-9]*)(\s*)(.*)?',i, re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the stringr'(.*?) (rs|rs |inr|inr |rs.|rs. )(.\d*\.\d+|.\d*) (.*)',i, re.M|re.I
if matchObj:         

    print ("matchObj.group(1) : ", matchObj.group(8))
    #print ("matchObj.group(2) : ", matchObj.group(14))
'''   
   print ("matchObj.group(3) : ", matchObj.group(3))                           
    print ("matchObj.group(4) : ", matchObj.group(4))
    print("price Found= " +price_str(matchObj.group(3)))
    print("Debited Amount = "+str(int(float(price_str(matchObj.group(3))))))        #  Print int value of debited amount
    
        
    if re.search(r"Balance\b | bal\b",matchObj.group(4)):       #regex to search balance in the str
        matchObj = re.match( r'(.*)(rs|rs |inr|inr |rs.|rs. )(.\d*\.\d+|.\d*)(.*)', i, re.M|re.I) # regex to find digits after inr|inr |rs.|rs. in the string
        if matchObj:
            print ("matchObj.group() : ", matchObj.group())
            print ("matchObj.group(1) : ", matchObj.group(1))
            print ("matchObj.group(2) : ", matchObj.group(2))
            print ("matchObj.group(3) : ", matchObj.group(3))
            print ("matchObj.group(4) : ", matchObj.group(4))
            print ("Avl Balance = "+ str(int(float(price_str(matchObj.group(3)))))) # Print int value of avl balance
'''
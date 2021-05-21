import requests
from bs4 import BeautifulSoup
import re
import termcolor
import pyfiglet

print("\t\t__"*25)
print(termcolor.colored("\t\t    My instagram:\n    \thttps://instagram.com/mostafa_elguerdawi", color = "red"))
print("\t\t__" *25)

print(" ")

print("\t\t", "#" *19)
print(" \t\t |♣Get Webs Data♣  |")
print("\t\t", "#" *19)

Shape = pyfiglet.figlet_format("Mostafa\nElgerdawi")
print(termcolor.colored(Shape, color = "green"))

while True:
	
	choose = input("1---> Get Emails\n2---> Get Phone Numbers\n===> ").strip()
	
	url = input("Enter Web Url: ")
	
	if choose == "1":
		
		response = requests.get(url).text
		
		soup = BeautifulSoup(response, 'html.parser')
		
		Email_regex = "\S{1,}\@\S{1,}"
		
		find = re.findall(Email_regex, soup.text)
		
		num = 1
		
		if len(find) >0:
		        
		        for email in find:
		        	
		        	print(" ")
		        	print("__"*20)
		        	print(f"{num} ==> {email}")
		        	print("__" *20)
		        	num += 1
		else:
		       print(" ")
		       print("__"*20)
		       print("No Emails Here...")
		       print("__"*20)
	    
	    
	elif choose == "2":
		
		response_2 = requests.get(url).text
		
		soup_2 = BeautifulSoup(response_2, 'html.parser')
		
		Email_regex_2 = "\+\d{1,}\s{1,}\d{1,}\s{1,}\d{1,}\s{1,}\d{1,}"
		
		find_2 = re.findall(Email_regex_2, soup_2.text)
		
		num_2 = 1
		
		if len(find_2) > 0:
		
		    for number in find_2:
			    print(" ")
			    print("__"*25)
			    print(f"{num_2} ===> {number}")
			    print("__"*25)
			    num_2 += 1
			    
		else:
		    print(" ")
		    print("__" *25)
		    print("No Numbers Here...")
		    print("__" *25)
		   
	else:
		print(" ")
		print("      \tError...Not in choice    ")
		print(" ")
	if choose == "Exit":
		print("Exit Succsefly")
		break

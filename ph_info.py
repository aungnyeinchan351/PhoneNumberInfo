import pyfiglet
import phonenumbers
from phonenumbers import timezone,carrier,geocoder
print(pyfiglet.figlet_format("Dust"))
print("=====================")
print("Phone Number Information")
print("++++++++++++++++++++++")
PhNum = input("Entet Phone Number : ")
Phone = phonenumbers.parse(PhNum)
Valid = phonenumbers.is_valid_number(Phone)
if Valid == True:
	Carrier = carrier.name_for_number(Phone,"en")
	TimeZone = timezone.time_zones_for_number(Phone)
	Region = geocoder.description_for_number(Phone,"en")
	print(Phone)
	print("ISP -- ",Carrier)
	print("Time Zone -- ",TimeZone)
	print("Region -- ",Region)
else:
	print("Invalid Phone Number")
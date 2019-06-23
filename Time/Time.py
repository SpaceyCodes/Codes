print ("How to use:")
print ("Enter number of seconds to convert it to hours, minutes, seconds.")
print ("__________________________________________")
total_sec = int(input("Enter number of seconds: "))
hours = total_sec//3600
sec_still_remaining = total_sec - hours * 3600
minutes = sec_still_remaining//60
seconds = sec_still_remaining - minutes * 60

print ("Hours:",hours ,"Minutes:",minutes ,"Seconds:",seconds)                                                             # By WenKang




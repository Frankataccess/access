#imports
import random
import time 
#character sets
basic = "abcdefghijklmnopqrstuvwxyz0123456789"
advanced = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%^&*()|/?,.<>;:'@#~[}]{+=-_`¬"
#advanced not running 
choice = input("would you like to use Basic character set (faster) or Advanced character set (slower): ")
if choice == "basic" or "B" or "Basic":
    allchar = list(basic)
else :
    allchar = list(advanced)
pwd = input("enter a password : ")

sample_pwd = ""

attempts=0

time_val = "seconds"

start_time = time.time ()

while (sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))

    attempts = attempts + 1

    print(attempts,")<===" + str(sample_pwd) + "===>")
    
    if (sample_pwd == list(pwd)):
        end_time = time.time()
        final_time = end_time-start_time
        if final_time >= 60:
            final_time = final_time / 60
            time_val ="minutes"
        elif final_time < 60 and final_time > 1:
            final_time = round(final_time,2)
            time_value = "seconds" 
        else:
            final_time = final_time
        print("after",attempts," attempts and",final_time, time_val,"the password is : "+"".join(sample_pwd))
        break
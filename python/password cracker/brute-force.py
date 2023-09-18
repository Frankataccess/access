#imports
import random
import pyautogui 
import time 

chars = "abcdefghijklmnopqrstuvwxyz123456789"


allchar = list(chars)

pwd = pyautogui.password("eneter a password : ")

sample_pwd = ""

attempts=0

start_time = time.time ()

while (sample_pwd != pwd):
    sample_pwd = random.choices(allchar, k=len(pwd))

    attempts = attempts + 1

    print(attempts,")<===" + str(sample_pwd) + "===>")
    
    if (sample_pwd == list(pwd)):
        end_time = time.time()
        final_time = end_time-start_time
        print("after",attempts," attempts and",final_time," seconds the password is : "+"".join(sample_pwd))
        break
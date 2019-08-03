#!//usr/bin/python3

from playsound import playsound
import os
import time

hostname = "8.8.8.8" #example



def alert(response):
  
    
    if response == 0: 
      playsound('/path/to/your/file')
    else:  
      playsound('/path/to/your/file')
            
def check():

    response = os.system("ping -c 3 " + hostname + " > /dev/null 2>&1 ")
    return response


state = check()
alert(state) 

while True:
  currstate = check()
  if(state != currstate):
     alert(currstate)
     state = currstate
      

    
         


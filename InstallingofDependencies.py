import subprocess
import sys
import json

f = open("requirements.json")
data=json.load(f)

failed=[]

for i in data["Dependencies"]:
   
   try:
      subprocess.check_call([sys.executable, "-m", "pip", "install", i])
   except:
      failed.append(i)


if failed:
   print('----Failed Dependencies------')
   for i in failed:
      print(i)
else:
   print('Success')




 

 

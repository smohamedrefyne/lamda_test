
import os
import subprocess

output = subprocess.check_output("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'", shell=True)
for dir in otput.split('/'):
  print (dir)
  os.system("aws lambda get-function --function-name %s")  (dir)
print ("working")


import os
import subprocess

output = os.popen("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'").read()
for dir in output.split('/'):
  print (dir)
  os.system("aws lambda get-function --function-name %s")  (dir)
print ("working")

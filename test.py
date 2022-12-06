
import os
import subprocess

output = os.popen("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'").read()
print (output)
for dir in output:
  print (dir)
  dir = dir.split('/')
  lambda_cmd = 'aws lambda get-function --function-name %s' % (dir)
  os.system(lambda_cmd) 
  print ("working")

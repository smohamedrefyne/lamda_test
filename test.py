
import os
import subprocess

output = os.popen("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'").read()
output = output.split("\n")
output.remove('')
print (output)
for dir in output:
  dir = dir.replace('/', '')
  zip_dir = 'zip -r temp.zip %s' % (dir)
  os.system(zip_dir)
  lambda_cmd = 'aws lambda update-function-code --function-name %s --zip-file "fileb://temp.zip"' % (dir)
  os.system(lambda_cmd) 
  os.system('rm -rf temp.zip')

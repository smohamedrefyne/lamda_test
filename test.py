
import os
dirs = os.system("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'")
for dir in dirs:
  print (dir)
  os.system("aws lambda get-function --function-name web")
print ("working")

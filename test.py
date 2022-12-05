
import os
os.system("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'")
print ("working")

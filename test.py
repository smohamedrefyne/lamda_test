
import os
os.system("git diff --dirstat=files,0 HEAD~1 | sed 's/^[ 0-9.]\+% //g'")
os.system("aws lambda list-functions --region us-south-1")

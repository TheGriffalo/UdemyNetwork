
import os.path
import time
import sys
import re

#Checkiing username/password file
#Prompting user for input - USEERNAME/PASSWORD FILE
user_file = input("\n# Enter user file path and name (e.g. /MyApps/myfile.txt) : ")

#Verifying the validity of the USWERNAME/PASSWORD file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid ;) \n")

else:
    print("\n* File {} does not exist :( Please check and try again.\n".format(user_file))
    sys.exit()

#Checking commands file
#Prompting user for input - COMMANDS FILE
cmd_file = input("\n# Enter commands file path and name (e.g. /MyApps/myfile.txt): ")

#Verifyiing the validity of teh COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid ;) \n")

else:
    print("\n* File {} does not exist :( Please check and try again. \n".format(cmd_file))
    sys.exit()



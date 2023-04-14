'''
Author: Mac Lawson
PoC: Server side execution CodeHS
'''

import subprocess

while True:
    command = input("$ ")
    if command == "exit":
        break
    
    # Execute the command in a subprocess
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Read the output and errors from the subprocess
    output, error = process.communicate()
    
    # Print the output and errors
    if output:
        print(output.decode("utf-8"))
    if error:
        print(error.decode("utf-8"))


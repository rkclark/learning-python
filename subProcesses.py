import subprocess

# Call a shell command from inside python
subprocess.call("ls", shell=True)

print("*****\n")

# Run the same command but this time save the output into a variable
output = subprocess.check_output("ls", shell=True, universal_newlines=True)
print(output)

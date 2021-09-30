import sys

# stderr out (red text)

sys.stderr.write("This is stderr text\n")
sys.stderr.flush()

# stdout

sys.stdout.write("This is stdout text\n")

# access args passed into py file from command line

print(sys.argv)

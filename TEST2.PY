import subprocess

# Run the "pip freeze" command and store the output in a variable
output = subprocess.check_output(["pip", "freeze"])

# Convert the output to a string and split it into a list of library names
library_list = output.decode("utf-8").split()

# Print the list of library names
print(library_list)

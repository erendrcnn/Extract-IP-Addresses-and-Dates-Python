# IP & Date Extracter (v0.1)

import re

# Open the input file
inputFile = open("log_task1.txt", "r")

# Will contain the entire content of the file as a string
database = inputFile.read()

# The regex pattern that we created
content = re.sub("/", "-", database)
patternDate = r"\d{1,2}[-](?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[-]\d{1,4}"
patternIP = r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}"

# Will return all the strings that are matched
matchDate = re.findall(patternDate, content)
matchIP = re.findall(patternIP, database)

# Write all output to file
with open("output_task1.txt", 'w') as fp1:
    for item in matchIP:
        fp1.write("%s\n" % item)
    fp1.close()

with open("output_task1.txt", "r+") as fp2:
    lines = list(fp2)
    fp2.seek(0)
    for i in range(min(len(lines), len(matchDate))):
        fp2.write(lines[i].rstrip('\n'))
        fp2.write(' ')
        fp2.write(str(matchDate[i]))
        fp2.write('\n')
    fp2.close()

"""                 -- EXAMPLE --
[INPUT] : log_task1.txt
54.36.148.10 - - [22/Jan/2019:03:56:58 +0330] ...
5.211.97.39 - - [22/Jan/2019:03:56:58 +0330] ...

[OUTPUT] : output_task1.txt
54.36.148.10 22-Jan-2019
5.211.97.39 22-Jan-2019
"""

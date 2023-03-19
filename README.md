# Extract-IP-Addresses-and-Dates-Python
In this program, you are asked to extract IP Addresses and Dates from the server logs. However, since the existing dates have unnecessary information we want you to convert the format as well. You should remove hour, minute and second part of the date and replace ’/’ characters of the date with ’-’.

# Example Input:
54.36.148.10 - - [22/Jan/2019:03:56:58 +0330] ...
5.211.97.39 - - [22/Jan/2019:03:56:58 +0330] ...

# Console Command:
python task1.py

# Example Output:
54.36.148.10 22-Jan-2019
5.211.97.39 22-Jan-2019

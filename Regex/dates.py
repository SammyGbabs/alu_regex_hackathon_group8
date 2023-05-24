import re
dates = re.compile(r'\b\d{2}-[A-Za-z]{3}-\d{4}\b')
print(dates)

import re

text = "My Roll Number is 12345"

result = re.search(r"\d+", text)

if result:
    print("Number Found:", result.group())
else:
    print("No Number Found")

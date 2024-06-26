import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\s)+@(\w|\s)?\w+\.(edu|com|uk|gov)$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")
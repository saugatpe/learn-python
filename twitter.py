import re
url = input("url: ").strip()

if matches := re.search(r"^(https?://?www\.)?twitter\.com/([a-z0-9]+)$",url, re.IGNORECASE):
    print(f"username:", matches.group(2))
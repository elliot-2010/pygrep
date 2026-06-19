import sys
import re

word = sys.argv[1]
file = sys.argv[2]

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

with open(file, "r") as f:
    lines = f.readlines()

ip_pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
email_pattern = re.compile(r"\w+@\w+\.\w+")

count = 0
for line in lines:
    if re.search(word, line):
        count += 1
        word_colored_line = re.sub(word, f"{RED}{word}{RESET}", line)
        print(word_colored_line)
        if "--ip" in sys.argv:
            ip = ip_pattern.search(line)
            if ip:
                print(f"{GREEN}{ip.group()}{RESET}")
        if "--email" in sys.argv:
            email = email_pattern.search(line)
            if email:
                print(f"{GREEN}{email.group()}{RESET}")
if "--count" in sys.argv:
    print(f"{YELLOW}{count}{RESET}")

import re
regex_pattern = r"[,\.](?=\d+)"	
print("\n".join(re.split(regex_pattern, input())))

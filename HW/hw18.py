import re
num = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
reg = "[+]?[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
print(re.findall(reg, num))
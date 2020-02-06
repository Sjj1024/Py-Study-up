import re

str1 = "1.day01_01_Java语言发展史(Av27219781,P4).mp4"
re_res = re.compile(r"\(.*?\)")
new_name = re_res.search(str1)
print(new_name.group())

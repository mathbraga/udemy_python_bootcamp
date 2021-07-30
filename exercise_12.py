import os
import re

nums = []

for folder, subfolder, file in os.walk('extracted_content/'):
    for f in file:
        match = []
        cur_file = open(folder + '/' + f, 'r')
        f_str = cur_file.read()
        cur_file.close()
        match = re.findall(r'\d{3}-\d{3}-\d{4}', f_str)
        if match:
            nums += match

print(nums)
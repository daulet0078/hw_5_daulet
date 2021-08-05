import re
f = open('data_corey.txt', 'r')
content = f.read()
num = re.findall(r"\d{3}-\d{3}-\d{4}", content)
num2 = re.findall(r'\d{3}-\d{3}-\d{3}7', content)
print(f'Total amount of phone numbers: {len(num)}')
print(f"Total amount of phone numbers with ending 7: {len(num2)}")
f.close()



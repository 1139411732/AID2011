
import re

s='Alex:1996:,Sunny:1995,'
# pattern=r'(\w+):(\d+)'
pattern=r'(?P<name>\w+):(?P<y>\d+)'

# result=re.finditer(pattern,s)
#
# for i in result:
#     print(f'匹配的位置{i.span()}')
#     print(f'匹配到的内容{i.group()}')
#

# result=re.match(pattern,s)
# print(result.group('name','y'))

result=re.search(pattern,s)
print(result.group())
print(result.groupdict())
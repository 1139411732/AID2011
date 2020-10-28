a="""Sunzi
带了成
大孙子带了成
带了成也是小孙子
"""
import re
# result=re.findall(r'.+',a,flags=re.S)
# result=re.findall(r'^\w+',a,flags=re.M)
result=re.findall(r'^\w+',a)
print(result)


# How to etract all duplictes with in list 

a = [7,7,0,4,1,2,9,8,8,4,'the','the','the']

from collections import Counter
from xml.dom.minidom import Element

print([element for element ,count in Counter(a).items()if count > 1])
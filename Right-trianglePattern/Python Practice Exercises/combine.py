import string
import random

random.seed(3)

letters = string.ascii_lowercase

values = random.sample(letters,8)

dict_1 ={i:j for i,j in enumerate(values[:4])}
dict_2 ={i:j for i,j in enumerate(values[4:8],4)}

print('dict1',dict_1)
print('dict2',dict_2)

dict_3 = {**dict_1, **dict_2}
print(dict_3)
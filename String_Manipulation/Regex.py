import collections

name_list = [('kim','sungbum'), ('kim','jisung'),('lee','insong')]
new_dict = collections.defaultdict(list)
for k, v in name_list:
    print('k:', k)
    print('v:', v)
    new_dict[k].append(v)


print(new_dict)
# 2)
import operator
def sort_by_key(dict):
    return sorted(dict.items())
def reverse_sort_by_key(dict):
    return sorted(dict.items(), reverse=True)
def sort_by_value(dict):
    return sorted(dict.items(), key=operator.itemgetter(1))
d = {
    1: 'hi',
    3: 'poofy cat',
    2: 'bai bai',
}
print(sort_by_value(d))


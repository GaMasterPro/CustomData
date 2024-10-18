#Custom Dictionary
class CustomDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_value(self, key):
        return self.get(key, 'Key not found')

    def __str__(self):
        return f"CustomDict({super().__str__()})"

    def __repr__(self):
        return f"CustomDict({super().__repr__()})"

    def __getitem__(self, key):
        return super().get(key, 'Key not found')

    def __setitem__(self, key, value):
        print(f"Adding {key}: {value}")
        super().__setitem__(key, value)

    def __delitem__(self, key):
        if key in self:
            print(f"Removing {key}")
            super().__delitem__(key)
        else:
            print(f"{key} not found; cannot delete")

my_custom_dict = CustomDict(apple=1, banana=2)
print(my_custom_dict.get_value('apple'))   
print(my_custom_dict.get_value('orange'))  

my_custom_dict['orange'] = 3               
print(my_custom_dict)                      

del my_custom_dict['banana']               
print(my_custom_dict)                       

del my_custom_dict['grape']

print(my_custom_dict.__str__())




# Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_arr.append(right[j])
            j += 1
        else:
            sorted_arr.append(left[i])
            i += 1
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    return sorted_arr


nums = [5, 26, 3, 108, 21, 58, 35]
print(merge_sort(nums))

    
import module_1  
import useful_functions as uf
# print(module_1.num)
scores=[88,92,79,93,85]
old_mean=uf.mean(scores)
new_list=uf.add_five(scores)
new_mean=sum(new_list)/len(new_list)
print(f"list_of_numbers: {scores}")
print(f"old mean:{old_mean}, new_mean:{new_mean}")
print(__name__)
print(uf.__name__)


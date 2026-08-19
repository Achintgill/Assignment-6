#initial nested list
nested_list=[[1,2,3],[3,4,5,6],[6,7,8,9]]
#new elements to be added
new_elements=[[2,543,346,234,56]]
nested_list[1].extend(new_elements)
print("Updated Nested List: ",nested_list)

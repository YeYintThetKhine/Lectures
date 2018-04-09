my_dict = {'a':2, 3:['x', 'y'], 'joe':'smith'}
dict_value_view = my_dict.values()
dict_value_view
dict_values([2,['x','y'],'smith'])
type(dict_value_view)
class 'dict_values'
for val in dict_value_view:
print(val)

['x','y']
smith =()
my_dict['new_key']='new_value'
dict_value_view
dict_values([2,'new_value',['x','y'],'smith'])
dict_key_view=my_dict.keys()
dict_keys(['a','new_key',3,'joe'])
dict_value_view
dict_values([2,'new_value',['x','y'],'smith'])




ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}
name=input("Enter new name:")
age =int(input("Enter age:"))
ages_dict[name]=age
for key, value in ages_dict.items():
    print(key,"_" ,value)

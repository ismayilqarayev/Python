def print_person(name, /, age, company="Microsoft"):
    print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
print_person("Tom", company="JetBrains", age = 24)     
print_person("Bob", 41)              





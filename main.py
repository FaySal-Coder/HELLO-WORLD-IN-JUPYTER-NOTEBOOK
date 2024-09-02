name:str = "Faisal" 
print (name)

#print (id(name))

#print (dir(name))


print (name.capitalize())

print (name.casefold())
print (name.center(10,"*"))

print([i for i in dir (name) if not i.startswith("_")])
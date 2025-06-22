dic = {
    "Carla": "Human Being",
    "Spoon" : "Object"
}
print(dic["Carla"])
print(dic["Spoon"])

print(" ")

info = {'name' : 'Karan' ,'age' :19 , 'eligible' : True}
print(info)
print(info['name'])
print(info.get('name2'))

info = {'name' : 'Karan' ,'age' :19 , 'eligible' : True}
print(info)
print(info.keys())

print(" ")

for key in info.keys():
    print(info[key])
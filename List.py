book=["JavaScript","Java","C","C#","C++","HTML","CSS","PHP","MySQL","PYTHON"]

print(f"{book}")
#or 
print(book)

#append list
append_family=["Joseph","John","Johanna"]
append_family.append("Mama Anna")
print(append_family)

#insert list
insert_family=["Joseph","John","Johanna","Mama"]
insert_family.insert(4,"Papa Antonio")
print(insert_family)

#sort list
car=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini"]
car.sort()
print(car)

#pop list
listcar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini"]
popped_listcar=listcar.pop()
print("This is my car ",popped_listcar)

#pop selected list
selectcar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini"]
selected_popped=selectcar.pop(1)
print("this is my select car",selected_popped)

#del list
deletecar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini"]
del deletecar[1]
print(deletecar)

#remove list
removecar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini"]
removecar.remove("AUDI")
print(removecar)

#reverse list
reversecar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini"]
reversecar.reverse()
print(reversecar)

#sorted list
sortedcar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini","Honda"]
print(sorted(sortedcar))

#avioding error list
errorcar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini","Honda"]
print(errorcar[-1])

#len list
lencar=["BMW","Ferrari","AUDI","RollsRoyce","Maseratti","Lamborghini","Honda"]
print("there are",len (lencar),"cars")
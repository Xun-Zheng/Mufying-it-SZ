names = ["Shane", "Teo", "Eden", "Soo", "Darhin"]
to_remove = ["Shane", "Teo","Darhin"]
print(names[0])
print(names[4])

filtered = [x for x in names if x not in to_remove]
print(filtered)

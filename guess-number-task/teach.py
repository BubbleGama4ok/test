#students = [('Ivanov',1),('Smirnov',4),('Petrov',3),('Kuznetsova',1),
            ('Nikitina',2),('Markov',3),('Pavlov',2)]


#from collections import defaultdict
#создаем пустой объект Counter
#groups = defaultdict(list)

#for student, group in students:
    groups[group].append(student)

#print(groups)
# Будет напечатано:
# Counter({'red':})
#print(groups[3077])


data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
client_ages = dict(data)
print(client_ages)
#16 Nested Lists 


l = []
second_lowest_names = []
scores = set() 
            
for i in range(int(input())):
    name = ['Harry','Berry','Tina','Akriti','Harsh']
    score = [37.21,37.21,37.2,41]
    l.append([name, score]) #Crear una matriz 
    scores.add(score) 
second_lowest = sorted(scores)[1]

for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')


#def bubleSort(lista):
#    for pasanum in range(len(lista)-1,0,-1):
#        for i in range(pasanum):
#            if lista[i] > lista[i+1]:
#                temp = lista [i]
#                lista[i] = lista[i+1]
#                lista[i+1] = temp
#lista = [7,-8,10,5]
#bubleSort(lista)
#print(lista)'''




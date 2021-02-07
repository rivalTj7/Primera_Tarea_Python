#6 Any or All
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
a = input().split(" ")  #Lista de datos separados por espacio
print(all(int(i)>=0 for i in a) and any(i == i[::-1]for i in a)) #Formulas locas que hay en el inicio 

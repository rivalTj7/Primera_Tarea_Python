#9 sWAP cASE
def swap_case(s):
    result = []
    
    for i in s:                
        if i == i.lower():           # Lower() Metodo propio de python Convertir una cadena a minusculas
            result.append(i.upper())
        elif i == i.upper():   # Upper() Metodo de Python Convertir una cadena a mayusculas.
            result.append(i.lower())
        else:
            result.append(i)
    return ''.join(result) # intermprear los espacios en el texto jaja 

s = 'HackerRank.com presents Pythonist 2.'
result = swap_case(s)
print(result)

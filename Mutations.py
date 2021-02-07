#12 Mutations

# las listas son mutables (se pueden cambiar) y las tuplas son inmutables (no se pueden cambiar).
#Task
#Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    
    
    
    return string

#input().split() lee la entra con 1 salto de linea 
s = 'randomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomnessrandomness'
i= 27
c ='p'
s_new = mutate_string(s, int(i), c)
print(s_new)

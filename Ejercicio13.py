#13 Find a string
#en Python, la longitud de una cadena la encuentra la función len(s), dondee s es la cadena.
#startswith, Saber si una cadena comienza con una subcadena determinada

def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            count += 1
        
    return count


string = 'ABCDCDC'
sub_string ='CDC' 
    
count = count_substring(string, sub_string)
print(count)

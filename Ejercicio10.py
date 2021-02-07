#10 String Split and Join

def split_and_join(line):
    # write your code here
    line=line.split(" ") #Primero se le quita los espacios
    line = "-".join(line) #Conversion de "" a "-"
    return line
    
line = 'this is a string' #Ejemplo que hay. 
result = split_and_join(line)
print(result)
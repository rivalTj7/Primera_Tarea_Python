#18 Default Arguments


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
 
def print_from_stream(n, stream=EvenStream()):
    stream.__init__() #Inciador del evento stream, como a cada pasada deve iniciarse la primera pasada si cumple ya que al inicia no esta lleno pero en la segunda cadena o test no sirve ya que este ya fue usado previamente o mas bien no a sido iniciado. 
    for _ in range(n):
        print(stream.get_next())


        

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
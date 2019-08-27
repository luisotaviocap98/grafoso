class No:

    def __init__(self, valor):
        self.valor = valor 
        self.adj = list()

    def listadj(self):
        for i in self.adj:
            print(' - ', i.valor, end="")
        print()


class Aresta:
    def __init__(self,no,no2):
        self.origem = no
        self.destino = no2

    
class Grafo:

    def __init__(self):
        self.newNo = list()
        self.arrst = list()

    def printGrafo(self):
        for i in self.newNo:
            print(i.valor)

    def addNo(self,no):
        self.newNo.append(no)

    def createAresta(self,no1,no2):
        a = Aresta(no1,no2)
        b = Aresta(no2,no1)
        self.arrst.append(a)
        self.arrst.append(b)
        no1.adj.append(no2)
        no2.adj.append(no1)


    def printAresta(self):
        print('lista de adjacencia')
        for i in self.newNo:
            print("Saindo de [%s]->" %i.valor , end="")
            for j in i.adj:
                print(" [%s]" % j.valor, end="")
            print()
        
    def feixotrans():
        print()


    

if __name__ == "__main__":
    x = Grafo()
    a = No(5)
    b = No(3)
    c = No(8)
    d = No(90)


    x.addNo(a)
    x.addNo(b)
    x.addNo(c)
    x.addNo(d)
    x.createAresta(a,b)
    x.createAresta(a,c)
    x.createAresta(b,c)
    x.createAresta(b,d)
    x.createAresta(d,c)
    #x.createAresta(a,d)
    

    x.printGrafo()
    x.printAresta()


    
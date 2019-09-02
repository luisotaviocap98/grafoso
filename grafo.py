class Vtx:
    def __init__(self, valor):
        self.valor = valor 
        self.adj = list()

    def listadj(self):
        for i in self.adj:
            print(' - ', i.valor, end="")
        print()


class Aresta:
    def __init__(self,vtx,vtx2):
        self.origem = vtx
        self.destino = vtx2

    
class Grafo:
    def __init__(self):
        self.newvtx = list()
        self.arrst = list()

    def printGrafo(self):
        for i in self.newvtx:
            print(i.valor)

    def addvtx(self,vtx):
        self.newvtx.append(vtx)

    def createAresta(self,vtx1,vtx2):
        self.arrst.append(Aresta(vtx1,vtx2))
        self.arrst.append(Aresta(vtx2,vtx1))
        vtx1.adj.append(vtx2)
        vtx2.adj.append(vtx1)


    def printAdj(self):
        print('lista de adjacencia')
        for i in self.newvtx:
            print("Saindo de [%s]->" %i.valor , end="")
            for j in i.adj:
                print(" [%s]" %j.valor, end="")
            print()
            
    def printAresta(self):
        print('arestas')
        for i in self.arrst:
            print('de',i.origem.valor,'para',i.destino.valor)
    

    def buscalarg(self,start):
        s = start
        cor = list()
        pai = list()
        queue = list()
        distancia = list()
        
        for i in self.newvtx:
            if i != s:
                cor[index(i)] = "branco"
                distancia[index(i)] = "inf"
                pai[index(i)] = None
            else:
                t = index(i)
        
        cor[t] = "cinza"
        distancia[t]=0
        pai[t]=None
        queue.append(s)    
        
        while len(queue):
            j=queue.pop()
            for i in self.newvtx.adj:
                if cor[i] == "branco":
                    cor[i]="cinza"
                    distancia[i]=distancia[j] + 1
                    pai[i]= j.valor
                    queue.append(queue, i)
                cor[j]="preto"
                      
    

if __name__ == "__main__":
    x = Grafo()
    a = Vtx(5)
    b = Vtx(3)
    c = Vtx(8)
    d = Vtx(90)


    x.addvtx(a)
    x.addvtx(b)
    x.addvtx(c)
    x.addvtx(d)
    x.createAresta(a,b)
    x.createAresta(a,c)
    x.createAresta(b,c)
    x.createAresta(b,d)
    x.createAresta(d,c)
    

    x.printGrafo()
    x.printAdj()
    x.printAresta()


    
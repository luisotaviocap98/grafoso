global cont 
cont =0


class Vtx:
    def __init__(self, valor):
        self.valor = valor 
        self.adj = list()
        global cont
        self.numero = cont
        cont = cont + 1

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
        queue = list()
        pai = [None] * len(self.newvtx)
        cor = [None] * len(self.newvtx)
        distancia = [None] * len(self.newvtx)
        
        for i in self.newvtx:
            if i != s:
                cor[i.numero] = "branco"
                distancia[i.numero] = None
                pai[i.numero] = None
        
        cor[s.numero] = "cinza"
        distancia[s.numero]=0
        pai[s.numero]=None
        queue.append(s)    
        
        while len(queue):
            j=queue.pop()
            for i in j.adj:
                if cor[i.numero] == "branco":              
                    cor[i.numero]="cinza"
                    distancia[i.numero]=distancia[j.numero] + 1
                    pai[i.numero]= j.valor
                    queue.append(i)
                cor[j.numero]="preto"
                  
        print("as cores",cor)
        print("as distancias", distancia)
        print('os pais',pai)
        print('fila atual',queue)


if __name__ == "__main__":
    x = Grafo()
    a = Vtx(5)
    b = Vtx(3)
    c = Vtx(8)
    d = Vtx(90)
    e = Vtx(800)

    x.addvtx(a)
    x.addvtx(b)
    x.addvtx(c)
    x.addvtx(d)
    x.addvtx(e)
    x.createAresta(a,b)
    x.createAresta(a,c)
    x.createAresta(b,c)
    x.createAresta(b,d)
    x.createAresta(d,c)
    x.createAresta(d,e)
    
    x.buscalarg(a)
    x.printGrafo()
    x.printAdj()
    x.printAresta()


    
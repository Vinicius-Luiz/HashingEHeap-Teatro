def main():
    class Pessoa():
        def __init__ (self, cadastro, nome,  prioridade, fileira = None):
            self.cadastro   = cadastro
            self.nome       = nome
            self.prioridade = prioridade
            self.fileira    = fileira
            self.proximo    = None
            self.anterior   = None
            
    class Hash_Fechado():
        def __init__(self, tam):
            self.tamanho       = tam
            self.lista         = []
            self.qtd_n_sentado = 0
            for x in range(tam):
                self.lista.append(None)
        
        def hash_set_fileira(self, menorPrioridade = None, referencia = None, fileira = None):
            if referencia == 'remover sentado':
                for cadTemp in range (self.tamanho):
                    pessoa = self.hash_buscar(cadTemp, 'set_fileira')
                    if pessoa != None:
                        fim = False
                        while not fim:
                            if pessoa == None:
                                fim = True
                            elif pessoa.prioridade == menorPrioridade[0]:
                                pessoa.fileira = False
                                pessoasCadastradas.qtd_n_sentado += 1
                                break
                            else:
                                pessoa = pessoa.proximo
            else:
                maiorPref = [None, 0]
                sentados_verificados = 0
                for cadTemp in range(self.tamanho):
                    if sentados_verificados == self.qtd_n_sentado:
                        break
                    pessoa = self.hash_buscar(cadTemp, 'set_fileira')
                    if pessoa != None and pessoa.fileira == False:
                        sentados_verificados += 1
                        if pessoa.prioridade > maiorPref[1]:
                            maiorPref = [pessoa, pessoa.prioridade]

                if maiorPref[0] != None:
                    pessoasCadastradas.qtd_n_sentado -= 1
                    cad = maiorPref[0].cadastro
                    nome = maiorPref[0].nome
                    prioridade = maiorPref[0].prioridade
                    
                    pessoasCadastradas.hash_remover(maiorPref[0].cadastro)
                    p   = Pessoa(cad, nome, prioridade)
                    fileira.heap_inserir(p)
                    pessoasCadastradas.hash_inserir(p)
                    p.fileira = numFileira

        def hash_buscar(self, cadastro, referencia = None):
            tabela = self.lista
            j = self.hash_funcao(cadastro)
            if referencia == 'hash_remover':
                return j
            pessoa = tabela[j]
            if referencia == 'set_fileira':
              return pessoa
            else:
                r = self._hash_buscar(cadastro, pessoa, j)
                if r is None:
                    return 'Inexistente'
                return r            

        def _hash_buscar(self, cadastro, pessoa, j):
            flag = True
            while flag:
                if pessoa == None:
                    return 'Inexistente'
                
                elif pessoa.cadastro == cadastro:
                    if pessoa.nome == nome:
                        if pessoa.fileira is not False:
                            return 'Sentado(a) na fileira {}'.format(pessoa.fileira)
                        else:
                            return 'Sem assento' 
                else:
                    pessoa = pessoa.proximo

        def hash_funcao(self, x):
            return x%self.tamanho

        def hash_inserir(self, pessoa):
            tabela = self.lista
            j = self.hash_funcao(pessoa.cadastro)
            if tabela[j] == None:
                tabela[j] = pessoa
            else:
                self.aux_ponteiro(tabela[j], pessoa)
                

        def aux_ponteiro(self, elemento, novoEle):
            flag = True
            while flag:
                if elemento.proximo == None:
                    elemento.proximo = novoEle
                    novoEle.anterior = elemento
                    flag = False
                else:
                    elemento = elemento.proximo

        def hash_remover(self, cadastro):
            j = (self.hash_buscar(cadastro, 'hash_remover'))
            if j == None:
                return None
            else:
                tabela = self.lista
                elemento = tabela[j]
                achou = False
                while not achou:
                    if elemento.cadastro == cadastro:
                        if elemento.anterior == None and elemento.proximo == None:
                            tabela[j] = None
                        elif elemento.proximo != None:
                            elemento.proximo.anterior = elemento.anterior
                            if elemento.anterior == None:
                                tabela[j] = elemento.proximo
                        return 'Removido(a)'

                    else:
                        if elemento.proximo != None:
                            elemento = elemento.proximo
                        else:
                            return None      
    class Heap:
        def __init__(self, comprimento):
            self.comprimento  = comprimento
            self.tamanho_heap = 0
            self.vetor        = []
            for i in range(self.comprimento):
                self.vetor.append(None)

        def pai(self, i):
            if i == 2:
                return 0
            else:
                return i//2

        def esquerda(self, i):
            return (2*i)+1

        def direita(self,i):
            return (2*i)+2

        def heap_inserir(self, pessoa):
            vetor = self.vetor
            vetor[self.tamanho_heap] = 101
            self.heap_incrementar(self.tamanho_heap, pessoa)
            self.tamanho_heap += 1

        def heap_incrementar(self, i, pessoa):
            vetor = self.vetor
            if pessoa.prioridade > vetor[i]:
                return
            vetor[i] = pessoa.prioridade
            fim = False
            if vetor[self.pai(i)] is None:
                vetor[i], vetor[self.pai(i)] = vetor[self.pai(i)], vetor[i]
                return
            while not fim and vetor[self.pai(i)] > vetor[i]:
                vetor[i], vetor[self.pai(i)] = vetor[self.pai(i)], vetor[i]
                if i > 0:
                    i = self.pai(i)
                else:
                    fim = True

        def min_heapify(self, i = 0):
            menor    = i
            esquerda = self.esquerda(i)
            direita  = self.direita(i)
            vetor    = self.vetor
            if esquerda < self.tamanho_heap and vetor[esquerda] < vetor[i]:
                menor = esquerda
                
            if direita < self.tamanho_heap and vetor[direita] < vetor[menor]:
                menor = direita
                
            if menor != i:
                vetor[i], vetor[menor] = vetor[menor], vetor[i]
                self.min_heapify(menor)

        def heap_min_remover(self):
            vetor = self.vetor
            if vetor[0] is None:
                return
            if self.tamanho_heap == 1:
                vetor[0] = None
                return
            else:
                vetor[0], vetor[-1] = vetor[-1], vetor[0]
                self.tamanho_heap -= 1
                print(self.tamanho_heap, self.comprimento)
                return self.min_heapify()

        def max_heapify(self, i = 0):
            esquerda = self.esquerda(i)
            direita  = self.direita(i)
            vetor = self.vetor
            if esquerda < self.tamanho_heap and vetor[esquerda] > vetor[i]:
                maior = esquerda
            else:
                maior = i

            if direita < self.tamanho_heap and vetor[direita] > vetor[maior]:
                maior = direita

            if maior != i:
                vetor[i], vetor[maior] = vetor[maior], vetor[i]
                self.max_heapify(maior)

        def heap_max_remover(self):
            self.max_heapify()
            vetor = self.vetor
            if vetor[0] is None:
                return
            if self.tamanho_heap == 1:
                vetor[0] = None
                return
            else:
                vetor[0], vetor[-1] = vetor[-1], None
                self.tamanho_heap -= 1
                return self.max_heapify()

    def cadastrar(op, numCadastro, qtd_cadeiras, qtd_fileiras):
        cad          = op.split(' ')
        nome         = cad[1]
        prioridade   = int(cad[2])
        numCadastro += 1
        p   = Pessoa(numCadastro, nome, prioridade)                            
            
        fil             = 1
        menorPrioridade = [101, 0]
        menorTemp       = [101, 0]
        disponivel          = False
        for fileira in assentos:
            if fileira.tamanho_heap < qtd_cadeiras:
                fileira.heap_inserir(p)
                disponivel = True
                break
            fileira.min_heapify()
            if fileira.vetor[0] < menorTemp[0]:
                menorTemp = [fileira.vetor[0], fil]
            if menorTemp[0] < menorPrioridade[0]:
                menorPrioridade = menorTemp
            fil += 1
            
        if disponivel:
            p.fileira = fil
            print('{} ({}) foi alocado(a) na fileira {}'.format(nome,numCadastro,fil))            
        
        else:
            if p.prioridade > menorPrioridade[0]:
                fileira = menorPrioridade[1]
                assentos[fileira-1].heap_min_remover()
                print(assentos[fileira-1].comprimento, assentos[fileira-1].tamanho_heap)
                pessoasCadastradas.hash_set_fileira(menorPrioridade, 'remover sentado')
                assentos[fileira-1].heap_inserir(p)
                p.fileira = fileira
                print('{} ({}) foi alocado(a) na fileira {}'.format(nome, numCadastro, fileira))
            else:
                p.fileira = False
                pessoasCadastradas.qtd_n_sentado += 1
                print('{} ({}) nao foi alocado(a) em nenhuma fileira'.format(nome,numCadastro))
        pessoasCadastradas.hash_inserir(p)
        return numCadastro

    qtd_f_q        = input()
    qtd_f_q        = qtd_f_q.split(' ')
    qtd_fileiras   = int(qtd_f_q[0])
    qtd_cadeiras   = int(qtd_f_q[1])
    assentos       = []
    for i in range(qtd_fileiras):
        fileira = Heap(qtd_cadeiras)
        assentos.append(fileira)
    pessoasCadastradas = Hash_Fechado(2*(qtd_fileiras*qtd_cadeiras))

    qtd_comandos = int(input())
    ops          = ['CAD ','VER ', 'REM ']
    numCadastro  = 0
    for x in range(qtd_comandos):
        op = input()
        if ops[0] in op:
            numCadastro = cadastrar(op, numCadastro, qtd_cadeiras, qtd_fileiras)
            
        elif ops[1] in op:
            ver      = op.split(' ')
            nome     = ver[1]
            cadastro = int(ver[2])
            print(pessoasCadastradas.hash_buscar(cadastro))
            
        elif ops[2] in op:
            rem      = op.split(' ')
            nome     = rem[1]
            cadastro = int(rem[2])
            fileira  = pessoasCadastradas.hash_buscar(cadastro)
            if fileira == 'Inexistente':
                print(fileira)
                
            elif fileira == 'Sem assento':
                print(pessoasCadastradas.hash_remover(cadastro))
            else:
                numFileira = int(fileira[-1])
                fileira = assentos[numFileira-1]
                fileira.heap_max_remover()
                print(pessoasCadastradas.hash_remover(cadastro))
                if fileira.tamanho_heap < fileira.comprimento:
                    pessoasCadastradas.hash_set_fileira(menorPrioridade = None, referencia = None, fileira = fileira)
                
if __name__ == '__main__':
    main()

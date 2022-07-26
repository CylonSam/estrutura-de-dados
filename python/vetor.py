class Vetor:
    vetor = []
    tamanho = 0

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [None for x in range(tamanho)]

    def _posicao_invalida(self, posicao):
        return posicao not in range(self.tamanho)

    def _tem_espaco(self):
        return None in self.vetor

    def _desloca_direita(self, posicao):
        self.vetor[posicao + 1:] = self.vetor[posicao:-1]
        self.vetor[posicao] = None

    def _desloca_esquerda(self, posicao):
        self.vetor[posicao:] = self.vetor[posicao + 1:]
        self.vetor.append(None)

    def inserir(self, item, posicao=None):
        '''
        Insere um item no vetor na posicao especificada.
        '''

        if not self._tem_espaco():
            print("Erro: vetor não possui espaco")
            return

        if self._posicao_invalida(posicao):
            print(f"Erro: posicao {posicao} extrapola tamanho do vetor")
            return

        if posicao == None:
            self.vetor.append(item)
            return

        if self.vetor[posicao] != None:
            self._desloca_direita(posicao)
        self.vetor[posicao] = item

    def remover(self, posicao):
        '''
        Remove o item na posicao especificada.
        '''
        self.vetor[posicao] = None
        self._desloca_esquerda(posicao)

    def pega_item(self, posicao):
        '''
        Retorna o item na posicao especificada.
        '''
        if self._posicao_invalida(posicao):
            print(f"Erro: posicao {posicao} extrapola tamanho do vetor")
            return
        return self.vetor[posicao]

    def pega_tamanho(self):
        '''
        Retorna o tamanho do vetor.
        '''
        return len(self.vetor)

    def pega_vetor(self):
        '''
        Retorna o vetor
        '''
        return self.vetor


print("Criando vetor...")
v = Vetor(5)

print("Tamanho da vetor: " + str(v.pega_tamanho()))

v.inserir(1, posicao=0)
v.inserir(5, posicao=1)
v.inserir(3, posicao=2)
v.inserir(42, posicao=3)


print(v.pega_vetor())

print(v.pega_item(3))

v.inserir(66, posicao=3)

print(v.pega_vetor())

v.remover(posicao=2)

print(v.pega_vetor())

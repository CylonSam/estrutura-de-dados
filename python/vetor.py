class Vetor:
    vetor = []
    tamanho = 0

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.vetor = [None for x in range(tamanho)]

    def _posicao_invalida(self, posicao):
        return posicao not in range(self.tamanho)

    def inserir(self, item, posicao):
        '''
        Insere um item no vetor na posicao especificada.
        '''
        if self._posicao_invalida(posicao):
            print(f"Erro: posicao {posicao} extrapola tamanho do vetor")
            return

        self.vetor[posicao] = item

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


v = Vetor(5)

print(v.pega_tamanho())

v.inserir(1, posicao=0)
v.inserir(5, posicao=1)
v.inserir(3, posicao=2)
v.inserir(42, posicao=3)
v.inserir(69, posicao=5)

print(v.pega_vetor())

print(v.pega_item(3))

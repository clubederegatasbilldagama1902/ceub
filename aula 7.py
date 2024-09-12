red = "\33[1;49;31m"
green = "\33[1;49;32m"
yellow = "\33[1;49;33m"
blue = "\33[1;49;34m"
pink = "\33[1;49;35m"
cyan = "\33[1;49;36m"
white = "\33[1;49;37"
nc = "\33[m"

def linha():
    print("+=+="*69)

class Produto(object):
    def __init__(self,nome="Nome Padrão", preco=32.54, vendas=98, qntd_estoque=100, qntd_minima=10):
        self.nome = nome
        self.preco = preco
        self.vendas = vendas
        self.qntd_estoque = qntd_estoque
        self.qntd_minima = qntd_minima

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        if isinstance(nome, str):
            self.nome = nome
        else:
            print("Erro! O nome deve ser uma string!")

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        if isinstance(preco, (int, float)) and preco >= 0:
            self.preco = preco
        else:
            print("Erro! Valor não pode ser menor do que 0!")

    def get_vendas(self):
        return self.vendas

    def set_vendas(self, vendas):
        if isinstance(vendas, (int, float)) and vendas >= 0:
            self.vendas = vendas
        else:
            print("Erro! Valor não pode ser menor do que 0!")

    def get_qntd_estoque(self):
        return self.qntd_estoque

    def set_qntd_estoque(self, nova_qntd):
        self.qntd_estoque = nova_qntd

    def set_qntd_estoque(self, qntd_estoque):
        if isinstance(qntd_estoque, int) and qntd_estoque >= 0:
            self.qntd_estoque = qntd_estoque

    def get_qntd_minima(self):
        return self.qntd_minima

    def set_qntd_minima(self, nova_qntdMin):
        self.qntd_minima = nova_qntdMin

    def set_qntd_minima(self, qntd_minima):
        if isinstance(qntd_minima, int) and qntd_minima >= 0:
            self.qntd_minima = qntd_minima

    def desconto(self, percentual):
        if 0 < percentual < 100:
            self.preco -= self.preco * (percentual / 100)

    def lucro(self):
        return self.venda - self.preco

    def mostrar_dados(self):
        print(f"\n{yellow}Nome: {self.nome}{nc}")
        print(f"{yellow}Preço: R${self.preco:.2f}{nc}")
        print(f"{yellow}Vendas: {self.vendas}{nc}")
        print(f"{yellow}Quantidade no estoque: {self.qntd_estoque}{nc}")
        print(f"{yellow}Quantidade no mínima: {self.qntd_minima}{nc}")
        print(f"{yellow}Lucro: {lucro()}{nc}\n")

    def mostrar_dadosGET(self):
        print(f"\n{red}Nome: {self.get_nome()}{nc}")
        print(f"{red}Preço: R${self.get_preco():.2f}{nc}")
        print(f"{red}Vendas: {self.get_vendas()}{nc}")
        print(f"{red}Quantidade no estoque: {self.get_qntd_estoque()}{nc}")
        print(f"{red}Quantidade no mínima: {self.get_qntd_minima()}{nc}")
        print(f"{yellow}Lucro: {lucro()}{nc}\n")

    def retornar_dados(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "vendas": self.vendas,
            "qntd_estoque": self.qntd_estoque,
            "qntd_minima": self.qntd_minima
        }

    def aumentar_estoque(self, qntd_estoque):
        if qntd_estoque > 0:
            self.qntd_estoque += self.qntd_estoque
        else:
            print("Erro: A quantidade a ser aumentada deve ser maior que zero.")

from calabreso import *

if __name__ == "__main__":
    produto1 = Produto("Carregador",26.98,46,80,20)
    produto2 = Produto("Fone de ouvido", 120.45, 60, 50, 10)
    produto3 = Produto()

    print(f"\n{blue}{">>Mostrar dados com atributos<<":^224}{nc}\n")
    linha()
    produto1.mostrar_dados()
    produto1.aumentar_estoque(60)
    linha()
    print(f"\n{pink}{">>Dados utilizando os métodos get<<":^224}{nc}\n")
    linha()
    produto1.mostrar_dadosGET()

    linha()

    produto2.desconto(15)
    produto2.mostrar_dados()
    linha()

    produto3.set_nome("Capinha")
    produto3.set_preco(40.59)
    produto3.set_vendas(80)
    produto3.set_qntd_estoque(170)
    produto3.set_qntd_minima(30)
    produto3.mostrar_dados()
    linha()



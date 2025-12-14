from abc import ABC, abstractmethod 
class Metodo(ABC):
    @abstractmethod
    def realizar_pagamento(self, valor: float):
        pass

class Pagamento(Metodo):
    def __init__(self, valor: float, descricao: str, metod: Metodo):
        self.valor: float = valor
        self.descricao = descricao
        self.metodo = metodo
    def validar_valor(self):
        if self.valor<=0:
            raise ("tu é pobre ein")
            
    def final(self):
        return f"Pagamento de R${self.valor}: {self.descricao}"
    
    def processar(self):
        pass

class Pix(Metodo):
    def __init__(self, valor: float, descricao:str, chave:str, banco:str):
        super().__init__(valor, descricao)
        self.chave = chave        
        self.banco = banco

    def processar(self):
        print(f"Pagando pix produto {self.descricao} para {self.chave} do bando {self.banco} no valor de {self.valor}")
    

class CartaoCredito(Metodo):
    def __init__(self, num: int, nome: str, limite_disp: float, valor:float, desc:str):
        super().__init__(valor, desc)
        self.num = num
        self.nome = nome
        self.limite = limite_disp
        self.valor = valor
        self.desc = desc 


    def processar(self):
        if self.valor >self.limite:
            print(f"Erro: limite insuficiente no cartao {self.num}")
            return
        else:

            self.limite-self.valor
            print(f"Pagamento aprovado no cartao Cliente {self.nome}. Limite restante:{self.limite}")
class Boleto(Metodo):
    def __init__(self, valor: float, desc:str, codigo_b: float, venc:int):
        super().__init__(valor, descricao)
        self.codigo_b: codigo_b
        self.venc: venc

    def processar(self):
        print("Boleto gerado. Aguardando pagamento..")

    def processar_pagamento(pagamento: Pagamento):
        pagamento.validar_valor()
        pagamento.final()
        pagamento.processar()

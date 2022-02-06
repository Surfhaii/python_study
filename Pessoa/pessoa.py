class Pessoa:

    def __init__(self, nome, idade, sexo, comendo=False, falando=False, andando=False, dormindo=False):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.comendo = comendo
        self.falando = falando
        self.andando = andando
        self.dormindo = dormindo

    # Definindo as ações da Peessoa

    def comer(self):
        if self.comendo:
            print(f"{self.nome} já está comendo!")
        elif self.falando or self.andando or self.dormindo:
            print(f"{self.nome} Não pode comer pois está fazendo outra ação.")
        else:
            print(f"{self.nome} começou a comer!!")
            self.comendo = True
    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
        else:
            print(f"{self.nome} parou de comer.")
            self.comendo = False

    def falar(self):
        if self.falando:
            print(f"{self.nome} já está falando!")
        elif self.comendo or self.dormindo:
            print(f"{self.nome} Não pode falar pois já está fazendo outra ação.")
        else:
            print(f"{self.nome} começou a falar!!")
            self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
        else:
            print(f"{self.nome} parou de falar!")
            self.falando = False

    def andar(self):
        if self.andando:
            print(f"{self.nome} já está andando!")
        elif self.comendo or self.dormindo:
            print(f"{self.nome} Não pode andar pois já está fazendo outra ação.")
        else:
            print(f"{self.nome} começou a andar!!")
            self.andando = True

    def parar_andar(self):
        if not self.andando:
            print(f"{self.nome} Não está andando!")
        else:
            print(f"{self.nome} parou de andar!")
            self.andando = False

    def dormir(self):
        if self.dormir:
            print(f"{self.nome} já está dormindo!")
        elif self.comendo or self.andando or self.falando:
            print(f"{self.nome} Não pode dormir pois está fazendo outra ação!")
        else:
            print(f"{self.nome} começou a dormir, boa noite!!")
            self.dormindo = True

    def parar_dormir(self):
        if not self.dormindo:
            print(f"{self.nome} Não está dormindo")
        else:
            print(f"{self.nome} Parou de dormir!!")
            self.dormindo = False




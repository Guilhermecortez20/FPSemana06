import json
import os

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, inimigo):
        inimigo.vida -= self.ataque
        print(f"{self.nome} ataca {inimigo.nome} e causa {self.ataque} de dano!")

    def __str__(self):
        return f"{self.nome} - Vida: {self.vida}"

class Guerreiro(Personagem):
    def especial(self, inimigo):
        dano = 30
        inimigo.vida -= dano
        print(f"{self.nome} usa Golpe Poderoso em {inimigo.nome} e causa {dano} de dano!")

class Mago(Personagem):
    def especial(self):
        cura = 45
        self.vida += cura
        print(f"{self.nome} usa Cura e ganha {cura} pontos de vida!")

class Arqueiro(Personagem):
    def especial(self, inimigos):
        dano = 12
        for inimigo in inimigos:
            inimigo.vida -= dano
        print(f"{self.nome} usa Chuva de Flechas e causa {dano} de dano a todos os inimigos!")

def importar_personagens(caminho):
    """
    Importa personagens a partir de um arquivo JSON.
    Retorna uma lista de personagens e a quantidade total.
    """
    if not os.path.exists(caminho):
        print(f"Erro: O arquivo '{caminho}' não foi encontrado.")
        return [], 0

    with open(caminho, 'r') as file:
        dados = json.load(file)

    personagens = []
    for dado in dados:
        if dado['classe'] == 'Guerreiro':
            personagens.append(Guerreiro(dado['nome'], dado['vida'], dado['ataque']))
        elif dado['classe'] == 'Mago':
            personagens.append(Mago(dado['nome'], dado['vida'], dado['ataque']))
        elif dado['classe'] == 'Arqueiro':
            personagens.append(Arqueiro(dado['nome'], dado['vida'], dado['ataque']))

    return personagens, len(personagens)

def ordenar_personagens_por_vida(personagens):
    """
    Ordena a lista de personagens pelo valor de vida (crescente).
    """
    return sorted(personagens, key=lambda p: p.vida)


caminho_arquivo = r'c:\Users\Guilh\Desktop\Lusófona\FP\FPSemana06\personagens.json'



print(f"Diretório atual: {os.getcwd()}")


personagens, num_personagens = importar_personagens(caminho_arquivo)
if num_personagens == 0:
    print("Nenhum personagem foi importado. Encerrando o programa.")
else:
    print(f"{num_personagens} personagens entram em batalha!")

    
    personagens = ordenar_personagens_por_vida(personagens)

    for p in personagens:
        print(p)

    
    personagens[0].atacar(personagens[1])
    personagens[1].atacar(personagens[2])
    personagens[2].atacar(personagens[0])

  
    if isinstance(personagens[0], Guerreiro):
        personagens[0].especial(personagens[1])
    if isinstance(personagens[1], Arqueiro):
        personagens[1].especial([personagens[0], personagens[2]])
    if isinstance(personagens[2], Mago):
        personagens[2].especial()

 
    for p in personagens:
        print(p)

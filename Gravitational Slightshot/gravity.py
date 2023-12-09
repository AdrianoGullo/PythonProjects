import pygame

class Planeta:
    def __init__(self, nome, raio, massa, gravidade, imagem):
        self.nome = nome
        self.raio = raio
        self.massa = massa
        self.gravidade = gravidade
        self.imagem = imagem

def criar_planetas():
    dados_planetas = [
        {"nome": "Mercúrio", "raio": 2439.7, "massa": 3.3011e23, "gravidade": 3.7, "imagem": "images/mercurio.jpg"},
        {"nome": "Vênus", "raio": 6051.8, "massa": 4.8675e24, "gravidade": 8.87, "imagem": "images/venus.jpg"},
        {"nome": "Terra", "raio": 6371, "massa": 5.972e24, "gravidade": 9.8, "imagem": "images/terra.jpg"},
        {"nome": "Marte", "raio": 3389.5, "massa": 6.4171e23, "gravidade": 3.7, "imagem": "images/marte.jpg"},
        {"nome": "Júpiter", "raio": 69911, "massa": 1.898e27, "gravidade": 24.79, "imagem": "images/jupiter.jpg"},
        {"nome": "Saturno", "raio": 58232, "massa": 5.683e26, "gravidade": 10.44, "imagem": "images/saturno.jpg"},
        {"nome": "Urano", "raio": 25362, "massa": 8.681e25, "gravidade": 8.69, "imagem": "images/urano.jpg"},
        {"nome": "Netuno", "raio": 24622, "massa": 1.0247e26, "gravidade": 11.15, "imagem": "images/netuno.jpg"}
    ]

    planetas = [Planeta(**dados) for dados in dados_planetas]

    return planetas

def exibir_informacoes(planetas):
    # Exemplo de acesso a informações
    for planeta in planetas:
        print(
            f"{planeta.nome}: Raio = {planeta.raio} km, Massa = {planeta.massa} kg, "
            f"Gravidade = {planeta.gravidade} m/s²")

def main():

    planetas = criar_planetas()
    exibir_informacoes(planetas)

    pygame.init()

    width, height = 800, 600
    janela = pygame.set_mode((width, height))
    pygame.display.set_caption("Gravitational Slingshot")

if __name__ == "__main__":
    main()

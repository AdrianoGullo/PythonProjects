import pygame

pygame.init()

width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravitational Slingshot")
FPS = 60
tam_nave = 2

#Cores
branco = (255, 255, 255)
vermelho = (255, 0, 0)
azul = (0, 0, 255)

class aeronave:
    def __int__(self, x, y, vel_x, vel_y, massa):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.massa = massa

    def draw(self):
        pygame.draw.circle(win, vermelho, (int(self.x), int(self.y)), tam_nave)

class Planeta:
    def __init__(self, nome, raio, massa, gravidade, imagem):
        self.nome = nome
        self.raio = raio
        self.massa = massa
        self.gravidade = gravidade
        self.imagem = imagem

# def criar_planetas():
#     dados_planetas = [
#         {"nome": "Mercúrio", "raio": 2439.7, "massa": 3.3011e23, "gravidade": 3.7, "imagem": "images/mercurio.jpg"},
#         {"nome": "Vênus", "raio": 6051.8, "massa": 4.8675e24, "gravidade": 8.87, "imagem": "images/venus.jpg"},
#         {"nome": "Terra", "raio": 6371, "massa": 5.972e24, "gravidade": 9.8, "imagem": "images/terra.jpg"},
#         {"nome": "Marte", "raio": 3389.5, "massa": 6.4171e23, "gravidade": 3.7, "imagem": "images/marte.jpg"},
#         {"nome": "Júpiter", "raio": 69911, "massa": 1.898e27, "gravidade": 24.79, "imagem": "images/jupiter.jpg"},
#         {"nome": "Saturno", "raio": 58232, "massa": 5.683e26, "gravidade": 10.44, "imagem": "images/saturno.jpg"},
#         {"nome": "Urano", "raio": 25362, "massa": 8.681e25, "gravidade": 8.69, "imagem": "images/urano.jpg"},
#         {"nome": "Netuno", "raio": 24622, "massa": 1.0247e26, "gravidade": 11.15, "imagem": "images/netuno.jpg"}
#     ]
#
#     tabela_dados = [Planeta(**dados) for dados in dados_planetas]
#     return tabela_dados

def exibir_informacoes(planetas):
    for planeta in planetas:
        print(
            f"{planeta.nome}: Raio = {planeta.raio} km, Massa = {planeta.massa} kg, "
            f"Gravidade = {planeta.gravidade} m/s²")

#planetas = criar_planetas()
velocidade = 100    # m/s

background = pygame.transform.scale(pygame.image.load("images/background.gif"), (width, height))
#img_planeta = pygame.transform.scale(pygame.image.load(planetas[escolha].imagem), ((planetas[escolha].raio/1000)*2, (
#        planetas[escolha].raio/1000)*2))
#nave = pygame.transform.scale(pygame.image.load("images/rocket.gif"), (0, 0))

def main():
    running = True
    clock = pygame.time.Clock()

    objects = []
    temp_obj_position = None

    while running:
        clock.tick(FPS)

        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                temp_obj_position = mouse_position

        win.blit(background, (0, 0))
        if temp_obj_position:
            pygame.draw.line(win, branco, temp_obj_position, mouse_position, 1)
            pygame.draw.circle(win, vermelho, temp_obj_position, tam_nave)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()

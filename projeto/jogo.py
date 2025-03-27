import random

class personagem :
    def __init__(self, nome, vida, nivel):
        self.__nome = nome 
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome   
    def get_vida(self):
        return self.__vida  
    def get_nivel(self):
        return self.__nivel  
    def exibir_detelhes(self):
        return f'Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNivel: {self.get_nivel()}'
    
    def receber_dano(self, dano):
        """Método para receber dano."""
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0

    def atacar(self, alvo):
        """Método para atacar outro personagem.""" 
        dano = random.randint(self.get_nivel() * 2 , self.get_nivel() * 4)  # Dano aleatório entre 1 e 10
        alvo.receber_dano(dano)  # O alvo recebe o dano
        print (f'{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!')
    
        
    
class heroi(personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    def get_habilidade(self):
        return self.__habilidade
    def exibir_detelhes(self):
        return f'{super().exibir_detelhes()} \nHabilidade: {self.get_habilidade()}\n'
    def usar_habilidade(self, alvo):
        """Método para usar a habilidade especial."""
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 10)  # Dano aleatório entre 1 e 10
        alvo.receber_dano(dano)  # O alvo recebe o dano
        print(f'{self.get_nome()} usou a habilidade {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!')
    
class vilao(personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    def get_tipo(self): 
        return self.__tipo
    def exibir_detelhes(self):
        return f'{super().exibir_detelhes()} \nTipo: {self.get_tipo()}\n'
    
class jogo :
    """Classe orquestradora do jogo."""

    def __init__(self):
        self.heroi = heroi(nome='Thor',vida= 100, nivel=10,habilidade= 'Raio')
        self.vilao = vilao(nome='Loki', vida=80, nivel=8, tipo= 'Trapaceiro')

    def iniciar_batalha(self):
        """ Fazer a gestão da batalha em turnos"""
        print('Iniciando batalha entre:', self.heroi.get_nome(), 'e', self.vilao.get_nome())
        while self.heroi.get_vida() > 0 and self.vilao.get_vida() > 0:
            print("Detalhes dos personagens:")
            # Exibe os detalhes dos personagens
            print(self.heroi.exibir_detelhes())
            print(self.vilao.exibir_detelhes())
        
             
            input('Pressione Enter para atacar...')
            escolha = input('Escolha uma ação: 1 - Atacar, 2 - Usar habilidade: ')
            if escolha == '1':
                self.heroi.atacar(self.vilao)
            elif escolha == '2':
                self.heroi.usar_habilidade(self.vilao)
            else:
                print('Escolha inválida!')
            if self.vilao.get_vida() > 0:
                self.vilao.atacar(self.heroi)
    
        if self.heroi.get_vida() > 0:
                print(f'Você venceu a batalha!')
        else:
                print(f'Você perdeu a batalha!')
           
# Cria uma instância do jogo e inicia a batalha
jogo = jogo()
jogo.iniciar_batalha()



        
        
     
import os

class Wclass:
    def __init__(self, playername, charname, hp, force, classe):
        self.nome = charname
        self.hp = hp
        self.força = force
        self.classe = classe
        self.nomejogador = playername
        
os.system("clear")
print("nome de jogador:")
playername=input()
os.system('clear')
print('nome do personagem:')
charname=input()
os.system('clear')
print("qual a classe de seu personnagem?")
print("1 - Guerreiro")
print("2 - Mago")
charclass=input()

if charclass== ('1'):
	os.system("clear")
	print("fihca personagem:")
	player = Wclass(playername, charname, "20", "30", "guerreiro")
	print("Nome jogador: "+player.nomejogador)
	print("nome: "+player.nome)
	print("HP: "+player.hp)
	print("força: "+player.força)
	print("classe: "+player.classe)
	print('')
	print("_______________________")
	print("escolha uma opção:")
	print('1 - iniciar jogo')
	start = input()
	while True:
		if start == ('1'):
			os.system("clear")
			print("_______________________")
			print("Jogador: "+player.nomejogador)
			print("Hero: "+player.nome)
			print("HP: "+player.hp)
			print("Classe: "+player.classe)
			print("_______________________")
			print("Um gobblin apareceu o que vai fazer?")
			print("1 - atacar")
			print("2 - defender")
			print("3 - correr")
			
			input()			
			os.system("clear")

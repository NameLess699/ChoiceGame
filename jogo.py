import time
import random

# starter = random.randint(0, 2)
starter = 1
path = ""
pathlist = ["1", "2"]
name = input("Qual seu nome? ")
name = name.title()
chance = 0
noun = input("[1 ELE | 2 ELA] ")
greatmage = ""
life = True

while noun not in pathlist:
    noun = input("[1 ELE | 2 ELA] ")

if noun == "1":
    greatmage = "O grande mago"
elif noun == "2":
    greatmage = "A grande maga"    



print("\n")

time.sleep(2)

print(f"Olá {name}, aqui, sua história começa: \n")

print("...\n")

time.sleep(2)

while life == True:

    if starter == 1:
        print(f"Você acorda em uma floresta escura.\n ")
        time.sleep(1)
        path = input("Na sua frente tem 2 caminhos, direita, ou esquerda, em cada um tem uma placa, dizendo que o caminho da esquerda é longo, e o da direita é curto, qual você escolhe? [1 ESQUERDA | 2 DIREITA] ")
        print("\n")
        pathlist = ["1", "2"]
        
        while path not in pathlist:
            path = input("Resposta invalida, tente novamente: ")
            
        if path in pathlist:
            
            if path == "1":
                print("Você decide ir para o caminho da esquerda, você começa a seguir o longo caminho...\n") #LEFT PATH
                time.sleep(5)
                path = input("Você encontra um tigre dormindo no meio do caminho, do lado dele tem um objeto estranho, tentar pegar o objeto ou contornar com cautela o tigre? [1 PEGAR | 2 CONTORNAR] ")
                print("\n")
                pathlist = ["1", "2"]
                
                while path not in pathlist:
                    path = input("Resposta invalida, tente novamente: ")
                                
                if path == "1":
                    print("Você se aproxima do tigre e tenta pegar o objeto...\n") #TRY TO GET SWORD
                    chance = random.randint(1, 2)
                    # print(chance) ###
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    print("...\n")
                    time.sleep(1)
                    
                    if chance == 1:
                        print("Você consegue pegar o objeto sem acordar o tigre, era uma espada.\n") #SUCESS SWORD
                        time.sleep(1)
                        print("Você continua o longo caminho...")
                        chance = random.randint(1, 3)
                        # print(chance) ###
                        
                        if chance == 1:
                            print("Quando você estava prestes a continuar seu caminho, o tigre acorda e te ataca, começando uma épica batalha! \n") #TIGER PERCEPTION
                            chance = random.randint(1, 2)
                            # print(chance) ###
                            time.sleep(3)
                            
                            if chance == 1:
                                print("Com a combinação certa de sorte e habilidade com a espada, você consegue decapitar o tigre. \n") #TIGER DIES
                                print("Continuando o caminho você encontra uma casa. \n")
                                path = input("Entrando na casa  você encontra uma velha senhora, ela parece não ter te visto. [1 CONVERSAR | 2 MATAR] ") #WITCH SWORD
                                
                                while path not in pathlist:
                                    path = input("Resposta invalida, tente novamente: ")
                                    
                                if path == "1":
                                    print("Ela fica furiosa com um intruso em sua casa, se revelando uma bruxa e te transformando em um sapo, GAME OVER") #WITCH KILLS TALK
                                    live = False
                                elif path == "2":
                                    chance = random.randint(1, 5)
                                    # print(chance) ###
                                    
                                    if chance == "1":
                                        time.sleep(1)
                                        print("...")
                                        time.sleep(1)
                                        print("...")
                                        time.sleep(1)
                                        print("...")
                                        time.sleep(1)
                                        print("\n")
                                        print("Quando você estava prestes a atacar com sua espada, a senhora percebe, e te transforma em sapo, GAME OVER") #WITCH KILLS
                                        life = False
                                        
                                    elif chance != "1":
                                        time.sleep(1)
                                        print("...")
                                        time.sleep(1)
                                        print("...")
                                        time.sleep(1)
                                        print("...")
                                        time.sleep(1)
                                        print("\n")
                                        print(f"Você mata a  senhora, e explorando sua casa, chega a conclusão que se tratava de uma bruxa, estudando seus livros, você conjuro uma magia que faz relembrar seu passado e retornar para casa, nesse tempo você recebe o titulo de {name}, o grande mago. VOCÊ VENCEU!") #WITCH DIES

                                
                            if chance != "1":
                                print("O tigre te mata, GAME OVER ") #TIGER KILLS
                                life = False
                        
                        if chance != "1":
                            
                            time.sleep(2)
                            print("Continuando o caminho você encontra uma casa. \n")
                            path = input("Entrando na casa  você encontra uma velha senhora, ela parece não ter te visto. [1 CONVERSAR | 2 MATAR] ") #WITCH SWORD
                            pathlist = ["1", "2"]
                            
                            while path not in pathlist:
                                path = input("Resposta invalida, tente novamente: ")
                                        
                            if path == "1":
                                time.sleep(1)
                                print("\n")
                                print("Ela fica furiosa com um intruso em sua casa, se revelando uma bruxa e te transformando em um sapo, GAME OVER") #WITCH KILLS TALK

                                    
                            elif path == "2":
                                time.sleep(1)
                                chance = random.randint(1, 5)
                                # print(chance) ###
                                print("\n")
                                
                                if chance == "1":
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("\n")
                                    print("Quando você estava prestes a atacar com sua espada, a senhora percebe, e te transforma em sapo, GAME OVER") #WITCH KILLS
                                    life = False
                                    
                                    input("")
                                    exit()
                                            
                                elif chance != "1":
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("...")
                                    time.sleep(1)
                                    print("\n")
                                    print(f"Você mata a  senhora, e explorando sua casa, chega a conclusão que se tratava de uma bruxa, estudando seus livros, você conjuro uma magia que faz relembrar seu passado e retornar para casa, nesse tempo você recebe o titulo de {name}, {greatmage}. VOCÊ VENCEU!") #WITCH DIES
                                    
                                    input("")
                                    exit()
                            
                    if chance == 2:
                        print("O tigre acorda, te ataca e você morre. GAME OVER") 
                        life = False 

                        input("")
                        exit()
                
                if path == "2":
                    chance = random.randint(1, 3)
                    # print(chance) ###
                    if chance == 1:
                        print("O tigre acorda e te ataca. GAME OVER")
                        life = False
                        
                        input("")
                        exit()
                    elif chance != 1:
                        print("Você continua o longo caminho...")
                        time.sleep(2)
                        print("Continuando o caminho você encontra uma casa. \n")
                        path = input("Entrando na casa  você encontra uma velha senhora, ela parece não ter te visto. [1 CONVERSAR | 2 MATAR] ") #WITCH SWORD
                                
                        while path not in pathlist:
                            path = input("Resposta invalida, tente novamente: ")
                                    
                        if path == "1":
                            print("Ela fica furiosa com um intruso em sua casa, se revelando uma bruxa e te transformando em um sapo, GAME OVER") #WITCH KILLS TALK
                            life = False
                                
                        elif path == "2":
                            chance = random.randint(1, 10)
                                
                            if chance != "1":
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                print("\n")
                                print("Quando você estava prestes a atacar, a senhora percebe, e te transforma em sapo, GAME OVER") #WITCH KILLS
                                life = False
                                  
                            elif chance == "1":
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                print("...")
                                time.sleep(1)
                                print("\n")
                                print(f"Você mata a  senhora, e explorando sua casa, chega a conclusão que se tratava de uma bruxa, estudando seus livros, você conjuro uma magia que faz relembrar seu passado e retornar para casa, nesse tempo você recebe o titulo de {name}, {greatmage}. VOCÊ VENCEU!") #WITCH DIES
    
            elif path == "2":
                print("Você decide ir para o caminho da direita, você começa a seguir o curto caminho... \n") #RIGHT PATH
                time.sleep(2)   
                path = input("No meio do caminho, você encontra um bau relativamente estranho, deseja abri-lo? [1 ABRIR | IGNORAR] ")
                print("\n")
                
                if path == "1":
                    print("Chegando mais perto você percebe que o bau tem uma divisão no meio, se tornando um bau duplo, com 2 cadiados e 1 chave jogada logo ao seu lado.")
                    path = input("Você vai abrir o cadeado da esquerda ou da direita? [1 ESQUERDA | 2 DIREITA]")
                    
                    if path == "1":
                        print("Era uma armadilha, o bau explode e você junto, GAME OVER")
                        life = False
                    
                    elif path == "2":
                        print("teste")
                        
                    
                
                
            




# elif starter == 2:
#     print("Você acorda em um campo. ")
    



input("")
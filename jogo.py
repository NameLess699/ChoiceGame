import time
import random
import os
import webbrowser
from datetime import datetime

#SETTINGS

tester = False
setup = True
game = True

#DEFINE MAIN

def main():

#SETUP:

    if setup:
        
        file = "E:\Importante\Codes\PY\PROJECTS\CHOICE GAME\gamedata.txt"
        life = True
        name = None
        noun = None
        path = None
        chance = None
        greatwitch = None
        pathlist = ["1", "2"]
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        # starter = random.randint(0, 2)
        starter = 1

        with open(file, "a") as t:
            
                t.write("\n")
                t.write("\n")
                
        def reset():
            
            global chance
            global path
            global pathlist
            chance = ""
            path = "" 
            pathlist = ["1", "2"]       

        def write(text):
            
            global name
            with open(file, "a") as t:
                t.write(f"{text} ")

        def clear_screen():
            
            if os.name == 'posix':
                _ = os.system('clear')
            elif os.name == 'nt':
                _ = os.system('cls')
                
        def suspense(cooldown):   
            
            print("\n")   
            time.sleep(cooldown)
            print("...")
            time.sleep(cooldown)
            print("...")
            time.sleep(cooldown)
            print("...\n")
            time.sleep(cooldown)


        if not tester:
            
            clear_screen()
            name = input("Qual seu nome? ")
            name = name.title()
            noun = input("[1 ELE | 2 ELA] ")
            while noun not in pathlist:
                noun = input("[1 ELE | 2 ELA] ")
                
        elif tester:
            
            name = "nome sobrenome"
            name = name.title()
            noun = "1"

        if noun == "1":
            
            greatwitch = "O grande bruxo"
            yournewleader = "seu novo rei"
            
        elif noun == "2":
            
            greatwitch = "A grande bruxa"    
            yournewleader = "sua nova rainha"

#GAME:

    if game:
        
        write(f"{now}: Aqui comeca a historia de {name}:")

        print("\n")

        time.sleep(1)

        print(f"Olá {name}, aqui, sua história começa: \n")

        print("...\n")

        time.sleep(2)

        while life:

            if starter == 1:
                
                reset()
                print(f"Você acorda em uma floresta escura, sem memórias e sem ideia de quem você é, apenas seu nome ({name}), seu principal objetivo no momento é recuperar sua memória, é melhor ir andando...\n ")
                time.sleep(1)
                path = input("Na sua frente tem 2 caminhos, direita, ou esquerda, em cada um tem uma placa, dizendo que o caminho da esquerda é longo, e o da direita é curto, qual você escolhe? [1 ESQUERDA | 2 DIREITA] ")
                print("\n")
                
                while path not in pathlist:
                    
                    path = input("Resposta invalida, tente novamente: ")
                    
                if path in pathlist:
                    
                    if path == "1":
                        
                        reset()
                        write("escolheu o caminho da esquerda,")
                        print("Você decide ir para o caminho da esquerda, você começa a seguir o longo caminho...\n") #LEFT PATH
                        time.sleep(5)
                        path = input("Você encontra um tigre dormindo no meio do caminho, do lado dele tem um objeto estranho, tentar pegar o objeto ou contornar com cautela o tigre? [1 PEGAR | 2 CONTORNAR] ")
                        print("\n")
                        pathlist = ["1", "2"]
                        
                        while path not in pathlist:
                            
                            path = input("Resposta invalida, tente novamente: ")
                                        
                        if path == "1":
                            
                            reset()
                            write("tentou pegar o objeto misterioso,")
                            print("Você se aproxima do tigre e tenta pegar o objeto...\n") #TRY TO GET SWORD
                            chance = random.randint(1, 2)
                            suspense(1)
                            
                            if chance == 1:
                                
                                reset()
                                write("conseguiu pegar a espada,")
                                print("Você consegue pegar o objeto sem acordar o tigre, era uma espada.\n") #SUCESS SWORD
                                time.sleep(1)
                                print("Você continua o longo caminho...")
                                chance = random.randint(1, 3)
                                suspense(0.5)
                                
                                if chance == 1:
                                    
                                    reset()
                                    write("lutou com o tigre,")
                                    print("Quando você estava prestes a continuar seu caminho, o tigre acorda e te ataca, começando uma épica batalha! \n") #TIGER PERCEPTION
                                    suspense(1)
                                    chance = random.randint(1, 2)
                                    time.sleep(3)
                                    
                                    if chance == 1:
                                        
                                        reset()
                                        write("matou o tigre,")
                                        print("Com a combinação certa de sorte e habilidade com a espada, você consegue decapitar o tigre. \n") #TIGER DIES
                                        print("Continuando o caminho você encontra uma casa. \n")
                                        path = input("Entrando na casa  você encontra uma velha senhora, ela parece não ter te visto. [1 CONVERSAR | 2 MATAR] ") #WITCH SWORD
                                        
                                        while path not in pathlist:
                                            
                                            path = input("Resposta invalida, tente novamente: ")
                                            
                                        if path == "1":
                                            
                                            reset()
                                            write("na tentativa de conversar morre para a bruxa. GAME OVER")
                                            print("Ela fica furiosa com um intruso em sua casa, se revelando uma bruxa e te transformando em um sapo, GAME OVER") #WITCH KILLS TALK
                                            life = False
                                            reset()
                                            
                                        elif path == "2":
                                            
                                            reset()
                                            write("tenta matar a bruxa,")
                                            chance = random.randint(1, 5)
                                            
                                            if chance == "1":
                                                reset()
                                                write("morre para a bruxa. GAME OVER")
                                                suspense(1)
                                                print("Quando você estava prestes a atacar com sua espada, a senhora percebe, e te transforma em sapo, GAME OVER") #WITCH KILLS
                                                life = False
                                                reset()
                                                
                                            elif chance != "1":
                                                
                                                reset()
                                                write(f"mata a bruxa, ganhando o titulo de {name} {greatwitch}")
                                                write("GANHOU!")
                                                suspense(1)
                                                print(f"Você mata a  senhora, e explorando sua casa, chega a conclusão que se tratava de uma bruxa, estudando seus livros, você conjuro uma magia que faz relembrar seu passado e retornar para casa, nesse tempo você recebe o titulo de {name}, {greatwitch}. VOCÊ VENCEU!") #WITCH DIES
                                                print("VOCÊ GANHOU")
                                                life = False
                                                reset()
                                        
                                    elif chance == "2":
                                        
                                        reset()
                                        write("morre para o tigre. GAME OVER")
                                        print("O tigre te mata, GAME OVER ") #TIGER KILLS
                                        life = False
                                        reset()
                                
                                elif chance != "1":
                                    
                                    reset()
                                    write("entrou na casa da floresta,")
                                    time.sleep(2)
                                    print("Continuando o caminho você encontra uma casa. \n")
                                    path = input("Entrando na casa  você encontra uma velha senhora, ela parece não ter te visto. [1 CONVERSAR | 2 MATAR] ") #WITCH SWORD
                                    
                                    while path not in pathlist:
                                        path = input("Resposta invalida, tente novamente: ")
                                                
                                    if path == "1":
                                        
                                        reset()
                                        write("morre para a bruxa. GAME OVER")
                                        time.sleep(1)
                                        print("\n")
                                        print("Ela fica furiosa com um intruso em sua casa, se revelando uma bruxa e te transformando em um sapo, GAME OVER") #WITCH KILLS TALK
                                        life = False
                                        reset()

                                    elif path == "2":
                                        
                                        reset()
                                        write("tenta matar a bruxa,")
                                        time.sleep(1)
                                        chance = random.randint(1, 5)
                                        print("\n")
                                        
                                        if chance == "1":
                                            
                                            reset()
                                            write("falha, resultando em morte. GAME OVER")
                                            suspense(1)
                                            print("Quando você estava prestes a atacar com sua espada, a senhora percebe, e te transforma em sapo, GAME OVER") #WITCH KILLS
                                            life = False
                                            reset()
                                                    
                                        elif chance != "1":
                                            
                                            reset()
                                            write(f"mata a bruxa, ganhando o titulo de {name} {greatwitch}")
                                            write("GANHOU!")
                                            suspense(1)
                                            print(f"Você mata a  senhora, e explorando sua casa, chega a conclusão que se tratava de uma bruxa, estudando seus livros, você conjuro uma magia que faz relembrar seu passado e retornar para casa, nesse tempo você recebe o titulo de {name}, {greatwitch}. VOCÊ VENCEU!") #WITCH DIES
                                            print("VOCÊ GANHOU")
                                            life = False
                                            reset()
                                    
                            elif chance == 2:
                                
                                reset()
                                write("morre para o tigre. GAME OVER")
                                print("O tigre acorda, te ataca e você morre. GAME OVER") 
                                life = False 
                                reset()
                        
                        if path == "2":
                            
                            chance = random.randint(1, 3)
                            suspense(1)
                            
                            if chance == 1:
                                
                                reset()
                                write("morre para o tigre. GAME OVER")
                                print("O tigre acorda e te ataca. GAME OVER")
                                life = False
                                reset()
                                
                            elif chance != 1:
                                
                                reset()
                                write("continuou o longo caminho,")
                                print("Você continua o longo caminho...")
                                time.sleep(2)
                                print("Continuando o caminho você encontra uma casa. \n")
                                path = input("Entrando na casa  você encontra uma velha senhora, ela parece não ter te visto. [1 CONVERSAR | 2 MATAR] ") #WITCH SWORD
                                        
                                while path not in pathlist:
                                    
                                    path = input("Resposta invalida, tente novamente: ")
                                            
                                if path == "1":
                                    
                                    reset()
                                    write("na tentativa de conversar morre para a bruxa. GAME OVER")
                                    print("Ela fica furiosa com um intruso em sua casa, se revelando uma bruxa e te transformando em um sapo, GAME OVER") #WITCH KILLS TALK
                                    life = False
                                    reset()
                                        
                                elif path == "2":
                                    
                                    reset()
                                    write("tenta matar a bruxa,")
                                    chance = random.randint(1, 10)
                                        
                                    if chance != "1":
                                        
                                        reset()
                                        write("falha, resultando em morte. GAME OVER")
                                        suspense(1)
                                        print("Quando você estava prestes a atacar, a senhora percebe, e te transforma em sapo, GAME OVER") #WITCH KILLS
                                        life = False
                                        reset()
                                        
                                    elif chance == "1":
                                        
                                        reset()
                                        write(f"mata a bruxa, ganhando o titulo de {name} {greatwitch}")
                                        write("GANHOU!")
                                        suspense(1)
                                        print(f"Você mata a  senhora, e explorando sua casa, chega a conclusão que se tratava de uma bruxa, estudando seus livros, você conjuro uma magia que faz relembrar seu passado e retornar para casa, nesse tempo você recebe o titulo de {name}, {greatwitch}. VOCÊ VENCEU!") #WITCH DIES
                                        print("VOCÊ GANHOU")
                                        life = False
                                        reset()
                                        
                    elif path == "2":
                        
                        reset()
                        write("decide ir pelo caminho da direita,")
                        print("Você decide ir para o caminho da direita, você começa a seguir o curto caminho... \n") #RIGHT PATH
                        time.sleep(2)   
                        path = input("No meio do caminho, você encontra um bau relativamente estranho, deseja abri-lo? [1 ABRIR | 2 IGNORAR] ")
                        print("\n")
                        
                        while path not in pathlist:
                                
                            path = input("Resposta invalida, tente novamente: ")
                        
                        if path == "1":
                            
                            reset()
                            write("tenta abrir o bau,")
                            print("Chegando mais perto você percebe que o bau tem uma divisão no meio, se tornando um bau duplo, com dois cadeados e uma chave jogada logo ao seu lado.")
                            path = input("Você vai abrir o cadeado da esquerda ou da direita? [1 ESQUERDA | 2 DIREITA] ")
                            print("\n")
                            
                            while path not in pathlist:
                                
                                path = input("Resposta invalida, tente novamente: ")
                            
                            if path == "1":
                                
                                reset()
                                write("falha em abrir o bau, sendo explodido. GAME OVER") #DIES TO CHEST
                                suspense(1)
                                print("Era uma armadilha, o bau explode e você junto, GAME OVER\n")
                                life = False
                                reset()

                            elif path == "2":
                                
                                reset()
                                write("consegue abrir o bau,") #OPENS CHEST
                                suspense(1)
                                print("Você escolhe abrir o cadeado da direita. Com um clique, o cadeado se abre e você abre a tampa do baú. Dentro, você encontra um mapa antigo.")
                                path = input("Após ler o mapa, percebe-se que o destino (marcado com um grande X vermelho) é bem perto, deseja continuar o caminho atual ou ir em direção à densa floresta aonde o atrante X vermelho se encontra? [1 CONTINUAR | 2 SEGUIR O MAPA] ")
                                print("\n")
                                
                                while path not in pathlist:
                                    
                                    path = input("Resposta invalida, tente novamente:")
                                
                                if path == "1":
                                    
                                    reset()
                                    time.sleep(2)
                                    write("continua o caminho, chegando no deserto,")
                                    print("\n")
                                    print("Continuando o caminho você acaba chegando em um deserto, chegando de encontro com uma esfinge...")
                                    time.sleep(2)
                                    print("\n")
                                    print("A esfinge diz que ira fazer uma charada, e seu pedido sera realizado...")
                                    time.sleep(3)
                                    print("\n")
                                    path = input("Ela então diz: Oque é Oque é, quanto mais enxuga, mais molhado fica? ").lower()
                                    answer = "toalha"
                                    suspense(1)
                                    
                                    if answer in path:
                                        
                                        reset()
                                        write("Acerta a charada, entao a esfinge, faz a proxima charada.")
                                        print("Resposta certa, responda mais 2 charadas, e realizarei seu desejo de voltar para casa. diz a esfinge, enquanto brilha com uma aura magica.")
                                        print("\n")
                                        path = input("O que é que quanto mais você tira, maior ele fica? ")
                                        answer = "buraco"
                                        suspense(1)
                                        
                                        if answer in path:
                                            
                                            reset()
                                            write("Acerta pela segunda vez a charada da esfinge,")
                                            print("Resposta certa, responda mais 1 charada, e realizarei seu desejo de voltar para casa. diz a esfinge, enquanto brilha com uma aura ainda mais magica.")
                                            print("\n")
                                            path = input("Quanto mais houver de mim, menos você vera, quem sou eu? ")
                                            answer = ["escuro", "sombra", "escuridão"]
                                            index = 0
                                            suspense(1)
                                            
                                            if path in answer:
                                                reset()
                                                write("Acerta a charada, entao a esfinge, com seus poderes magicos, recupera sua memoria e te leva de volta para casa.")
                                                write("GANHOU!")
                                                suspense(1)
                                                print("Resposta certa! diz a esfinge, enquanto brilha com uma aura magica, você sente sua memória voltando, e quando percebe, ja se encontra em casa, deitado em sua cama.")
                                                print("VOCÊ GANHOU")
                                                life = False
                                                reset()

                                            elif path not in answer:
                                                reset()
                                                write("erra a charada. GAME OVER")
                                                print("Resposta errada! diz a esfinge enquanto te esmaga com sua grande pata de pedra. GAME OVER") #ERRADO
                                                life = False
                                                reset()
                                                
                                        elif answer not in path:
                                            
                                            reset()
                                            write("erra a charada. GAME OVER")
                                            print("Resposta errada! diz a esfinge enquanto te esmaga com sua grande pata de pedra. GAME OVER")
                                            life = False
                                            reset()
                                        
                                        
                                    elif answer not in path:
                                        
                                        reset()
                                        write("erra a charada. GAME OVER")
                                        print("Resposta errada! diz a esfinge enquanto te esmaga com sua grande pata de pedra. GAME OVER")
                                        life = False
                                        reset()
                                    
                                elif path == "2":
                                    
                                    reset()
                                    write("segue o caminho marcado no mapa, encontrando uma caverna,")
                                    time.sleep(1)
                                    print("Seguindo o caminho marcado no mapa, você encontra uma caverna com uma grande entrada.")
                                    time.sleep(1)
                                    path = input("Entrando nela você se depara com 2 caminhos, sendo eles esquerda e direita, qual você escolhe? [1 ESQUERDA | 2 DIREITA] ")
                                    print("\n")
                                    time.sleep(3)

                                    while path not in pathlist:
                                    
                                        path = input("Resposta invalida, tente novamente: ")
                                        
                                    if path == "1":
                                        
                                        reset()
                                        write("dentro da caverna, decide seguir o caminho da esquerda")
                                        print("Enquanto segue o caminho da esquerda, percebe pequenas risadas e cochichos vindo das sombras")
                                        suspense(1)
                                        path = input("Quando menos espera, você percebe cercado por goblins. [1 LUTAR | 2 FUGIR] ")
                                        print("\n")
                                        suspense(2)
                                        
                                        while path not in pathlist:
                                            
                                            path = input("Resposta invalida, tente novamente: ")
                                            
                                        if path == "1":
                                            
                                            reset()
                                            write("decide lutar contra os goblins,")
                                            chance = random.randint(1, 5)
                                            
                                            if chance != 1:
                                                
                                                reset()
                                                write("consegue a vitória na luta contra a gangue de goblins")
                                                suspense(1)
                                                path = input("Você derrota os goblins, o lider deles está no chão pedindo por misericórdia. [1 MATAR | 2 POUPAR] ")
                                                print("\n")
                                                suspense(1)
                                                
                                                while path not in pathlist:
                                                    
                                                    path = input("Resposta invalida, tente novamente: ")
                                                    
                                                if path == "1":
                                                    
                                                    reset()
                                                    write("nao tem piedade sobre o lider dos goblins,")
                                                    print("Você decide não dar o beneficio da segunda chance para o lider dos goblins, finalizando-o com um golpe de misericórdia.")
                                                    print("\n")
                                                    time.sleep(3)
                                                    path = input("Após explorar melhor o acampamento dos goblins, você encontra um baú com luzes saindo de suas frestas. [1 ABRIR] ")
                                                    pathlist ["1"]
                                                    
                                                    while path not in pathlist:
                                                        
                                                        path = input("Resposta invalida, tente novamente: ")
                                                        
                                                    if path == "1":
                                                        
                                                        reset()
                                                        write("morre na tentativa de abrir o bau brilhante. GAME OVER")
                                                        print("Quando se aproxima para abrir o bau, percebe que pisou em uma armadilha, causando uma grande explosão, e sua morte, GAME OVER")
                                                        life = False
                                                        reset()
                                           
                                                elif path == "2":
                                                    
                                                    reset()
                                                    write("tem piedade sobre o lider dos goblins,")  
                                                    print("Após demonstrar tamanho poder e piedade com o lider, ele decide conceder a você o maior tesouro, após desarmar as armadilhas de um bau que libera luzes pelas suas frestas, ao abri-lo, te revela uma grande coroa com uma brilhante gema preciosa")
                                                    print("\n")
                                                    time.sleep(3)
                                                    path = input("Aceitar o presente? [1 SIM | 2 NÃO] ")
                                                    suspense(1)
                                                    
                                                    while path not in pathlist:
                                                        
                                                        path = input("Resposta invalida, tente novamente: ") 
                                                
                                                    if path == "1":
                                                        
                                                        reset()
                                                        write(f"aceita o presente, recuperando as memorias com a gema magica, agora os goblins se curvam diante de {name} {yournewleader}.")
                                                        write("GANHOU!")
                                                        print("No mesmo momento que você coloca a coroa, sente uma energia magica fluindo sobre ela, conforme a magia adentra sua mente, a memória do seu antigo eu começa a voltar.")
                                                        print("\n")
                                                        print(f"Assim, com sua memória recuperada, agora os goblins se curvam diante de {name} {yournewleader}.")
                                                        print("VOCÊ GANHOU")
                                                        life = False
                                                        reset()
                                                        
                                                    elif path == "2":
                                                        
                                                        reset()  
                                                        write("recusa o presente, levando um golpe surpresa do goblin, resultando em sua morte. GAME OVER")
                                                        print("Você recusa o presente, e quando da as costas para o lider goblin, ele da um golpe certeiro com uma adaga, resultando em sua morte, GAME OVER")
                                                        life = False
                                                        reset()
                                                        
                                            elif chance == 1:
                                                
                                                reset()
                                                write("morre na luta contra os goblins. GAME OVER")
                                                print("Você tenta lutar contra a gangue de goblins, mas não é forte o suficiente, resultando em sua morte, GAME OVER")
                                                life = False
                                                reset()
                                                                                              
                                        elif path == "2":
                                            
                                            reset()
                                            write("tenta fugir dos goblins, morrendo no processo. GAME OVER")
                                            print("Quando você vira as costas e começa a correr, sente um calafrio, percebe que uma flecha atravessou seu peito, GAME OVER")
                                            life = False
                                            reset()    
                                        

                                        
                                    elif path == "2":
                                        
                                        reset()
                                        write("dentro da caverna, decide seguir o caminho da direita")
                                        path = input("Seguindo o caminho da direita, você percebe mais 2 caminhos, dessa vez um está claro a sua frente, e outro escondido em um lugar alto, porém relativamente facil de alcançar, uma vez que tem pedras formando uma escada, você nota uma musica peculiar vindo do caminho escondido nas alturas, qual caminho você escolhe? [1 CONTINUAR | 2 SUBIR] ")
                                        suspense(2)
                                        
                                        while path not in pathlist:
                                            
                                            path = input("Resposta invalida, tente novamente: ")

                                        if path == "1":
                                            
                                            reset()
                                            write("entra na sala astral,")
                                            print("À medida que você se aventura mais fundo, o tempo parece perder todo o significado. Horas podem passar como minutos, ou minutos podem se esticar em eternidades. Sussurros ecoam pelas câmaras, carregando segredos ancestrais e profecias misteriosas. Portais para outros mundos se abrem e se fecham, oferecendo vislumbres fugazes de realidades alternativas.")
                                            print("\n")
                                            suspense(3)
                                            print("Nesta caverna surreal, a linha entre o sonho e a realidade se desfaz, e os limites da imaginação são desafiados a cada passo.")
                                            print("\n")
                                            suspense(1)
                                            path = input("Você percebe uma luz no fim da caverna, e uma passagem sombria na sua direita, qual você escolhe? [1 LUZ | 2 PASSAGEM] ")
                                            suspense(2)
                                            
                                            while path not in pathlist:
                                                
                                                path = input("Resposta invalida, tente novamente: ")
                                                
                                            if path == "1":
                                                
                                                reset()
                                                write("escolhe o caminho da luz, morrendo com a força avassaladora. GAME OVER")
                                                print("Você segue em direção à luz cintilante, mas conforme se aproxima, é consumido por uma força avassaladora e desaparece para sempre na escuridão.")
                                                life = False
                                                reset()
                                            
                                            elif path == "2":
                                                
                                                reset()
                                                write("investiga a passagem sombria, transcendendo,")
                                                print("Você decide investigar a passagem escura e sinistra. Enquanto avança, sente uma sensação de leveza e claridade. De repente, você se vê emergindo de um portal, transcendendo para um plano superior de existência, assim transcendendo sua vida humana, para uma entidade superior, de tal grandeza, que suas memórias anteriores e vida passada não tem mais significado, agora você é um novo ser.")
                                                print("\n")
                                                suspense(3)
                                                path = input("Sua mente começa a se encher de conhecimento nunca visto antes, deseja se aprofundar no desconhecido ou limitar seu cerebro? [1 APROFUNDAR | 2 LIMITAR] ")
                                                suspense(1)
                                                
                                                while path not in pathlist:
                                                    
                                                    path = input("Resposta invalida, tente novamente: ")
                                                
                                                if path == "1":
                                                    
                                                    reset()
                                                    write("transcende muito, e acaba se matando. GAME OVER")
                                                    print("Se aprofundando em dito conhecimento transcedental, você percebe, que mesmo sendo uma entidade superior, sua vida não tem sentido, quando em comparação com a grandeza da existencia, e acaba se matando, GAME OVER")
                                                    life = False
                                                    reset()
                                                
                                                elif path == "2":
                                                
                                                    reset()
                                                    write("limita a ascensão, mantendo partes de sua humanidade, assim, caminhando na terra como um novo ser.")
                                                    write("GANHOU!")
                                                    print("Você limita a ascensão, mantendo partes de sua humanidade, assim, caminhando na terra como um novo ser, mesmo tendo conhecimento e memória de sua antiga vida, agora nada disso tem importância.")
                                                    print("VOCÊ GANHOU")
                                                    life = False
                                                    reset()                                            
                                        
                                        
                                        elif path == "2":
                                            
                                            reset()
                                            write("never gonna give you up. GAME OVER")
                                            print("Você sente uma energia estranha... Demoniaca, e quanto mais se aproxima, mais forte fica, quando finalmente ganha visão doque há dentro da pequena entrada, percebe um homem, dançando ao som  de uma contagiante música...")
                                            suspense(4)
                                            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                                            life = False
                                            clear_screen()
                                            reset()
                                    
                        elif path == "2":
                            
                            write("decide ignorar o bau,")
                            reset()
                            time.sleep(2)
                            write("continua o caminho, chegando no deserto,")
                            print("\n")
                            print("Continuando o caminho você acaba chegando em um deserto, chegando de encontro com uma esfinge...")
                            time.sleep(2)
                            print("\n")
                            print("A esfinge diz que ira fazer uma charada, e seu pedido sera realizado...")
                            time.sleep(2)
                            print("\n")
                            path = input("Ela então diz: Oque é Oque é, quanto mais enxuga, mais molhado fica? ").lower()
                            answer = "toalha"
                            suspense(1)
                            
                            if answer in path:
                                
                                reset()
                                write("Acerta a charada, entao a esfinge, faz a proxima charada.")
                                print("Resposta certa, responda mais 2 charadas, e realizarei seu desejo de voltar para casa. diz a esfinge, enquanto brilha com uma aura magica.")
                                print("\n")
                                path = input("O que é que quanto mais você tira, maior ele fica? ")
                                answer = "buraco"
                                suspense(1)
                                
                                if answer in path:
                                    
                                    reset()
                                    write("Acerta pela segunda vez a charada da esfinge,")
                                    print("Resposta certa, responda mais 1 charada, e realizarei seu desejo de voltar para casa. diz a esfinge, enquanto brilha com uma aura ainda mais magica.")
                                    print("\n")
                                    path = input("Quanto mais houver de mim, menos você vera, quem sou eu? ")
                                    answer = ["escuro", "sombra", "escuridão"]
                                    index = 0
                                    suspense(1)
                                    
                                    if path in answer:
                                        reset()
                                        write("Acerta a charada, entao a esfinge, com seus poderes magicos, recupera sua memoria e te leva de volta para casa.")
                                        write("GANHOU!")
                                        suspense(1)
                                        print("Resposta certa! diz a esfinge, enquanto brilha com uma aura magica, você sente sua memória voltando, e quando percebe, ja se encontra em casa, deitado em sua cama.")
                                        print("VOCÊ GANHOU")
                                        life = False
                                        reset()

                                        
                                        
                                    elif path not in answer:
                                        reset()
                                        write("erra a charada. GAME OVER")
                                        print("Resposta errada! diz a esfinge enquanto te esmaga com sua grande pata de pedra. GAME OVER") #ERRADO
                                        life = False
                                        reset()
                                        

                                    
                                elif answer not in path:
                                    
                                    reset()
                                    write("erra a charada. GAME OVER")
                                    print("Resposta errada! diz a esfinge enquanto te esmaga com sua grande pata de pedra. GAME OVER")
                                    life = False
                                    reset()
                                
                                
                            elif answer not in path:
                                
                                reset()
                                write("erra a charada. GAME OVER")
                                print("Resposta errada! diz a esfinge enquanto te esmaga com sua grande pata de pedra. GAME OVER")
                                life = False
                                reset()
                                        
#OTHER:                     
                            
    if setup and game:

        def scary():
            clear_screen()
            print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣠⡭⣿⣽⣿⣯⣴⢏⡨⣌⣩⡈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠈⠶⡉⠍⠯⢿⣿⠿⠗⠈⠌⢿⣷⡷⡗⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⣠⠠⣾⡀⡙⡵⣵⢨⣧⢮⣦⣵⣿⣷⣧⠀⠠⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣶⢝⣾⣿⣷⣶⣿⣾⣧⣷⣶⣿⣿⣿⣿⣿⣿⣿⣪⣹⢔⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠺⢭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣝⣵⣤⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⠍⠁⢪⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⢉⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡉⢒⣺⣴⣵⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠟⢯⠽⠙⠃⢀⠀⠹⠹⣿⣿⣿⣿⣿⡿⠟⠋⠉⠉⠙⠛⣿⣿⣧⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⢀⠱⣀⠀⠀⠈⢿⣿⣿⠁⠀⠄⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠀⠀⠀⠀⠀⠀⠀⠦⠈⠃⠀⠀⣘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⠀⢀⠀⠀⢀⣴⣴⣾⣿⣿⣄⠀⢀⠀⠀⠀⢀⡀⠀⠠⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠓⠀⠈⠀⠂⠚⠃⢀⣤⣾⣿⣿⣿⣿⣿⣿⣧⣌⠓⠂⠒⠁⣀⣤⠞⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠰⣾⣾⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⡐⡤⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠐⢿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⠓⠝⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠘⢃⣿⣷⣿⣿⣿⣇⣹⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⠏⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠂⠙⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠻⠛⠛⠛⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⡡⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  
            """)
            time.sleep(0.1)
            clear_screen()
            clear_screen()
            print("""
            ⠀⠀⠀⢀⣠⣤⣶⣷⣿⣾⣦⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⢴⣾⣿⣿⠟⠛⠛⠻⠿⣿⣿⣿⣿⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⣶⣶⣶⣶⣦⡤⠀⠀⠀
            ⠀⣴⣿⣿⡟⣡⣴⣶⣶⣶⣤⣄⠉⢿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⣷⡀⠀
            ⣼⣿⣿⡟⣰⣿⣿⣿⣿⣿⣿⣿⣷⡀⠙⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠈⠙⠻⣿⣿⣷⡄
            ⣻⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠸⣿⡇⠀⠀⠀⠀⣠⠀⠀⠀⣿⣿⣿⠃⠀⠀⣠⣾⣿⣿⣿⣶⣤⡀⣿⣿⣿⡄
            ⠿⣿⣿⣿⣌⠻⣿⣿⣿⣿⣿⣿⣿⠟⠀⢠⣿⠇⠀⠀⠀⣤⣯⠀⠀⠀⣿⣿⡇⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⡇
            ⠐⢿⣿⣿⣿⣷⣌⡙⠛⠻⠛⠋⢁⣠⣴⣿⠏⠀⢀⣴⣿⣿⣿⣷⡀⠀⢹⣿⣷⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⠀
            ⠀⠝⢻⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⠋⢀⣴⣿⣿⣿⣿⣿⣿⣷⠀⠙⣿⣿⣷⣄⡈⠛⠛⠛⠛⢛⣫⣵⣿⣿⣿⡇⠀
            ⠀⠄⠀⠛⣿⢿⣿⣿⣿⣿⣿⠟⠉⠀⠁⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠐⠿⢿⣿⣿⣿⣷⣶⣶⣿⣿⣿⣿⣿⣿⣿⠃⠀
            ⠀⢠⣤⣄⣛⣹⣿⣇⣙⡏⠁⠀⠀⠀⠀⠀⠻⢿⠛⠻⢿⢿⣿⣿⣿⡇⠀⠀⠀⠙⠿⣿⡟⠭⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀
            ⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣤⣀⣀⣀⡘⠀⠀⠀⠀⠐⢿⡿⠁⠀⠀⠀⠀⠀⣸⠃⠀⣨⣴⣿⣿⣿⣿⠇⠀⠀⠀
            ⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣧⡟⠹⣉⡿⠋⠻⡿⠻⢷⡶⠦⣾⣇⣀⣀⣀⣴⣶⣶⣿⣷⣾⣿⣿⡿⢿⣿⠏⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠸⣿⣿⣿⣾⣿⣩⣷⣤⣨⣧⡀⢀⠇⠀⠀⡇⠀⠀⢿⠀⢿⣭⣿⣿⣼⣿⣿⣿⡿⠋⠀⢸⡟⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣶⣶⣧⣤⣼⣷⣿⣿⣿⣿⣿⠏⠀⠀⠀⠈⠇⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⣿⡈⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠈⠣⠀⠘⠻⣿⣿⣿⢿⣿⣿⣿⣿⡿⢿⣿⢿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣤⣧⣀⠀⡇⠀⠀⣧⠀⠸⠀⠘⢿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣶⣶⣿⣦⣾⣷⣾⡿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⠟⠉⠁⠀⣸⡟⠑⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠃⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      
            """)
            time.sleep(0.1)
            clear_screen()
            clear_screen()
            print("""
            ⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣷⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⠟⡿⠙⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
            ⠀⢀⣴⣿⣿⣿⣿⣿⣏⠤⠞⠈⠀⠀⢐⠃⠒⠡⡷⢿⢻⢎⣿⣿⣿⣷⡀⠀⠀⠀
            ⠀⢸⡟⢹⣿⣂⡹⢨⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⢉⠁⠀⢫⣻⣿⣿⣷⠀⠀⠀
            ⠀⣼⣇⣸⣿⣿⣿⣿⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠒⢹⢿⣿⣿⣾⣿⣿⣿⡀⠠⠀
            ⠀⣿⡿⢿⡟⢣⠝⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠸⣿⣿⢿⣿⣿⣿⡇⠀⠀
            ⠀⣿⠂⠈⠁⡀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠉⡈⠹⢿⣿⡇⢀⠀
            ⢀⣯⠀⠀⡞⢋⣩⣭⣭⣿⣯⡃⠀⠀⠀⠀⠀⢋⣉⣉⣉⣙⣛⠳⠤⡀⣛⣇⡀⠀
            ⣷⣿⡅⠀⢿⣿⣿⣿⣿⣻⢿⣿⣆⡄⠀⢀⣴⣿⢟⣝⣿⣽⣿⣷⣴⢩⣿⣿⡇⠀
            ⣿⣿⡅⢰⠯⡿⣿⣿⣿⠯⠿⢿⣿⣿⠀⡿⠻⠿⠾⣾⣿⣿⣿⢿⡿⣚⣿⣿⣇⠀
            ⢿⣿⡇⢸⡦⠁⠙⠉⠉⠀⠐⣸⣿⣿⢒⠇⠀⠀⠀⠉⠉⠉⣏⠘⣳⢛⣿⣿⣯⡂
            ⢸⣿⣷⡈⠁⠀⠀⠀⠀⠀⣰⣿⣿⣏⠼⠞⣠⡀⠀⠀⠀⠀⣸⠾⡽⠬⣿⣿⢇⡀
            ⠘⣿⡇⢰⡆⢀⢀⣀⣀⣴⣿⣿⣿⣷⣀⣖⡈⢻⣄⡤⣀⡠⣰⢠⣿⣠⣿⡿⠺⠁
            ⠀⢸⡟⢸⣓⣰⣰⢶⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣷⢫⠘⣵⣶⠻⣸⣯⠀⠸⡁
            ⠀⠈⢷⣺⣷⡃⣷⠾⢟⣻⢟⢻⢿⣿⣿⣿⠊⢵⣾⠺⢘⡻⡿⢻⣾⣗⠇⠀⢸⠃
            ⠀⠀⠈⢽⣿⣿⣽⠚⢾⣽⣿⣿⣿⣿⣿⣿⣾⣿⣟⣶⢺⢚⣿⢿⠿⠃⠀⠀⢰⡂
            ⠀⠀⠀⠈⣿⣿⣿⣾⡛⢿⣿⣿⣿⣾⣿⣿⣾⠿⡟⣻⢿⣿⣿⣿⡇⠀⠀⠀⠰⠆
            ⠀⠀⠀⠀⣿⣿⣿⣿⣞⣡⣨⡎⢩⣺⠸⡟⣂⣟⣇⣻⣾⣿⣿⣿⡇⠀⠀⠀⢸⠀
            ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣶⣭⣦⣶⣶⣴⣿⢰⣾⣾⣿⣿⣿⣿⣟⡁⠀⠀⠀⠸⠆
            ⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⡅
            ⠀⠀⠀⠀⣿⠿⢿⢿⡿⠿⠿⠿⡿⠿⡿⠿⠿⡿⠿⠿⠿⠛⠿⠿⠻⠀⠀⠀⢸⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      
            """)
            time.sleep(0.1)
            clear_screen()
        
        troll = input("")

        if troll == "":

            if life == False:
                scary()
                scary()
                scary()
                clear_screen()
                exit()
  
#EXECUTE:

if __name__ == "__main__":
    main()  

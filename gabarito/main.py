##################################################################
##                                                              ##
##      CODIGO CRIADO PELO GRUPO TURING - POLI USP 2016         ##
##      https://www.facebook.com/grupoturing.poliusp            ##
##      Todos podem usar este c�digo livremente                 ##
##                                                              ##
##################################################################

import jogo
import algoritmoGenetico as ag

def main():
    '''
    Nessa funcao voce deve vai procurar um individuo capaz de vencer o jogo,
    Para isso voc� precisa:

    1) Declarar a Geracao Zero, com 10 individuos

    2) Avaliar os individuos de cada geracao

    3) Selecionar os 3 melhores e utilizar eles para reproduzir a proxima Geracao


    Dicas: voc� ja criou diversas funcoes no outro arquivo e deve cham�-las quando achar necess�rio.
        As que voc� vai precisar usar s�o:        
            -ag.Geracoes()
            -individuo.fitness(gameState)
            -geracao.selecao(numSelec)
            -geracao.reproduzir(m, chanceCO, chanceMut)
        Alem disso, voc� pode usar a func�o:
            -gameState = jogo.jogar(individuo,numBat,multVelocidade)
                -essa fun��o utiliza o individuo para jogar uma partida de Pong,
                    al�m disso, deve-se escolher o n�mero de batidas para "ganhar" e finalizar o jogo
                    e tamb�m definir o qu�o r�pido deve estar o jogo

                -lembrando que gameState possui:    
                    #gameState[0] = player.y (normalizado de -1 a +1)
                    #gameState[1] = ball.x   (normalizado de -1 a +1)
                    #gameState[2] = ball.y   (normalizado de -1 a +1)
                    #gameState[3] = ball.speed_x
                    #gameState[4] = ball.speed_y
                    #gameState[5] = numBat (numero de vezes que a bolinha bateu no player)
                    #gameState[6] = ganhou (True/False, se o player sobreviveu o tempo definido)

    '''
                         
    
    multVel = 100
    i = 0
    #geracao0
    generation = ag.Geracao(10)
    
    cont = True    
    while cont:
        print('geracao %d'%i)
        for individuo in generation.individuos:
            gameState = jogo.jogar(individuo,40,multVel)
            individuo.fitness(gameState)

            if gameState[6] == True:
                cont = False
                print('Ganhei!')
            #print(individuo)
            #print(individuo.score)
        

        #condicao de parada
        if cont == True and i < 100:       
            generation.selecao(3)
            generation.reproduzir(10)
            i+=1
        else:
            cont = False
          
    
    generation.selecao(1)
    
    return(generation)



gen = main()

for i in range(len(gen.individuos)):
    arq = open('inds/ind{}.txt'.format(i), 'w')
    arq.write(' '.join(map(str, gen.individuos[i].pesos)))
    arq.close()


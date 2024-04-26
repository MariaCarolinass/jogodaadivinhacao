import random, time

numPCList = list(range(1, 101))

def getNumUser():
    return int(input("Tente adivinhar qual o número (de 1 - 100): "))

def getNumPc():
    time.sleep(0.5)
    numPC = random.randint(numPCList[0], numPCList[len(numPCList)-1])
    print(f"O Computador chutou o número: {numPC}")
    return numPC

def removeNumPcList(start, end):
    for num in range(start, end+1):
        numPCList.remove(num)
        
def main():
    numSecret = random.randint(1, 100)
    attempt = 0
    
    print("Bem-vindo ao jogo da adivinhação")
    print("----------------------")
        
    while attempt < 20:
        attempt += 1
        print(f"Tentativa: {attempt} de 20\n")
        
        numUser = getNumUser()
        numPC = getNumPc()
        
        if numUser == numSecret and numPC == numSecret:
            print(f"Empate! Ambos adivinharam o número secreto, com {attempt} tentativa(s)!")
            break
        elif numUser == numSecret:
            print(f"Parabéns! Você adivinhou o número secreto, com {attempt} tentativa(s)!")
            break
        elif numPC == numSecret:
            print(f"O computador adivinhou o número secreto, com {attempt} tentativa(s). Você perdeu!")
            break
        else:
            time.sleep(0.5)
            if numSecret > numUser and numSecret > numPC:
                tip = f"O número secreto é MAIOR que {numUser} e {numPC}"
                if numUser > numPC:
                    removeNumPcList(numPCList[0], numUser)
                else:
                    removeNumPcList(numPCList[0], numPC)
            elif numSecret > numUser and numSecret < numPC:
                tip = f"O número secreto é MAIOR que {numUser} e MENOR que {numPC}"
                removeNumPcList(numPCList[0], numUser)
                removeNumPcList(numPC, numPCList[len(numPCList)-1])
            elif numSecret < numUser and numSecret > numPC:
                tip = f"O número secreto é MENOR que {numUser} e MAIOR que {numPC}"
                removeNumPcList(numPCList[0], numPC)
                removeNumPcList(numUser, numPCList[len(numPCList)-1])
            else:
                tip = f"O número secreto é MENOR que {numUser} e {numPC}"
                if numPC < numUser:
                    removeNumPcList(numPC, numPCList[len(numPCList)-1])
                else:
                    removeNumPcList(numUser, numPCList[len(numPCList)-1])
            print(f"\n{tip}")
            print("----------------------")
    else:
        print(f"Fim do jogo! as tentativas acabaram, o número secreto era {numSecret}")

if __name__ == "__main__":
    main()
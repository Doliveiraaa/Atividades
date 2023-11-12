
def converterAvaliacao():
    if (avaliacao == 1):
        return "Ótimo"
    if (avaliacao == 2):
        return "Bom"
    if (avaliacao == 3):
        return "Regular"
    if (avaliacao == 4):
        return "Péssimo"


votos = 0
votootimo = 0
votobom = 0
votoregular = 0
votopessimo = 0 
maisvelho = 0
maisnovo = 0
respvelho = 0
respnovo = 0

while (True):
    idade = int(input("QUAL A SUA IDADE?"))
    avaliacao = input("QUAL SUA AVALIAÇÃO? (1-ÓTIMO, 2-BOM, 3-REGULAR, 4-PÉSSIMO): ")
        
    votos += 1
    
    if avaliacao == 1:
        votootimo += 1
    
    if avaliacao == 2:
        votobom += 1
        
    if avaliacao == 3:
        votoregular += 1
    
    if avaliacao == 4:
        votopessimo += 1
    
    if (idade > maisvelho):
        maisvelho = idade
        respvelho = avaliacao
        
    if (idade < maisnovo):
        maisnovo = idade
        

    
    continuar = int(input("DESEJA CONTINUAR? (1-SIM, 2-NÃO)"))
    if continuar == 2:
        break
    
    
print("Total de respondentes: ",votos)
print("Quantidade de respostas com avaliação Ótima: ",votootimo)
print("Quantidade de respostas com avaliação Bom: ",votobom)
print("Quantidade de respostas com avaliação Regular: ",votoregular)
print("Quantidade de respostas com avaliação Péssima: ",votopessimo)

print("O respondente mais velho tem a idade: ", maisvelho)
print("O respondente mais velho votou em:", respvelho)
print("O respondente mais novo tem a idade: ", maisnovo)
print("O respondente mais novo votou em:", respnovo)
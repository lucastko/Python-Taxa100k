#RM 93918- Henrique Incerpi
#RM 96263- Lucas Ribeiro Lourenço de Aquino
#RM 95303- Renan Souza Calejon
#RM 92848 – Samuel Santos Baggio
#RM 94327 - André Santi


dados = dict()

registro = list()


#SUBALGORITMOS-------------------------

def validaTamanhoMesAno(mes):  
    if len(mes) < 7 or len(mes) > 7:
        return False
    return True


def validaMesAno(mesAno):
    if '-' not in mesAno: 
        return False    
    return True



def cadastroMesAno(d: dict, r: list):


            while True:
                d['mes_ano_referencia'] = str(input("\nDigite o Mês-ano.....: "))
                if validaMesAno(d['mes_ano_referencia']) == False:
                    print("Mês-Ano inválido! Digite novamente.")

                elif validaTamanhoMesAno(d['mes_ano_referencia']) == False:
                    print("Mês-Ano inválido! Digite novamente.")

                else:
                    break
                
            d['total_habitantes'] = int(input("\nDigite o Total de Habitantes (APENAS NÚMEROS).....: "))

            d['Total_obitos'] = int(input("\nDigite o Total de óbitos (APENAS NÚMEROS).....: "))

            
            r.append(d.copy())

            print("-=" * 10)
            print("\nGRAVADO COM SUCESSO\n")
            print("-="*10)



def pesquisa(r:list):

    mes = input("\n Digite o mês-ano desejado: ")

    for i in range(len(r)):

        if mes == r[i]['mes_ano_referencia']:

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
            print("REGISTRO ENCONTRADO\n")

            print(f"Mês-Ano.....:", r[i]['mes_ano_referencia'])
            print(f"Total de Habitantes.....:", r[i]['total_habitantes'])
            print(f"Total de óbitos.....:", r[i]['Total_obitos'])

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" )

    if mes not in r[i]:
        print("-" * 20)
        print("\n REGISTRO NÃO ENCONTRADO \n")
        print("-" * 20)   

    elif len (r) == 0:
        print("=-" * 20)
        print("\nLISTA DE REGISTROS VAZIA\n")
        print("=-" * 20)   




def relatorio(r: list, d: dict): 

        c = str(input("\n Digite o ano desejado: "))

        habitantes = 0
        obitos = 0

        while c ==  d['mes_ano_referencia'][3:7]:

            for i in r:

                habitantes += i["total_habitantes"]
                obitos += i["Total_obitos"]

            resultado = (obitos * 100000) / habitantes

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" )
            print("RELATÓRIO\n")
            print(f"Total de Habitantes.....:{habitantes}")
            print(f"Total de óbitos.....:{obitos}" )
            print(f"Taxa por 100k habitantes - {i['mes_ano_referencia']}...: {resultado:.2f}" )
            print(f"Taxa por 100k habitantes - 2019...: 15.00" )

            if ((resultado *100) / 15) > 100:
                print(f"Comparativo porcentagem {i['mes_ano_referencia']} e 2019: +{((resultado *100 )/ 15) - 100:.2f}%")

            else:
                print(f"Comparativo de porcentagem entre {i['mes_ano_referencia']} e 2019: -{((resultado * 100) / 15) - 100:.2f}%")
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n" )
            
            break

def listar(r: list):

    for i in range(0, len(r), 1):
        print("-=" * 10)
        print(f"Ano.....:", r[i]['ano'])
        print(f"Mês-Ano.....:", r[i]['mes_ano_referencia'])
        print(f"Total de Habitantes.....:", r[i]['total_habitantes'])
        print(f"Total de óbitos.....:", r[i]['Total_obitos'])

    if len(r) == 0:
        print('\n----- LISTA DE REGISTROS VAZIA! -----\n')


#PROGRAMA PRINCIPAL--------------------------


while True: 
    print("\n----- ATLAS MOBILITY -----")

    print("1 - Cadastrar mês de referência") 

    print("\n2 – Exibir dados do mês de referência (pesquisa por mês)")

    print("\n3 - Relatório comparativo – Referência 2019")

    print("\n4 - Listar todos os meses cadastrados ")

    print("\n5 - Encerrar programa \n")

    opcao  = int(input("Digite a opção desejada -> "))


    if opcao == 1:
        cadastroMesAno(dados, registro)
    if opcao == 2:
        pesquisa(registro)
    if opcao == 3:
        relatorio(registro, dados)
    if opcao == 4:
        listar(registro)
    if opcao == 5:
        print("\nSaindo do programa...")
        break
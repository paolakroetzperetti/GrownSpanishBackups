import html
from GameDataLoader import GameDataLoader
from GameAnalyzer import GameAnalyzer

def main(filename):
    try:
        # Carregando os dados do arquivo usando o GameDataLoader
        loader = GameDataLoader(filename)
        game_data = loader.load_data()
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
        exit(1)
    except Exception as e:
        print("Erro ao carregar os dados:", e)
        exit(1)

    # Exibição das 2 primeiras linhas do arquivo para verificar se o mesmo está sendo lido corretamente.
    print("Primeiras 2 linhas do arquivo:")
    try:
        for item in game_data[:2]:
            if item:  # Verificando se a linha não está vazia
                print(item)
    except Exception as e:
        print("Erro ao exibir as linhas do arquivo:", e)
        exit(1)

    # Criando uma instância da classe GameAnalyzer
    try:
        analyzer = GameAnalyzer(game_data)
    except Exception as e:
        print("Erro ao criar a instância do GameAnalyzer:", e)
        exit(1)

    # Decodificar caracteres especiais nos resultados
    def print_decoded_results(results):
        for result in results:
            decoded_result = [html.unescape(item) for item in result]
            print(decoded_result)

    # Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
    percentual_pagos, percentual_gratuitos = analyzer.calcular_percentuais()
    percentual_pagos = round(percentual_pagos, 2)
    percentual_gratuitos = round(percentual_gratuitos, 2)

    # Pergunta 2: Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.
    anos_mais_jogos = analyzer.encontrar_anos_mais_jogos()

    # Pergunta 3: Qual é o jogo mais antigo?
    jogo_mais_antigo = analyzer.encontrar_jogo_mais_antigo()

    # Impressão dos resultados das perguntas:
    print("\nPergunta 1:")
    print("Percentual de jogos gratuitos:", f"{percentual_gratuitos:.2f}%")
    print("Percentual de jogos pagos:", f"{percentual_pagos:.2f}%")
    print()

    print("Pergunta 2:")
    if len(anos_mais_jogos) == 1:
        print("Ano com o maior número de jogos:", anos_mais_jogos[0])
    else:
        print("Ano(s) com o maior número de jogos:", ", ".join(anos_mais_jogos))
    print()

    print("Pergunta 3:")
    if jogo_mais_antigo is not None:
        print("Jogo mais antigo:")
        print(jogo_mais_antigo)
    else:
        print("Não foi possível encontrar o jogo mais antigo.")

# Executar para o arquivo completo
main("/content/steam_games.csv")

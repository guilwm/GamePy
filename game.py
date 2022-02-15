from models.calcular import Calcular

def main() -> None:
    pontos: int =0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade = int(input('Informe o nível da dificuldade desejada (1, 2, 3 ou 4)'))

    calc = Calcular(dificuldade=dificuldade)

    print('Informe o resultado para a seguinte operação:\n')
    calc.mostrar_operacao()

    resultado = int(input())

    if calc.checar_resultado(resultado) == 1:
        pontos +=1
        print(f'Você tem {pontos} ponto(s)!')

    continuar = int(input('Deseja continuar no jogo? 1 -> sim, 0 -> não'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s)!\n'
              f'Até a proxima!')

if __name__ == '__main__':
    main()


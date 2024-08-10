from modulos.inputs import leiaInt
from modulos.estilo import estilo
from modulos.texto import linha, titulo, erro
from time import sleep

try:
    while True:
        # Criando menu principal
        estilo(cor='ciano')
        titulo('MENU PRINCIPAL')
        print('''        \033[33m1 - \033[34mVer pessoas cadastradas
        \033[33m2 - \033[34mCadastrar nova pessoa
        \033[33m3 - \033[34mSair do sistema\033[m''')
        linha()
        # Solicitando e verificando opção
        while True:
            sleep(0.5)
            opc = leiaInt('Sua opção: ')
            if 1 <= opc <= 3:
                break
            else:
                erro('ERRO: opção inválida! Tente novamente.')
        # Exibindo pessoas cadastradas
        if opc == 1:
            estilo(cor='cinza')
            titulo('PESSOAS CADASTRADAS')
            sleep(1)
            try:
                with open('registro.txt', 'r', encoding='utf-8') as arquivo:
                    registro = arquivo.readlines()
                    if len(registro) == 0:
                        erro('ERRO: ainda não há pessoas cadastradas!')
                    else:
                        for c in range(0, len(registro), 2):
                            registro[c] = registro[c].replace('\n', '')
                            registro[c + 1] = registro[c + 1].replace('\n', '')
                            print(f'{registro[c]:<35}{registro[c + 1]:<3} anos')
            # Criando registro.txt caso ele não exista
            except FileNotFoundError:
                erro('O arquivo registro.txt não existe!')
                sleep(0.5)
                estilo(cor='verde')
                print('criando arquivo registro.txt')
                sleep(0.5)
                try:
                    with open('registro.txt', 'w'):
                        print('Arquivo criado!')
                except Exception:
                    erro('Houve um erro ao criar o arquivo!')
                estilo()
            sleep(1)

        # Cadastrando uma nova pessoa
        elif opc == 2:
            estilo(cor='amarelo')
            titulo('NOVO CADASTRO')
            sleep(1)
            # validando dado "nome"
            while True:
                estilo(cor='amarelo')
                nome = str(input('Nome: ')).strip()
                if nome == '':
                    erro('ERRO: insira um nome válido!')
                    sleep(0.5)
                else:
                    break
            idade = leiaInt('Idade: ')
            # Abrindo arquivo e registrando pessoa
            with open('registro.txt', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f'{nome}\n{str(idade)}\n')
            estilo(cor='verde')
            print(f'Novo registro {nome} adicionado com sucesso!')
            sleep(1)

        # Saindo do programa
        else:
            estilo(cor='vermelho')
            titulo('FECHANDO O SISTEMA')
            sleep(2)
            break

except KeyboardInterrupt:
    erro('ERRO: o usuário interrompeu o programa!')
except Exception as error:
    erro(f'ERRO DESCONHECIDO! Erro: {error}')
finally:
    estilo(cor='verde')
    print('VOLTE SEMPRE!')
    estilo()

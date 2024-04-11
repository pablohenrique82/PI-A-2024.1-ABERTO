while(True):
    busca = input("Digite aqui sua disciplina de busca no wiki, Sistemas Operacionais ou Arquitetura e organizaçao de Computadores: ")
    if busca == 'Sistemas Operacionais': # SISTEMA OPERACIONAL
        print("O sistema operacional introduz uma camada de abstração entre o hardware e o usuário, que transforma comandos no mouse, teclado e solicitações do sistema, como gerenciamento de recursos (CPU, memória RAM), em linguagem de máquina, enviando instruções ao processador.")
    elif busca == 'Arquitetura e Organizaçao de Computadores':
        print("A organização e arquitetura de computador fornece conhecimento profundo do trabalho interno. E também a estruturação e implementação de um sistema de computador. Visto que Organização define a maneira como o sistema é estruturado, de modo que todas as ferramentas catalogadas possam ser usadas adequadamente")
    else:
        print("Disciplina não encontrada!")

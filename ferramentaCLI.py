import sys
import re

def extrair_participantes(arquivo_transcricao):
    """Extrai participantes a partir da transcrição, considerando timestamps."""
    participantes = set()
    with open(arquivo_transcricao, 'r', encoding='utf-8') as f:
        for linha in f:
           match = re.match (r'^ \[\d{2}:\d{2}\] \s(.*?):', linha) 
        

        if match:
            participantes.add(match.group(1).strip())

    return sorted(participantes)

def salvar_lista(arquivo_saida, participantes):
    """Salva lista de participantes em um arquivo."""
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        for participante in participantes:
            f.write(participante + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python ferramentaCLI.py <arquivo-transcricao> <arquivo-saída>")
        sys.exit(1)

    arquivo_transcricao = sys.argv[1]
    arquivo_saida = sys.argv[2]

    participantes = extrair_participantes(arquivo_transcricao)
    salvar_lista(arquivo_saida, participantes)

    print(f"Lista de participantes salva em {arquivo_saida}")

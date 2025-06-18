def limpar_links(nome_arquivo):
    """
    Remove linhas em branco extras e links duplicados de um arquivo de texto.

    Args:
        nome_arquivo (str): O caminho para o arquivo de texto a ser processado.
    """
    try:
        # Abrir o arquivo original para leitura
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        # Usar um conjunto para armazenar links únicos e preservar a ordem de inserção (a partir do Python 3.7+)
        # Ou uma lista e verificar 'if link not in lista' para versões anteriores
        links_unicos_ordenados = []
        links_ja_vistos = set() # Usamos um set para verificação rápida de duplicatas

        # Processar cada linha do arquivo
        for linha in linhas:
            linha_limpa = linha.strip() # Remove espaços em branco do início e fim da linha

            # Verificar se a linha não está vazia após a limpeza
            # e se é um link (vamos assumir que links começam com "http" ou "https")
            if linha_limpa and (linha_limpa.startswith("http://") or linha_limpa.startswith("https://")):
                # Se o link ainda não foi visto, adicioná-lo à lista e ao conjunto
                if linha_limpa not in links_ja_vistos:
                    links_unicos_ordenados.append(linha_limpa)
                    links_ja_vistos.add(linha_limpa)

        # Preparar o conteúdo para escrita, adicionando uma quebra de linha após cada link
        conteudo_para_escrever = "\n".join(links_unicos_ordenados)

        # Sobrescrever o arquivo original com os links limpos e únicos
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo_para_escrever)

        print(f"O arquivo '{nome_arquivo}' foi limpo com sucesso!")
        print(f"{len(links_unicos_ordenados)} links únicos foram salvos.")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Como usar o script ---
if __name__ == "__main__":
    # Substitua 'links ted binho.txt' pelo nome do seu arquivo, se for diferente
    nome_do_seu_arquivo = 'links ted binho.txt'
    limpar_links(nome_do_seu_arquivo)


import os # Importa o módulo 'os' para lidar com caminhos de arquivo e diretórios

def limpar_links(caminho_completo_arquivo):
    """
    Remove linhas em branco extras e links duplicados de um arquivo de texto.

    Args:
        caminho_completo_arquivo (str): O caminho completo para o arquivo de texto a ser processado,
                                       incluindo o nome do arquivo e sua extensão.
                                       Exemplo: 'C:/Users/  /Documentos/meus_links.txt'
                                       ou 'links/links_uteis.txt'
    """
    try:
        # 1. Abrir o arquivo original para leitura ('r' - read)
        # 'encoding='utf-8'' é importante para lidar com caracteres especiais corretamente.
        with open(caminho_completo_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines() # Lê todas as linhas do arquivo e as armazena em uma lista.
                                   # Cada elemento da lista 'linhas' será uma linha do arquivo,
                                   # incluindo a quebra de linha (\n) no final.

        # 2. Inicializar estruturas para armazenar links únicos e controlar duplicatas
        links_unicos_ordenados = [] # Esta lista manterá os links na ordem em que são encontrados pela primeira vez.
                                    # É importante para preservar a ordem original dos links únicos.
        links_ja_vistos = set()     # Este é um 'set' (conjunto). Conjuntos são otimizados para
                                    # verificar rapidamente se um item já está presente (muito mais rápido que listas).
                                    # Usaremos isso para detectar links duplicados de forma eficiente.

        # 3. Processar cada linha do arquivo
        for linha in linhas:
            # 3.1. Remover espaços em branco do início e fim da linha
            # O método .strip() remove espaços, tabulações, quebras de linha (\n, \r) do começo e fim.
            linha_limpa = linha.strip()

            # 3.2. Verificar se a linha não está vazia após a limpeza E se parece ser um link
            # Assumimos que um link válido começa com "http://" ou "https://".
            # Você pode ajustar essa condição se seus links tiverem outros padrões (ex: ftp://).
            if linha_limpa and (linha_limpa.startswith("http://") or linha_limpa.startswith("https://")):
                # 3.3. Verificar se o link já foi visto
                # Se 'linha_limpa' NÃO estiver no conjunto 'links_ja_vistos', significa que é um link novo.
                if linha_limpa not in links_ja_vistos:
                    # 3.4. Adicionar o link à lista de links únicos (para manter a ordem)
                    links_unicos_ordenados.append(linha_limpa)
                    # 3.5. Adicionar o link ao conjunto de links já vistos (para controle de duplicatas)
                    links_ja_vistos.add(linha_limpa)

        # 4. Preparar o conteúdo para escrita
        # O método .join() une os elementos da lista 'links_unicos_ordenados' em uma única string,
        # usando "\n" (quebra de linha) como separador entre eles.
        conteudo_para_escrever = "\n".join(links_unicos_ordenados)

        # 5. Sobrescrever o arquivo original com os links limpos e únicos
        # Abrimos o arquivo novamente, mas agora no modo de escrita ('w' - write).
        # O modo 'w' irá apagar todo o conteúdo existente do arquivo e escrever o novo conteúdo.
        with open(caminho_completo_arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo_para_escrever) # Escreve a string de links limpos no arquivo.

        # 6. Mensagens de sucesso para o usuário
        print(f"✅ O arquivo '{caminho_completo_arquivo}' foi limpo com sucesso!")
        print(f"📊 {len(links_unicos_ordenados)} links únicos foram salvos.")

    except FileNotFoundError:
        # Captura o erro se o arquivo especificado não for encontrado no caminho fornecido.
        print(f"❌ Erro: O arquivo '{caminho_completo_arquivo}' não foi encontrado.")
        print("Certifique-se de que o caminho e o nome do arquivo estão corretos.")
    except Exception as e:
        # Captura qualquer outro erro inesperado que possa ocorrer durante o processo.
        print(f"💥 Ocorreu um erro inesperado: {e}")
        print("Por favor, verifique o arquivo e tente novamente.")

# --- Bloco Principal de Execução ---
# Este bloco de código só será executado quando o script for rodado diretamente.
# Não será executado se o script for importado como um módulo em outro programa.
if __name__ == "__main__":
    # --- CONFIGURAÇÃO DO ARQUIVO ---
    # Defina o nome do seu arquivo de texto aqui.
    nome_do_arquivo = 'links.txt'

    # Defina o caminho completo para a pasta onde o arquivo está localizado.
    # Exemplos:
    # 1. Se o arquivo estiver na MESMA pasta que este script:
    caminho_do_diretorio = '' # Deixe vazio se estiver na mesma pasta

    # 2. Se o arquivo estiver em uma pasta específica (Windows):
    # caminho_do_diretorio = 'C:/Users/    /Documentos/' # Use barras normais (/) ou barras duplas (\\)

    # 3. Se o arquivo estiver em uma pasta específica (Linux/macOS):
    # caminho_do_diretorio = '/home/    /Desktop/meus_arquivos/'

    # 4. Se o arquivo estiver em um subdiretório (ex: 'data' dentro da pasta do script):
    # caminho_do_diretorio = 'data/'

    # --------------------------------

    # Combina o caminho do diretório com o nome do arquivo para obter o caminho completo.
    # os.path.join é recomendado pois lida com barras de diretório corretamente em diferentes sistemas operacionais.
    caminho_completo_do_arquivo = os.path.join(caminho_do_diretorio, nome_do_arquivo)

    # Chama a função principal para limpar os links, passando o caminho completo do arquivo.
    limpar_links(caminho_completo_do_arquivo)


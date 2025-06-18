import os # Importa o módulo 'os' para lidar com caminhos de arquivo e diretórios

def limpar_e_salvar_links(caminho_completo_arquivo_entrada, caminho_completo_arquivo_saida):
    """
    Remove linhas em branco extras e links duplicados de um arquivo de texto,
    e salva o resultado em um NOVO arquivo.

    Args:
        caminho_completo_arquivo_entrada (str): O caminho COMPLETO para o arquivo de texto de ENTRADA
                                                 a ser processado (o arquivo original).
        caminho_completo_arquivo_saida (str): O caminho COMPLETO para o arquivo de SAÍDA onde os links limpos
                                              serão salvos.
    """
    try:
        # 1. Verificar se o arquivo de entrada existe antes de tentar abri-lo
        # os.path.exists() verifica se o caminho fornecido existe no sistema de arquivos.
        if not os.path.exists(caminho_completo_arquivo_entrada):
            # Se o arquivo não existir, levanta um erro FileNotFoundError com uma mensagem útil.
            raise FileNotFoundError(f"O arquivo de entrada '{caminho_completo_arquivo_entrada}' não foi encontrado.")

        # 2. Abrir o arquivo original para leitura ('r' - read)
        # Usa o 'caminho_completo_arquivo_entrada' que foi passado para a função.
        # 'encoding='utf-8'' é importante para lidar com caracteres especiais corretamente.
        with open(caminho_completo_arquivo_entrada, 'r', encoding='utf-8') as f:
            linhas = f.readlines() # Lê todas as linhas do arquivo e as armazena em uma lista.
                                   # Cada elemento da lista 'linhas' será uma linha do arquivo,
                                   # incluindo a quebra de linha (\n) no final.

        # 3. Inicializar estruturas para armazenar links únicos e controlar duplicatas
        links_unicos_ordenados = [] # Esta lista manterá os links na ordem em que são encontrados pela primeira vez.
                                    # É importante para preservar a ordem original dos links únicos.
        links_ja_vistos = set()     # Este é um 'set' (conjunto). Conjuntos são otimizados para
                                    # verificar rapidamente se um item já está presente (muito mais rápido que listas).
                                    # Usaremos isso para detectar links duplicados de forma eficiente.

        # 4. Processar cada linha do arquivo
        for linha in linhas:
            # 4.1. Remover espaços em branco do início e fim da linha
            # O método .strip() remove espaços, tabulações, quebras de linha (\n, \r) do começo e fim.
            linha_limpa = linha.strip()

            # 4.2. Verificar se a linha não está vazia após a limpeza E se parece ser um link
            # Assumimos que um link válido começa com "http://" ou "https://".
            # Você pode ajustar essa condição se seus links tiverem outros padrões (ex: ftp://).
            if linha_limpa and (linha_limpa.startswith("http://") or linha_limpa.startswith("https://")):
                # 4.3. Verificar se o link já foi visto
                # Se 'linha_limpa' NÃO estiver no conjunto 'links_ja_vistos', significa que é um link novo.
                if linha_limpa not in links_ja_vistos:
                    # 4.4. Adicionar o link à lista de links únicos (para manter a ordem)
                    links_unicos_ordenados.append(linha_limpa)
                    # 4.5. Adicionar o link ao conjunto de links já vistos (para controle de duplicatas)
                    links_ja_vistos.add(linha_limpa)

        # 5. Preparar o conteúdo para escrita
        # O método .join() une os elementos da lista 'links_unicos_ordenados' em uma única string,
        # usando "\n" (quebra de linha) como separador entre eles.
        conteudo_para_escrever = "\n".join(links_unicos_ordenados)

        # 6. Criar e escrever no NOVO arquivo de saída
        # Abre um NOVO arquivo no modo de escrita ('w' - write), usando o caminho completo fornecido pelo usuário.
        # Se o arquivo não existir, ele será criado. Se existir, seu conteúdo será sobrescrito.
        with open(caminho_completo_arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(conteudo_para_escrever) # Escreve a string de links limpos no novo arquivo.

        # 7. Mensagens de sucesso para o usuário
        print(f"\n✅ Processamento concluído com sucesso!")
        print(f"📦 Arquivo original de entrada: '{caminho_completo_arquivo_entrada}' (não modificado)")
        print(f"📄 Novo arquivo de saída gerado: '{caminho_completo_arquivo_saida}'")
        print(f"📊 {len(links_unicos_ordenados)} links únicos foram salvos no novo arquivo.")

    except FileNotFoundError as e:
        # Captura o erro se o arquivo de entrada não for encontrado.
        print(f"\n❌ Erro: {e}")
        print("Por favor, verifique se o caminho completo e o nome do arquivo de entrada estão corretos.")
    except Exception as e:
        # Captura qualquer outro erro inesperado que possa ocorrer durante o processo.
        print(f"\n💥 Ocorreu um erro inesperado: {e}")
        print("Por favor, verifique os caminhos e tente novamente.")

# --- Bloco Principal de Execução ---
# Este bloco de código só será executado quando o script for rodado diretamente.
if __name__ == "__main__":
    print("--- Ferramenta de Limpeza de Links ---")
    print("Por favor, insira os caminhos solicitados.")
    print("Dica: No Windows, você pode copiar o caminho de uma pasta na barra de endereços do Explorador de Arquivos.")
    print("Lembre-se de incluir o nome do arquivo e sua extensão no caminho (ex: C:/pasta/arquivo.txt).\n")

    # Loop para solicitar o caminho do arquivo de entrada até que seja válido
    while True:
        caminho_entrada = input("➡️ Digite o CAMINHO COMPLETO do arquivo de ENTRADA (com nome do arquivo): ")
        # O replace faz com que barras invertidas sejam convertidas para barras normais
        # para compatibilidade em todos os sistemas operacionais.
        caminho_entrada = caminho_entrada.replace('\\', '/')
        if os.path.isfile(caminho_entrada): # os.path.isfile() verifica se o caminho leva a um arquivo existente
            break # Sai do loop se o caminho for um arquivo válido
        else:
            print("🚫 Caminho do arquivo de entrada inválido ou arquivo não encontrado. Por favor, tente novamente.")

    # Loop para solicitar o caminho do arquivo de saída até que seja válido (ou um diretório válido)
    while True:
        caminho_saida = input("➡️ Digite o CAMINHO COMPLETO para o NOVO arquivo de SAÍDA (com nome do arquivo, ex: C:/pasta/saida.txt): ")
        caminho_saida = caminho_saida.replace('\\', '/')
        # Separa o diretório e o nome do arquivo de saída para verificar se o diretório existe.
        diretorio_saida = os.path.dirname(caminho_saida)
        if not diretorio_saida: # Se não houver diretório (apenas nome de arquivo), assume o diretório atual
            diretorio_saida = '.' # Representa o diretório atual
        
        if os.path.isdir(diretorio_saida): # os.path.isdir() verifica se o caminho leva a um diretório existente
            # Verifica se o nome do arquivo de saída é válido (não é um diretório, etc.)
            if os.path.basename(caminho_saida): # Verifica se o nome do arquivo não está vazio
                break # Sai do loop se o diretório for válido e o nome do arquivo existir
            else:
                print("🚫 Nome do arquivo de saída inválido. Certifique-se de incluir o nome do arquivo (ex: saida.txt).")
        else:
            print("🚫 O diretório para o arquivo de saída não existe. Por favor, crie-o ou forneça um caminho válido.")
            print(f"Diretório tentado: '{diretorio_saida}'")


    # Chama a função principal com os caminhos fornecidos pelo usuário.
    limpar_e_salvar_links(caminho_entrada, caminho_saida)




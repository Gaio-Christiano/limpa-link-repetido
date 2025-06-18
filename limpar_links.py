import os # Importa o módulo 'os' para lidar com caminhos de arquivo e diretórios

def limpar_e_salvar_links(caminho_completo_arquivo_entrada, nome_arquivo_saida_opcional=None):
    """
    Remove linhas em branco extras e links duplicados de um arquivo de texto,
    e salva o resultado em um NOVO arquivo.

    Args:
        caminho_completo_arquivo_entrada (str): O caminho completo para o arquivo de texto de ENTRADA
                                                 a ser processado (o arquivo original).
                                                 Exemplo: 'C:/Users/    /Documentos/meus_links.txt'
                                                 ou 'links/links_uteis.txt'
        nome_arquivo_saida_opcional (str, optional): Opcional. O nome do arquivo de SAÍDA onde os links limpos
                                                     serão salvos. Se não for fornecido, um nome padrão
                                                     será gerado (ex: 'links_limpo.txt').
    """
    try:
        # 1. Verificar se o arquivo de entrada existe antes de tentar abri-lo
        if not os.path.exists(caminho_completo_arquivo_entrada):
            raise FileNotFoundError(f"O arquivo de entrada '{caminho_completo_arquivo_entrada}' não foi encontrado.")

        # 2. Abrir o arquivo original para leitura ('r' - read)
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

        # 5. Gerar o nome do arquivo de saída
        # Obtém o diretório do arquivo de entrada e o nome base do arquivo (sem extensão).
        diretorio_entrada, nome_base_arquivo_entrada = os.path.split(caminho_completo_arquivo_entrada)
        nome_arquivo_sem_extensao, extensao_arquivo = os.path.splitext(nome_base_arquivo_entrada)

        # Se um nome de arquivo de saída opcional foi fornecido, use-o.
        if nome_arquivo_saida_opcional:
            nome_arquivo_saida = nome_arquivo_saida_opcional
        else:
            # Caso contrário, gera um nome padrão: "nome_original_limpo.txt"
            nome_arquivo_saida = f"{nome_arquivo_sem_extensao}_limpo{extensao_arquivo}"

        # Combina o diretório de entrada com o nome do arquivo de saída para obter o caminho completo do arquivo de saída.
        caminho_completo_arquivo_saida = os.path.join(diretorio_entrada, nome_arquivo_saida)

        # 6. Preparar o conteúdo para escrita
        # O método .join() une os elementos da lista 'links_unicos_ordenados' em uma única string,
        # usando "\n" (quebra de linha) como separador entre eles.
        conteudo_para_escrever = "\n".join(links_unicos_ordenados)

        # 7. Criar e escrever no NOVO arquivo de saída
        # Abrimos um NOVO arquivo no modo de escrita ('w' - write).
        # Se o arquivo não existir, ele será criado. Se existir, seu conteúdo será sobrescrito.
        with open(caminho_completo_arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(conteudo_para_escrever) # Escreve a string de links limpos no novo arquivo.

        # 8. Mensagens de sucesso para o usuário
        print(f"✅ Processamento concluído com sucesso!")
        print(f"📦 Arquivo original de entrada: '{caminho_completo_arquivo_entrada}' (não modificado)")
        print(f"📄 Novo arquivo de saída gerado: '{caminho_completo_arquivo_saida}'")
        print(f"📊 {len(links_unicos_ordenados)} links únicos foram salvos no novo arquivo.")

    except FileNotFoundError as e:
        # Captura o erro se o arquivo de entrada não for encontrado.
        print(f"❌ Erro: {e}")
        print("Certifique-se de que o caminho e o nome do arquivo de entrada estão corretos.")
    except Exception as e:
        # Captura qualquer outro erro inesperado que possa ocorrer durante o processo.
        print(f"💥 Ocorreu um erro inesperado: {e}")
        print("Por favor, verifique o arquivo e tente novamente.")

# --- Bloco Principal de Execução ---
# Este bloco de código só será executado quando o script for rodado diretamente.
# Não será executado se o script for importado como um módulo em outro programa.
if __name__ == "__main__":
    # --- CONFIGURAÇÃO DO ARQUIVO DE ENTRADA ---
    # Defina o nome do seu arquivo de texto original aqui.
    nome_do_arquivo_entrada = 'links.txt'

    # Defina o caminho completo para a pasta onde o arquivo de ENTRADA está localizado.
    # Exemplos:
    # 1. Se o arquivo estiver na MESMA pasta que este script:
    caminho_do_diretorio_entrada = '' # Deixe vazio se estiver na mesma pasta

    # 2. Se o arquivo estiver em uma pasta específica (Windows):
    # caminho_do_diretorio_entrada = 'C:/Users/      /Documentos/MeusLinks/' # Use barras normais (/) ou barras duplas (\\)

    # 3. Se o arquivo estiver em uma pasta específica (Linux/macOS):
    # caminho_do_diretorio_entrada = '/home/      /Desktop/MeusLinks/'

    # 4. Se o arquivo estiver em um subdiretório (ex: 'data' dentro da pasta do script):
    # caminho_do_diretorio_entrada = 'data/'

    # ----------------------------------------

    # --- CONFIGURAÇÃO DO ARQUIVO DE SAÍDA (OPCIONAL) ---
    # Você pode definir um nome específico para o NOVO arquivo que será gerado.
    # Se você deixar 'None', o script gerará um nome padrão (ex: 'links ted binho_limpo.txt').
    nome_do_arquivo_saida = None
    # Exemplo de nome de saída personalizado:
    # nome_do_arquivo_saida = 'meus_links_final.txt'

    # --------------------------------------------------

    # Combina o caminho do diretório com o nome do arquivo de entrada para obter o caminho completo.
    # os.path.join é recomendado pois lida com barras de diretório corretamente em diferentes sistemas operacionais.
    caminho_completo_do_arquivo_entrada = os.path.join(caminho_do_diretorio_entrada, nome_do_arquivo_entrada)

    # Chama a função principal para limpar e salvar os links, passando o caminho do arquivo de entrada
    # e, opcionalmente, o nome do arquivo de saída desejado.
    limpar_e_salvar_links(caminho_completo_do_arquivo_entrada, nome_do_arquivo_saida)


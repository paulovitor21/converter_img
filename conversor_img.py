from PIL import Image
import os

def converter_e_renomear(imagem, pasta_destino, contador):
    try:
        # Abre a imagem
        img = Image.open(imagem)

        # Verifica a extensão do arquivo de imagem
        base, ext = os.path.splitext(imagem)

        # Garante que a extensão seja .jpg
        if ext.lower() not in ('.jpg', '.jpeg'):
            base = f'img{contador:02d}'  # Renomeia para img01, img02, etc.
            img = img.convert('RGB')
            img.save(os.path.join(pasta_destino, f'{base}.jpg'))
            print(f'Conversão bem-sucedida: {imagem} -> {base}.jpg')
        else:
            print(f'A imagem já está em formato JPEG: {imagem}')

    except Exception as e:
        print(f"Ocorreu um erro ao converter {imagem}: {str(e)}")

if __name__ == "__main__":
    pasta_origem = 'origem'
    pasta_destino = 'destino'

    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    contador = 1  # Inicializa o contador
    for arquivo in os.listdir(pasta_origem):
        imagem_path = os.path.join(pasta_origem, arquivo)
        if os.path.isfile(imagem_path):
            converter_e_renomear(imagem_path, pasta_destino, contador)
            contador += 1  # Incrementa o contador

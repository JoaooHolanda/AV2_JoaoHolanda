import cv2
import numpy as np

# Coloque o nome da Imagem que deve estar na pasta!
imagem = cv2.imread('q3_imagem.jpeg')

# Verifique se a imagem foi carregada com sucesso
if imagem is None:
    print('Erro: Não foi possível carregar a imagem.')
else:
    # Obtém a altura e largura original da imagem
    altura, largura = imagem.shape[:2]

    # Calcula a nova altura e largura, reduzindo em 50%
    nova_altura = int(altura * 0.5)
    nova_largura = int(largura * 0.5)

    # Redimensiona a imagem para a nova altura e largura
    imagem_redimensionada = cv2.resize(imagem, (nova_largura, nova_altura))
    # Aumente o valor de brilho (por exemplo, adicione 50 a todos os canais de cor)
    brilho = 20
    imagem_brilhante = np.clip(imagem_redimensionada + brilho, 0, 255)

    # Exibe a imagem com aumento de brilho
    cv2.imshow('Imagem Original', imagem_redimensionada)
    cv2.imshow('Imagem com Aumento de Brilho', imagem_brilhante)

    # Espere por uma tecla e feche as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

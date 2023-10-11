from PIL import Image
import numpy as np

image_path = './q3_JoãoHolanda/q3_Imagem.jpeg'
img = Image.open(image_path)

width, height = img.size

im_info = lambda width, height: [[img.getpixel((x, y)) for y in range(height)] for x in range(width)]

# Função para aumentar o brilho dos canais RGB
increase_brightness = lambda pixel, value: tuple(min(255, component + value) for component in pixel)

modified_img_info = lambda funct, iminf: [[increase_brightness(iminf[x][y], funct) for y in range(len(iminf[x]))] for x in range(len(iminf))]

# Aumentar o brilho da imagem adicionando 50 a cada canal RGB
m = modified_img_info(50, im_info(width, height))

# Converter a matriz de imagem modificada em um array NumPy
modified_array = np.array(m, dtype=np.uint8)

# Criar uma nova imagem a partir do array NumPy
new_image = Image.fromarray(modified_array)

# Exibir a nova imagem
new_image.show()

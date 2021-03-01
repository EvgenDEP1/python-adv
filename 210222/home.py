from PIL import Image
import numpy as np

image_name = 'intro.jpg'
image = Image.open(image_name)
image_np = np.array(image)
image_np_conv = image_np + 30
new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'intro_conv.jpg'
new_image.save(save_name)

import imageio
from PIL import Image
import tempfile
import os


filenames = ["left.png", "right.jpeg"]
images = []
for fnm in filenames:
    img = Image.open(fnm)
    img = img.resize((500, 500))  
    
    temp_file_path = tempfile.mktemp(suffix='.png')
    img.save(temp_file_path)
    
    images.append(imageio.imread(temp_file_path))

    os.remove(temp_file_path)

imageio.mimsave('sign.gif', images, 'GIF', duration=1)

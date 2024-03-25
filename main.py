import easygui
from rembg import remove
from PIL import Image

input_path = easygui.fileopenbox(title='Select Image File')
output_path = easygui.filesavebox(title='Save file to..')


img = Image.open(input_path)

R = remove(img)
R.save(output_path)

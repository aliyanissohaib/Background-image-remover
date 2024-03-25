# import easygui
# from rembg import remove
# from PIL import Image
#
# input_path = easygui.fileopenbox(title='Select Image File')
# output_path = easygui.filesavebox(title='Save file to..')
# image_input= Image.open(input_path)
# output = remove(input_path)
# output.save(output_path)
from rembg import remove


from PIL import Image

img = Image.open("D:\\python\\bgremover\\input\\a.jpg")

R = remove(img)
R.save("a1.png")

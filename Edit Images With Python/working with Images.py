# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
https://pythonexamples.org/python-pillow-resize-image/
"""
# Python Imaging Library (PIL)

# from PIL import Image , ImageEnhance ,ImageFilter

# img1 = Image.open("Cycle.jpg")
# img1.show()

# img1.save("Cycle.png")
# img1.save("Cycle.jpeg")
# img1.save("Cycle.pdf")

# img2 = Image.open("Banch.jpg")
# Max_Size = (720,720)
# img2.thumbnail(Max_Size)
# img2.save("smallbanch.jpg")

# Multiple Image convert together

# import os
# for item in os.listdir():
#     if item.endswith(".jpg"):
#         img3 = Image.open(item)
#         filename ,extension = os.path.splitext(item)
#         img3.save(f"{filename}.png") 


# ------------------- Sharpness ---------------------

img1 = Image.open("zoltan-tasi.jpg")
enhencher = ImageEnhance.Sharpness(img1)
# enhencher.enhance(0).save("Zoltan_blured.jpg")   # blurry
# enhencher.enhance(1).save("zoltan_orginal.jpg")   # orginal
enhencher.enhance(8).save("zoltansharped.jpg")



# ------------------- color -------------------------




imge = Image.open("Cycle.jpg")
enhencher = ImageEnhance.Color(imge)
# enhencher.enhance(0).save("Cycle_BW.jpg")  
enhencher.enhance(3).save("Cycle_OverColour.jpg")  





# ------------------- brightness ----------------------





imge1 = Image.open("Hair.jpg")
enhencher = ImageEnhance.Brightness(imge1)
enhencher.enhance(0).save("HairBlack.jpg")  
enhencher.enhance(3).save("HairBright.jpg")  



im = Image.open("sample-image.png")
#image brightness enhancer
enhancer = ImageEnhance.Brightness(im)

# gives original image
enhancer.enhance(1).show()

#darkens the image
enhancer.enhance(0.5).show()

#increased brightens 
enhancer.enhance(2).show()






# -------------- Contrast ------------------------------

# imge2 = Image.open("robert_bike.jpg")
# enhencher = ImageEnhance.Contrast(imge2)
# enhencher.enhance(0).save("robert_bike_0contrast.jpg")  
# enhencher.enhance(3).save("robert_bike_Contrast.jpg")  


# im = Image.open("sample-image.png")
# #image contrast enhancer
# enhancer = ImageEnhance.Contrast(im)

# # gives original image
# enhancer.enhance(1).show()

# #decrease constrast
# enhancer.enhance(0.5).show()

# #increased contrast
# enhancer.enhance(2).show()






# imge2.filter(ImageFilter.GaussianBlur()).show() #By default 2
# imge2.filter(ImageFilter.GaussianBlur(radius=4)).show()



# image =Image.open("robert_bike.jpg")
# enhancer2 = ImageEnhance.Sharpness(image)

# for i in range(8):
#     factor = i / 4.0
#     enhancer2.enhance(factor).show("Sharpness %f" % factor)






# ------------------- Rotate an Image-------------------

# image.rotate(45).show()
# image.rotate(45,expand=True).show()  #Adjusting

# image.rotate(90).show()
# image.rotate(90,expand=True).show()
# image.rotate(180).show()





# image.filter(ImageFilter.MinFilter).show()
# image.filter(ImageFilter.MinFilter(5)).show()




# im = Image.open("robert_bike.jpg")
# # ------------------ Getting image size -------------------------
# print(im.size)


# width = im.size[0]
# height = im.size[1]

# print('Width  of the image is:', width)
# print('Height of the image is:', height)


# size=(200,200)
# #resize image
# im.resize(size).show()
# #save resized image
# #out.save('resize-output_robert.png')
 



# size = (200,200)
# box = (100,100,500,400)
# #resize image
# im.resize(size, box=box).show()

# import PIL
# # Flip an Image
# im.transpose(PIL.Image.FLIP_LEFT_RIGHT).show()
# im.transpose(PIL.Image.FLIP_TOP_BOTTOM).show()
# im.transpose(PIL.Image.FLOYDSTEINBERG).show()










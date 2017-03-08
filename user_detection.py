#
# from PIL import Image
# import pytesseract
#
# result = pytesseract.image_to_string(Image.open('user.png'), lang='Eng')
#
# print(result)

# from tesserocr import PyTessBaseAPI
#
# images = ['sample.jpg', 'sample2.jpg', 'sample3.jpg']
#
# with PyTessBaseAPI() as api:
#     for img in images:
#         api.SetImageFile(img)
#         print api.GetUTF8Text()
#         print api.AllWordConfidences()
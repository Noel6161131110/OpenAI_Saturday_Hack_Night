import ocrspace
api = ocrspace.API()

def convertImage(image1):
  text = api.ocr_file(image1)
  return text
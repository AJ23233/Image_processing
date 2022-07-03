# Filename: image_processing.py
# Description: This file contains all the operations which needs to be perform on the image
# Author: Ajay Vanara

import os
from PIL import Image

from config import CONF
import zipfile

class ImageProcessing():
	
	def __init__(self):
		
		self.images = os.path.join(os.path.dirname
                    (os.path.dirname(os.path.abspath(__file__))),
                    CONF['directory']['templates'])

	def compression(self, data):
		try:
			if not os.path.exists(self.images):
				os.mkdir(self.images)
			for uploaded_img in data :
				img = Image.open(uploaded_img)
				img = img.resize((img.width,img.height), Image.ANTIALIAS)
				img.save(os.path.join(self.images, uploaded_img.filename.split("/")[-1]))
		except Exception as ex:
			print("Error while compressing the image is :" + str(ex))
		return self.images

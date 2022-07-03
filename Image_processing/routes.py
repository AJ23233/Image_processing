# Filename: routes.py
# Description: This file contains all the routes which are part of image processing project
# Author: Ajay Vanara

from flask import Flask, jsonify, render_template, url_for, request
from flaskwebgui import FlaskUI

from operations.image_processing import ImageProcessing

app = Flask(__name__)

ui = FlaskUI(app, idle_interval=20, port=5000)

@app.route("/")
def home():
  """
  This method defines the Landing/Home page of the application 
  """
  return render_template("image_process.html")

@app.route("/compress_image", methods=['POST'])
def image_compression():
  """
  This method compresses the image uploaded from the UI
  """
  data = [i for i in request.files.listvalues()][0]
  obj = ImageProcessing()
  obj.compression(data)

  return "<h2>Compression done</h2>"

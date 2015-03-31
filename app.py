#!/usr/bin/python3
# coding: utf-8

from flask import Flask, render_template

from PIL import Image, ImageFilter
import random

app = Flask(__name__)

FILTER_OPTIONS = [
    ImageFilter.BLUR,
    ImageFilter.CONTOUR,
    ImageFilter.EDGE_ENHANCE,
    ImageFilter.EMBOSS,
    ImageFilter.SHARPEN,
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:pic_id>/')
def inmage_preview(pic_id):
    i = Image.open('static/images/{}.jpg'.format(pic_id))
    i.save('static/images/{}_processed.jpg'.format(pic_id))
    for x in range(0, 7):
        rand_filter = random.randint(0, len(FILTER_OPTIONS)-1)
        im = Image.open('static/images/{}_processed.jpg'.format(pic_id))
        im = im.filter(FILTER_OPTIONS[rand_filter])
        im.save('static/images/{}_processed.jpg'.format(pic_id))
    return render_template('display_img.html', image=str(pic_id))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

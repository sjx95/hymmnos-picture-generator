# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from tempfile import TemporaryFile


def index(request):
    return render(None, 'hymmnos2picture_welcome.html')


def pic(request):
    if request.method == "GET":
        if request.GET.has_key("text"):
            text = request.GET.get("text", None)
            size = 48
            # 生成图片
            font = ImageFont.truetype("hymmnos2picture/static/hymmnos.ttf", size)
            image = Image.new('1', font.getsize(text))
            draw = ImageDraw.Draw(image)
            draw.text((0,0), text, font=font, fill='#66ccff')
            # 写入临时文件
            tmp_file = TemporaryFile()
            image.save(tmp_file, 'png')
            tmp_file.seek(0);
            image_data = tmp_file.read()
            # 把图片文件返回给浏览器
            return HttpResponse(image_data, content_type="image/png")  # 注意旧版的资料使用mimetype,现在已经改为content_type
    return HttpResponse("Illegal Parameter")
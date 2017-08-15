# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from tempfile import TemporaryFile


def index(request):
    return render(None, 'hymmnos2picture_welcome.html')


def pic(request):
    # 获取参数
    text = request.GET.get("text", 'Hymmnos')
    size = request.GET.get("size", '36')
    fg = request.GET.get('fg', '000000')
    bg = request.GET.get('bg', 'FFFFFF')
    # 判断字符串格式是否正确
    if len(text)==0 or len(size)==0:
        return HttpResponse("Illegal Parameter")
    for ch in size:
        if not (ch>=0 and ch<='9'):
            return HttpResponse("Illegal Parameter")
    if len(fg)!=6:
        fg = '000000'
    else:
        for ch in fg:
            if not((ch>='0' and ch<='9') or (ch>='A' and ch<='F') or (ch>='a' and ch<='f')):
                fg = '000000'
                break
    if len(bg)!=6:
        bg = 'FFFFFF'
    else:
        for ch in bg:
            if not((ch>='0' and ch<='9') or (ch>='A' and ch<='F') or (ch>='a' and ch<='f')):
                bg = 'FFFFFF'
                break
    # 生成图片
    font = ImageFont.truetype("hymmnos2picture/static/hymmnos.ttf", int(size))
    image = Image.new('RGB', font.getsize(text), '#'+bg)
    draw = ImageDraw.Draw(image)
    draw.text((0,0), text, font=font, fill='#'+fg)
    # 写入临时文件
    tmp_file = TemporaryFile()
    image.save(tmp_file, 'png')
    tmp_file.seek(0);
    image_data = tmp_file.read()
    # 把图片文件返回给浏览器
    return HttpResponse(image_data, content_type="image/png")  # 注意旧版的资料使用mimetype,现在已经改为content_type
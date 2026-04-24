#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для конвертации PNG фото в WebP формат в папке portfolio
"""

from PIL import Image
import os

# Папка с фото
photo_folder = r'A:\ChatGPTplus\portfolio\photo'

# Список файлов для конвертации
files_to_convert = [
    ('brow master photo.png', 'brow-master-photo.webp'),
    ('psychologist photo.png', 'psychologist-photo.webp'),
    ('clean city photo.png', 'clean-city-photo.webp'),
    ('fitness photo.png', 'fitness-photo.webp'),
]

print("=" * 60)
print("🎨 Конвертация PNG в WebP (portfolio)")
print("=" * 60)

for png_name, webp_name in files_to_convert:
    png_path = os.path.join(photo_folder, png_name)
    webp_path = os.path.join(photo_folder, webp_name)
    
    if not os.path.exists(png_path):
        print(f"❌ Файл не найден: {png_name}")
        continue
    
    try:
        # Открываем PNG
        img = Image.open(png_path)
        
        # Конвертируем в RGB (если есть альфа-канал)
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        # Сохраняем в WebP (качество 85)
        img.save(webp_path, 'WEBP', quality=85)
        
        # Считаем размер файлов
        png_size = os.path.getsize(png_path) / 1024  # в KB
        webp_size = os.path.getsize(webp_path) / 1024  # в KB
        savings = ((png_size - webp_size) / png_size) * 100
        
        print(f"✅ {png_name}")
        print(f"   PNG:  {png_size:.1f} KB → WebP: {webp_size:.1f} KB")
        print(f"   Сэкономлено: {savings:.1f}%")
        print()
        
    except Exception as e:
        print(f"❌ Ошибка при конвертации {png_name}: {str(e)}")

print("=" * 60)
print("✨ Конвертация завершена!")
print("=" * 60)


from PIL import Image
import os

img_path = r'C:\Users\sushi\.gemini\antigravity-cli\brain\c95297d2-2b79-476a-ae7d-bf3b2d61fcf6\optilauncher_icon_no_eye_1781622781562.jpg'
base_res_path = r'C:\Users\sushi\PojavLauncher\app_pojavlauncher\src\main\res'

img = Image.open(img_path).convert('RGBA')

sizes = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}

for folder, size in sizes.items():
    folder_path = os.path.join(base_res_path, folder)
    if os.path.exists(folder_path):
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        resized_img.save(os.path.join(folder_path, 'ic_launcher.png'), 'PNG')
        resized_img.save(os.path.join(folder_path, 'ic_launcher_round.png'), 'PNG')
        resized_img.save(os.path.join(folder_path, 'ic_launcher_foreground.png'), 'PNG')
        
print('Icons replaced successfully!')

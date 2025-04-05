import os
from fontTools.ttLib import TTFont

# Define paths
ZAIN_FONTS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'packages', 'excalidraw', 'fonts', 'Zain')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# List of Zain font files to convert
font_files = [
    'Zain-Black.ttf',
    'Zain-Bold.ttf',
    'Zain-ExtraBold.ttf',
    'Zain-ExtraLight.ttf',
    'Zain-Italic.ttf',
    'Zain-Light.ttf',
    'Zain-LightItalic.ttf',
    'Zain-Regular.ttf'
]

# Convert each TTF file to WOFF2
for file in font_files:
    ttf_path = os.path.join(ZAIN_FONTS_DIR, file)
    woff2_path = os.path.join(OUTPUT_DIR, file.replace('.ttf', '.woff2'))

    if os.path.exists(ttf_path):
        print(f"Converting {file} to WOFF2 format...")
        font = TTFont(ttf_path)
        font.flavor = 'woff2'
        font.save(woff2_path)
        print(f"Successfully converted {file} to WOFF2 format")
    else:
        print(f"Warning: {file} not found in {ZAIN_FONTS_DIR}")

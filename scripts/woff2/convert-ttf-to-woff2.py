import os
from fontTools.ttLib import TTFont

# Define paths
FONTS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
ZAIN_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'packages', 'excalidraw', 'fonts', 'Zain')
IBM_OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'packages', 'excalidraw', 'fonts', 'IBMPlex')

# Ensure output directories exist
os.makedirs(ZAIN_OUTPUT_DIR, exist_ok=True)
os.makedirs(IBM_OUTPUT_DIR, exist_ok=True)

# List of Zain font files to convert
zain_font_files = [
    'Zain-Black.ttf',
    'Zain-Bold.ttf',
    'Zain-ExtraBold.ttf',
    'Zain-ExtraLight.ttf',
    'Zain-Italic.ttf',
    'Zain-Light.ttf',
    'Zain-LightItalic.ttf',
    'Zain-Regular.ttf'
]

# List of IBM Plex Sans font files to convert
ibm_font_files = [
    'IBMPlexSans-VariableFont_wdth,wght.ttf',
    'IBMPlexSans-Italic-VariableFont_wdth,wght.ttf'
]

# Convert Zain TTF files to WOFF2
for file in zain_font_files:
    ttf_path = os.path.join(FONTS_DIR, file)
    woff2_path = os.path.join(ZAIN_OUTPUT_DIR, file.replace('.ttf', '.woff2'))

    if os.path.exists(ttf_path):
        print(f"Converting {file} to WOFF2 format...")
        font = TTFont(ttf_path)
        font.flavor = 'woff2'
        font.save(woff2_path)
        print(f"Successfully converted {file} to WOFF2 format")
    else:
        print(f"Warning: {file} not found in {FONTS_DIR}")

# Convert IBM Plex Sans TTF files to WOFF2
for file in ibm_font_files:
    ttf_path = os.path.join(FONTS_DIR, file)
    # Simplify the output filenames
    if 'VariableFont_wdth,wght.ttf' in file:
        if 'Italic' in file:
            output_file = 'IBMPlexSans-Italic.woff2'
        else:
            output_file = 'IBMPlexSans-Regular.woff2'
    else:
        output_file = file.replace('.ttf', '.woff2')

    woff2_path = os.path.join(IBM_OUTPUT_DIR, output_file)

    if os.path.exists(ttf_path):
        print(f"Converting {file} to WOFF2 format...")
        font = TTFont(ttf_path)
        font.flavor = 'woff2'
        font.save(woff2_path)
        print(f"Successfully converted {file} to WOFF2 format")
    else:
        print(f"Warning: {file} not found in {FONTS_DIR}")

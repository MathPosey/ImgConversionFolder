from PIL import Image
import os

def convert_png_to_jpg(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            png_path = os.path.join(input_folder, filename)
            jpg_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

            img = Image.open(png_path)
            img.convert("RGB").save(jpg_path, "JPEG")
            print(f"Converted {filename} to {os.path.basename(jpg_path)}")

# Example usage
input_folder = "C:\programFile\ImgConversionFolder\pngFiles"
output_folder = "C:\programFile\ImgConversionFolder\jpgOutPut"
convert_png_to_jpg(input_folder, output_folder)

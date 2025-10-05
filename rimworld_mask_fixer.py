from PIL import Image
import sys
import os
#From redmattis on his discord server
def brightness_to_alpha(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()
    
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            
            brightness = max(r, max(b,g))
            new_alpha = brightness
            new_alpha = min(a, new_alpha)
            
            pixels[x, y] = (r, g, b, new_alpha)

    img.save(output_path, "PNG")
    print(f"Saved image with brightness-based alpha: {output_path}")


def process_all_pngs_in_folder(folder):
    print(folder)
    for file in os.listdir(folder):
        input_path = os.path.join(folder, file)
        if file.lower().endswith("m.png"):
            brightness_to_alpha(input_path, input_path)
        if os.path.isdir(input_path): #i stuck this in though
            process_all_pngs_in_folder(input_path)
        
if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    process_all_pngs_in_folder(folder)
    print("✅ Done processing all PNGs in folder.")
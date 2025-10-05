import sys
import os

def process(input_path):
    #tail
    if not try_image(input_path+"/Tail/Defaulttail_north.png", "UI/Icons/Genes/Gene_"+input_path+"Tail.png"):
        do_image(input_path+"/Tail/Male/Defaulttail_north.png", "UI/Icons/Genes/Gene_"+input_path+"Tail.png")
    #body
    if not try_image(input_path+"/Body/Male_Naked_Thin_south.png", "UI/Icons/Genes/Gene_"+input_path+"Body.png"):
        if not try_image(input_path+"/Body/Naked_Male_south.png", "UI/Icons/Genes/Gene_"+input_path+"Body.png"):
            if not try_image(input_path+"/Body/Male_Naked_Female_south.png", "UI/Icons/Genes/Gene_"+input_path+"Body.png"):
                print("No match for body: " + input_path)
    
    #head
    if not try_image_double(input_path+"/Head/Male_Average_Normal_south.png", input_path+"/Hairfront/fhair_south.png", "UI/Icons/Genes/Gene_"+input_path+"Head.png"):
        if not try_image_double(input_path+"/Head/Male_Average_Normal_south.png", input_path+"/Hairfront/Male/fhair_south.png", "UI/Icons/Genes/Gene_"+input_path+"Head.png"):
            if not try_image_triple(input_path+"/Head/Male_Average_Normal_south.png", input_path+"/Hairfront/var_south.png", input_path+"/Mane/mane_south.png", "UI/Icons/Genes/Gene_"+input_path+"Head.png"):
                if not try_image_triple(input_path+"/Head/Male_Average_Normal_south.png", input_path+"/Neckfin/neckfin_south.png", input_path+"/Fin/var_south.png", "UI/Icons/Genes/Gene_"+input_path+"Head.png"):
                    do_image(input_path+"/Head/Male_Average_Normal_south.png", "UI/Icons/Genes/Gene_"+input_path+"Head.png")
    #ears
    if not try_image_double(input_path+"/Ear/leftear_south.png", input_path+"/Ear/rightear_south.png", "UI/Icons/Genes/Gene_"+input_path+"Ears.png"):
        if not try_image_double(input_path+"/Earbase/Male/leftear_south.png", input_path+"/Earbase/Male/rightear_south.png", "UI/Icons/Genes/Gene_"+input_path+"Ears.png"):
            if not try_image_double(input_path+"/Ear/leftear_south.png", input_path+"/Ear/rightear_south.png", "UI/Icons/Genes/Gene_"+input_path+"Ears.png"):
                print("No match for ears: " + input_path)

def try_image(path, output):
    if os.path.exists(path):
        do_image(path, output)
        return True
    return False
def try_image_double(path, path2, output):
    if os.path.exists(path2):
        do_image_double(path, path2, output)
        return True
    return False
def try_image_triple(path, path2, path3, output):
    if os.path.exists(path3):
        do_image_triple(path, path2, path3, output)
        return True
    return False

def do_image(input, output):
    print(input)
    os.system(f"magick ./{input} -channel RGB -evaluate set 100% +channel -background black -alpha background -channel A -blur 0x3 -level 0,1% -trim -gravity center -resize 128x128 -background transparent -extent 128x128 ./{output}")
    
def do_image_double(input, input2, output):
    print(input)
    os.system(f"magick ./{input} ./{input2}  -composite -channel RGB -evaluate set 100% +channel -background black -alpha background -channel A -blur 0x3 -level 0,1% -trim -gravity center -resize 128x128 -background transparent -extent 128x128 ./{output}")
    
def do_image_triple(input, input2, input3, output):
    print(input)
    os.system(f"magick ./{input} ./{input2} ./{input3} -composite -channel RGB -evaluate set 100% +channel -background black -alpha background -channel A -blur 0x3 -level 0,1% -trim -gravity center -resize 128x128 -background transparent -extent 128x128 ./{output}")
    
if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir(folder):
        if os.path.isdir(file) and file != "UI":
            process(file)
    print("✅ Done processing all PNGs in folder.")
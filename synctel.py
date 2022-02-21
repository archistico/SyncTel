import os
import subprocess
import pathlib
import filecmp

# https://dl.google.com/android/repository/platform-tools-latest-windows.zip
# ./adb.exe devices
# Ricordarsi di poter vedere il cellulare (usb debug ON, dopo aver messo modalità sviluppatore)
# c/Users/Archemi/Downloads/platform-tools_r32.0.0-windows/platform-tools

def Comando_copia_immagine(cartella, img, cartella_export, img_temp):
    return "adb pull " + cartella + "/" + img + " " + cartella_export + "/" + img_temp
    
CARTELLA_TELEFONO = "/sdcard/DCIM/Camera"
CARTELLA_EXPORT = "./export"
COMANDO_LETTURA_CARTELLA_TELEFONO = "adb shell ls " + CARTELLA_TELEFONO

result_read_phone = subprocess.check_output(COMANDO_LETTURA_CARTELLA_TELEFONO, shell=True)
lista_immagini = result_read_phone.decode('UTF-8').splitlines()

for img in lista_immagini:
    file_extension = pathlib.Path(img).suffix
    if file_extension.upper() == '.JPG' or file_extension.upper() == '.PNG':
        img_temp = img + ".temp"
        subprocess.check_output(Comando_copia_immagine(CARTELLA_TELEFONO, img, CARTELLA_EXPORT, img_temp), shell=True)
        if not os.path.exists(CARTELLA_EXPORT + "/" + img):
            os.rename(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + img)
            print("File copiato: " + img)
        else:
            if filecmp.cmp(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + img, shallow = True):
                os.remove(CARTELLA_EXPORT + "/" + img_temp) 
                print("File presente e non copiato: " + img)
            else:
                cicla = True
                num = 0
                while cicla:
                    num = num + 1
                    nuovo_nome_file = pathlib.Path(img).stem + "_" + f'{num:03}' + pathlib.Path(img).suffix
                    if not os.path.exists(CARTELLA_EXPORT + "/" + nuovo_nome_file):
                        os.rename(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + nuovo_nome_file)
                        print("File con nome: " + img + " presente ma differente e rinominato: " + nuovo_nome_file)
                        cicla = False
                    else:
                        if filecmp.cmp(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + nuovo_nome_file, shallow = True):
                            os.remove(CARTELLA_EXPORT + "/" + img_temp) 
                            print("File con nome: " + img + " presente e non copiato: " + nuovo_nome_file)
                            cicla = False
                    
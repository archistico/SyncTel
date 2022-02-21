import os
import subprocess
import pathlib
import filecmp

def Comando_copia_immagine(cartella, img, cartella_export, img_temp):
    return "adb pull " + cartella + "/" + img + " " + cartella_export + "/" + img_temp

def Comando_elimina_immagine(cartella, img):
    return "adb shell rm -f " + cartella + "/" + img

def Scarica(CARTELLA_TELEFONO, CARTELLA_EXPORT):

    COMANDO_LETTURA_CARTELLA_TELEFONO = "adb shell ls " + CARTELLA_TELEFONO

    result_read_phone = subprocess.check_output(COMANDO_LETTURA_CARTELLA_TELEFONO, shell=True)
    lista_immagini = result_read_phone.decode('UTF-8').splitlines()

    if not os.path.exists(CARTELLA_EXPORT):
        os.makedirs(CARTELLA_EXPORT)

    for img in lista_immagini:
        file_extension = pathlib.Path(img).suffix
        if file_extension.upper() == '.JPG' or file_extension.upper() == '.PNG' or file_extension.upper() == '.JPEG' or file_extension.upper() == '.MP4':
            img_temp = img + ".temp"
            subprocess.check_output(Comando_copia_immagine(CARTELLA_TELEFONO, img, CARTELLA_EXPORT, img_temp), shell=True)
            if not os.path.exists(CARTELLA_EXPORT + "/" + img):
                os.rename(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + img)
                print("File copiato: " + CARTELLA_TELEFONO + "/" + img)
            else:
                if filecmp.cmp(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + img, shallow = True):
                    os.remove(CARTELLA_EXPORT + "/" + img_temp) 
                    print("File presente e non copiato: " + CARTELLA_TELEFONO + "/" + img)
                else:
                    cicla = True
                    num = 0
                    while cicla:
                        num = num + 1
                        nuovo_nome_file = pathlib.Path(img).stem + "_" + f'{num:03}' + pathlib.Path(img).suffix
                        if not os.path.exists(CARTELLA_EXPORT + "/" + nuovo_nome_file):
                            os.rename(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + nuovo_nome_file)
                            print("File con nome: " + CARTELLA_TELEFONO + "/" + img + " presente ma differente e rinominato: " + nuovo_nome_file)
                            cicla = False
                        else:
                            if filecmp.cmp(CARTELLA_EXPORT + "/" + img_temp, CARTELLA_EXPORT + "/" + nuovo_nome_file, shallow = True):
                                os.remove(CARTELLA_EXPORT + "/" + img_temp) 
                                print("File con nome: " + CARTELLA_TELEFONO + "/" + img + " presente e non copiato: " + nuovo_nome_file)
                                cicla = False

    if len(lista_immagini) > 0:
        risposta = str(input("Cancello le immagini sul telefono? [si/no]"))

        if risposta.upper() == "SI" or risposta.upper() == "S":
            for img in lista_immagini:
                file_extension = pathlib.Path(img).suffix
                if file_extension.upper() == '.JPG' or file_extension.upper() == '.PNG':
                    subprocess.check_output(Comando_elimina_immagine(CARTELLA_TELEFONO, img), shell=True)
                    print("Cancellato immagine: " + CARTELLA_TELEFONO + "/" + img)
    else:
        print("Non ci sono file nella cartella da copiare")


lista_dir = [
    { 'cartella_telefono': "/sdcard/DCIM/Camera", 'cartella_export': "./export/camera"}
]

for el in lista_dir:
    Scarica(el['cartella_telefono'], el['cartella_export'])

print("Fine")
    
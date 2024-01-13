import json
import zipfile
import os

api_token ={"username":"sebastian1414","key":"8500d45c06bc4ebaba9f198c71508617"}

##Conectar a Kaggle
with open('C:/Users/Tu vieja/.kaggle/kaggle.json',"w") as file:
    json.dump(api_token, file)

location = "c:/Users/Tu vieja/Documents/Proyecto/dataset"

##Validar que la carpeta exista
if not os.path.exists(location):
##Si no existe la carpeta dataset entonces la creo
    os.mkdir(location)
else:
##Si la carpeta si existe, entonces voy a borrar su contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ##elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) ##elimino todas las carpetas

##Descargar dataset de Kaggle
os.system("kaggle datasets download -d henryshan/starbucks -p c:/Users/USER/Documents/Proyecto/dataset")

##Descomprimir el archivo de Kaggle
os.chdir(location)
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file,"r") ##lee archivo .zip
    zip_ref.extractall() ##extrae contenido de archivo .zip
    zip_ref.close() ##cierra archivo





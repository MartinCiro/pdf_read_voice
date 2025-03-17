# region importando librerias necesarias
import os
import json
import pathlib
from customtkinter import CTkFont, filedialog, CTkImage
from cryptography.fernet import Fernet
from PIL import ImageTk, Image, ImageFont
from fitz import Document


# endregion importando librerias necesarias

# region Instanciar Objetos y variables Globales
relativePath = os.getcwd()
KEYENCRYPT = "ecTNu1JkrN8WOEZQ667dOGOqBcS9Peh0RShN83l1WK0="
f = Fernet(KEYENCRYPT)
# endregion importando librerias necesarias

# region Creando una clase
class Helpers:
    # Contructores e inicializadores
    def __init__(self):
        self.__routeConfig = relativePath + "/config.json"
        self.__initial_count = 0
    
    # region Metodos
    # Nos ayuda para traer las rutas completas del config
    def getRoutes(self, key, value):
        data = self.getValue(key, value)        
        fullpath = relativePath + data
        return fullpath
    
    def encriptarData(self, valor: str):
        """
            Se encrypta un dato dado, en tipo str para
            hacer su encryptación a través de la llave
            recibida en el llamado del metodo
        - `Args:`
            - valor (str): Valor del metodo a encryptar
        - `Returns:`
            - str: Valor encryptado
        """
        token = f.encrypt(str.encode(valor)).decode("utf-8")
        return token
        
    def desEncriptarData(self, valor: str):
        """
            Toma la llave de encriptación, y el
            valor a desencriptar, y retorna el valor
            en formato str.
            - `Args:`
                - valor (str): Valor a desencriptar
            - `Returns:`
                - texto (str): Valor desencriptado en UTF8
        """
        texto = f.decrypt(valor)
        return texto.decode("utf-8")

    # Nos ayuda a extraer un valor del config
    def getValue(self, key, value):
        with open(self.__routeConfig, 'r') as file: 
            config = json.load(file)
            if config[key][value] == "":
                file.close()
            else:
                data = str(config[key][value])
                file.close()
        
        return data
    
    # Nos permite cargar una imagen de forma dinamica
    def getImage(self, key, size):
        """
        Carga una imagen, la redimensiona y la convierte en un objeto CTkImage.
        
        Parámetros:
            key (str): La clave para obtener la ruta de la imagen.
            size (tuple): El tamaño deseado para la imagen (ancho, alto).
        
        Retorna:
            CTkImage: La imagen redimensionada y convertida a CTkImage.
        """
        try:
            # Abrir la imagen
            image = Image.open(self.getRoutes(key, "Value"))
            # Redimensionar la imagen con el filtro LANCZOS
            image = image.resize(size, Image.Resampling.LANCZOS)
            # Convertir a un objeto CTkImage
            return CTkImage(light_image=image, size=size)
        except Exception as e:
            print(f"Error cargando la imagen: {e}")
            # Si falla, devuelve una imagen predeterminada
            default_image = Image.new("RGB", size, color="white")
            return CTkImage(light_image=default_image, size=size)
        
    #Nos permite realizar un centrado de la ventana
    def centerWindows(self,windows,height,withs):    
        pantall_ancho = windows.winfo_screenwidth()
        pantall_largo = windows.winfo_screenheight()
        x = int((pantall_ancho/2) - (withs/2))
        y = int((pantall_largo/2) - (height/2))
        return windows.geometry(f"{withs}x{height}+{x}+{y}")
    
    # Nos permite habilitar ingresar valor y deshabilitar
    def SetInfoDisabled(self, inputTxt, value):
        inputTxt.configure(state='normal')
        inputTxt.delete(0,"end")
        inputTxt.insert(0,str(value))
        inputTxt.configure(state='disabled')
    
    # Nos permite realizar el conteo de las carpetas
    def countFolder(self,ruta):
        self.__initial_count = 0
        for path in pathlib.Path(ruta).iterdir():
            if path.is_dir():
                self.__initial_count += 1
                
        return self.__initial_count
    
    # Metodo para realizar la validacion del destino
    def ValidateDestiny(self, ruta):
        cont = 0
        dir = ruta
        for f in os.listdir(dir):
            cont += 1
        return cont
    

    def ValidateSource(self, font, size=40):
        try:
            # Intentar cargar la fuente personalizada
            ruta_fuente = self.getRoutes("Fonts", font)  # Obtén la ruta de la fuente
            fuente_real = ImageFont.truetype(ruta_fuente, size=size)  # Carga la fuente con el tamaño especificado

            # Devuelve una instancia de CTkFont
            return CTkFont(family=fuente_real.font.family, size=size)
        except Exception as e:
            print(f"Error cargando la fuente: {e}")
            # Si falla, usa una fuente predeterminada
            return CTkFont(family="Times", size=size)  # Devuelve una instancia de CTkFont


    def open_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            try:
                pdf_document = Document(file_path)  
                self.text = "\n".join([pdf_document.load_page(i).get_text() for i in range(pdf_document.page_count)])
                print(self.text)
                return self.text
            except Exception as e:
                print(f"Error al leer el PDF: {e}")
                return None
    # endregion Metodos
# endregion
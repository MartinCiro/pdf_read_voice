# ===========================================================================
# Importaciones de clases y librerias necesarias en esta vista
# ===========================================================================
# Region - Importación de librerias y clases.
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, messagebox

from controller.utils.Helpers import Helpers
# Endregion - Importación de librerias y clases.

# Region - Inicialización de clases para uso de metodos.
helpers = Helpers()
# Endregion - Inicialización de clases para uso de metodos.

class VentanaPrincipalForm:
    """
    VentanaPrincipalForm
    ====================
    Clase para gestionar la creación del formulario
    de ttk, con estilos personalizados para el proceso
    de armado de cuentas del proyecto zentria.
    """
    def __init__(self):
        # Region - Configuración de ventana (Form)
        self.ventana = tk.Tk()  # Instancia de Tkinter en var ventana

        super().__init__()                        
        self.ventana.title('Radicación Zentria - V1.0.0.0') # Titulo de la ventana
        self.ventana.geometry('800x500') # Dimensiones iniciales de la ventana
        self.ventana.config(bg = '#FFF3F1') # Fondo de la ventana
        self.ventana.resizable(width = 0, height = 0) # Inhabilita el resize de la ventana por usuario
        helpers.centerWindows(self.ventana, 450, 860) # height | width Se centra la ventana en pantalla
        style = ttk.Style(self.ventana) # Se le asignan estilos desde una var a la ventana
        
        self.ventana.tk.call("source", "forest-light.tcl") # Importación de los estilos, desde un theme
        style.theme_use("forest-light") # Instancia del theme desde la variable Style
        # Endregion - Configuración de ventana (Form)

        # region - Variables globales a usar dentro del form
        

        # Colors
        self.colorRed   = helpers.getValue("Colors", "red")
        self.color_white = helpers.getValue("Colors", "white")
        self.colorGreen = helpers.getValue("Colors", "green")
        self.color_backg = helpers.getValue("Colors", "backg")
        self.colorIcon  = helpers.getValue("Colors", "icon")
        # style.configure("FAB.TButton", background=self.color_backg, relief="flat", padding=5)

        # Fonts
        self.fontsTitle = helpers.getValue("Fonts", "title")
        self.fontsText  = helpers.getValue("Fonts", "text")
        self.textBold   = helpers.getValue("Fonts", "textBold")
        self.textItalic = helpers.getValue("Fonts", "textItalic")
        self.textBoldItalic = helpers.getValue("Fonts", "textBoldItalic")
        self.textLight  = helpers.getValue("Fonts", "textLight")
        fuente_title = helpers.ValidateSource("title")
        fuente_text_bold = helpers.ValidateSource("textBold", 20)

        # Images
        self.icon_play_pause = helpers.getImage("PlayPause", (60, 60))
        self.icon_speed = helpers.getImage("Speed", (40, 30))
        self.icon_prev_page = helpers.getImage("PrevPage", (30, 30))
        self.icon_next_page = helpers.getImage("NextPage", (30, 30))
        self.icon_prev_f = helpers.getImage("PrevF", (50, 50))
        self.icon_next_f = helpers.getImage("NextF", (50, 50))
        self.icon_logo   = helpers.getImage("Logo", (10, 15))
        self.icon_app    = helpers.getImage("IconApp", (10, 15))
        self.icon_upload_light = helpers.getImage("UploadLight", (10, 15))
        self.icon_upload = helpers.getImage("Upload", (30, 35))

        #self.__listadoIPS = [item["nombre_ips"] for item in self.__dataSedes]
        self.__listadoEPS =[]
        self.__listadoContratos =[]

        #self.__listadoIPS.insert(0, "-- Selecciona una IPS --") # Se les añade una opción por Deafult
        self.__listadoEPS.insert(0, "-- Selecciona una EPS --") # Se les añade una opción por Deafult
        self.__listadoContratos.insert(0, "-- Selecciona un Contrato --") # Se les añade una opción por Deafult
        tipoIPS = StringVar() # Asignación de tipo a una variable

        self.dfExcel = ""
        # Endregion - Variables globales a usar dentro del form
          
        # region Metodos internos

        # Metodo para validar los campos para ejecutar el proceso
        def validatefields():
            if("Selecciona" in tipoIPS.get()):
                messagebox.showwarning(message = "No has seleccionado una [IPS] aún", title = "¡ERROR!")
            else:
                return True

        # Metodo para ejecutar el procesos principal
        def Execute(): 
            try:
                if validatefields():
                    continuar = messagebox.askyesno(message="¿Estás seguro de ejecutar el proceso?", title = "Espera...")
            except Exception  as e:
                messagebox.showinfo(message = f"No ha sido posible realizar la ejecución, valida con soporte. Error: {str(e)}", title = "¡ERROR!")

        # Endregion Metodos internos
            
        # Region - Header del formulario.
        # =========================================================================
        # | Frame - Header completo
        # =========================================================================
        frameHeader = tk.Frame(self.ventana, bd = 0, height = 100, relief = tk.SOLID, padx = 1, pady = 1, bg = self.color_backg)
        frameHeader.pack(side = "top", expand = tk.FALSE, fill = tk.BOTH)
        
        # Region Right side Header
        # =========================================================================
        # | Frame Right side Header
        # =========================================================================
       
        # Configuración del titulo del formulario
        title = tk.Label(frameHeader, text="PDF TO VOICE", font = fuente_title, fg=self.colorRed, bg=self.color_backg, pady=20)  
        title.pack(expand = tk.TRUE, fill = tk.BOTH)

        # Endregion Right side Header
        # Endregion - Header del formulario.

        # Region - Cuerpo principal del formulario        
        # Region rightbody
        # =========================================================================
        # | frame form campos y botones
        # =========================================================================
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg=self.color_backg)
        frame_form.pack(expand=tk.TRUE, fill=tk.BOTH)
        

        # =========================================================================
        # | Frame Left Body
        # =========================================================================
        frame_right = tk.Frame(frame_form, bd=0, relief=tk.SOLID, bg=self.color_backg, padx=100, pady=10)
        frame_right.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        frame_right.columnconfigure(0, weight=1)

        frame_texto = tk.Frame(frame_right, bd=2, relief="solid", background=self.colorGreen)
        frame_texto.grid(row=8, column=0, padx=10, pady=(2, 5), sticky="nsew")

        # Etiqueta para indicar el cuadro de texto
        lbl_texto_leer = ttk.Label(frame_right, text="Texto a leer:", font=fuente_text_bold, background=self.color_backg)
        lbl_texto_leer.grid(row=7, column=0, padx=10, pady=(10, 2), sticky="w")

        # Cuadro de texto dentro del frame para simular el borde de color
        self.text_widget = tk.Text(frame_texto, wrap="word", width=40, height=10, bd=0, highlightthickness=0, bg=self.color_white)
        self.text_widget.pack(padx=2, pady=2, fill="both", expand=True)
        self.text_widget.config(font=self.fontsText)

        # Organizar tamaño del cuadro de texto
        frame_fab = tk.Frame(frame_texto, bd=0, relief=tk.SOLID, bg=self.color_white, width=10)
        frame_fab.place(relx=0.01, rely=0.98, anchor="sw")

        # Estilo para el botón flotante
        style.configure(
            "btnTextBox.Toolbutton",
            foreground=self.color_white,  
            background=self.color_white,
            width=frame_fab.winfo_width(),
        )

        # Boton flotante add
        self.boton_flotante_add = ttk.Button(frame_fab, image=self.icon_upload, style="btnTextBox.Toolbutton", compound="center", command=helpers.open_pdf)
        self.boton_flotante_add.pack(fill="both", expand=True)

        # Boton flotante left page
        frame_btn_flotante_page = tk.Frame(frame_texto, bd=0, relief=tk.SOLID, bg=self.color_white, width=0.1, height=1)
        frame_btn_flotante_page.place(relx=1, rely=1, anchor="s", x=-35, y=-5) 

        txt_num_page = ttk.Entry(frame_btn_flotante_page, width=4, justify="center", font=self.fontsTitle)
        txt_num_page.pack(fill="x", ipady=1)
        txt_num_page.insert(0, "1")












        style.configure(
            "btnPlay.Toolbutton",
            foreground=self.color_backg,  
            background=self.color_backg
        )

        # Configuración del frame de botones
        frame_btns = tk.Frame(frame_right, bd=0, relief=tk.SOLID, bg=self.color_backg, padx=0, pady=5)
        frame_btns.grid(row=11, column=0, padx=0, pady=0, sticky="ew")

        # Configurar columnas para centrar botones
        frame_btns.grid_columnconfigure(0, weight=1)  # Espacio a la izquierda
        frame_btns.grid_columnconfigure(1, weight=1)
        frame_btns.grid_columnconfigure(2, weight=2)  # Botón Play centrado
        frame_btns.grid_columnconfigure(3, weight=1)
        frame_btns.grid_columnconfigure(4, weight=1)  # Espacio a la derecha

        # Botones
        btn_next_f = ttk.Button(frame_btns, image=self.icon_next_f, style="btnPlay.Toolbutton", compound="center", command=Execute)
        btn_next_f.grid(row=11, column=4, padx=2, pady=0, sticky="ew")

        btn_netx_page = ttk.Button(frame_btns, image=self.icon_next_page, style="btnPlay.Toolbutton", compound="center", command=Execute)
        btn_netx_page.grid(row=11, column=3, padx=2, pady=0, sticky="ew")

        btn_play = ttk.Button(frame_btns, image=self.icon_play_pause, style="btnPlay.Toolbutton", compound="center", command=Execute)
        btn_play.grid(row=11, column=2, padx=2, pady=0, sticky="ew")  # Centrado

        btn_prev_page = ttk.Button(frame_btns, image=self.icon_prev_page, style="btnPlay.Toolbutton", compound="center", command=Execute)
        btn_prev_page.grid(row=11, column=1, padx=2, pady=0, sticky="ew")

        btn_prev_f = ttk.Button(frame_btns, image=self.icon_prev_f, style="btnPlay.Toolbutton", compound="center", command=Execute)
        btn_prev_f.grid(row=11, column=0, padx=2, pady=0, sticky="ew")


        # para el speed
        frame_speed = tk.Frame(frame_right, bd=0, relief=tk.SOLID, bg=self.color_backg, width=10)
        frame_speed.place(relx=0.99, rely=0.76, anchor="sw")

        # Estilo para el botón flotante
        style.configure(
            "btnSpeed.Toolbutton",
            foreground=self.color_backg,  
            background=self.color_backg,
            width=frame_speed.winfo_width(),
        )

        # Boton flotante add
        self.boton_change_speed = ttk.Button(frame_speed, image=self.icon_speed, style="btnSpeed.Toolbutton", compound="center", command=Execute)
        self.boton_change_speed.pack(fill="both", expand=True)

        


        # Endregion - rightbody
        # Endregion  - Cuerpo principal del formulario 
        self.ventana.mainloop()

# Metodo para inicializar el metodo ventana principal    
if __name__ == '__main__':
    VentanaPrincipalForm()
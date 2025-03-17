# ===========================================================================
# Importaciones de clases y librerias necesarias en esta vista
# ===========================================================================
# Region - Importación de librerias y clases.
import customtkinter as ctk

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
    de customtkinter, con estilos personalizados para el proceso
    de armado de cuentas del proyecto zentria.
    """
    def __init__(self):
        # Region - Configuración de ventana (Form)
        self.ventana = ctk.CTk()  # Instancia de CustomTkinter en var ventana

        self.ventana.title('Radicación Zentria - V1.0.0.0')  # Titulo de la ventana
        self.ventana.geometry('800x500')  # Dimensiones iniciales de la ventana
        self.ventana.configure(fg_color ='#FFF3F1')  # Fondo de la ventana
        self.ventana.resizable(width =False, height =False)  # Inhabilita el resize de la ventana por usuario
        helpers.centerWindows(self.ventana, 450, 860)  # height | width Se centra la ventana en pantalla

        # Endregion - Configuración de ventana (Form)

        # region - Variables globales a usar dentro del form
        # Colors
        self.colorRed = helpers.getValue("Colors", "red")
        self.color_white = helpers.getValue("Colors", "white")
        self.color_green = helpers.getValue("Colors", "green")
        self.color_backg = helpers.getValue("Colors", "backg")
        self.colorIcon = helpers.getValue("Colors", "icon")

        # Fonts
        self.fontsTitle = helpers.ValidateSource("title", 40)  # Numero establece el tamaño de fuente
        self.fontsText = helpers.ValidateSource("text", 20)  # Numero establece el tamaño de fuente
        self.textBold = helpers.ValidateSource("textBold", 35)  # Numero establece el tamaño de fuente


        # Images
        self.icon_play_pause = helpers.getImage("PlayPause", (70, 70))
        self.icon_speed = helpers.getImage("Speed", (40, 30))
        self.icon_prev_page = helpers.getImage("PrevPage", (30, 30))
        self.icon_next_page = helpers.getImage("NextPage", (30, 30))
        self.icon_prev_f = helpers.getImage("PrevF", (50, 50))
        self.icon_next_f = helpers.getImage("NextF", (50, 50))
        self.icon_logo = helpers.getImage("Logo", (10, 15))
        self.icon_app = helpers.getImage("IconApp", (10, 15))
        self.icon_upload_light = helpers.getImage("UploadLight", (10, 15))
        self.icon_upload = helpers.getImage("Upload", (45, 50))
        # Endregion - Variables globales a usar dentro del form

        # Region - Header del formulario.
        # =========================================================================
        # | Frame - Header completo
        # =========================================================================
        frameHeader = ctk.CTkFrame(
            self.ventana, 
            fg_color = self.color_backg, 
            corner_radius = 0
        )
        frameHeader.pack(side = "top", expand =False, fill = "both")

        # Region Right side Header
        # =========================================================================
        # | Frame Right side Header
        # =========================================================================

        # Configuración del titulo del formulario
        title = ctk.CTkLabel(
            frameHeader, 
            text = "PDF TO VOICE", 
            font = self.fontsTitle, 
            text_color = self.colorRed, 
            fg_color = self.color_backg, 
            pady = 10
        )
        title.pack(expand = True, fill = "both", pady = (10, 0))

        # Endregion Right side Header
        # Endregion - Header del formulario.

        # Region - Cuerpo principal del formulario
        # Region rightbody
        # =========================================================================
        # | frame form campos y botones
        # =========================================================================
        frame_form = ctk.CTkFrame(
            self.ventana, 
            fg_color = self.color_backg, 
            corner_radius = 0
        )
        frame_form.pack(expand = True, fill = "both")

        # =========================================================================
        # | Frame Left Body
        # =========================================================================
        frame_right = ctk.CTkFrame(
            frame_form, 
            fg_color = self.color_backg, 
            corner_radius = 0
        )
        frame_right.pack(side = "right", expand = True, fill = "both", padx = 100, pady = 10)
        frame_right.columnconfigure(0, weight = 1)

        frame_texto = ctk.CTkFrame(
            frame_right,
            fg_color = self.color_green,
            corner_radius = 5,
            width=400,
            height=200
        )
        frame_texto.grid(row = 8, column = 0, padx = 10, pady = (2, 5), sticky = "nsew")
        frame_texto.grid_propagate(False)

        # Etiqueta para indicar el cuadro de texto
        lbl_texto_leer = ctk.CTkLabel(
            frame_right, 
            text = "Texto a leer:", 
            font = self.textBold, 
            fg_color = self.color_backg
        )
        lbl_texto_leer.grid(row = 7, column = 0, padx = 10, pady = (0, 2), sticky = "w")

        # Cuadro de texto dentro del frame para simular el borde de color
        self.text_widget = ctk.CTkTextbox(
            frame_texto, 
            wrap= "word", 
            width = 40, 
            height = 200,
            fg_color = self.color_white,
            border_width = 0
        )
        self.text_widget.pack(padx = 2, pady = 2, fill = "both", expand = True)
        self.text_widget.configure(font = self.fontsText)

        # Organizar tamaño del cuadro de texto
        frame_fab = ctk.CTkFrame(
            frame_texto, 
            fg_color = self.color_white, 
            corner_radius = 0, 
            width = 45, 
            height = 50
        )
        frame_fab.place(relx = 0.01, rely = 0.98, anchor = "sw")

        # Boton flotante add
        self.boton_flotante_add = ctk.CTkButton(
            frame_fab, 
            image = self.icon_upload, 
            fg_color = self.color_white, 
            text = "",  
            hover_color = self.color_white,  
            cursor = "hand2",  
            border_width = 0, 
            command = helpers.open_pdf,
            width = self.icon_upload._size[0],
            height = self.icon_upload._size[1]
        )
        self.boton_flotante_add.pack(fill = "both", expand = True)

        # Boton flotante left page
        frame_btn_flotante_page = ctk.CTkFrame(
            frame_texto, 
            fg_color = self.color_white
        )
        frame_btn_flotante_page.place(relx = 1, rely = 1, anchor = "s", x =-28, y =-5)

        txt_num_page = ctk.CTkEntry(frame_btn_flotante_page, 
            width = 40, 
            justify = "center", 
            font = self.fontsText,
            border_width = 2,
            border_color = self.colorRed, 
        )
        txt_num_page.pack(fill = "x", ipady = 1)
        txt_num_page.insert(0, "1")

        # Configuración del frame de botones
        frame_btns = ctk.CTkFrame(frame_right, fg_color = self.color_backg, corner_radius = 0)
        frame_btns.grid(row = 11, column = 0, padx = 0, sticky = "ew", pady = (2, 5))

       

        # Botones
        # btn prev five
        btn_prev_f = ctk.CTkButton(
            frame_btns, 
            image = self.icon_prev_f, 
            fg_color = self.color_backg, 
            text = "", 
            hover_color = self.color_backg,
            cursor = "hand2",
            border_width = 0, 
            width = self.icon_prev_f._size[0],
            height = self.icon_prev_f._size[1]
        ) #command = Execute)
        btn_prev_f.pack(side = "left", padx =(160, 0), pady =(5, 0))

        # btn prev page
        btn_prev_page = ctk.CTkButton(
            frame_btns, 
            image = self.icon_prev_page, 
            fg_color = self.color_backg, 
            text = "",
            hover_color = self.color_backg,
            cursor = "hand2",
            border_width = 0,  
            width = self.icon_prev_page._size[0] ,
            height = self.icon_prev_page._size[1]
        ) #command = Execute)
        btn_prev_page.pack(side = "left", padx =(4, 0), pady =(5, 0))


        # btn play
        btn_play = ctk.CTkButton(
            frame_btns, 
            image = self.icon_play_pause, 
            fg_color = self.color_backg, 
            text = "",
            hover_color = self.color_backg,
            cursor = "hand2",
            border_width = 0, 
            width = self.icon_play_pause._size[0],
            height = self.icon_play_pause._size[1]
        ) #command = Execute)
        #btn_play.grid(row= 0, column=2, padx =(2, 0), pady =(9, 0))
        btn_play.pack(side = "left", padx =6, pady =(5, 0))


        btn_netx_page = ctk.CTkButton(
            frame_btns, 
            image = self.icon_next_page, 
            fg_color = self.color_backg, 
            text = "",
            hover_color = self.color_backg,
            cursor = "hand2",
            border_width = 0,  
            width = self.icon_next_page._size[0],
            height = self.icon_next_page._size[1]
        ) #command = Execute)
        btn_netx_page.pack(side = "left", padx =(0, 4), pady =(5, 0))  

        btn_next_f = ctk.CTkButton(
            frame_btns,
            image = self.icon_next_f,
            fg_color = self.color_backg,
            text = "",
            hover_color = self.color_backg,
            cursor = "hand2",
            border_width = 0, 
            width = self.icon_next_f._size[0],
            height = self.icon_next_f._size[1]
        ) #command = Execute)
        btn_next_f.pack(side = "left", padx =(0, 50), pady =(5, 0))

        # Boton flotante change speed
        boton_change_speed = ctk.CTkButton(
            frame_btns, 
            image = self.icon_speed, 
            fg_color = self.color_backg, 
            text = "",
            hover_color = self.color_backg,
            cursor = "hand2",
            border_width = 0, 
            width = self.icon_speed._size[0],
            height = self.icon_speed._size[1]
        )
        boton_change_speed.pack(side = "left", padx =(0, 40), pady =(0, 50))

        # Endregion - rightbody
        # Endregion  - Cuerpo principal del formulario
        self.ventana.mainloop()

# Metodo para inicializar el metodo ventana principal
if __name__ == '__main__':
    VentanaPrincipalForm()
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
        self.ventana.configure(fg_color='#FFF3F1')  # Fondo de la ventana
        self.ventana.resizable(width=False, height=False)  # Inhabilita el resize de la ventana por usuario
        helpers.centerWindows(self.ventana, 450, 860)  # height | width Se centra la ventana en pantalla

        # Endregion - Configuración de ventana (Form)

        # region - Variables globales a usar dentro del form
        # Colors
        self.colorRed = helpers.getValue("Colors", "red")
        self.color_white = helpers.getValue("Colors", "white")
        self.colorGreen = helpers.getValue("Colors", "green")
        self.color_backg = helpers.getValue("Colors", "backg")
        self.colorIcon = helpers.getValue("Colors", "icon")

        # Fonts
        self.fontsTitle = helpers.ValidateSource("title", 20)  # Devuelve una instancia de CTkFont
        self.fontsText = helpers.ValidateSource("text", 12)  # Devuelve una instancia de CTkFont
        self.textBold = helpers.ValidateSource("textBold", 12)  # Devuelve una instancia de CTkFont


        # Images
        self.icon_play_pause = helpers.getImage("PlayPause", (60, 60))
        self.icon_speed = helpers.getImage("Speed", (40, 30))
        self.icon_prev_page = helpers.getImage("PrevPage", (30, 30))
        self.icon_next_page = helpers.getImage("NextPage", (30, 30))
        self.icon_prev_f = helpers.getImage("PrevF", (50, 50))
        self.icon_next_f = helpers.getImage("NextF", (50, 50))
        self.icon_logo = helpers.getImage("Logo", (10, 15))
        self.icon_app = helpers.getImage("IconApp", (10, 15))
        self.icon_upload_light = helpers.getImage("UploadLight", (10, 15))
        self.icon_upload = helpers.getImage("Upload", (30, 35))
        # Endregion - Variables globales a usar dentro del form

        # Region - Header del formulario.
        # =========================================================================
        # | Frame - Header completo
        # =========================================================================
        frameHeader = ctk.CTkFrame(self.ventana, fg_color=self.color_backg, corner_radius=0)
        frameHeader.pack(side="top", expand=False, fill="both")

        # Region Right side Header
        # =========================================================================
        # | Frame Right side Header
        # =========================================================================

        # Configuración del titulo del formulario
        title = ctk.CTkLabel(frameHeader, text="PDF TO VOICE", font=self.fontsTitle, text_color=self.colorRed, fg_color=self.color_backg, pady=20)
        title.pack(expand=True, fill="both")

        # Endregion Right side Header
        # Endregion - Header del formulario.

        # Region - Cuerpo principal del formulario
        # Region rightbody
        # =========================================================================
        # | frame form campos y botones
        # =========================================================================
        frame_form = ctk.CTkFrame(self.ventana, fg_color=self.color_backg, corner_radius=0)
        frame_form.pack(expand=True, fill="both")

        # =========================================================================
        # | Frame Left Body
        # =========================================================================
        frame_right = ctk.CTkFrame(frame_form, fg_color=self.color_backg, corner_radius=0)
        frame_right.pack(side="right", expand=True, fill="both", padx=100, pady=10)
        frame_right.columnconfigure(0, weight=1)

        frame_texto = ctk.CTkFrame(frame_right, fg_color=self.colorGreen, corner_radius=5)
        frame_texto.grid(row=8, column=0, padx=10, pady=(2, 5), sticky="nsew")

        # Etiqueta para indicar el cuadro de texto
        lbl_texto_leer = ctk.CTkLabel(frame_right, text="Texto a leer:", font=self.fontsText, fg_color=self.color_backg)
        lbl_texto_leer.grid(row=7, column=0, padx=10, pady=(10, 2), sticky="w")

        # Cuadro de texto dentro del frame para simular el borde de color
        self.text_widget = ctk.CTkTextbox(frame_texto, wrap="word", width=40, height=10, fg_color=self.color_white,
                                          border_width=0)
        self.text_widget.pack(padx=2, pady=2, fill="both", expand=True)
        self.text_widget.configure(font=self.fontsText)  # Usa la instancia de CTkFont

        # Organizar tamaño del cuadro de texto
        frame_fab = ctk.CTkFrame(frame_texto, fg_color=self.color_white, corner_radius=0, width=10)
        frame_fab.place(relx=0.01, rely=0.98, anchor="sw")

        # Boton flotante add
        self.boton_flotante_add = ctk.CTkButton(frame_fab, image=self.icon_upload, fg_color=self.color_white, text="",
                                                width=30, height=30, command=helpers.open_pdf)
        self.boton_flotante_add.pack(fill="both", expand=True)

        # Boton flotante left page
        frame_btn_flotante_page = ctk.CTkFrame(frame_texto, fg_color=self.color_white, corner_radius=0, width=0.1,
                                               height=1)
        frame_btn_flotante_page.place(relx=1, rely=1, anchor="s", x=-35, y=-5)

        txt_num_page = ctk.CTkEntry(frame_btn_flotante_page, width=40, justify="center", font=self.fontsTitle)
        txt_num_page.pack(fill="x", ipady=1)
        txt_num_page.insert(0, "1")

        # Configuración del frame de botones
        frame_btns = ctk.CTkFrame(frame_right, fg_color=self.color_backg, corner_radius=0)
        frame_btns.grid(row=11, column=0, padx=0, sticky="ew", pady=(2, 5))

        # Configurar columnas para centrar botones
        frame_btns.grid_columnconfigure(0, weight=1)  # Espacio a la izquierda
        frame_btns.grid_columnconfigure(1, weight=1)
        frame_btns.grid_columnconfigure(2, weight=2)  # Botón Play centrado
        frame_btns.grid_columnconfigure(3, weight=1)
        frame_btns.grid_columnconfigure(4, weight=1)  # Espacio a la derecha

        # Botones
        btn_next_f = ctk.CTkButton(frame_btns, image=self.icon_next_f, fg_color=self.color_backg, text="", width=30,
                                   height=30) #command=Execute)
        btn_next_f.grid(row=11, column=4, padx=2, pady=0, sticky="ew")

        btn_netx_page = ctk.CTkButton(frame_btns, image=self.icon_next_page, fg_color=self.color_backg, text="", width=30,
                                      height=30) #command=Execute)
        btn_netx_page.grid(row=11, column=3, padx=2, pady=0, sticky="ew")

        btn_play = ctk.CTkButton(frame_btns, image=self.icon_play_pause, fg_color=self.color_backg, text="", width=30,
                                 height=30) #command=Execute)
        btn_play.grid(row=11, column=2, padx=2, pady=0, sticky="ew")  # Centrado

        btn_prev_page = ctk.CTkButton(frame_btns, image=self.icon_prev_page, fg_color=self.color_backg, text="", width=30,
                                      height=30) #command=Execute)
        btn_prev_page.grid(row=11, column=1, padx=2, pady=0, sticky="ew")

        btn_prev_f = ctk.CTkButton(frame_btns, image=self.icon_prev_f, fg_color=self.color_backg, text="", width=30,
                                   height=30) #command=Execute)
        btn_prev_f.grid(row=11, column=0, padx=2, pady=0, sticky="ew")

        # para el speed
        frame_speed = ctk.CTkFrame(frame_right, fg_color=self.color_backg, corner_radius=0, width=10)
        frame_speed.place(relx=0.99, rely=0.76, anchor="sw")

        # Boton flotante add
        self.boton_change_speed = ctk.CTkButton(frame_speed, image=self.icon_speed, fg_color=self.color_backg, text="",
                                                width=30, height=30) #command=Execute)
        self.boton_change_speed.pack(fill="both", expand=True)

        # Endregion - rightbody
        # Endregion  - Cuerpo principal del formulario
        self.ventana.mainloop()

# Metodo para inicializar el metodo ventana principal
if __name__ == '__main__':
    VentanaPrincipalForm()
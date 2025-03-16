# ===========================================================================
# Importaciones de clases y librerias necesarias en esta vista
# ===========================================================================
# Region - Importación de librerias y clases.
from controller.utils.Helpers import Helpers
# Endregion - Importación de librerias y clases.

# Region - Inicialización de clases para uso de metodos.
helper = Helpers()
# Endregion - Inicialización de clases para uso de metodos.

# Clase pivote para realizar la ejecución del bot. 
class Ejecucion:
    """
    Esta clase se encargará de enviar la información
    recolectada por el formulario a la base de datos
    de PgSQL, de manera que el bot de armado solo deba
    consultar la tabla asignada.
    """
    # Contructores e inicializadores de clase
    def __init__(self):
        """
        Constructor de la clase, se inicializarán las
        variables a utilizar dentro de la base de datos
        y se re asignaran sus valores luego de que se
        complete el formulario.
        """
        self.text = ""
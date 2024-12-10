class Profesor:
    def __init__(self, id, nombres, apellidos, numeroEmpleado, horasClase):
        # Valide que chaque champ est conforme aux attentes
        if not isinstance(id, int):
            raise ValueError("ID debe ser un número entero")
        if not nombres or not isinstance(nombres, str):
            raise ValueError("Nombres debe ser una cadena de caracteres")
        if not apellidos or not isinstance(apellidos, str):
            raise ValueError("Apellidos debe ser una cadena de caracteres")
        if not numeroEmpleado or not isinstance(numeroEmpleado, int):
            raise ValueError("Número de Empleado debe ser ser un número entero")
        if not isinstance(horasClase, (int, float)) or horasClase < 0:
            raise ValueError("Horas de Clase debe ser un número positivo")

        # Initialisation des attributs de l'objet
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.numeroEmpleado = numeroEmpleado
        self.horasClase = horasClase

    def to_dict(self):
        """Retourne les données du professeur sous forme de dictionnaire"""
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "numeroEmpleado": self.numeroEmpleado,
            "horasClase": self.horasClase
        }

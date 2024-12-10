class Alumno:
    def __init__(self, id, nombres, apellidos, matricula, promedio):
        # Valide que chaque champ est conforme aux attentes
        if not isinstance(id, int):
            raise ValueError("ID debe ser un número entero")
        if not nombres or not isinstance(nombres, str):
            raise ValueError("Nombres debe ser una cadena de caracteres")
        if not apellidos or not isinstance(apellidos, str):
            raise ValueError("Apellidos debe ser una cadena de caracteres")
        if not matricula or not isinstance(matricula, str):
            raise ValueError("Matrícula debe ser una cadena de caracteres")
        if not isinstance(promedio, (int, float)) or promedio < 0 or promedio > 10:
            raise ValueError("Promedio debe ser un número entre 0 y 10")

        # Initialisation des attributs de l'objet
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.matricula = matricula
        self.promedio = promedio

    def to_dict(self):
        """Retourne les données de l'étudiant sous forme de dictionnaire"""
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "matricula": self.matricula,
            "promedio": self.promedio
        }

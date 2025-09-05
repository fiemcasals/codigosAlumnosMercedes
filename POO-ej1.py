class Biologicos:
    def __init__(self, altura: float, peso: float) -> None:
        self.altura = altura
        # self._peso = 0
        # self._altura = 0
        self.peso = peso

    @property
    def peso(self) -> str:
        return f"{self._peso:.1f}kg"

    @peso.setter
    def peso(self, peso: float) -> None:
        self._peso = peso

    @property
    def altura(self):
        return f"{self._altura:.1f}m"

    @altura.setter
    def altura(self, altura: float):
        self._altura = altura


class Universidad:
    def __init__(self, nombre: str, departamento: str, fundacion: int):
        self.nombre = nombre
        self.departamento = departamento
        self.fundacion = fundacion


class Academicos:
    def __init__(self,
                 universidad: Universidad,
                 carrera: str,
                 promedio: float
                 ) -> None:
        self.universidad = universidad
        self.carrera = carrera
        self.promedio = promedio


class Persona(Biologicos, Academicos):
    def __init__(
            self,
            nombre: str,
            edad: int,
            altura: float,
            peso: float,
            universidad: Universidad,
            carrera: str,
            promedio: float,
            ) -> None:

        Biologicos.__init__(self, altura, peso)
        Academicos.__init__(self, universidad, carrera, promedio)
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        # s = f"Atributos:\nnombre:
        # {self.nombre}\naltura: {self.altura:.2f}\npeso: {self.peso}\ncarrera:
        # {self.carrera}\npromedio: {self.promedio}"

        return f"""
Atributos:
nombre: {self.nombre}
edad: {self.edad}
altura: {self.altura}
peso: {self.peso}
universidad: {self.universidad.nombre}
    departamento: {self.universidad.departamento}
    fundacion: {self.universidad.fundacion}
carrera: {self.carrera}
promedio: {self.promedio}
"""
# f"""
# Atributos:\n
# nombre: {self.nombre}\n
# altura: {self.altura:.2f}\n
# peso: {self.peso}\n
# carrera: {self.carrera}\n
# promedio: {self.promedio}
# """


def main() -> None:
    argumentos = {
            "nombre": "ramon",
            "altura": 1.50,
            "edad": 75,
            "peso": 100.0,
            "universidad": Universidad("UBA", "Ciencias Biologicas", 1849),
            "carrera": "Biologo",
            "promedio": 9.3,
            }

    pedrito = Persona(**argumentos)
    print(pedrito)


if __name__ == "__main__":
    main()


from __future__ import annotations #permite leer objetos que aun no estan definidos
from abc import ABC, abstractmethod
from typing import Optional

class Biologicos:
    def __init__(self, edad: int, altura: float, peso: int):
        self.edad = edad
        self.altura = altura
        self.peso = peso

class Academico:
    def __init__(self, carrera: str, promedio: float, materias_aprobadas: int):
        self.carrera = carrera
        self.promedio = promedio
        self.materias_aprobadas = materias_aprobadas



class Persona(Biologicos, Academico):
    def __init__(self, nombre: str, edad : int, altura: float, peso: int, carrera: str, promedio: int, materias_aprobadas: int, saludo: Saludos,email: Optional[str] = None ):
        Biologicos.__init__(self, edad, altura, peso)
        Academico.__init__(self, carrera, promedio, materias_aprobadas)
    
        self._nombre = " " 
        self.nombre = nombre
        self.email = email
        self.saludo = saludo
       
    @property
    def nombre(self) ->str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre) ->None:
        self._nombre = nombre

  # def presentacion(self) -> str:
    #     return f"mi nombre es {self.nombre}, mi edad es de {self.edad}, y tengo una altura de {self.altura}."
    
    def __str__(self) -> str:
        return f"mi nombre es {self.nombre}, tengo un peso de {self.peso}, tengo la edad de {self.edad}, mi altura es de {self.altura}, estudio la carrera {self.carrera}, tengo un promedio de {self.promedio}, con {self.materias_aprobadas} materias aprobadas"
  
    def __repr__(self) -> str:
        if self.email is None or self.email.strip() == "" or "@" not in self.email:
            return f" mi email no fue proporcionado"
        else:
         return f" mi email es  {self.email}"

class Saludos:
    def saludo(self):
        return "no estoy implementdo" 

class SaludoFormal(Saludos):
    def saludo(self):
        return "hola, que tal"

class SaludoInformal(Saludos):
    def saludo(self):
        return "hola"


class MovimientoPersona(ABC):
    @abstractmethod
    def mover(self) -> str:
        pass

class Caminar(MovimientoPersona):
    def mover (self) -> str:
        return "estoy caminando"
    
class Estudiar(MovimientoPersona):
    def mover (self) -> str:
        return "estoy estudiando"

class Correr(MovimientoPersona):
    def mover(self) -> str:
        return "estoy corriendo"

class FabricaPersona:

        REGISTRO ={

              "formal" : SaludoFormal,
              "informal" : SaludoInformal
        }
        @classmethod
        def crear(cls,tipo: str,nombre, edad, altura, peso, carrera, promedio,materias_aprobadas,email) -> Persona:
              tipo = tipo.lower()
              if tipo not in cls.REGISTRO:
               raise ValueError(f" tipo invalido: {tipo}")
              return Persona(nombre,edad, altura, peso, carrera, promedio, materias_aprobadas,cls.REGISTRO[tipo](),email) 

if __name__ == "__main__":
    caminar = Caminar()
    estudiar = Estudiar()
    correr = Correr()


    p = Persona("Maia", 19, 1.50, 50, "enfermero", 8, 10,SaludoFormal())
    print(p.saludo.saludo())
  
    
    persona_1 = FabricaPersona.crear("formal", "Maia", 19, 1.50, 50, "enfermero", 8, 10,"")   
    print(persona_1)
    print(persona_1.__repr__())

     # probar los movimientos
    print(caminar.mover())
    print(estudiar.mover())
    print(correr.mover())

 

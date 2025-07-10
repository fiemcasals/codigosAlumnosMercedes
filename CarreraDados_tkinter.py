#Juego de carrera de dados con tkinter, cada jugador lanza dos dados, en tres oportunidades cada uno y el que saque el mayor número gana.
import tkinter as tk
import random

class CarreraDados:
    def __init__(self, master):
        self.master = master
        self.master.title("Carrera de Dados")
        self.master.geometry("600x540")

        # Cargar imágenes de dados
        self.dado_imgs = [tk.PhotoImage(file=f"Dado{i}.png") for i in range(1, 7)]

        self.turnos_totales = 3
        self.turno_actual = 1
        self.jugador_actual = 1
        self.puntajes = {1: 0, 2: 0}

        # Crear frame principal para organizar en horizontal
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(expand=True, fill=tk.BOTH)

        # Frame jugador 1 (izquierda) con recuadro
        self.j1_frame = tk.LabelFrame(self.main_frame, text="Jugador 1", bd=3, relief=tk.GROOVE, labelanchor='n')
        self.j1_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=20, pady=10)
        self.jugador1_label = tk.Label(self.j1_frame, text="Puntaje: 0")
        self.jugador1_label.pack()
        self.dado1_img_label = tk.Label(self.j1_frame)
        self.dado1_img_label.pack()
        self.dado1_img_label2 = tk.Label(self.j1_frame)
        self.dado1_img_label2.pack()

        # Frame jugador 2 (derecha) con recuadro
        self.j2_frame = tk.LabelFrame(self.main_frame, text="Jugador 2", bd=3, relief=tk.GROOVE, labelanchor='n')
        self.j2_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=20, pady=10)
        self.jugador2_label = tk.Label(self.j2_frame, text="Puntaje: 0")
        self.jugador2_label.pack()
        self.dado2_img_label = tk.Label(self.j2_frame)
        self.dado2_img_label.pack()
        self.dado2_img_label2 = tk.Label(self.j2_frame)
        self.dado2_img_label2.pack()

        # Frame central para info y botones con recuadro
        self.center_frame = tk.LabelFrame(master, bd=3, relief=tk.GROOVE, width=560, height=120)
        self.center_frame.pack(pady=10)
        self.center_frame.pack_propagate(False)  # Mantiene el tamaño fijo
        self.info_label = tk.Label(self.center_frame, text="Turno 1 - Juega Jugador 1")
        self.info_label.pack(pady=(0, 2))
        self.resultado_label = tk.Label(self.center_frame, text="", font=("Arial", 32, "bold"), fg="blue")
        self.resultado_label.pack(pady=(0, 2))  # Muy poco espacio debajo
        # Botón para cada jugador
        self.lanzar_button_j1 = tk.Button(self.j1_frame, text="Lanzar Dados J1", command=lambda: self.animar_dados(1))
        self.lanzar_button_j1.pack(pady=10)
        self.lanzar_button_j2 = tk.Button(self.j2_frame, text="Lanzar Dados J2", command=lambda: self.animar_dados(2))
        self.lanzar_button_j2.pack(pady=10)
        self.lanzar_button_j1.config(state=tk.NORMAL)
        self.lanzar_button_j2.config(state=tk.DISABLED)
        self.reiniciar_button = tk.Button(self.center_frame, text="Jugar de nuevo", command=self.reiniciar_juego)
        self.reiniciar_button.pack(pady=(0, 2))
        self.reiniciar_button.pack_forget()

    def animar_dados(self, jugador):
        self.resultado_label.config(text="")
        self.lanzar_button_j1.config(state=tk.DISABLED)
        self.lanzar_button_j2.config(state=tk.DISABLED)
        self.anim_frames = 15  # 1.5 segundos, 100ms por frame
        self._animar(0, jugador)

    def _animar(self, frame, jugador):
        if frame < self.anim_frames:
            d1 = random.randint(1, 6)
            d2 = random.randint(1, 6)
            if jugador == 1:
                self.dado1_img_label.config(image=self.dado_imgs[d1-1])
                self.dado1_img_label2.config(image=self.dado_imgs[d2-1])
            else:
                self.dado2_img_label.config(image=self.dado_imgs[d1-1])
                self.dado2_img_label2.config(image=self.dado_imgs[d2-1])
            self.master.after(100, lambda: self._animar(frame+1, jugador))
        else:
            self.lanzar_dados(jugador)

    def lanzar_dados(self, jugador):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        suma = d1 + d2
        if jugador == 1:
            self.dado1_img_label.config(image=self.dado_imgs[d1-1])
            self.dado1_img_label2.config(image=self.dado_imgs[d2-1])
            self.puntajes[1] += suma
            self.jugador1_label.config(text=f"Jugador 1: {self.puntajes[1]}")
        else:
            self.dado2_img_label.config(image=self.dado_imgs[d1-1])
            self.dado2_img_label2.config(image=self.dado_imgs[d2-1])
            self.puntajes[2] += suma
            self.jugador2_label.config(text=f"Jugador 2: {self.puntajes[2]}")
        # Cambiar de jugador o turno
        if self.jugador_actual == 1 and jugador == 1:
            self.jugador_actual = 2
            self.info_label.config(text=f"Turno {self.turno_actual} - Juega Jugador 2")
            self.lanzar_button_j2.config(state=tk.NORMAL)
        elif self.jugador_actual == 2 and jugador == 2:
            self.jugador_actual = 1
            self.turno_actual += 1
            if self.turno_actual > self.turnos_totales:
                self.mostrar_resultado_final()
                return
            self.info_label.config(text=f"Turno {self.turno_actual} - Juega Jugador 1")
            self.lanzar_button_j1.config(state=tk.NORMAL)

    def mostrar_resultado_final(self):
        if self.puntajes[1] > self.puntajes[2]:
            resultado = "¡Jugador 1 gana la partida!"
        elif self.puntajes[2] > self.puntajes[1]:
            resultado = "¡Jugador 2 gana la partida!"
        else:
            resultado = "¡Empate en la partida!"
        self.info_label.config(text="Partida finalizada")
        self.resultado_label.config(text=resultado)
        self.lanzar_button_j1.config(state=tk.DISABLED)
        self.lanzar_button_j2.config(state=tk.DISABLED)
        self.reiniciar_button.pack()

    def reiniciar_juego(self):
        self.turno_actual = 1
        self.jugador_actual = 1
        self.puntajes = {1: 0, 2: 0}
        self.jugador1_label.config(text="Jugador 1: 0")
        self.jugador2_label.config(text="Jugador 2: 0")
        self.resultado_label.config(text="")
        self.info_label.config(text="Turno 1 - Juega Jugador 1")
        self.lanzar_button_j1.config(state=tk.NORMAL)
        self.lanzar_button_j2.config(state=tk.DISABLED)
        self.reiniciar_button.pack_forget()
        # Limpiar imágenes de dados
        self.dado1_img_label.config(image='')
        self.dado1_img_label2.config(image='')
        self.dado2_img_label.config(image='')
        self.dado2_img_label2.config(image='')

if __name__ == "__main__":
    root = tk.Tk()
    juego = CarreraDados(root)
    root.mainloop()

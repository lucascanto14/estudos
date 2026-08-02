import math
import random
import tkinter as tk


class AnalogDashboard:

  def __init__(self, root):
    self.root = root
    self.root.title("Painel de Telemetria Automotiva")
    self.root.geometry("900x520")
    self.root.configure(bg="#0f0f12")
    self.root.resizable(False, False)

    # Layout Principal: 2 Colunas para Manômetros e 1 Coluna para Dados Auxiliares
    self.root.columnconfigure((0, 1, 2), weight=1)
    self.root.rowconfigure(0, weight=1)

    # --- 1. TACÔMETRO (RPM - Analógico) ---
    self.canvas_rpm = tk.Canvas(
        self.root, bg="#18181c", highlightthickness=2, highlightbackground="#2a2a35"
    )
    self.canvas_rpm.grid(row=0, column=0, padx=15, pady=20, sticky="nsew")

    # --- 2. VELOCÍMETRO (Speed - Analógico) ---
    self.canvas_speed = tk.Canvas(
        self.root, bg="#18181c", highlightthickness=2, highlightbackground="#2a2a35"
    )
    self.canvas_speed.grid(row=0, column=1, padx=15, pady=20, sticky="nsew")

    # --- 3. PAINEL LATERAL (Temperaturas e Combustível) ---
    self.frame_aux = tk.Frame(self.root, bg="#0f0f12")
    self.frame_aux.grid(row=0, column=2, padx=15, pady=20, sticky="nsew")
    self.frame_aux.rowconfigure((0, 1, 2), weight=1)
    self.frame_aux.columnconfigure(0, weight=1)

    # Temp Motor
    self.card_temp_eng = tk.Frame(
        self.frame_aux,
        bg="#18181c",
        highlightthickness=1,
        highlightbackground="#2a2a35",
    )
    self.card_temp_eng.grid(row=0, column=0, sticky="nsew", pady=(0, 10))
    tk.Label(
        self.card_temp_eng,
        text="TEMP. MOTOR",
        font=("Segoe UI", 10, "bold"),
        fg="#8a8a9e",
        bg="#18181c",
    ).pack(pady=(15, 2))
    self.lbl_temp_eng = tk.Label(
        self.card_temp_eng,
        text="0 °C",
        font=("Segoe UI", 24, "bold"),
        fg="#ffffff",
        bg="#18181c",
    )
    self.lbl_temp_eng.pack()

    # Temp CVT
    self.card_temp_cvt = tk.Frame(
        self.frame_aux,
        bg="#18181c",
        highlightthickness=1,
        highlightbackground="#2a2a35",
    )
    self.card_temp_cvt.grid(row=1, column=0, sticky="nsew", pady=5)
    tk.Label(
        self.card_temp_cvt,
        text="TEMP. CVT",
        font=("Segoe UI", 10, "bold"),
        fg="#8a8a9e",
        bg="#18181c",
    ).pack(pady=(15, 2))
    self.lbl_temp_cvt = tk.Label(
        self.card_temp_cvt,
        text="0 °C",
        font=("Segoe UI", 24, "bold"),
        fg="#ffffff",
        bg="#18181c",
    )
    self.lbl_temp_cvt.pack()

    # Combustível
    self.card_fuel = tk.Frame(
        self.frame_aux,
        bg="#18181c",
        highlightthickness=1,
        highlightbackground="#2a2a35",
    )
    self.card_fuel.grid(row=2, column=0, sticky="nsew", pady=(10, 0))
    tk.Label(
        self.card_fuel,
        text="COMBUSTÍVEL",
        font=("Segoe UI", 10, "bold"),
        fg="#8a8a9e",
        bg="#18181c",
    ).pack(pady=(15, 2))
    self.lbl_fuel = tk.Label(
        self.card_fuel,
        text="0%",
        font=("Segoe UI", 24, "bold"),
        fg="#00e676",
        bg="#18181c",
    )
    self.lbl_fuel.pack()

    # Inicia o loop de animação
    self.update_data()

  def draw_gauge(
      self,
      canvas,
      title,
      val_text,
      unit,
      value,
      max_value,
      start_angle=135,
      end_angle=405,
  ):
    """Desenha um mostrador analógico circular com ponteiro no Canvas."""
    canvas.delete("all")
    w = canvas.winfo_width()
    h = canvas.winfo_height()

    if w <= 1 or h <= 1:
      return

    cx, cy = w / 2, h / 2 - 10
    radius = min(w, h) * 0.38

    # Arco de Fundo (Escala)
    canvas.create_arc(
        cx - radius,
        cy - radius,
        cx + radius,
        cy + radius,
        start=start_angle,
        extent=end_angle - start_angle,
        style=tk.ARC,
        outline="#2a2a35",
        width=12,
    )

    # Ângulo do Ponteiro
    pct = max(0, min(1, value / max_value))
    angle = start_angle + (pct * (end_angle - start_angle))
    rad = math.radians(angle)

    # Desenho do Ponteiro
    px = cx + (radius - 15) * math.cos(rad)
    py = cy - (radius - 15) * math.sin(rad)
    canvas.create_line(
        cx, cy, px, py, fill="#ff3366", width=4, capstyle=tk.ROUND
    )

    # Miolo do Ponteiro
    canvas.create_oval(
        cx - 8, cy - 8, cx + 8, cy + 8, fill="#ffffff", outline="#ff3366"
    )

    # Textos Principais
    canvas.create_text(
        cx, cy + 45, text=val_text, font=("Segoe UI", 32, "bold"), fill="#ffffff"
    )
    canvas.create_text(
        cx, cy + 75, text=unit, font=("Segoe UI", 10, "bold"), fill="#8a8a9e"
    )
    canvas.create_text(
        cx,
        cy - radius - 20,
        text=title,
        font=("Segoe UI", 12, "bold"),
        fill="#ffffff",
    )

  def update_data(self):
    # Simulação de valores (substitua com as chamadas OBD-II reais)
    speed = random.randint(40, 140)
    rpm = random.randint(1500, 5800)
    temp_motor = random.randint(88, 102)
    temp_cvt = random.randint(75, 92)
    fuel = 68

    # Desenhar medidores analógicos
    self.draw_gauge(
        self.canvas_rpm, "TACÔMETRO", f"{rpm}", "RPM", rpm, max_value=7000
    )
    self.draw_gauge(
        self.canvas_speed,
        "VELOCÍMETRO",
        f"{speed}",
        "KM/H",
        speed,
        max_value=220,
    )

    # Atualizar cartões digitais
    self.lbl_temp_eng.config(text=f"{temp_motor} °C")
    if temp_motor > 100:
      self.lbl_temp_eng.config(fg="#ff3366")  # Vermelho se aquecer
    else:
      self.lbl_temp_eng.config(fg="#ffffff")

    self.lbl_temp_cvt.config(text=f"{temp_cvt} °C")
    self.lbl_fuel.config(text=f"{fuel}%")

    # Atualiza a interface a cada 150 milissegundos (~6 a 7 quadros por segundo)
    self.root.after(150, self.update_data)


if __name__ == "__main__":
  root = tk.Tk()
  app = AnalogDashboard(root)
  root.mainloop()
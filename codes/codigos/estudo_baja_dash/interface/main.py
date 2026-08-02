
import random
import time
import customtkinter as ctk

# Se for usar conexão real no carro:
# import obd

# Configuração de temas da interface
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class CarDashboard(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title("Painel de Telemetria Automotiva")
    self.geometry("850x500")
    self.resizable(False, False)

    # Variavel de controle de simulação (True = dados simulados, False = OBD2 Real)
    self.simulation_mode = True

    # --- LAYOUT PRINCIPAL ---
    self.grid_columnconfigure((0, 1, 2), weight=1)
    self.grid_rowconfigure((0, 1), weight=1)

    # 1. VELOCIDADE (Grande / Destaque)
    self.card_speed = ctk.CTkFrame(self, corner_radius=15)
    self.card_speed.grid(
        row=0, column=0, columnspan=2, padx=15, pady=15, sticky="nsew"
    )

    ctk.CTkLabel(
        self.card_speed,
        text="VELOCIDADE",
        font=ctk.CTkFont(size=14, weight="bold"),
    ).pack(pady=(15, 0))
    self.lbl_speed = ctk.CTkLabel(
        self.card_speed, text="0", font=ctk.CTkFont(size=70, weight="bold")
    )
   # ✅ CORRETO (text_color dentro do CTkLabel)
    ctk.CTkLabel(
    self.card_speed,
    text="KM/H",
    font=ctk.CTkFont(size=12),
    text_color="gray",
    ).pack(pady=(0, 10))

    # 2. RPM (Com barra de progresso)
    self.card_rpm = ctk.CTkFrame(self, corner_radius=15)
    self.card_rpm.grid(row=0, column=2, padx=15, pady=15, sticky="nsew")

    ctk.CTkLabel(
        self.card_rpm, text="RPM", font=ctk.CTkFont(size=14, weight="bold")
    ).pack(pady=(15, 0))
    self.lbl_rpm = ctk.CTkLabel(
        self.card_rpm, text="0", font=ctk.CTkFont(size=36, weight="bold")
    )
    self.lbl_rpm.pack()

    self.bar_rpm = ctk.CTkProgressBar(self.card_rpm, orientation="horizontal")
    self.bar_rpm.pack(pady=15, padx=20, fill="x")
    self.bar_rpm.set(0)

    # 3. TEMPERATURA MOTOR
    self.card_temp_eng = ctk.CTkFrame(self, corner_radius=15)
    self.card_temp_eng.grid(row=1, column=0, padx=15, pady=15, sticky="nsew")

    ctk.CTkLabel(
        self.card_temp_eng,
        text="TEMP. MOTOR",
        font=ctk.CTkFont(size=12, weight="bold"),
    ).pack(pady=(15, 0))
    self.lbl_temp_eng = ctk.CTkLabel(
        self.card_temp_eng,
        text="0 °C",
        font=ctk.CTkFont(size=28, weight="bold"),
    )
    self.lbl_temp_eng.pack(pady=10)

    # 4. TEMPERATURA CVT
    self.card_temp_cvt = ctk.CTkFrame(self, corner_radius=15)
    self.card_temp_cvt.grid(row=1, column=1, padx=15, pady=15, sticky="nsew")

    ctk.CTkLabel(
        self.card_temp_cvt,
        text="TEMP. CVT",
        font=ctk.CTkFont(size=12, weight="bold"),
    ).pack(pady=(15, 0))
    self.lbl_temp_cvt = ctk.CTkLabel(
        self.card_temp_cvt,
        text="0 °C",
        font=ctk.CTkFont(size=28, weight="bold"),
    )
    self.lbl_temp_cvt.pack(pady=10)

    # 5. NÍVEL DE COMBUSTÍVEL
    self.card_fuel = ctk.CTkFrame(self, corner_radius=15)
    self.card_fuel.grid(row=1, column=2, padx=15, pady=15, sticky="nsew")

    ctk.CTkLabel(
        self.card_fuel,
        text="COMBUSTÍVEL",
        font=ctk.CTkFont(size=12, weight="bold"),
    ).pack(pady=(15, 0))
    self.lbl_fuel = ctk.CTkLabel(
        self.card_fuel, text="0%", font=ctk.CTkFont(size=28, weight="bold")
    )
    self.lbl_fuel.pack()

    self.bar_fuel = ctk.CTkProgressBar(self.card_fuel, orientation="horizontal")
    self.bar_fuel.pack(pady=10, padx=20, fill="x")
    self.bar_fuel.set(0)

    # Inicia o loop de atualização contínua
    self.update_telemetry()

  def update_telemetry(self):
    if self.simulation_mode:
      # Simulação de valores variando suavemente
      speed = random.randint(40, 110)
      rpm = random.randint(1500, 4500)
      temp_motor = random.randint(88, 96)
      temp_cvt = random.randint(75, 88)
      fuel = 65  # Porcentagem estática para teste

    else:
      # Exemplo de leitura real via OBD-II (Python-OBD)
      # speed = connection.query(obd.commands.SPEED).value.magnitude
      # rpm = connection.query(obd.commands.RPM).value.magnitude
      # temp_motor = connection.query(obd.commands.COOLANT_TEMP).value.magnitude
      pass

    # --- ATUALIZANDO OS COMPONENTES DA TELA ---
    self.lbl_speed.configure(text=f"{int(speed)}")

    self.lbl_rpm.configure(text=f"{int(rpm)}")
    self.bar_rpm.set(rpm / 7000.0)  # Escala proporcional de 0 a 7000 RPM

    self.lbl_temp_eng.configure(text=f"{int(temp_motor)} °C")
    # Alerta visual para motor quente (>100°C)
    if temp_motor > 100:
      self.lbl_temp_eng.configure(text_color="red")
    else:
      self.lbl_temp_eng.configure(text_color="white")

    self.lbl_temp_cvt.configure(text=f"{int(temp_cvt)} °C")

    self.lbl_fuel.configure(text=f"{int(fuel)}%")
    self.bar_fuel.set(fuel / 100.0)

    # Atualiza a interface a cada 200ms (5 vezes por segundo)
    self.after(200, self.update_telemetry)


if __name__ == "__main__":
  app = CarDashboard()
  app.mainloop()














#      ______
#   .-"      "-.        |) | |) /\ -+-/\ /_
#  /            \       |  | |\ |-| | |-| /
# |,  .-.  .-.  ,|               |\ /\  | |/\ | |]
# | )(_ /  \_ )( |               |/ \/  \/ |-||_|_
# |/     /\     \|           __
# (_     ^^     _)          |__)   =  === =
#  \__|IIIIII|__/           |   \ |-|  | |-|
#   | \IIIIII/ |            |__ / | ||_| | |
#   \          /
#    `--------`                                    
# =================================================================================
#   Criado por: vicky, Candiru, Papai Urso, Billy    \\ equipe da eletronica 2026
# =================================================================================

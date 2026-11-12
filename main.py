import tkinter as tk

# Inicialização da janela principal
root = tk.Tk()
root.title("Warth Menu - Rio Rise")
root.geometry("480x320")
root.configure(bg="#16161a")
root.resizable(False, False)

# Cores do Tema
COR_BG = "#16161a"
COR_SIDEBAR = "#1a1a1e"
COR_TEXTO = "#e0e0e0"
COR_MUTED = "#888892"
COR_VERMELHO = "#d32f2f"
COR_VERDE = "#2e7d32"

# ==========================================
# 1. BARRA LATERAL (Esquerda) - DECLARADA PRIMEIRO!
# ==========================================
sidebar = tk.Frame(root, bg=COR_SIDEBAR, width=105)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(
    sidebar,
    text="Warth Menu",
    bg=COR_SIDEBAR,
    fg="#ff3333",
    font=("Arial", 8, "bold"),
).pack(pady=6, padx=4, anchor="w")

# ==========================================
# 2. ÁREA DE CONTEÚDO COM ROLAGEM (Direita)
# ==========================================
container = tk.Frame(root, bg=COR_BG)
container.pack(side="right", fill="both", expand=True, padx=4, pady=4)

canvas = tk.Canvas(container, bg=COR_BG, highlightthickness=0)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
conteudo = tk.Frame(canvas, bg=COR_BG)

conteudo.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all")),
)
canvas.create_window((0, 0), window=conteudo, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


def limpar():
  for w in conteudo.winfo_children():
    w.destroy()
  canvas.yview_moveto(0)


def titulo(txt):
  tk.Label(
      conteudo,
      text=txt,
      bg=COR_BG,
      fg=COR_TEXTO,
      font=("Arial", 9, "bold"),
  ).pack(anchor="w", pady=(0, 4), padx=4)


def toggle(txt, ativo=False):
  f = tk.Frame(conteudo, bg=COR_BG)
  f.pack(fill="x", pady=2, padx=4)
  tk.Label(f, text=txt, bg=COR_BG, fg=COR_TEXTO, font=("Arial", 7)).pack(
      side="left"
  )

  btn = tk.Button(
      f,
      text="ON" if ativo else "OFF",
      bg=COR_VERDE if ativo else COR_VERMELHO,
      fg="white",
      width=5,
      relief="flat",
      font=("Arial", 7, "bold"),
  )

  def alternar():
    if btn["text"] == "OFF":
      btn.config(text="ON", bg=COR_VERDE)
    else:
      btn.config(text="OFF", bg=COR_VERMELHO)

  btn.config(command=alternar)
  btn.pack(side="right")


# ==========================================
# TODAS AS ABAS COMPLETAS
# ==========================================


def aba_menu():
  limpar()
  titulo("Menu")
  toggle("Esconder Ico...")
  toggle("Players Onli...", True)
  toggle("Status Conex...", True)
  toggle("Mostrar Chave")


def aba_camera():
  limpar()
  titulo("Camera")
  toggle("Aimbot")
  toggle("Aim Visible")
  toggle("Free Y")


def aba_visual():
  limpar()
  titulo("Visual")
  toggle("Esp Line")
  toggle("Esp Box")
  toggle("Esp Skeleton")
  toggle("Esp Name")
  toggle("Esp Aimbot")
  toggle("Esp Fov")


def aba_esp_config():
  limpar()
  titulo("ESP Config")
  tk.Label(
      conteudo,
      text="• Paleta de Cores (Line/Box)",
      bg=COR_BG,
      fg=COR_MUTED,
      font=("Arial", 7),
  ).pack(anchor="w", pady=2, padx=4)
  toggle("Skeleton Color", True)
  toggle("Box Color", True)


def aba_player():
  limpar()
  titulo("Player")
  toggle("Fake Lag")
  toggle("Invisible Sub")
  toggle("Infinity Sta...", True)
  toggle("NoClip")
  toggle("Free Cam")
  toggle("Anti Stun")


def aba_teleport():
  limpar()
  titulo("Teleport")
  for t in [
      "Set Fix Position",
      "Teleport to Fla",
      "Teleport to Map",
      "Teleport to CHP",
      "Tp Espantalho",
  ]:
    tk.Button(
        conteudo,
        text=t,
        bg="#222228",
        fg=COR_TEXTO,
        font=("Arial", 7),
        relief="flat",
        anchor="w",
        padx=4,
    ).pack(fill="x", pady=2, padx=4)


def aba_vehicle():
  limpar()
  titulo("Vehicle")
  toggle("Troll Crash")
  toggle("Car Power")
  toggle("Auto Drive")
  toggle("Godmode Veic...")
  toggle("Anti-Gravida...")
  toggle("Congelar")
  toggle("Super Pulo")


def aba_weapons():
  limpar()
  titulo("Weapons")
  for w in ["Give", "Spawn All", "Set Marker"]:
    tk.Button(
        conteudo,
        text=w,
        bg="#222228",
        fg=COR_TEXTO,
        font=("Arial", 7),
        relief="flat",
    ).pack(fill="x", pady=3, padx=4)


def aba_farm():
  limpar()
  titulo("Farm")
  toggle("Auto Mina")
  toggle("Auto Fazenda")
  toggle("Auto Ifood")
  toggle("Farm Mina")
  toggle("Farm Ifood")
  toggle("Fast Farm", True)
  toggle("Auto Reconnect", True)


def aba_world():
  limpar()
  titulo("World")
  toggle("Speed World")
  toggle("Anti Crash")


# ==========================================
# BOTÕES DA BARRA LATERAL
# ==========================================
botoes = [
    ("Menu", aba_menu),
    ("Camera", aba_camera),
    ("Visual", aba_visual),
    ("ESP Config", aba_esp_config),
    ("Player", aba_player),
    ("Teleport", aba_teleport),
    ("Vehicle", aba_vehicle),
    ("Weapons", aba_weapons),
    ("Farm", aba_farm),
    ("World", aba_world),
]

for nome, cmd in botoes:
  tk.Button(
      sidebar,
      text=nome,
      bg=COR_SIDEBAR,
      fg=COR_MUTED,
      activebackground="#2a2a32",
      activeforeground="white",
      relief="flat",
      anchor="w",
      font=("Arial", 7),
      padx=4,
      command=cmd,
  ).pack(fill="x", pady=1)

# Iniciar na aba Camera por padrão
aba_camera()

root.mainloop()

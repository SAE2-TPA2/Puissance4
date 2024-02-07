import customtkinter as ctk
from CTkColorPicker import *


class Settings(ctk.CTk):
    def __init__(self, players_type):
        super().__init__()

        self.color2 = "#ff0000"
        self.color1 = "#0000ff"
        self.name1 = players_type.split("vs")[0]
        self.name2 = players_type.split("vs")[1]


        self.title("Puissance 4")
        self.geometry("400x600")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")


        self.create_widgets(players_type)

        self.mainloop()

    def create_widgets(self, players_type):
        self.title_label = ctk.CTkLabel(self, text="Paramétrage", font=("Arial", 24))
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

        j1, j2 = players_type.split("vs")

        # Horizontal line
        hr1 = ctk.CTkFrame(self, height=1, bg_color="grey")
        hr1.grid(row=1, column=0, columnspan=2, sticky="ew")

        # Player 1 section
        self.player_1_label = ctk.CTkLabel(self, text=f"Paramètres {j1} 1", font=("Arial", 18))
        self.player_1_label.grid(row=2, column=0, columnspan=2)

        if "IA" not in j1:
            self.player_1_name_label = ctk.CTkLabel(self, text="Nom du joueur 1:")
            self.player_1_name_label.grid(row=3, column=0)
            self.player_1_entry = ctk.CTkEntry(self)
            self.player_1_entry.grid(row=3, column=1, sticky="ew", padx=10)

        self.player_1_color_button = ctk.CTkButton(self, text="Choisir une couleur de pion"
                                                       , command=lambda: self.choose_color_1())
        self.player_1_color_button.grid(row=4, column=0)

        self.player_1_color_display = ctk.CTkLabel(self, width=2, height=1, bg_color="red", text="                  ")
        self.player_1_color_display.grid(row=4, column=1)


        # Horizontal line
        hr2 = ctk.CTkFrame(self, height=1, bg_color="grey")
        hr2.grid(row=5, column=0, columnspan=2, sticky="ew")

        # Player 2 section
        if "IA" in j2:
            self.player_2_label = ctk.CTkLabel(self, text=f"Paramètres Ordinateur", font=("Arial", 18))
            self.player_2_label.grid(row=6, column=0, columnspan=2)
        else:
            self.player_2_label = ctk.CTkLabel(self, text=f"Paramètres {j2} 2", font=("Arial", 18))
            self.player_2_label.grid(row=6, column=0, columnspan=2)

        if "IA" not in j2:
            self.player_2_name_label = ctk.CTkLabel(self, text="Nom du joueur 2:")
            self.player_2_name_label.grid(row=7, column=0, sticky="ew")
            self.player_2_entry = ctk.CTkEntry(self)
            self.player_2_entry.grid(row=7, column=1, sticky="ew", padx=10)

        self.player_2_color_button = ctk.CTkButton(self, text="Choisir une couleur de pion"
                                                   , command=lambda: self.choose_color_2())
        self.player_2_color_button.grid(row=8, column=0)

        self.player_2_color_display = ctk.CTkLabel(self, width=2, height=1, bg_color="blue", text="                  ")
        self.player_2_color_display.grid(row=8, column=1)


        # Horizontal line
        hr3 = ctk.CTkFrame(self, height=1, bg_color="grey")
        hr3.grid(row=9, column=0, columnspan=2, sticky="ew")

        self.start_game_button = ctk.CTkButton(self, text="Commencer le jeu", command=self.start_game)
        self.start_game_button.grid(row=10, column=0, columnspan=2)

        # Add padding to the grid
        for i in range(2):
            self.grid_columnconfigure(i, weight=1, pad=10)
        for i in range(11):
            self.grid_rowconfigure(i, weight=1, pad=10)

    def choose_color_1(self):
        pick_color = AskColor()  # open the color picker
        self.color1 = pick_color.get()  # get the color string
        self.player_1_color_display.configure(bg_color=self.color1)

    def choose_color_2(self):
        pick_color = AskColor()  # open the color picker
        self.color2 = pick_color.get()  # get the color string
        self.player_2_color_display.configure(bg_color=self.color2)

    def start_game(self):
        if "IA" not in self.name1:
            self.name1 = self.player_1_entry.get()
        if "IA" not in self.name2:
            self.name2 = self.player_2_entry.get()

        print("Nom Joueur 1:", self.name1)
        print("Nom Joueur 2:", self.name2)

        print("Couleur Joueur 1:", self.color1)
        print("Couleur Joueur 2:", self.color2)
        self.destroy()



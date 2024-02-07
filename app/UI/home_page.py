import customtkinter as ctk

from App.UI.settings_page import Settings


class home(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Puissance 4")
        self.geometry("300x300")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")

        self.create_widgets()

    def player_vs_player(self):
        self.destroy()
        settings = Settings("Joueur vs Joueur")
        settings.mainloop()

    def player_vs_ai(self):
        self.destroy()
        settings = Settings("Joueur vs IA")
        settings.mainloop()

    def ai_vs_ai(self):
        self.destroy()
        settings = Settings("IA vs IA")
        settings.mainloop()


    def create_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Puissance 4", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.player_vs_player_button = ctk.CTkButton(self, text="Joueur vs Joueur", command=self.player_vs_player)
        self.player_vs_player_button.pack(pady=10)

        self.player_vs_ai_button = ctk.CTkButton(self, text="Joueur vs AI", command=self.player_vs_ai)
        self.player_vs_ai_button.pack(pady=10)

        self.ai_vs_ai_button = ctk.CTkButton(self, text="AI vs AI", command=self.ai_vs_ai)
        self.ai_vs_ai_button.pack(pady=10)

        self.quit_button = ctk.CTkButton(self, text="Quitter", command=self.quit)
        self.quit_button.pack(pady=10)


if __name__ == "__main__":
    window = home()
    window.mainloop()

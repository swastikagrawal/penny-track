import customtkinter as ctk
import sys
import os
from PIL import Image, ImageTk
from database import initialize_db
from seed import seed_categories
from ui.main_view import MainView

def get_asset_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "assets", filename)
    return os.path.join("assets", filename)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Penny Track")
        self.geometry("1000x650")
        self.resizable(False, False)

        icon_image = Image.open(get_asset_path("icon.png"))
        icon_photo = ImageTk.PhotoImage(icon_image)
        self.wm_iconphoto(True, icon_photo)
        self.after(200, lambda: self.iconbitmap(get_asset_path("icon.ico")))

        initialize_db()
        seed_categories()

        MainView(self).pack(fill="both", expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
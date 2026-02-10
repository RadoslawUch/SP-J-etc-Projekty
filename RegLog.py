import tkinter as tk
from tkinter import messagebox
import json
import os
import time

DB_FILE = "users.json"

def load_users():
    if not os.path.exists(DB_FILE): return {}
    with open(DB_FILE, "r") as f: return json.load(f)

def save_user(username, password):
    users = load_users()
    users[username] = password
    with open(DB_FILE, "w") as f: json.dump(users, f)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System Pracowniczy v2.0")
        self.geometry("400x500")
        self.start_time = None
        self.working = False
        
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.show_login_screen()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_screen()
        frame = tk.Frame(self.container)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(frame, text="LOGOWANIE", font=("Arial", 14, "bold")).pack(pady=10)
        self.entry_user = tk.Entry(frame, justify='center')
        self.entry_user.insert(0, "Login")
        self.entry_user.pack(pady=5)
        self.entry_pass = tk.Entry(frame, show="*", justify='center')
        self.entry_pass.pack(pady=5)

        tk.Button(frame, text="Zaloguj", width=15, bg="#4CAF50", fg="white", command=self.handle_login).pack(pady=10)
        tk.Button(frame, text="Rejestracja", width=15, command=self.handle_register).pack()

    def show_user_panel(self, username):
        self.clear_screen()
        self.username = username
        
        tk.Label(self.container, text=f"Pracownik: {username}", fg="gray").pack(anchor="e", padx=10, pady=5)
        
        # Panel danych
        data_frame = tk.LabelFrame(self.container, text="Profil", padx=10, pady=10)
        data_frame.pack(fill="x", padx=20, pady=10)
        tk.Label(data_frame, text="Status:").grid(row=0, column=0, sticky="w")
        self.status_label = tk.Label(data_frame, text="Gotowy do pracy", fg="blue", font=("Arial", 9, "bold"))
        self.status_label.grid(row=0, column=1)

        # Licznik czasu
        self.timer_label = tk.Label(self.container, text="00:00:00", font=("Courier", 30))
        self.timer_label.pack(pady=20)

        # Przycisk Akcji (PRACUJ / ZAKOŃCZ)
        self.work_btn = tk.Button(self.container, text="PRACUJ", font=("Arial", 16, "bold"),
                                 bg="#2196F3", fg="white", width=15, height=2,
                                 command=self.toggle_work)
        self.work_btn.pack(pady=10)

        tk.Button(self.container, text="Wyloguj", command=self.show_login_screen).pack(side="bottom", pady=20)

    def update_timer(self):
        if self.working:
            elapsed = int(time.time() - self.start_time)
            mins, secs = divmod(elapsed, 60)
            hrs, mins = divmod(mins, 60)
            self.timer_label.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
            self.after(1000, self.update_timer)

    def toggle_work(self):
        if not self.working:
            # Start pracy
            self.working = True
            self.start_time = time.time()
            self.work_btn.config(text="ZAKOŃCZ PRACĘ", bg="#f44336")
            self.status_label.config(text="W TRAKCIE PRACY", fg="red")
            self.update_timer()
        else:
            # Koniec pracy
            self.working = False
            end_time = time.time()
            total_seconds = int(end_time - self.start_time)
            
            self.work_btn.config(text="PRACUJ", bg="#2196F3")
            self.status_label.config(text="ZAKOŃCZONO", fg="green")
            
            mins, secs = divmod(total_seconds, 60)
            messagebox.showinfo("Raport", f"Praca zakończona!\nCzas trwania: {mins} min {secs} sek.")
            self.timer_label.config(text="00:00:00")

    def handle_login(self):
        u, p = self.entry_user.get(), self.entry_pass.get()
        users = load_users()
        if u in users and users[u] == p:
            self.show_user_panel(u)
        else:
            messagebox.showerror("Błąd", "Niepoprawne dane!")

    def handle_register(self):
        u, p = self.entry_user.get(), self.entry_pass.get()
        if not u or not p or u == "Login":
            messagebox.showwarning("Błąd", "Wprowadź poprawne dane!")
            return
        users = load_users()
        if u in users:
            messagebox.showerror("Błąd", "Użytkownik istnieje!")
        else:
            save_user(u, p)
            messagebox.showinfo("Sukces", "Zarejestrowano!")

if __name__ == "__main__":
    app = App()
    app.mainloop()

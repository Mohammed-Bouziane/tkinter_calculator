'''##                                                                                                   ##'''
#!                                              By: Mohamed Bouziane


# Importer le module tkinter
import tkinter as tk


# création de la classe Calculatrice, héritant de la classe tk.Tk et qui représente la fenêtre principale de l'application
class Calculatrice(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice DD101 - 2022/2023")
        self.geometry("400x400")
        self.resizable(False, False)
        self.configure(bg='#cfc7ab')
        self.iconbitmap("icone/Calculator.ico")

        # Création d'un conteneur pour tous les widgets
        self.container = tk.Frame(self, bg='#FFFFFF', borderwidth=1, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#ccc")
        self.container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, anchor="center")

        # Titre de la fenêtre
        self.label = tk.Label(self.container, text="Calculatrice", font=("Arial", 18), fg='#000000', bg='#FFFFFF')
        self.label.place(x=200, y=30, anchor="center")

        # Créer un cadre pour les widgets label1, entry1, label2 et entry2
        self.input_frame = tk.Frame(self.container, bg='#FFFFFF', borderwidth=0, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#ccc")
        self.input_frame.place(x=40, y=100, width=320, height=80)

        # Définir le padding pour toutes les cellules de la grille
        self.input_frame.grid_rowconfigure(1, minsize=40, weight=1)
    
        # Label et entrée pour le premier nombre
        self.label1 = tk.Label(self.input_frame, text="Premier nombre :", fg='#000000', bg='#FFFFFF')
        self.label1.grid(row=0, column=0, sticky="w", padx=(10,0), pady=5)

        self.entry1 = tk.Entry(self.input_frame, width=15, font=("Arial", 12), bg='#FFFFFF', fg='#000000', borderwidth=0, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#ccc")
        self.entry1.grid(row=0, column=1, sticky="e", padx=(0,10), pady=5)

        # Label et entrée pour le deuxième nombre
        self.label2 = tk.Label(self.input_frame, text="Deuxième nombre :", fg='#000000', bg='#FFFFFF')
        self.label2.grid(row=1, column=0, sticky="w", padx=(10,0), pady=5)

        self.entry2 = tk.Entry(self.input_frame, width=15, font=("Arial", 12), bg='#FFFFFF', fg='#000000', borderwidth=0, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#ccc")
        self.entry2.grid(row=1, column=1, sticky="e", padx=(0,10), pady=5)

        # Conteneur pour les boutons d'opération
        self.operation_frame = tk.Frame(self.container, bg='#FFFFFF', borderwidth=0, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#ccc")
        self.operation_frame.place(x=40, y=200, width=320, height=60)
        
        # Label pour demander à l'utilisateur de choisir un opérateur
        self.operator_label = tk.Label(self.operation_frame, text="Choisissez un opérateur :", fg='#000000', bg='#FFFFFF')
        self.operator_label.grid(row=0, column=0, padx=(10,0), pady=10)
        
        # Boutons pour les opérations
        # Chaque bouton appelle la fonction calculate() avec un opérateur différent grâce à la fonction anonyme lambda
        self.addition_button = tk.Button(self.operation_frame, text="+", command=lambda: self.calculate("+"), bg='#11e852', fg='#FFFFFF', font=("Arial", 12), borderwidth=0)
        self.addition_button.grid(row=0, column=1, padx=10, pady=10)
        self.subtraction_button = tk.Button(self.operation_frame, text="-", command=lambda: self.calculate("-"), bg='#fac310', fg='#FFFFFF', font=("Arial", 12), borderwidth=0)
        self.subtraction_button.grid(row=0, column=2, padx=10, pady=10)
        self.multiplication_button = tk.Button(self.operation_frame, text="x", command=lambda: self.calculate("x"), bg='#6fa5fc', fg='#FFFFFF', font=("Arial", 12), borderwidth=0)
        self.multiplication_button.grid(row=0, column=3, padx=10, pady=10)
        self.division_button = tk.Button(self.operation_frame, text="/", command=lambda: self.calculate("/"), bg='#767265', fg='#FFFFFF', font=("Arial", 12), borderwidth=0)
        self.division_button.grid(row=0, column=4, padx=10, pady=10)

        # Frame pour le résultat
        self.result_frame = tk.Frame(self.container, bg='#FFFFFF', width=200, height=50, borderwidth=0, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#ccc")
        self.result_frame.place(x=40, y=290, anchor="nw", width=320, height=50)

        # Label pour afficher le résultat
        self.result_label = tk.Label(self.result_frame, text="Résultat :", fg='#000000', bg='#FFFFFF', font=("Arial", 12))
        self.result_label.pack(side=tk.LEFT, padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Entrée pour le résultat
        self.result_entry = tk.Entry(self.result_frame, width=11, font=("Arial", 16), bg='#FFFFFF', fg='#000000', borderwidth=0, highlightthickness=1, highlightbackground="#ccc", highlightcolor="#ccc")
        self.result_entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.result_entry.config(state='disabled')  # désactiver l'entrée

        # Label pour afficher les messages d'erreur
        self.error_label = tk.Label(self.container, text="", fg='red', bg='#FFFFFF', font=("Arial", 10))
        self.error_label.place(x=70, y=340, anchor="nw", width=280, height=20,)

    # la fonction calculate() prend un opérateur en paramètre
    def calculate(self, operator):
        val1 = self.entry1.get()
        val2 = self.entry2.get()
        if val1 and val2:  # Vérifie que les entrées ne sont pas vides
            try:
                if operator == "+":
                    result = float(val1) + float(val2)
                elif operator == "-":
                    result = float(val1) - float(val2)
                elif operator == "x":
                    result = float(val1) * float(val2)
                else:
                    result = round((float(val1) / float(val2)),2)
                self.result_entry.config(state='normal')  # activer l'entrée
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, result)
                self.result_entry.config(state='disabled')  # désactiver l'entrée
                self.error_label.configure(text="")
            except ValueError:
                self.error_label.configure(text="Les entrées doivent être des nombres entiers.")
            except ZeroDivisionError:
                self.error_label.configure(text="La division par zéro est impossible.")
        else:
            self.error_label.configure(text="Les entrées ne doivent pas être vides.")

# Créer une instance de la classe Calculatrice
if __name__ == "__main__":
    app = Calculatrice()
    app.mainloop()
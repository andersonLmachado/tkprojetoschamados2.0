from tkinter import *
from customtkinter import *
from tkinter import Tk, Button, Label

class RegistroAtendimentos2(CTk):
    def __init__(self):
        super().__init__()

        self.title("Registro de Atendimentos")
        self.geometry("880x750")
        
        self.frametitle = CTkFrame(master=self, border_width=2)
        self.frametitle.pack(expand=True, anchor="center")
        self.labeltitle = CTkLabel(master=self.frametitle, text="Registro de Atendimentos", font=("Arial", 18, "bold"))

        set_default_color_theme("blue")
        
        # Criar os frames da aplicação
        
        self.frame = CTkFrame(master=self, border_width=2)
        
        self.frame.pack(expand=True, anchor="w")
        
        self.label_suzano = CTkLabel(master=self.frame, text="Suzano", font=("Arial", 18, "bold"))
        
        #Botões Suzano
        
        self.btn_suzano1 = CTkButton(master=self.frame, text="Atividade 1")
        
        self.label_suzano1 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano2 = CTkButton(master=self.frame, text="Atividade 2")
        
        self.label_suzano2 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano3 = CTkButton(master=self.frame, text="Atividade 3")
        
        self.label_suzano3 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano4 = CTkButton(master=self.frame, text="Atividade 4")
        
        self.label_suzano4 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano5 = CTkButton(master=self.frame, text="Atividade 5")
        
        self.label_suzano5 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano6 = CTkButton(master=self.frame, text="Atividade 6")
        
        self.label_suzano6 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano7 = CTkButton(master=self.frame, text="Atividade 7")
        
        self.label_suzano7 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano8 = CTkButton(master=self.frame, text="Atividade 8")
        
        self.label_suzano8 = CTkLabel(master=self.frame, text="0")
        
        #Contadores Suzano
        
        self.contador_suzano1 = 0
        self.contador_suzano2 = 0
        self.contador_suzano3 = 0
        self.contador_suzano4 = 0
        self.contador_suzano5 = 0
        self.contador_suzano6 = 0
        self.contador_suzano7 = 0
        self.contador_suzano8 = 0
        
        #Posições
        
        self.labeltitle.pack(pady=10, padx=10)
        
        self.label_suzano.grid(row=0, column=0, pady=10, padx=10) 
        
        self.btn_suzano1.grid(row=1,column=0, pady=10, padx=10)
        self.label_suzano1.grid(row=1,column=1, pady=10, padx=10)
        
        self.btn_suzano2.grid(row=2,column=0, pady=10, padx=10)
        self.label_suzano2.grid(row=2,column=1, pady=10, padx=10)
        
        self.btn_suzano3.grid(row=3,column=0, pady=10, padx=10)
        self.label_suzano3.grid(row=3,column=1, pady=10, padx=10)
        
        self.btn_suzano4.grid(row=4,column=0, pady=10, padx=10)
        self.label_suzano4.grid(row=4,column=1, pady=10, padx=10)
        
        self.btn_suzano5.grid(row=5,column=0, pady=10, padx=10)
        self.label_suzano5.grid(row=5,column=1, pady=10, padx=10)
        
        self.btn_suzano6.grid(row=6,column=0, pady=10, padx=10)
        self.label_suzano6.grid(row=6,column=1, pady=10, padx=10)
        
        self.btn_suzano7.grid(row=7,column=0, pady=10, padx=10)
        self.label_suzano7.grid(row=7,column=1, pady=10, padx=10)
        
        self.btn_suzano8.grid(row=8,column=0, pady=10, padx=10)
        self.label_suzano8.grid(row=8,column=1, pady=10, padx=10)
        
    def Suzanocontador1(self, event):
        self.contador_suzano1 += 1
        self.label_suzano1.config(text=f"{self.contador_suzano1}")
        
    def Suzanocontador2(self, event):
        self.contador_suzano2 += 1
        self.label_suzano2.config(text=f"{self.contador_suzano2}")
        
    def Suzanocontador3(self, event):
        self.contador_suzano3 += 1
        self.label_suzano3.config(text=f"{self.contador_suzano3}")
        
    def Suzanocontador4(self, event):
        self.contador_suzano4 += 1
        self.label_suzano4.config(text=f"{self.contador_suzano4}")
        
    def Suzanocontador5(self, event):
        self.contador_suzano5 += 1
        self.label_suzano5.config(text=f"{self.contador_suzano5}")
        
    def Suzanocontador6(self, event):
        self.contador_suzano6 += 1
        self.label_suzano6.config(text=f"{self.contador_suzano6}")
        
    def Suzanocontador7(self, event):
        self.contador_suzano7 += 1
        self.label_suzano7.config(text=f"{self.contador_suzano7}")
        
    def Suzanocontador8(self, event):
        self.contador_suzano8 += 1
        self.label_suzano8.config(text=f"{self.contador_suzano8}")
        
        self.btn_suzano1.bind("<Button-1>", self.Suzanocontador1)
        self.btn_suzano2.bind("<Button-1>", self.Suzanocontador2)
        self.btn_suzano3.bind("<Button-1>", self.Suzanocontador3)
        self.btn_suzano4.bind("<Button-1>", self.Suzanocontador4)
        self.btn_suzano5.bind("<Button-1>", self.Suzanocontador5)
        self.btn_suzano6.bind("<Button-1>", self.Suzanocontador6)
        self.btn_suzano7.bind("<Button-1>", self.Suzanocontador7)
        self.btn_suzano8.bind("<Button-1>", self.Suzanocontador8)

app = RegistroAtendimentos2()
app.mainloop()

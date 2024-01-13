from tkinter import *
from customtkinter import *
from PIL import Image


class RegistroAtendimentos2(CTk):
    def __init__(self):
        super().__init__()

        self.title("Registro de Atendimentos")
        self.geometry("880x750")
        
        self.frametitle = CTkFrame(master=self, border_width=2)
        self.frametitle.pack(expand=True, anchor="center")
        self.labeltitle = CTkLabel(master=self.frametitle, text="Registro de Atendimentos", font=("Arial", 18, "bold"))
        
        imglixo = Image.open("lixo.png")

        set_default_color_theme("green")
        
        #Contadores Suzano
        
        self.contador_suzano1 = 0
        self.contador_suzano2 = 0
        self.contador_suzano3 = 0
        self.contador_suzano4 = 0
        self.contador_suzano5 = 0
        self.contador_suzano6 = 0
        self.contador_suzano7 = 0
        self.contador_suzano8 = 0
        
        # Criar os frames da aplicação
        
        self.frame = CTkFrame(master=self, border_width=2)
        self.frame.pack(expand=True, anchor="w")
        
        #Label Suzano
        self.label_suzano = CTkLabel(master=self.frame, text="Suzano", font=("Arial", 18, "bold"))
        
        #Botões Suzano
        
        self.btn_suzano1 = CTkButton(master=self.frame, text="Cadastro Omnilink", command=self.Suzanocontador1)
        self.label_suzano1 = CTkLabel(master=self.frame, text="0")
        self.btn_suzano1reduzir = CTkButton(master=self.frame, command=self.Suzanocontador1reduzir, width=15, height=1,image=CTkImage(dark_image=imglixo, light_image=imglixo))
        
        self.btn_suzano2 = CTkButton(master=self.frame, text="Verficar Espelhamento", command=self.Suzanocontador2)
        self.label_suzano2 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano3 = CTkButton(master=self.frame, text="Trocar Rastreador", command=self.Suzanocontador3)
        self.label_suzano3 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano4 = CTkButton(master=self.frame, text="Voltar para PNA", command=self.Suzanocontador4)
        self.label_suzano4 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano5 = CTkButton(master=self.frame, text="Treinamento", command=self.Suzanocontador5)
        self.label_suzano5 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano6 = CTkButton(master=self.frame, text="Cadastro", command=self.Suzanocontador6)
        self.label_suzano6 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano7 = CTkButton(master=self.frame, text="Dúvidas", command=self.Suzanocontador7)
        self.label_suzano7 = CTkLabel(master=self.frame, text="0")
        
        self.btn_suzano8 = CTkButton(master=self.frame, text="Outros", command=self.Suzanocontador8)
        self.label_suzano8 = CTkLabel(master=self.frame, text="0")
        
        #Posições
        
        self.labeltitle.pack(pady=10, padx=10)
        
        self.label_suzano.grid(row=0, column=0, pady=10, padx=10) 
        
        self.btn_suzano1.grid(row=1,column=0, pady=10, padx=10)
        self.label_suzano1.grid(row=1,column=1, pady=10, padx=10)
        self.btn_suzano1reduzir.grid(row=1,column=2, pady=10, padx=10)
        
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
        
    def Suzanocontador1(self):
        self.contador_suzano1 += 1
        self.label_suzano1.configure(text=f"{self.contador_suzano1}")
        
    def Suzanocontador2(self):
        self.contador_suzano2 += 1
        self.label_suzano2.configure(text=f"{self.contador_suzano2}")
        
    def Suzanocontador3(self):
        self.contador_suzano3 += 1
        self.label_suzano3.configure(text=f"{self.contador_suzano3}")
        
    def Suzanocontador4(self):
        self.contador_suzano4 += 1
        self.label_suzano4.configure(text=f"{self.contador_suzano4}")
        
    def Suzanocontador5(self):
        self.contador_suzano5 += 1
        self.label_suzano5.configure(text=f"{self.contador_suzano5}")
        
    def Suzanocontador6(self):
        self.contador_suzano6 += 1
        self.label_suzano6.configure(text=f"{self.contador_suzano6}")
        
    def Suzanocontador7(self):
        self.contador_suzano7 += 1
        self.label_suzano7.configure(text=f"{self.contador_suzano7}")
        
    def Suzanocontador8(self):
        self.contador_suzano8 += 1
        self.label_suzano8.configure(text=f"{self.contador_suzano8}")
    
    #Funções para reduzir o contador
    def Suzanocontador1reduzir(self):
        if self.contador_suzano1 > 0:
            self.contador_suzano1 -= 1
            self.label_suzano1.configure(text=f"{self.contador_suzano1}")

if __name__ == "__main__":
    app = RegistroAtendimentos2()
    app.mainloop()

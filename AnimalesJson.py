import json 
Conocimiento = False

with open ("animales.json", "r") as read_file:
    data = json.load(read_file)
    conocimiento = data['conocimiento']
    

        
    def Checar(animal,verbo,cosa):
        cambio=animal
        cambio2=animal
        valor=False
        for t in conocimiento:
            if animal == t[0] and verbo == "tiene" and cosa==t[2]:
                valor=True
            if animal == t[0] and verbo == "vive" and cosa==t[2]:
                valor=True
            if cambio==t[0] and t[1]=="es":
                cambio = t[2]
                if cosa == cambio:
                    valor=True
        if verbo=="es":
            for t in reversed (conocimiento):
                if cambio2 == t[2] and verbo == t[1]:
                    cambio2 = t[0]
                if cosa == cambio2:
                    valor=True
            
        
        print(valor)
                    

def main():
    print("animales")
    Terminar= False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)
        
if __name__ == "__main__":
     main()

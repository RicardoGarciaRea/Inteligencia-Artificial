import json 
Conocimiento = False

with open ("animales.json", "r") as read_file:
    data = json.load(read_file)
    conocimiento = data['conocimiento']
    

        
    def Checar(animal,verbo,cosa):
        valor=False
        for t in conocimiento:
            if animal == t[0] and verbo == "tiene" and cosa==t[2]:
                valor=True
            if animal == t[0] and verbo == "vive" and cosa==t[2]:
                valor=True
            if animal==t[0] and t[1]=="es":
                animal = t[2]
                if cosa == animal:
                    valor=True
        print(valor)
                    

def main():
    print("Bienvenido a este programa")
    Terminar= False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)
        
if __name__ == "__main__":
     main()

import json 
Conocimiento = False

with open ("datos.json", "r") as read_file:
    data = json.load(read_file)
    tieneCon = data['CON'][0]['TieneCon']
    viveCon = data['CON'][1]['ViveCon']
    esCon = data['CON'][2]['ConEs']
    

    
    def Checar(animal,verbo,cosa):
        valor=False
        if verbo == "tiene":
            for t in tieneCon:
                if animal == t[0]:
                    if t[1] == cosa:
                        valor=True
        
        if verbo == "vive":
            for v in viveCon:
                if animal == v[0]:
                    if v[1] == cosa:
                        valor=True
        
        
        if verbo == "es":
            for e in esCon:
                if animal == e[0]:
                    animal = e[1]
                    if animal == cosa:
                        valor=True
        
        print(valor)

def main():
    print('Checar("animal","verbo","cosa")')
    print('Checar("Gato","tiene","garras")')
    print('Checar("gato","es","viviparo")')
    print('Checar("gato","vive","tierra")')
    Terminar= False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)
        
if __name__ == "__main__":
     main()
            
        
        
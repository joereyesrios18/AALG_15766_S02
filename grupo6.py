

def contar_votos():
   
    votos = [0, 0, 0, 0]
    
    print("Ingrese los votos del 1 al 4. Ingrese '0' para finalizar.")
    
    while True:
        voto = int(input())  
        if voto == 0:  
            break
        if 1 <= voto <= 4: 
            votos[voto - 1] += 1  
        else:
            print("candidato no exites")
            return

    total_votos = sum(votos)  
    if total_votos == 0:  
        print("No se han registrado votos.")
        return
    
   
    print("\nResultados de la elección:")
    for i in range(4):
        porcentaje = (votos[i] / total_votos) * 100  
        print(f"Candidato {i + 1}: {votos[i]} votos, {porcentaje:.2f}% del total.")


contar_votos()


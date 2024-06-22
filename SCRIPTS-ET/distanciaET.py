import googlemaps
from datetime import datetime

# Función para calcular la distancia y duración del viaje con opción de modo de transporte
def calcular_distancia_duracion(ciudad_origen, ciudad_destino, modo_viaje):
    # Clave de API de Google Maps
    gmaps = googlemaps.Client(key='AIzaSyDKDhuHF2px4pfHfvLd1fXBOW_0vMnVJ1I') 
    
    try:
        # Obtener la distancia y duración del viaje según el modo de transporte especificado
        distancia = gmaps.distance_matrix(ciudad_origen, ciudad_destino, mode=modo_viaje, language='es', units='metric')
        distancia_millas = distancia['rows'][0]['elements'][0]['distance']['text']
        distancia_kilometros = distancia['rows'][0]['elements'][0]['distance']['value'] / 1000.0
        duracion = distancia['rows'][0]['elements'][0]['duration']['text']
    except Exception as e:
        print("Error al obtener la información de la API:", e)
        return None, None, None
    
    return distancia_millas, distancia_kilometros, duracion

# Función para mostrar la narrativa del viaje
def narrativa_viaje(ciudad_origen, ciudad_destino, distancia_millas, duracion):
    narrativa = f"Viajando desde {ciudad_origen} a {ciudad_destino}, que está a una distancia de {distancia_millas}. El viaje tomará aproximadamente {duracion}."
    return narrativa

# Función principal del script
def main():
    print("Bienvenido al calculador de distancia y duración de viaje!")
    print("Por favor, ingresa los nombres de las ciudades")
    
    while True:
        ciudad_origen = input("Ciudad de Origen (o presione la tecla 's' para salir): ").strip()
        if ciudad_origen.lower() == 's':
            break
        
        ciudad_destino = input("Ciudad de Destino: ").strip()
        
        # Solicita modo de transporte
        print("Elige el medio de transporte:")
        print("1. Auto")
        print("2. Caminata")
        print("3. Bicicleta")
        print("4. Transporte público")
        modo = input("Selecciona una opción (1/2/3/4): ").strip()
        
        # Mapear la opción elegida por el usuario al modo de transporte correspondiente, investigado desde API Google Cloud Console
        if modo == '1':
            modo_viaje = 'driving'
        elif modo == '2':
            modo_viaje = 'walking'
        elif modo == '3':
            modo_viaje = 'bicycling'
        elif modo == '4':
            modo_viaje = 'transit'
        else:
            print("Opción no válida. Se utilizará el modo de transporte por defecto (coche).")
            modo_viaje = 'driving'
        
        # Calcular distancia y duración del viaje
        distancia_millas, distancia_kilometros, duracion = calcular_distancia_duracion(ciudad_origen, ciudad_destino, modo_viaje)
        
        if distancia_millas and duracion:
            print(f"Distancia: {distancia_millas}")
            print(f"Duración del viaje: {duracion}")
            
            # Mostrar la narrativa del viaje
            narrativa = narrativa_viaje(ciudad_origen, ciudad_destino, distancia_millas, duracion)
            print("Narrativa del viaje:")
            print(narrativa)
        else:
            print("No se pudo obtener la información del viaje consultado")
        
        print("\n")

if __name__ == "__main__":
    main()

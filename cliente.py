import grpc
import calculation_pb2
import calculation_pb2_grpc

# Crear un canal inseguro para conectarse al servidor gRPC en localhost:50051
with grpc.insecure_channel('localhost:50051') as channel:
    # Crea un objeto cliente para interactuar con el servidor
    cliente = calculation_pb2_grpc.CalculationServiceStub(channel)

    try:
        while True:
            # Solicita al usuario que ingrese cuatro números en una sola línea, separados por espacios
            user_input = input("Ingrese los números (o 'q' para salir): ")

            # Verifica si el usuario desea salir
            if user_input.lower() == 'q':
                print("Saliendo del cliente...")
                break

            # Convierte la entrada del usuario en una lista de números enteros
            numbers = list(map(int, user_input.split()))

            # Verifica si se ingresaron exactamente cuatro números
            if len(numbers) != 4:
                print("Por favor, ingrese exactamente 4 números separados por espacios.")
                continue

            number1, number2, number3, number4 = numbers

            # Crea una solicitud de cálculo con los cuatro números
            request = calculation_pb2.CalculationRequest(
                number1=number1, number2=number2, number3=number3, number4=number4
            )

            # Llama al método remoto CalculateSum con la solicitud creada
            response = cliente.CalculateSum(request)

            # Imprime el resultado de la suma recibido del servidor
            print("Resultado de la suma: ", response.result)

    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números enteros.")
    except grpc.RpcError as e:
        print(f"Error al realizar la solicitud: {e}")
    except KeyboardInterrupt:
        print("\nCliente interrumpido. Cerrando la conexión...")
    finally:
        print("Conexión cerrada.")
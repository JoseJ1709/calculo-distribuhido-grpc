import grpc
from concurrent import futures
import calculation_pb2
import calculation_pb2_grpc
import signal
import sys

# Definir los hosts y puertos de los workers (servidores de cálculo)
WORKER1_HOST = 'localhost'
WORKER1_PORT = '50054'

WORKER2_HOST = 'localhost'
WORKER2_PORT = '50055'


class CentralServer(calculation_pb2_grpc.CalculationServiceServicer):
    def CalculateSum(self, request, context):
        # Recibe los 4 números
        number1 = request.number1
        number2 = request.number2
        number3 = request.number3
        number4 = request.number4

        print(f"Servidor central: Recibida solicitud de cálculo. Números recibidos: {number1}, {number2}, {number3}, {number4}")

        # Inicializa variables para almacenar resultados
        resultado_worker1 = None
        resultado_worker2 = None

        # Conectar y enviar solicitud al Worker 1
        try:
            with grpc.insecure_channel(f'{WORKER1_HOST}:{WORKER1_PORT}') as channel1:
                print(f"Servidor central: Conectándose al Worker 1 en {WORKER1_HOST}:{WORKER1_PORT}...")
                stub1 = calculation_pb2_grpc.CalculationServiceStub(channel1)

                print("Servidor central: Enviando solicitud al Worker 1...")
                response1 = stub1.CalculateSum(calculation_pb2.CalculationRequest(number1=number1, number2=number2))
                resultado_worker1 = response1.result
                print(f"Servidor central: Respuesta recibida del Worker 1. Resultado parcial: {resultado_worker1}")
        except grpc.RpcError as e:
            print(f"Error al conectarse al Worker 1: {e}")
            print("Calculando localmente para los números 1 y 2...")
            resultado_worker1 = self.calculate_locally([number1, number2])

        # Conectar y enviar solicitud al Worker 2
        try:
            with grpc.insecure_channel(f'{WORKER2_HOST}:{WORKER2_PORT}') as channel2:
                print(f"Servidor central: Conectándose al Worker 2 en {WORKER2_HOST}:{WORKER2_PORT}...")
                stub2 = calculation_pb2_grpc.CalculationServiceStub(channel2)

                print("Servidor central: Enviando solicitud al Worker 2...")
                response2 = stub2.CalculateSum(calculation_pb2.CalculationRequest(number1=number3, number2=number4))
                resultado_worker2 = response2.result
                print(f"Servidor central: Respuesta recibida del Worker 2. Resultado parcial: {resultado_worker2}")
        except grpc.RpcError as e:
            print(f"Error al conectarse al Worker 2: {e}")
            print("Calculando localmente para los números 3 y 4...")
            resultado_worker2 = self.calculate_locally([number3, number4])

        # Asegurar que los resultados no sean None
        if resultado_worker1 is None:
            resultado_worker1 = 0
        if resultado_worker2 is None:
            resultado_worker2 = 0

        # Sumar los resultados de ambos workers
        total_result = resultado_worker1 + resultado_worker2
        print(f"Servidor central: Suma total calculada: {total_result}")

        # Enviar la respuesta final al cliente
        return calculation_pb2.CalculationResponse(result=total_result)

    def calculate_locally(self, numbers):
        # Función para calcular la suma localmente
        result = sum(numbers)
        print(f"Resultado calculado localmente: {result} para los números {numbers}")
        return result

 # Crea un servidor gRPC con un ThreadPoolExecutor que maneja hasta 2 hilos
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))

# Registra el servicio 'CentralServer' en el servidor gRPC
calculation_pb2_grpc.add_CalculationServiceServicer_to_server(CentralServer(), server)

# Asigna al servidor un puerto inseguro para escuchar peticiones (localhost:50051)
server.add_insecure_port('[::]:50051')

# Inicia el servidor
server.start()

print("Servidor central gRPC escuchando en el puerto 50051...")

# Maneja la señal de interrupción (Ctrl+C) para detener el servidor limpiamente
def handle_sigint(signal, frame):
    print("\nDeteniendo el servidor gRPC...")
    server.stop(0)
    print("Servidor detenido.")
    sys.exit(0)

# Registra la función de manejo de señal para Ctrl+C
signal.signal(signal.SIGINT, handle_sigint)

# Mantiene el servidor en ejecución indefinidamente
server.wait_for_termination()

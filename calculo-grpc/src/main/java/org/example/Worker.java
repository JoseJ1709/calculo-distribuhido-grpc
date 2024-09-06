package org.example;

import io.grpc.Server;
import io.grpc.ServerBuilder;
import io.grpc.stub.StreamObserver;
import calculation.CalculationServiceGrpc;
import calculation.Calculation.CalculationRequest;
import calculation.Calculation.CalculationResponse;

import java.io.IOException;

public class Worker {

    private static Server server;

    public static void main(String[] args) throws IOException, InterruptedException {
        // Permite pasar el puerto como argumento; si no, usa el puerto 50052 por defecto
        int port = args.length > 0 ? Integer.parseInt(args[0]) : 50052;

        // Inicia el servidor gRPC en el puerto especificado
        server = ServerBuilder.forPort(port)
                .addService(new CalculationServiceImpl())
                .build()
                .start();

        System.out.println("Servidor de cálculo gRPC iniciado en el puerto " + port + "...");

        // Añade un shutdown hook para capturar Ctrl+C y cerrar el servidor limpiamente
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("Recibida señal de cierre (Ctrl+C). Cerrando el servidor...");
            if (server != null) {
                server.shutdown();
                System.out.println("Servidor cerrado.");
            }
        }));

        // Mantiene el servidor en ejecución
        server.awaitTermination();
    }

    static class CalculationServiceImpl extends CalculationServiceGrpc.CalculationServiceImplBase {
        @Override
        public void calculateSum(CalculationRequest request, StreamObserver<CalculationResponse> responseObserver) {
            System.out.println("Worker: Solicitud de cálculo recibida.");
            System.out.println("Worker: Números recibidos - number1: " + request.getNumber1() + ", number2: " + request.getNumber2());

            // Realiza el cálculo
            int number1 = request.getNumber1();
            int number2 = request.getNumber2();
            int result = number1 + number2;

            System.out.println("Worker: Resultado del cálculo: " + result);

            // Prepara la respuesta
            CalculationResponse response = CalculationResponse.newBuilder()
                    .setResult(result)
                    .build();

            // Envía la respuesta de vuelta al servidor central
            System.out.println("Worker: Enviando respuesta de vuelta al servidor central.");
            responseObserver.onNext(response);
            responseObserver.onCompleted();

            System.out.println("Worker: Respuesta enviada exitosamente.");
        }
    }
}
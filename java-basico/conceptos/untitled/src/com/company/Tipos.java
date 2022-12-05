package com.company;

public class Tipos {

    public static void main(String[] args) {

        // Asignación en una linea
        // tipo identificador = 38;

        // Asignación en dos lineas
        // tipo idetificador;
        // identificador = 38;

        // enteros (p)
        byte number1 = 1;  // 1 byte
        short number2 = 2; // 2 byte
        int number3 = 3;   // 4 byte
        long number4 = 4L;  // 8 byte

        // punto flotante (p)
        float decimal1 = 4.5f;
        double decimal2 = 9.49d;

        // tipo caracter (p)
        char caracter = 'a';

        // tipo booleano (p)
        boolean falso = false;
        boolean verdadero = true;

        // tipo cadena
        String nombre = "Agustin";
        String apellido = "Rodriguez";


        // Los tipos primitivos(p) no pueden ser null, para ello se utilizan los
        // tipo envoltorio
        Integer numero = null; // Estos son clases que envuelven al tipo primitivo
        Long numero2 = 4L;
    }
}

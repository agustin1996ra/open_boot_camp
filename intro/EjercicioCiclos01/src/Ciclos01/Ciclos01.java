/*
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir 
el proceso hasta que se Introduzca un número negativo.
*/

package Ciclos01;

import java.util.Scanner;

public class Ciclos01 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        int numero, cuadrado;
        System.out.println("Por favor intgrese un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0){  // Mientras el numero sea igual a cenro o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es  = " + cuadrado);
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        
    }
}

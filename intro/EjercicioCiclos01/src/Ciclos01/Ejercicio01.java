/*
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir 
el proceso hasta que se Introduzca un número negativo.
*/
package Ciclos01;
import javax.swing.JOptionPane;
        

public class Ejercicio01 {
    public static void main(String[] args) {
        
        
        int numero, cuadrado;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){  // Mientras el numero sea igual a cenro o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es  = " + cuadrado);
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        }
        System.out.println("El Programa finalizo, por que se ingreso un numero negativo");
    }
}

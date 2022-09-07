/*
 Ejercicio 2: Leer un número e idicar si es positivo o negativo. El proceso se
repetira hasta que se introduzca un cero.
 */
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio02 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0) {
            if (numero > 0) {
                System.out.println("Es Positivo");
            }
            else{
                System.out.println("Es negativo");        
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        }
        System.out.println("El programa finalizo porque se ingreso un zero.");
    }
}

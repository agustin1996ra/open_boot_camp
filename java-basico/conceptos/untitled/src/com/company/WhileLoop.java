package com.company;

public class WhileLoop {
    public static void main(String[] args) {

        int count = 0;

        while (count < 10) {
            if (count == 6){
                System.out.println(count);
                continue; // Termina la ejecución del ciclo actual y se prosige con el próximo
                // break; rompe la ejecución del bucle
            }
            System.out.println("Hola mundo" + count);
            count++;
        }


        System.out.println("fin");

    }
}

package com.company;

public class Funciones {
    public static void main(String[] args) {

        holaMundo();
        holaMundo();

        holaMundo("Agustin");
        holaMundo("Facundo");

        holaMundo(3);

        holaMundo("Agustin", "Rodriguez");
        
        String hola = devolverHola();
        System.out.println("hola = " + hola);
    }
    // Stactic es un modificador, indica que pertenece la clase, lo que quiere decir que no hace fata instanciar a la clase Funciones para utilizarlo.
    // public y private son modificadores de visibilidad.
    // Private, que solo será accesible desde este archivo java
    public static void holaMundo() {
        System.out.println("Hola mundo");
        System.out.println("Hola mundo");
        System.out.println("Hola mundo");
    }

    private static void holaMundo(String nombre) {
        System.out.println("Hola " + nombre);
    }

    private static void holaMundo(Integer number) {
        System.out.println("El numero es: "+ number);
    }

    private static void holaMundo(String name, String surname) {
        System.out.println("Hola " + name + " " + surname);
    }
    
    private static String devolverHola() {
        return "Hola";
    }

    private static int sum(int num1, int num2) {
        return num1 + num2;
    }
}

package com.company;

public class IfElse {

    public static void main(String[] args) {
        boolean check = 5 < 10;

        if (check) {
            System.out.println("Verdadero");
        }

        if (5 < 10) {
            System.out.println("True");
        }

        int number1 = 50;
        int number2 = 10;
        int number3 = 20;

        if (number1< number2 && number2 < number3) {
            System.out.println("verdadero");
        } else if (number3 < number1) {
            System.out.println("else if");
        }else {
            System.out.println("falso");
        }



        System.out.println("fin");


    }
}

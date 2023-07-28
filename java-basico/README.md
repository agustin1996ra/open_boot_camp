# Curso de Java básico

## Conceptos
### Comentarios y documentación
Ahora veremos un ejemplo de varios tipos de cometarios y documentación

```java
package com.company;
/**
 * Clase principal punto de entrada aplicación
 * 
 * @author agsutin1996
 */
public class Main {
	/**
	 * 
	 * Funcion principal punto de entrada a la aplicación
	 * @param args
	 * @since 1.0
	 */
	public static void main(String[] args) {
		// Write your code here

		/* Aqui un texto de comentario */

		/*
		1. Abrir fichero 
		2. Leer fichero
		3. Procesar fichero
		4. Cerrar fichero
		*/

		// Imprimir texto
		System.out.println("Hola mundo"); // Imprimir texto

	}
}
```

### Variables y tipos de datos
```java
package com.company;

public class Tipos {


	public static void main(String[] args) {
		
		// Asignación en una linea
		// tipo identificador = 38;

		// Asignación en dos lineas
		// tipo identificador;
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
```

### Operadores

```java
package con.company

public class Operadores {

	public static void main(String[] args) {

		// Operadores

		// aritmeticos
		// + - / * %

		int number1 = 1;
		int numero2 = 2;

		int resultado1 = number1 + number2;
		int resultado2 = number1 - number2;
		int resultado3 = number1 * number2;
		int resultado4 = number1 / number2;

		// logicos, relacion, comparación, booleanos
		/*
		- >		mayor que
		- >=	mayor o igual que
		- <		menor que
		- <=	menor o igual que
		- ==	igual que
		- !=	diferentes
		- &&	and
		- ||	or
		*/

		// asignación
		/*

		- =
		- +=
		- -=
		- /=
		- *=
		- %=
		
		*/

		// incremento
		// ++

		// decremento
		// --

		// concatenación
		// +

	}
}
```

### Palabras reservadas
Java Language Keywords

Esta es la lista de palabras reservadas en Java. No se puede usar ninguna de estas como identificadores en un programa. Las palabras `const` y `goto` estan reservadas, aunque altualmente no se usan. `true`, `false` y `null` pueden parecer palabras, pero en realidad son literales, tampoco se pueden usar como identificadores en un programa.

- `abstract`
- `assert`***
- `boolean`
- `break`
- `byte`
- `case`
- `catch`
- `char`
- `class`
- `const`*
- `continue`
- `default`
- `do`
- `double`
- `else`	
- `enum`****
- `extends`
- `final`
- `finally`
- `float`
- `for`
- `goto`*
- `if`
- `implements`
- `import`
- `instanceof`
- `int`
- `interface`
- `long`
- `native`
- `new`
- `package`
- `private`
- `protected`
- `public`
- `return`
- `short`
- `static`
- `strictfp`**
- `super`
- `switch`
- `synchronized`
- `this`
- `throw`
- `throws`
- `transient`
- `try`
- `void`
- `volatile`
- `while`

* 	  not used
** 	  added in 1.2
***   added in 1.4
****  added in 5.0

### Funciones y parametros
```java
package con.company;

public class Funciones {

	public static void main(String[] args) {

		holaMundo();
	}
	// Stactic es un modificador, indica que pertenece la clase, lo que quiere decir que no hace fata instanciar a la clase Funciones para utilizarlo.
	// public y private son modificadores de visibilidad.
	public static String devolverHolaMundo() { // Public quiere decir que sera accesible desde otros archivos de este programa
        return "Hola mundo";
	}

	private static void holaMundo() { // Private, que solo será accesible desde este archivo java
		System.out.println("Hola mundo");
	}
}
```

### Sobrecarga de funciones
Una función se dice que está sobrecargada cuando el nombre de función es utilizado 
en más de una implementación
```java
package com.company;

public class Funciones {
    public static void main(String[] args) {

        holaMundo();
        holaMundo();

        holaMundo("Agustin");
        holaMundo("Facundo");

        holaMundo(3);

        holaMundo("Agustin", "Rodriguez");
    }
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
    
}
```

Esto se puede hacer porque se entiende que son diferentes funciones según 
la configuración de los parámetros de entrada.

Ósea, si uno invoca a la función `holaMundo(3);`, estará llamado a la tercera implementación de
la función, lo cual devolverá como resultado, `"El número es: 3"`.

### Crear clases

Vamos a ver como crear clase del paradigma de programacion orientada a objetos.

Las partes principales de la estructura de una clase son, los atributos,
los constructores, los métodos de comportamiento y los setters y getters.




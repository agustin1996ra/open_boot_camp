# Curso de Java básico

# Comentarios y documentación
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

# Variables y tipos de datos
```java
package com.company;

public class Tipos {


	public static void main(String[] args) {
		
		// Asignación en una linea
		// tipo identificador = 38;

		// Asignacón en dos lineas
		// tipo idetificador;
		// identificador = 38;

		// Enteros:
		byte number1 = 1;  // 1 byte
		short number2 = 2; // 2 byte
		int number3 = 3;   // 4 byte
		long number4 = 4;  // 8 byte
		

	}
}
```
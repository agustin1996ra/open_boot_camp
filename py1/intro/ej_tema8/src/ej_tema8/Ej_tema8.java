/*
 Para practicar la encapsulación:

Crear clase Persona.

Crear variables las privadas edad, nombre y telefono de la clase Persona.

Crear gets y sets de cada propiedad.

Crear un objeto persona en el main.

Utiliza los gets y sets para darle valores a las propiedades edad, nombre y 
telefono, por último muéstralas por consola.
 */
package ej_tema8;


public class Ej_tema8 {

    
    public static void main(String[] args) {
        Persona nuevaPersona = new Persona();
        nuevaPersona.setEdad(26);
        nuevaPersona.setNombre("Agustin");
        nuevaPersona.setTelefono("1234567890");
        
        System.out.println(nuevaPersona.getEdad());
        System.out.println(nuevaPersona.getNombre());
        System.out.println(nuevaPersona.getTelefono());
    }
    
}
class Persona{
    private int edad;
    private String nombre;
    private String telefono;
    
    public void setEdad(int edad){
        this.edad = edad;
    }
    public int getEdad() {
        return edad;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }
    
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    public String getTelefono() {
        return telefono;
    }
    
}

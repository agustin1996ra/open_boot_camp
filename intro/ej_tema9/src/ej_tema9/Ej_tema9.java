
package ej_tema9;


public class Ej_tema9 {

    
    public static void main(String[] args) {
        System.out.println("Datos del Cliente");
        Cliente cliente = new Cliente();
        cliente.setEdad(26);
        cliente.setNombre("Agustin");
        cliente.setTelefono("1234567890");
        cliente.setCredito(10000);
        
        System.out.println("edad: " + cliente.getEdad());
        System.out.println("nombre: " + cliente.getNombre());
        System.out.println("telefono: " + cliente.getTelefono());
        System.out.println("credito: " + cliente.getCredito());
        
        System.out.println("");
        System.out.println("Datos del tabajador");
        Trabajador trabajador = new Trabajador();
        trabajador.setEdad(24);
        trabajador.setNombre("Juan");
        trabajador.setTelefono("0987654321");
        trabajador.setSalario(8000);
        
        System.out.println("edad: " + trabajador.getEdad());
        System.out.println("nombre: " + trabajador.getNombre());
        System.out.println("telefono: " + trabajador.getTelefono());
        System.out.println("salario: " + trabajador.getSalario());
                
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

class Cliente extends Persona{
    private int credito;
    
    public void setCredito(int credito){
        this.credito = credito;
    }
    public int getCredito() {
        return this.credito;
    }
}

class Trabajador extends Persona{
    private int salario;
    
    public void setSalario(int salario){
        this.salario = salario;
    }
    public int getSalario() {
        return this.salario;
        
    }
}
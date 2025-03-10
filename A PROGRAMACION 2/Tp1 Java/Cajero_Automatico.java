import com.sun.management.GarbageCollectionNotificationInfo;

import java.lang.management.GarbageCollectorMXBean;

public class Cajero_Automatico {
    //Atributos
    public final double efectivo = 10;
    protected static boolean acepta;
    private String devuelve;



    //Metodos

    public static void caca(){
        System.out.println("mucha caca");
    }
    public boolean isAcepta() {
        return acepta;
    }


    public String getDevuelve() {
        return devuelve;
    }

    public void setDevuelve(String devuelve) {
        this.devuelve = devuelve;
    }


    public void procesarPedido(){

    }

    public boolean pago(double pago){
        return false;
    }

}

package InformationExpert;

import java.util.Random;

public class CzujnikTemperatury {
    private int Temperatura;

    public CzujnikTemperatury(int temperatura) {
        Temperatura = temperatura;
    }

    public CzujnikTemperatury() {
    }

    public int getTemperatura() {
        return Temperatura;
    }

    public void setTemperatura(int temperatura) {
        Temperatura = temperatura;
    }

    public void sprawdzTemperature(){
        this.Temperatura = (int) (Math.random() * 150);
    }
}

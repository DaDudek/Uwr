package InformationExpert;

public class Piec {
    private Wegiel[] pojemnik;
    private CzujnikTemperatury czujnik;
    private int iloscWegla;

    public Piec(Wegiel[] pojemnik, CzujnikTemperatury czujnik, int iloscWegla) {
        this.pojemnik = pojemnik;
        this.czujnik = czujnik;
        this.iloscWegla = iloscWegla;
    }

    public int getIloscWegla() {
        return iloscWegla;
    }

    public void setIloscWegla(int iloscWegla) {
        this.iloscWegla = iloscWegla;
    }

    public CzujnikTemperatury getCzujnik() {
        return czujnik;
    }

    public void setCzujnik(CzujnikTemperatury czujnik) {
        this.czujnik = czujnik;
    }

    public Wegiel[] getPojemnik() {
        return pojemnik;
    }

    public void setPojemnik(Wegiel[] pojemnik) {
        this.pojemnik = pojemnik;
    }

    public void podlozDoPieca(){
        this.czujnik.sprawdzTemperature();
        if (this.czujnik.getTemperatura() < 30){
            if (iloscWegla <=0){
                System.out.println("Niestety zabrakło węgla i piec zgasł");
            }else{
                pojemnik[iloscWegla-1] = null;
                iloscWegla--;
                czujnik.setTemperatura(czujnik.getTemperatura() + 10);
                System.out.println("Podlozono do pieca");
            }
        }
    }
}

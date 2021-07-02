public class Main {
    public static void main(String[] args) {
        Bankomat bankomat =  new Bankomat();
        bankomat.Logowanie();
        bankomat.Wplata();
        bankomat.potwierdzWplate();
        bankomat.Wyplata();
        bankomat.potwierdzWyplate();
        bankomat.Wylogowanie();
    }
}

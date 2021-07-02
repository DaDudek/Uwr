public class UnloggedBankomat implements IBankomat {
    private Bankomat bankomat;

    public UnloggedBankomat(Bankomat bankomat) {
        this.bankomat = bankomat;
    }

    @Override
    public void Logowanie(){
        System.out.println("Zalogowano");
        bankomat.setBankomatState(new LoggedBankomat(this.bankomat));
    }

    @Override
    public void Wplata() {
        throw new NullPointerException(); // to avoid throws signature
    }

    @Override
    public void Wyplata() {
        throw new NullPointerException(); // to avoid throws signature
    }

    @Override
    public void Wylogowanie() {
        throw new NullPointerException(); // to avoid throws signature
    }

    @Override
    public void potwierdzWplate() {
        throw new NullPointerException(); // to avoid throws signature
    }

    @Override
    public void potwierdzWyplate() {
        throw new NullPointerException(); // to avoid throws signature
    }
}

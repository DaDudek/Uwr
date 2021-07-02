public class WyplacajacyBankomat implements IBankomat {
    private Bankomat bankomat;

    public WyplacajacyBankomat(Bankomat bankomat) {
        this.bankomat = bankomat;
    }

    @Override
    public void Logowanie() {
        throw new NullPointerException(); // to avoid throws signature
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
        System.out.println("Potwierdzono wypłate");
        this.bankomat.setBankomatState(new LoggedBankomat(this.bankomat));
    }
}

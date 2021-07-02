public class WplacajacyBankomat implements IBankomat{
    private Bankomat bankomat;

    public WplacajacyBankomat(Bankomat bankomat) {
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
        System.out.println("Potwierdzono wpłate");
        this.bankomat.setBankomatState(new LoggedBankomat(this.bankomat));
    }

    @Override
    public void potwierdzWyplate() {
        throw new NullPointerException(); // to avoid throws signature

    }
}

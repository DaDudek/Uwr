public class LoggedBankomat implements IBankomat {
    private Bankomat bankomat;

    public LoggedBankomat(Bankomat bankomat) {
        this.bankomat = bankomat;
    }

    @Override
    public void Logowanie() {
        throw new NullPointerException(); // to avoid throws signature
    }

    @Override
    public void Wplata() {
        System.out.println("Wybrano opcje wypłaty pieniędzy");
        this.bankomat.setBankomatState(new WplacajacyBankomat(this.bankomat));
    }

    @Override
    public void Wyplata() {
        System.out.println("Wybrano opcje wpłaty pieniędzy");
        this.bankomat.setBankomatState(new WyplacajacyBankomat(this.bankomat));
    }

    @Override
    public void Wylogowanie() {
        System.out.println("Wylogowano");
        this.bankomat.setBankomatState(new UnloggedBankomat(this.bankomat));
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

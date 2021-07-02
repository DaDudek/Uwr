public class Bankomat{
    private IBankomat bankomatState;

    public Bankomat() {
        this.bankomatState = new UnloggedBankomat(this);
    }

    public IBankomat getBankomatState() {
        return bankomatState;
    }

    public void setBankomatState(IBankomat bankomatState) {
        this.bankomatState = bankomatState;
    }

    public void Logowanie() {
        this.bankomatState.Logowanie();
    }

    public void Wplata() {
        this.bankomatState.Wplata();
    }

    public void Wyplata() {
        this.bankomatState.Wyplata();
    }

    public void Wylogowanie() {
        this.bankomatState.Wylogowanie();
    }

    public void potwierdzWplate() {
        this.bankomatState.potwierdzWplate();
    }

    public void potwierdzWyplate() {
        this.bankomatState.potwierdzWyplate();
    }
}

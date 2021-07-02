public class PozostaleHandler extends AbstractHandler {
    @Override
    public boolean ProcessRequest(Request request) {
        System.out.println("Pozostale");
        return true;
    }
}

public class PochwalneHandler extends AbstractHandler {
    @Override
    public boolean ProcessRequest(Request request) {
        System.out.println("Pochwala");
        return true;
    }
}

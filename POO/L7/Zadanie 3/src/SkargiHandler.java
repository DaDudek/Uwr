public class SkargiHandler extends AbstractHandler {
    @Override
    public boolean ProcessRequest(Request request) {
        System.out.println("Skarga");
        return true;
    }
}

public class ArchiwumHandler extends  AbstractHandler {
    @Override
    public boolean ProcessRequest(Request request) {
        System.out.println("Archiwum");
        return true;
    }
}

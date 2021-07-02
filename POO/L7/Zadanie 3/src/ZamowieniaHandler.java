public class ZamowieniaHandler extends AbstractHandler {
    @Override
    public boolean ProcessRequest(Request request) {
        System.out.println("Zamowienie");
        return true;
    }
}

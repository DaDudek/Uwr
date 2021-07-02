public class HTTPCommand implements Command {
    String url;
    String fileName;
    HTTPReceiver receiver;

    public HTTPCommand(String url, String fileName) {
        this.url = url;
        this.fileName = fileName;
        this.receiver = new HTTPReceiver(url, fileName);
    }

    @Override
    public void Execute() {
        this.receiver.Action();
    }
}

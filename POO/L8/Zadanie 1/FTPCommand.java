public class FTPCommand implements Command{
    String url;
    String fileName;
    FTPReceiver receiver;

    public FTPCommand(String url, String fileName) {
        this.url = url;
        this.fileName = fileName;
        this.receiver = receiver;
        receiver = new FTPReceiver(url,fileName);
    }

    @Override
    public void Execute() {
        this.receiver.Action();
    }
}

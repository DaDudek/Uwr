public class CreateFileCommand implements Command{
    String fileName;
    CreateFileReceiver receiver;

    public CreateFileCommand(String fileName) {
        this.fileName = fileName;
        this.receiver = new CreateFileReceiver(fileName);
    }


    @Override
    public void Execute() {
        this.receiver.Action();
    }
}

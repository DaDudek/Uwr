public class CopyFileCommand implements Command{
    String destinationFileName;
    String sourceFileName;
    CopyFileReceiver receiver;

    public CopyFileCommand(String destinationFileName, String sourceFileName) {
        this.destinationFileName = destinationFileName;
        this.sourceFileName = sourceFileName;
        this.receiver = new CopyFileReceiver(destinationFileName,sourceFileName);
    }

    @Override
    public void Execute() {
        this.receiver.Action();
    }
}

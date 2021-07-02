public class CopyFileReceiver {
    String destinationFileName;
    String sourceFileName;

    public CopyFileReceiver(String destinationFileName, String sourceFileName) {
        this.destinationFileName = destinationFileName;
        this.sourceFileName = sourceFileName;
    }

    public void Action(){
        System.out.println("Skopiowano plik "+sourceFileName +" do pliku "+destinationFileName);
    }
}

public class CreateFileReceiver {
    String fileName;

    public CreateFileReceiver(String fileName) {
        this.fileName = fileName;
    }

    public void Action(){
        System.out.println("utworzono plik: " + fileName);
    }
}

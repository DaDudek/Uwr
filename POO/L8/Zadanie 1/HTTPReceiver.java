public class HTTPReceiver {
    String url;
    String fileName;

    public HTTPReceiver(String url, String fileName) {
        this.url = url;
        this.fileName = fileName;
    }

    public void Action(){
        System.out.println("pobrano plik: "+fileName+" z adresu "+url +" za pomocą FTP");
    }
}

package Controller;

public class ImageController {

    public void click(Image image){
        // bardzo skomplikowana logika
        System.out.println("Wciśnięto obrazek więc kontroller wykonał skomplikowaną prace aby sobie poradzić z tym eventem");
        image.setSize(image.getSize()+10);
    }
}

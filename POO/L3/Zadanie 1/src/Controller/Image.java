package Controller;

// musimy użyć wyobrazni ze mamy jakies GUI
public class Image {
    private int size;
    private ImageController imageController;

    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public Image() {
    }

    public Image(int size, ImageController imageController) {
        this.size = size;
        this.imageController = imageController;
    }

    public void ImageClick(){
        this.imageController.click(this);
    }
}

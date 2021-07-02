package after;

public class SquareB extends Shape{

    @Override
    public void setWidth(int width) {
        super.setWidth(width);
        super.setHeight(width);
    }

    @Override
    public void setHeight(int height) {
        super.setHeight(height);
        super.setWidth(height);
    }

    @Override
    public int calculateArea() {
        return getWidth() * getHeight();
    }
}

package before;

public class Item {
    private double Price;
    private String Name;

    public Item(double price, String name) {
        Price = price;
        Name = name;
    }

    public String getName() {
        return Name;
    }

    public double getPrice() {
        return Price;
    }

}

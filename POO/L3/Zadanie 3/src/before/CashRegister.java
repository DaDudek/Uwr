package before;

public class CashRegister {
    public TaxCalculator taxCalculator = new TaxCalculator();

    public double CalculatePrice(Item[] items) {
        double price = 0;
        for (Item item : items) {
            price += item.getPrice() + taxCalculator.CalculateTax(item.getPrice());
        }
        return price;
    }

    public void PrintBill(Item[] items){
        for (Item item:
             items) {
            System.out.printf("towar %s : cena %.2f  + podatek %.2f \n", item.getName(),item.getPrice(),taxCalculator.CalculateTax(item.getPrice()));
        }
    }
}

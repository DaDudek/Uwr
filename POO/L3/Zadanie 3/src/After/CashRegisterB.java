package After;


import java.util.Arrays;
import java.util.Comparator;

public class CashRegisterB {
    public TaxCalculator taxCalculator;

    public CashRegisterB(TaxCalculator taxCalculator) {
        this.taxCalculator = taxCalculator;
    }

    public double CalculatePrice(ItemB[] items) {
        double price = 0;
        for (ItemB item : items) {
            price += item.getPrice() + taxCalculator.CalculateTax(item.getPrice());
        }
        return price;
    }



    public void PrintBill(ItemB[] items){
        for (ItemB item:
                items) {
            System.out.printf("towar %s : cena %.2f  + podatek %.2f \n", item.getName(),item.getPrice(),taxCalculator.CalculateTax(item.getPrice()));
        }
    }


    public void PrintBill(ItemB[] items, Comparator<ItemB> comparator){
        Arrays.sort(items, comparator);
        for (ItemB item:
                items) {
            System.out.printf("towar %s : cena %.2f  + podatek %.2f \n", item.getName(),item.getPrice(),taxCalculator.CalculateTax(item.getPrice()));
        }
    }

}

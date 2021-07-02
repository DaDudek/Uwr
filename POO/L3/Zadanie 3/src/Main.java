import After.*;
import before.CashRegister;
import before.Item;

public class Main {
    public static void main(String[] args) {
        Item[] items = new Item[3];
        items[0] = new Item(10.0,"Seler");
        items[1] =  new Item(15.0, "Marchewka");
        items[2] = new Item(102.3, "Monitor");


        CashRegister cashRegister = new CashRegister();
        cashRegister.PrintBill(items);
        System.out.println();
        System.out.println();

        CashRegisterB cashRegisterB = new CashRegisterB(new TaxCalculatorB());
        CashRegisterB cashRegisterBLow = new CashRegisterB(new LowTaxRateCalculator());
        CashRegisterB cashRegisterBHigh = new CashRegisterB(new HighTaxRateCalculator());
        ItemB[] itemsB1 = new ItemB[3];
        itemsB1[0] = new ItemB(10.0,"Seler");
        itemsB1[1] =  new ItemB(15.0, "Marchewka");
        itemsB1[2] = new ItemB(102.3, "Monitor");

        cashRegisterB.PrintBill(itemsB1);
        System.out.println();
        System.out.println();

        cashRegisterB.PrintBill(itemsB1, new DecreasingOrder<ItemB>() );
        System.out.println();
        System.out.println();

        cashRegisterB.PrintBill(itemsB1, new AlphabeticOrder<ItemB>() );
        System.out.println();
        System.out.println();


        cashRegisterBLow.PrintBill(itemsB1);
        System.out.println();
        System.out.println();


        cashRegisterBHigh.PrintBill(itemsB1);
        System.out.println();
        System.out.println();





    }
}

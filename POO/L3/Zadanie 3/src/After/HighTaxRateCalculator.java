package After;

public class HighTaxRateCalculator implements TaxCalculator {

    public double CalculateTax(double price) {
        return 0.7 * price;
    }
}

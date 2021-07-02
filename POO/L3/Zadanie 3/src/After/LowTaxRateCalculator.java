package After;

public class LowTaxRateCalculator implements TaxCalculator {


    @Override
    public double CalculateTax(double prize) {
        return 0.17 * prize;
    }
}

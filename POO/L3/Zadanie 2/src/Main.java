import AfterChange.BetterReportPrinter;
import AfterChange.DataProvider;
import BeforeChange.ReportPrinter;

public class Main {
    public static void main(String[] args) {
        new ReportPrinter().PrintReport();
        new BetterReportPrinter(new DataProvider()).printReport();
    }
}

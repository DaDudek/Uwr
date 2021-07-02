package AfterChange;

public class BetterReportPrinter {
    DataProvider dataProvider;

    public BetterReportPrinter(DataProvider dataProvider) {
        this.dataProvider = dataProvider;
    }

    public void printReport(){
        Report report = dataProvider.getData();
        report.formatDocument();
        System.out.println(report.getData());
    }

}

public class Main {
    public static void main(String[] args) {
        ReportPrinter reportPrinter = new ReportPrinter();
        reportPrinter.printReport(new ReportComposer(new DataProvider(), new FormatDocument()));
    }
}

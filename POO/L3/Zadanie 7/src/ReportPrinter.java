public class ReportPrinter implements  IReportPrinter {

    public void printReport(IReportComposer iReportComposer){
        Report report = iReportComposer.composerReport();
        System.out.println(report.getMessage());
    };
}

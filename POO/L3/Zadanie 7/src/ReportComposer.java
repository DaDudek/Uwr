public class ReportComposer implements IReportComposer{
    private IDataProvider dataProvider;
    private IFormatDocument formatDocument;

    public IDataProvider getDataProvider() {
        return dataProvider;
    }

    public void setDataProvider(IDataProvider dataProvider) {
        this.dataProvider = dataProvider;
    }

    public ReportComposer() {};

    public ReportComposer(IDataProvider dataProvider, IFormatDocument formatDocument) {
        this.dataProvider = dataProvider;
        this.formatDocument = formatDocument;
    }

    public IFormatDocument getFormatDocument() {
        return formatDocument;
    }

    public void setFormatDocument(IFormatDocument formatDocument) {
        this.formatDocument = formatDocument;
    }

    @Override
    public Report composerReport() {
        Report report = this.dataProvider.provideData();
        this.formatDocument.formatData(report);
        return report;
    }
}

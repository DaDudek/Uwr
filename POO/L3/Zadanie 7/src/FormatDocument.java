public class FormatDocument implements IFormatDocument{
    @Override
    public void formatData(Report report) {
        report.setMessage(report.getMessage().toUpperCase());
    }
}

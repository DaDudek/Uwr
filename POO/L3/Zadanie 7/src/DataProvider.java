public class DataProvider implements IDataProvider {
    @Override
    public Report provideData() {
        return new Report("wydrukuj mnie");
    }
}

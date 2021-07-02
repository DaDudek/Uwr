import java.util.List;

public class SQLAccess extends DataAccessHandler<List<Table>>{
    @Override
    void connectToDatabase() {
        System.out.println("Nastąpiło połączenie z bazą SQL");
    }

    @Override
    List<Table> getData() {
        return new SQLDatabase().getData();
    }

    @Override
    void processData(List<Table> data) {
        int sum = 0;
        for (int i = 0; i < data.size(); i++) {
            sum += data.get(i).getColumn2();
        }
        System.out.println("Suma kolumny 2 wynosi: "+ sum);
    }

    @Override
    void closeConnection() {
        System.out.println("Zamknięto połączenie z bazą SQL");
    }
}

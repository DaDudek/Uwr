import java.util.List;

public class SQLAccessStrategy implements DataAccessHandlerStrategy<List<Table>>{

    public void connectToDatabase() {
        System.out.println("Nastąpiło połączenie z bazą SQL");
    }

    public List<Table> getData() {
        return new SQLDatabase().getData();
    }

    public void processData(List<Table> data) {
        int sum = 0;
        for (int i = 0; i < data.size(); i++) {
            sum += data.get(i).getColumn2();
        }
        System.out.println("Suma kolumny 2 wynosi: "+ sum);
    }

    public void closeConnection() {
        System.out.println("Zamknięto połączenie z bazą SQL");
    }
}

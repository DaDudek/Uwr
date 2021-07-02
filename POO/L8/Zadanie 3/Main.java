import java.util.List;

public class Main {
    public static void main(String[] args) {
        DataAccessHandler SQL = new DataAccessHandler(new SQLAccessStrategy());
        DataAccessHandler XML = new DataAccessHandler(new XMLAccessStrategy());

        SQL.Execute();
        XML.Execute();
    }
}

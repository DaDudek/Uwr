public class Main {
    public static void main(String[] args) {
        DataAccessHandler sql =  new SQLAccess();
        DataAccessHandler xml = new XMLAccess();

        sql.Execute();
        System.out.println("\n\n");
        xml.Execute();
    }
}

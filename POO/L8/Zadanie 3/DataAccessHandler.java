public class DataAccessHandler {
    private DataAccessHandlerStrategy strategy;

    public DataAccessHandler(DataAccessHandlerStrategy strategy) {
        this.strategy = strategy;
    }

    public void Execute(){
        this.strategy.connectToDatabase();
        this.strategy.processData(this.strategy.getData());
        this.strategy.closeConnection();
    }
}

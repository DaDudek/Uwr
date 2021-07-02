public abstract class DataAccessHandler<T> {
    abstract void connectToDatabase();
    abstract T getData();
    abstract void processData(T data);
    abstract void closeConnection();

    public void Execute(){
        connectToDatabase();
        T data = getData();
        processData(data);
        closeConnection();
    }
}

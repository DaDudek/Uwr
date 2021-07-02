public interface DataAccessHandlerStrategy<T> {
    void connectToDatabase();
    T getData();
    void processData(T data);
    void closeConnection();
}

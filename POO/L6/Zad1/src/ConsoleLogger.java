public class ConsoleLogger implements ILogger{

    @Override
    public void Log(String message) {
        System.out.println("message");
    }
}

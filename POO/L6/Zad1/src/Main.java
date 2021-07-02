public class Main {
    public static void main(String[] args) {
        ILogger logger1 = LoggerFactory.getInstance().getLogger(LogType.File, "file.txt");
        logger1.Log("foo bar");

        ILogger logger2 = LoggerFactory.getInstance().getLogger(LogType.Console);
        logger2.Log("console");

        ILogger logger3 = LoggerFactory.getInstance().getLogger(LogType.None);
        logger3.Log("nic sie nie dzieje");
    }
}

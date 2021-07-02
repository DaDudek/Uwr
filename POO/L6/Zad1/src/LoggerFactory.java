public class LoggerFactory {
    private static LoggerFactory loggerFactoryInstance;

    public static LoggerFactory getInstance(){
        if (loggerFactoryInstance == null){
            loggerFactoryInstance = new LoggerFactory();
        }
        return loggerFactoryInstance;
    }

    public ILogger getLogger(LogType logType){
        switch (logType){
            case File:
                return new FileLogger();
            case Console:
                return new ConsoleLogger();
            default:
                return new NullObjectLogger();
        }
    }

    public ILogger getLogger(LogType logType, String parameters){
        switch (logType){
            case File:
                return new FileLogger(parameters);
            case Console:
                return new ConsoleLogger();
            default:
                return new NullObjectLogger();
        }
    }
}

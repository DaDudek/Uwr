import java.time.Duration;
import java.time.Instant;

public class TimeSingleton {
    private static Instant createTime;
    private final static int SECONDS = 5;
    private static TimeSingleton instance;

    private TimeSingleton(){};

    public static TimeSingleton getInstance() {
        if (instance == null){
            instance = new TimeSingleton();
            createTime = Instant.now();
        }
        else {
            Duration duration = Duration.between(createTime, Instant.now());
            System.out.println(duration.getSeconds());
            if (duration.getSeconds() >= 5) {
                instance = new TimeSingleton();
                createTime = Instant.now();
            }
        }
        return instance;
    }
}

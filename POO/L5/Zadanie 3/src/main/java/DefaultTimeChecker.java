import java.time.Instant;
import java.util.Calendar;

public class DefaultTimeChecker implements TimeChecker {
    @Override
    public boolean checkAvailability() {
        Calendar rightNow = Calendar.getInstance();
        int hour = rightNow.get(Calendar.HOUR_OF_DAY);
        if((hour >= 22) || (hour <= 8 )){
            return false;
        }
        return true;
    }
}

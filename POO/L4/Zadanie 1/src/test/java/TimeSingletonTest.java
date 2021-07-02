import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class TimeSingletonTest {

    @Test
    void shouldNotReturnNull(){
        //given
        TimeSingleton timeSingleton;

        //when
        timeSingleton = TimeSingleton.getInstance();

        //then
        Assertions.assertNotNull(timeSingleton);
    }

    @Test
    void shouldReturnSameSingleton(){
        //given
        TimeSingleton timeSingleton;
        TimeSingleton timeSingleton1;

        //when
        timeSingleton = TimeSingleton.getInstance();
        timeSingleton1 = TimeSingleton.getInstance();

        //then
        Assertions.assertEquals(timeSingleton,timeSingleton1);
    }

    @Test
    void shouldReturnDifferentSingleton() throws InterruptedException {
        //given
        TimeSingleton timeSingleton;
        TimeSingleton timeSingleton1;

        //when
        timeSingleton = TimeSingleton.getInstance();
        Thread.sleep(6000);
        timeSingleton1 = TimeSingleton.getInstance();

        //then
        Assertions.assertNotEquals(timeSingleton,timeSingleton1);
    }

    @Test
    void shouldSleepAndReturnSameSingleton() throws InterruptedException {
        //given
        TimeSingleton timeSingleton;
        TimeSingleton timeSingleton1;

        //when
        timeSingleton = TimeSingleton.getInstance();
        Thread.sleep(3000);
        timeSingleton1 = TimeSingleton.getInstance();

        //then
        Assertions.assertEquals(timeSingleton,timeSingleton1);
    }


}

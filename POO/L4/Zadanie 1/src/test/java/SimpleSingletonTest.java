import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class SimpleSingletonTest {

    @Test
    void shouldGiveSameObjectTwice(){
        //given
        SimpleSingleton simpleSingleton1;
        SimpleSingleton simpleSingleton2;

        //when
        simpleSingleton1 = SimpleSingleton.getInstance();
        simpleSingleton2 = SimpleSingleton.getInstance();

        //then
        Assertions.assertEquals(simpleSingleton1,simpleSingleton2);
    }
}

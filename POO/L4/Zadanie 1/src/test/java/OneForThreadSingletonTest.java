import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

public class OneForThreadSingletonTest {


    @Test
    void shouldReturnSameSingletonTwice() throws InterruptedException {
        //given
        MyThread myThread1 = new MyThread();
        OneForThreadSingleton instance1;
        OneForThreadSingleton instance2;

        //when
        myThread1.run();
        Thread.sleep(1000);
        instance1 = myThread1.getInstance();
        myThread1.run();
        Thread.sleep(1000);
        instance2 = myThread1.getInstance();

        //then
        Assertions.assertEquals(instance1,instance2);

    }




    @Test
    void shouldReturnTwoDifferentSingletons() throws InterruptedException {
        //given
        MyThread t1 = new MyThread();
        MyThread t2 = new MyThread();
        MyThread t3 = new MyThread();
        OneForThreadSingleton instance1;
        OneForThreadSingleton instance2;
        OneForThreadSingleton instance3;


        //when
        t1.start();
        Thread.sleep(1000);
        instance1 = t1.getInstance();

        t2.start();
        Thread.sleep(1000);
        instance2 = t2.getInstance();

        t3.start();
        Thread.sleep(1000);
        instance3 = t3.getInstance();


        //then
        Assertions.assertNotNull(instance1);
        Assertions.assertNotNull(instance2);
        Assertions.assertNotNull(instance3);
        Assertions.assertNotEquals(instance1,instance2);
        Assertions.assertNotEquals(instance2,instance3);
        Assertions.assertNotEquals(instance1,instance3);



    }
}

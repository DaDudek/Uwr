import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class AirportTest {
    @Test
    void shouldThrowExceptionWhenCapacityEqualZero(){
        Assertions.assertThrows(IllegalArgumentException.class,()-> new Airport(0));
    }

    @Test
    void shouldThrowExceptionWhenCapacityNegative(){
        Assertions.assertThrows(IllegalArgumentException.class,()->new Airport(-5));
    }

    @Test
    void shouldReturnAirportObjectWhenCapacityPositive(){
        //given
        Airport airport;

        //when
        airport = new Airport(5);

        //then
        Assertions.assertNotNull(airport);
        Assertions.assertTrue(airport instanceof Airport);

    }

    @Test
    void shouldThrowExceptionWhenCapacityUsed(){
        //given
        Airport airport = new Airport(2);
        Plane plane = airport.AcquireReusable();
        Plane plane1 = airport.AcquireReusable();


        Assertions.assertThrows(IndexOutOfBoundsException.class, airport::AcquireReusable);

    }

    @Test
    void shouldReturnDifferentPlanes(){
        //given
        Airport airport = new Airport(2);
        Plane plane = airport.AcquireReusable();
        Plane plane1 = airport.AcquireReusable();


        Assertions.assertNotEquals(plane,plane1);
    }

    @Test
    void shouldReturnSamePlane(){
        //given
        Airport airport = new Airport(2);
        Plane plane = airport.AcquireReusable();
        airport.ReleasePlane(plane);
        Plane plane1 = airport.AcquireReusable();
        Assertions.assertEquals(plane,plane1);
    }

    @Test
    void shouldThrowExceptionWhenPlaneIsNotFromAnyPool(){
        //given
        Airport airport = new Airport(2);
        Plane plane =new Plane("Samolot");

        Assertions.assertThrows(IllegalArgumentException.class, ()->airport.ReleasePlane(plane));
    }

    @Test
    void shouldThrowExceptionWhenPlaneIsFromWrongPool(){
        //given
        Airport airport = new Airport(2);
        Airport airport1 = new Airport(2);
        Plane plane =airport.AcquireReusable();
        Assertions.assertThrows(IllegalArgumentException.class, ()->airport1.ReleasePlane(plane));
    }

}

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ShapeFactoryProtectionProxyTest {

    @Test
    void shouldThrowExceptionAfterCallCreate(){
        ShapeFactoryProtectionProxy proxy = new ShapeFactoryProtectionProxy(new TimeChecker() {
            @Override
            public boolean checkAvailability() {
                return false;
            }
        });

        Assertions.assertThrows(IllegalAccessException.class,()->proxy.CreateShape("rectangle",3,5));

    }

    @Test
    void shouldThrowExceptionAfterCallRegister(){
        ShapeFactoryProtectionProxy proxy = new ShapeFactoryProtectionProxy(new TimeChecker() {
            @Override
            public boolean checkAvailability() {
                return false;
            }
        });

        Assertions.assertThrows(IllegalAccessException.class,()->proxy.RegisterWorker(new IShapeFactoryWorker() {
            @Override
            public boolean acceptsParameters(String parameter) {
                return false;
            }

            @Override
            public IShape create(int... args) {
                return null;
            }
        }));

    }


    @Test
    void shouldNotThrowExceptionAfterCallCreate() throws IllegalAccessException {
        ShapeFactoryProtectionProxy proxy = new ShapeFactoryProtectionProxy(new TimeChecker() {
            @Override
            public boolean checkAvailability() {
                return true;
            }
        });

        RectangleFactoryWorker rectangleFactoryWorker = new RectangleFactoryWorker();

        //when
        proxy.RegisterWorker(rectangleFactoryWorker);
        IShape rectangle = proxy.CreateShape("rectangle",3,5);

        //then
        Assertions.assertTrue(rectangle instanceof Rectangle);

    }

}

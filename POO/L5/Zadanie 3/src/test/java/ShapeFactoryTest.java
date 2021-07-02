import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class ShapeFactoryTest {

    @Test
    void shouldNotReturnNull() throws IllegalAccessException {
        //given
        ShapeFactory shapeFactory = new ShapeFactory();

        //when
        IShape square = shapeFactory.CreateShape("Square",5);

        //then
        Assertions.assertNotNull(square);
    }

    @Test
    void shouldReturnSquare() throws IllegalAccessException {
        //given
        ShapeFactory shapeFactory = new ShapeFactory();

        //when
        IShape square = shapeFactory.CreateShape("Square",5);

        //then
        Assertions.assertTrue(square instanceof Square);
    }

    @Test
    void shouldBeOpenToRectangle() throws IllegalAccessException {
        //given
        ShapeFactory factory = new ShapeFactory();
        RectangleFactoryWorker rectangleFactoryWorker = new RectangleFactoryWorker();

        //when
        factory.RegisterWorker(rectangleFactoryWorker);
        IShape rectangle = factory.CreateShape("rectangle",3,5);

        //then
        Assertions.assertTrue(rectangle instanceof Rectangle);
    }

    @Test
    void shouldThrowErrorBecauseNoWorkerForCase(){
        //given
        IllegalArgumentException exception;
        ShapeFactory factory = new ShapeFactory();

        //then
        Assertions.assertThrows(IllegalArgumentException.class,()->factory.CreateShape("rectangle",3,5));
    }
}

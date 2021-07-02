public class SquareFactoryWorker implements IShapeFactoryWorker{
    public static final String PARAMETER = "square";

    @Override
    public boolean acceptsParameters(String parameter) {
        return parameter.toLowerCase().equals(PARAMETER);
    }

    @Override
    public IShape create(int... args) {
        return new Square(args[0]);
    }
}

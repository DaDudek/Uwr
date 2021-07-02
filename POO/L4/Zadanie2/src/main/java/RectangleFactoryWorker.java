public class RectangleFactoryWorker implements IShapeFactoryWorker {
    public static final String PARAMETER = "rectangle";


    @Override
    public boolean acceptsParameters(String parameter) {
        return parameter.toLowerCase().equals(PARAMETER);
    }

    @Override
    public IShape create(int... args) {
        return new Rectangle(args[0],args[1]);
    }
}

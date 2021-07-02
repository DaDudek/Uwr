public interface IShapeFactoryWorker {
    boolean acceptsParameters(String parameter);
    IShape create(int... args);
    
}

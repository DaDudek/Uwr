public class ShapeFactoryProtectionProxy extends ShapeFactory{
    ShapeFactory factory;
    TimeChecker checker;

    public ShapeFactoryProtectionProxy(TimeChecker checker) {
        this.factory = new ShapeFactory();
        this.checker = checker;
    }

    public void RegisterWorker(IShapeFactoryWorker worker) throws IllegalAccessException {
        if(checker.checkAvailability()){
            factory.RegisterWorker(worker);
        }
        else {
            throw new IllegalAccessException();
        }
    }

    public IShape CreateShape(String ShapeName, int... args) throws IllegalAccessException {
        if(checker.checkAvailability()){
            return factory.CreateShape(ShapeName,args);
        }
        else{
            throw new IllegalAccessException();
        }
    }

}

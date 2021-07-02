import java.time.Instant;

public class ShapeFactoryLogProxy extends ShapeFactory{
    ShapeFactory factory;

    public ShapeFactoryLogProxy() {
        this.factory = new ShapeFactory();
    }

    public void RegisterWorker(IShapeFactoryWorker worker) throws IllegalAccessException {
        System.out.println("START");
        System.out.println(Instant.now());
        System.out.println("Register Worker:");
        System.out.println("Parametr:" + worker);
        factory.RegisterWorker(worker);
        System.out.println();
        System.out.println();
        System.out.println("KONIEC");
        System.out.println(Instant.now());
        System.out.println("Zwrócono: void");



    }

    public IShape CreateShape(String ShapeName, int... args) throws IllegalAccessException {
        System.out.println("START");
        System.out.println(Instant.now());
        System.out.println("Register Worker:");
        String parameter = "Parametry: "+ "ShapeName " ;
        for (int i = 0; i < args.length; i++) {
            parameter = parameter + args[i]+" ";
        }
        System.out.println("Parametry:" +parameter);
        IShape shape = factory.CreateShape(ShapeName,args);
        System.out.println();
        System.out.println();
        System.out.println("KONIEC");
        System.out.println(Instant.now());
        System.out.println("Zwrócono: "+shape);
        return shape;

    }

}


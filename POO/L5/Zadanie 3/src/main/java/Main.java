public class Main {
    public static void main(String[] args) throws IllegalAccessException {
        ShapeFactoryLogProxy logProxy = new ShapeFactoryLogProxy();

       logProxy.RegisterWorker(new RectangleFactoryWorker());
        System.out.println();
        System.out.println();
       logProxy.CreateShape("rectangle",4,5);


    }
}

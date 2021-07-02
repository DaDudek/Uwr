import java.util.ArrayList;
import java.util.List;

public class ShapeFactory {
    private final List<IShapeFactoryWorker> workers = new ArrayList<>();

    public ShapeFactory(){
        workers.add(new SquareFactoryWorker());
    }

    public void RegisterWorker(IShapeFactoryWorker worker){
        workers.add(worker);
    }

    public IShape CreateShape(String ShapeName, int... args){
        for (IShapeFactoryWorker worker : workers) {
            if(worker.acceptsParameters(ShapeName)){
                return worker.create(args);
            }
        }
        throw new IllegalArgumentException();
    }
}

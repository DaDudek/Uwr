public class SimpleSingleton {
    private static volatile SimpleSingleton instance;

    private SimpleSingleton(){};

    public synchronized static SimpleSingleton getInstance(){
        if(instance == null){
            instance = new SimpleSingleton();
        }
        return instance;
    }

}

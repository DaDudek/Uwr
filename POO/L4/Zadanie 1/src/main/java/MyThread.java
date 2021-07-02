public class MyThread extends Thread {
    private OneForThreadSingleton instance;

    public void run() {
        instance = OneForThreadSingleton.getInstance();
    }

    public OneForThreadSingleton getInstance() {
        return instance;
    }
}

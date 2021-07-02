public class OneForThreadSingleton {

    private OneForThreadSingleton() {
        // Private constructor
    }

    private static ThreadLocal<OneForThreadSingleton> _threadLocal =
            new ThreadLocal<OneForThreadSingleton>() {
                @Override
                protected OneForThreadSingleton initialValue() {
                    return new OneForThreadSingleton();
                }
            };

    /**
     * Returns the thread local singleton instance
     */
    public static OneForThreadSingleton getInstance() {
        return _threadLocal.get();
    }

}

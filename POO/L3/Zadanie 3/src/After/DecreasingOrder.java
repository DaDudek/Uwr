package After;

import java.util.Comparator;

public class DecreasingOrder<T> implements Comparator<ItemB> {
    @Override
    public int compare(ItemB o1, ItemB o2) {
        return (Double.valueOf(o2.getPrice()).compareTo(Double.valueOf(o1.getPrice())));
    }
}

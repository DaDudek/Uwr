package After;

import java.util.Comparator;

public class AlphabeticOrder<T> implements Comparator<ItemB> {
    @Override
    public int compare(ItemB o1, ItemB o2) {
        return o1.getName().compareTo(o2.getName());
    }
}
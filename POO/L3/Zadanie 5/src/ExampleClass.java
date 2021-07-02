import java.util.Collection;
import java.util.Iterator;

/*
Jak widzimy interfejs collection jest ogromny jednak niektóre metody nie są potrzebne - w szczególności
możemy wyobrazić sobie kolekcje która nigdy nie dostaję wiecej niż jednego obiektu do dodania na raz.
W tym momencie musimy sztucznie rozpisać addAll jako pętle która będzie wywoływać już zaimplementowaną metodę add.
To samo dotyczy innych metod z sufixem "all" - w określonych sytuacjach są to operacje totalnie zbędne / takie których
wykonywanie i tak będzie używać wcześniej zdefiniowanych metod w pętli.

Dodatkowo mając zbiór raczej nie chcemy go konwertować do tablicy ponieważ będzie to nakładać jakiś "porządek" - jak
wiemy elementy w zbiorze nie mają indexów zatem ta metoda również wydaje się zbędna.

Tak samo metoda isEmpty może być nie używana ponieważ mamy metodę size która może spełnić jej role.

 */

public class ExampleClass implements Collection {
    @Override
    public int size() {
        return 0;
    }

    @Override
    public boolean isEmpty() {
        return false;
    }

    @Override
    public boolean contains(Object o) {
        return false;
    }

    @Override
    public Iterator iterator() {
        return null;
    }

    @Override
    public Object[] toArray() {
        return new Object[0];
    }

    @Override
    public boolean add(Object o) {
        return false;
    }

    @Override
    public boolean remove(Object o) {
        return false;
    }

    @Override
    public boolean addAll(Collection c) {
        return false;
    }

    @Override
    public void clear() {

    }

    @Override
    public boolean retainAll(Collection c) {
        return false;
    }

    @Override
    public boolean removeAll(Collection c) {
        return false;
    }

    @Override
    public boolean containsAll(Collection c) {
        return false;
    }

    @Override
    public Object[] toArray(Object[] a) {
        return new Object[0];
    }
}

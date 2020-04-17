import java.io.Serializable;
import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

public class MyCollection<T extends Comparable> implements Serializable {
    List<T> myList = new ArrayList<T>();

    public void addElement(T element) {
        int tmp = myList.size();
        for (int i = 0; i < myList.size(); i++) {
            if (element.compareTo(myList.get(i)) < 1) {
                myList.add(i,element);
                break;
            }
        }

        if(tmp == myList.size()){
            myList.add(element);
        }
    }

    public T removeElement(){
        if (this.myList.size()==0){
            throw new EmptyStackException();
        }
        return this.myList.remove(0);
    }

}

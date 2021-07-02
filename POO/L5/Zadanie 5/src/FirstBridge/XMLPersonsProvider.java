package FirstBridge;

import java.util.ArrayList;
import java.util.List;

public class XMLPersonsProvider extends PersonRegistryFirstBridge{

    public XMLPersonsProvider(PersonNotifier notifier) {
        super(notifier);
    }

    @Override
    public List<Person> getPerson() {
            System.out.println("Skomplikowane wczytywanie z XML");
            List<Person> list = new ArrayList<>();
            list.add(new Person("Karol ","Nowak"));
            list.add(new Person("Mariusz","Kowalski"));
            list.add(new Person("Dawid","Dudek"));
            System.out.println("Przeczytano dokument");
            return list;
    }
}

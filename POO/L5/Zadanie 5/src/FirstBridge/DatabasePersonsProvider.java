package FirstBridge;

import java.util.ArrayList;
import java.util.List;

public class DatabasePersonsProvider extends PersonRegistryFirstBridge{
    public DatabasePersonsProvider(PersonNotifier notifier) {
        super(notifier);
    }

    @Override
    public List<Person> getPerson() {
        System.out.println("Skomplikowane wczytywanie z bazy");
        List<Person> list = new ArrayList<>();
        list.add(new Person("Dawid"," Dudek"));
        list.add(new Person("Oliwia","Slisewka"));
        list.add(new Person("Jan","Nowak"));
        System.out.println("Zakończono wczytanie z bazy");
        return list;
    }
}

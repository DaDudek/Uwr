package SecondBridge;

import java.util.ArrayList;
import java.util.List;

public class DatabasePersonsProvider extends PersonProvider{
    @Override
    public List<PersonS> getPerson() {
        System.out.println("Skomplikowane wczytywanie z bazy");
        List<PersonS> list = new ArrayList<>();
        list.add(new PersonS("Dawid"," Dudek"));
        list.add(new PersonS("Oliwia","Slisewka"));
        list.add(new PersonS("Jan","Nowak"));
        System.out.println("Zakończono wczytanie z bazy");
        return list;
    }
}

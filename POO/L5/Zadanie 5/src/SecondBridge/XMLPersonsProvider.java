package SecondBridge;

import java.util.ArrayList;
import java.util.List;

public class XMLPersonsProvider extends PersonProvider{
    @Override
    public List<PersonS> getPerson() {
        System.out.println("Skomplikowane wczytywanie z XML");
        List<PersonS> list = new ArrayList<>();
        list.add(new PersonS("Karol ","Nowak"));
        list.add(new PersonS("Mariusz","Kowalski"));
        list.add(new PersonS("Dawid","Dudek"));
        System.out.println("Przeczytano dokument");
        return list;
    }
}

package FirstBridge;

import java.util.List;

public class EmailPersonNotifier extends PersonNotifier{
    @Override
    public void notifyPersons(List<Person> persons) {
        System.out.println("Rozpoczynam wysyłanie @");
        for (Person person : persons) {
            System.out.println("wysłano @ do " + person);
        }
    }
}

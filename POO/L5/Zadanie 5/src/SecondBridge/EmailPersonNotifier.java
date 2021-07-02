package SecondBridge;

import java.util.List;

public class EmailPersonNotifier extends PersonRegistrySecondBridge{
    public EmailPersonNotifier(PersonProvider provider) {
        super(provider);
    }

    @Override
    public void NotifyPersons() {
        List<PersonS> personList = getProvider().getPerson();
        System.out.println("Rozpoczynam wysyłanie @");
        for (PersonS person : personList) {
            System.out.println("wysłano @ do " + person);
        }
    }
}

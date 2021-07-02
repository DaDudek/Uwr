package FirstBridge;

import java.util.List;

public class SMSPersonNotifier extends PersonNotifier{
    @Override
    public void notifyPersons(List<Person> persons) {
        System.out.println("Rozpoczynam wysyłanie sms");
        for (Person person : persons) {
            System.out.println("wysłano sms do " + person);
        }
    }
}

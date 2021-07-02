package SecondBridge;

import java.util.List;

public class SMSPersonNotifier extends PersonRegistrySecondBridge{


    public SMSPersonNotifier(PersonProvider provider) {
        super(provider);
    }

    @Override
    public void NotifyPersons() {
        List<PersonS> personList = getProvider().getPerson();
        System.out.println("Rozpoczynam wysyłanie sms");
        for (PersonS person : personList) {
            System.out.println("wysłano sms do " + person);
        }
    }
}

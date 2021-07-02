import FirstBridge.DatabasePersonsProvider;
import FirstBridge.PersonRegistryFirstBridge;
import FirstBridge.SMSPersonNotifier;
import SecondBridge.EmailPersonNotifier;
import SecondBridge.PersonRegistrySecondBridge;
import SecondBridge.XMLPersonsProvider;

public class Main {
    public static void main(String[] args) {
        PersonRegistryFirstBridge firstBridger = new DatabasePersonsProvider(new SMSPersonNotifier());
        firstBridger.NotifyPersons();

        System.out.println();
        System.out.println();

        PersonRegistrySecondBridge secondBridge = new EmailPersonNotifier(new XMLPersonsProvider());
        secondBridge.NotifyPersons();
    }
}

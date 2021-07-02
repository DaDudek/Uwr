package FirstBridge;

import java.util.List;

public abstract class PersonRegistryFirstBridge {
    private PersonNotifier notifier;
    private List<Person> personList;

    public PersonRegistryFirstBridge(PersonNotifier notifier) {
        this.notifier = notifier;
    }

    public abstract List<Person> getPerson();

    public void NotifyPersons(){
        personList = getPerson();
        notifier.notifyPersons(personList);
    }



}

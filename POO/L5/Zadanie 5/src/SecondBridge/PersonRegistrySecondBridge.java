package SecondBridge;

import java.util.List;

public abstract class PersonRegistrySecondBridge {
    private PersonProvider provider;

    public PersonProvider getProvider() {
        return provider;
    }

    public PersonRegistrySecondBridge(PersonProvider provider) {
        this.provider = provider;
    }

    public List<PersonS> getPerson(){
        return provider.getPerson();
    }

    public abstract void NotifyPersons();


}

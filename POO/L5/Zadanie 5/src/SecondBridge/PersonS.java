package SecondBridge;

public class PersonS {
    private String firstName;
    private String lasName;

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLasName() {
        return lasName;
    }

    public void setLasName(String lasName) {
        this.lasName = lasName;
    }

    public PersonS(String firstName, String lasName) {
        this.firstName = firstName;
        this.lasName = lasName;
    }

    @Override
    public String toString() {
        return "SecondBridge.Person{" +
                "firstName='" + firstName + '\'' +
                ", lasName='" + lasName + '\'' +
                '}';
    }
}

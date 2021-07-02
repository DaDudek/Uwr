package FirstBridge;

public class Person {
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

    public Person(String firstName, String lasName) {
        this.firstName = firstName;
        this.lasName = lasName;
    }

    @Override
    public String toString() {
        return "FirstBridge.Person{" +
                "firstName='" + firstName + '\'' +
                ", lasName='" + lasName + '\'' +
                '}';
    }
}

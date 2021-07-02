package Polymorphism;

public class Animal {
    private String name;
    private String sound;

    public Animal() {
    }

    public Animal(String name, String sound) {
        this.name = name;
        this.sound = sound;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSound() {
        return sound;
    }

    public void setSound(String sound) {
        this.sound = sound;
    }

    public void giveSound() {
        System.out.println("Jestem zwierzę "+this.name +" i robie "+this.sound);
    }
}

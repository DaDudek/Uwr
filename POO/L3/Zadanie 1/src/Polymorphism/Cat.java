package Polymorphism;

public class Cat extends Animal{

    public Cat() {
    }

    public Cat(String name, String sound) {
        super(name, sound);
    }

    @Override
    public void giveSound() {
        System.out.println("Jestem kot "+ this.getName() +" i robie " +this.getSound());
    }
}

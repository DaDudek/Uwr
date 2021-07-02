package Polymorphism;

public class Dog extends Animal{
    public Dog() {
    }

    public Dog(String name, String sound) {
        super(name, sound);
    }

    @Override
    public void giveSound() {
        System.out.println("Jestem pies "+ this.getName() +" i robie " +this.getSound());
    }
}

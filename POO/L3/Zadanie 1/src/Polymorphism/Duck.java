package Polymorphism;

public class Duck extends Animal{
    public Duck() {
    }

    public Duck(String name, String sound) {
        super(name, sound);
    }

    @Override
    public void giveSound() {
        System.out.println("Jestem kaczką "+ this.getName() +" i robie " +this.getSound());
    }
}

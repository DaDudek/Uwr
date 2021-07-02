import Controller.Image;
import Controller.ImageController;
import CreatorAndProtectedVariations.DAOFactory;
import CreatorAndProtectedVariations.User;
import CreatorAndProtectedVariations.UserDAO;
import InformationExpert.CzujnikTemperatury;
import InformationExpert.Piec;
import InformationExpert.Wegiel;
import Polymorphism.Animal;
import Polymorphism.Cat;
import Polymorphism.Dog;
import Polymorphism.Duck;

public class Main {
    public static void main(String[] args) {
        //Polymorphism

        Animal[] zoo = new Animal[3];
        zoo[0] = new Dog("burek","hau");
        zoo[1] = new Cat("mruczek","miau");
        zoo[2] = new Duck("dziwaczka","kwa");
        for (Animal animal : zoo) {
            animal.giveSound();
        }
        System.out.println("\n\n\n\n");

        //Creator

        //DAOFactory daoFactory = DAOFactory.getDAOFactory(DAOFactory.GRAPH_DAO);
        DAOFactory daoFactory = DAOFactory.getDAOFactory(DAOFactory.MYSQL_DAO);

        /*Możemy zauważyć,że zasada Protected Variations również jest spełniona tym razem przez userDAO -
            Wiemy, że metoda create jest bardzo zależna od implementacji(tego jakiej bazy używamy) zatem
            w momencie w którym zmienimy baze klient musiałby zmieniać typ zmiennej np z MySQLUser na GraphUser itp.
            Mogłoby to spowodować wiele błędów chociażby w sygnaturach metod. W tym momencie klient wie, że zawsze
            jak chce dodać usera do bazy to potrzebuje wywołać daoFactory.getUserDao().create() - obojętnie jaka
            jest to baza dla klienta ten punkt pozostaje niezmienny dzięki dodatkowej abstrakcji w postaci interfejsu
            UserDAO.
        */
        UserDAO userDAO = daoFactory.getUserDao();
        userDAO.create(new User("Dawid", "Dudek"));
        System.out.println("\n\n\n\n");


        //Controller
        Image image = new Image(100,new ImageController());
        System.out.println(image.getSize());
        image.ImageClick();
        System.out.println(image.getSize());
        System.out.println("\n\n\n\n");



        //InformationExpert
        Wegiel[] wegiels = new Wegiel[10];
        wegiels[0] = new Wegiel();
        wegiels[1] = new Wegiel();
        wegiels[2] = new Wegiel();
        wegiels[3] = new Wegiel();
        Piec piec = new Piec(new Wegiel[10],new CzujnikTemperatury(),4);
        piec.podlozDoPieca();
        piec.podlozDoPieca();
        piec.podlozDoPieca();
        piec.podlozDoPieca();
    }
}

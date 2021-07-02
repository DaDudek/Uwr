package CreatorAndProtectedVariations;

public class GraphUserDao implements UserDAO{
    @Override
    public void create(User user) {
        System.out.println("Do bazy grafowej dodano, obiekt "+user);
    }
}

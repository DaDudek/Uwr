package CreatorAndProtectedVariations;

public class MySQLUserDao implements UserDAO {
    @Override
    public void create(User user) {
        //here insert sql query
        System.out.println("Do bazy dodano,  za pomocą mySQL, obiekt "+user);
    }
}

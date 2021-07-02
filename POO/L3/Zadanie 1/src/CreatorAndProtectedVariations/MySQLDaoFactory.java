package CreatorAndProtectedVariations;

public class MySQLDaoFactory extends DAOFactory{
    @Override
    public UserDAO getUserDao() {
        return new MySQLUserDao();
    }
}

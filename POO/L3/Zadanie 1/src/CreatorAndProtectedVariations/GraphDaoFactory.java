package CreatorAndProtectedVariations;

public class GraphDaoFactory extends DAOFactory {
    @Override
    public UserDAO getUserDao() {
        return new GraphUserDao();
    }
}

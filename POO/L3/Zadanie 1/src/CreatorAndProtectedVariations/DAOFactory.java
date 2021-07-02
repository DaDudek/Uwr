package CreatorAndProtectedVariations;

public abstract class DAOFactory {
    public static final int MYSQL_DAO = 1;
    public static final int GRAPH_DAO = 2;

    private static DAOFactory instance;

    public static DAOFactory getDAOFactory(int factoryType){
        if(factoryType == MYSQL_DAO){
            instance = new MySQLDaoFactory();
        }
        else if(factoryType == GRAPH_DAO){
            instance = new GraphDaoFactory();
        }
        return instance;
    }


    public abstract UserDAO getUserDao();
}

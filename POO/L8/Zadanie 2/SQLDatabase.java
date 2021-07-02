import java.util.ArrayList;
import java.util.List;

public class SQLDatabase {

    public List<Table> getData(){
        Table table = new Table("s",1,2,"d");
        Table table1 = new Table("s",6,1,"d");
        Table table2 = new Table("s",5,4,"d");
        Table table3 = new Table("s",0,7,"d");
        Table table4 = new Table("s",2,8,"d");
        Table table5 = new Table("s",3,3,"d");
        List<Table> tableList = new ArrayList<>();
        tableList.add(table);
        tableList.add(table1);
        tableList.add(table2);
        tableList.add(table3);
        tableList.add(table4);
        tableList.add(table5);
        return tableList;
    }
}

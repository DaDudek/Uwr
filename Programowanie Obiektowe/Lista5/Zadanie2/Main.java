import java.util.Hashtable;

public class Main
{
    public static void main(String[] args)
    {
        Hashtable<String, Integer> varHashTable = new Hashtable<String, Integer>();

        varHashTable.put("x", 0);
        varHashTable.put("z", 2);
        varHashTable.put("y", 7);

        Variable.var_dict = varHashTable;


        Expression test1 = new Add(new Constant(4), new Variable("x"));
        Expression test2 = new Multiply(new Constant(6), test1);
        Expression test3 = new Divide(test1, new Variable("z"));
        Expression test4 = new Subtract(test1, new Variable("y"));
        System.out.println(test1.toString() + " = " + test1.Eval());
        System.out.println(test2.toString() + " = " + test2.Eval());
        System.out.println(test3.toString() + " = " + test3.Eval());
        System.out.println(test4.toString() + " = " + test4.Eval());

    }
}

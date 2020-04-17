import java.util.Hashtable;

public class Variable implements Expression {
    String variable_name;
    static Hashtable<String, Integer> var_dict = new Hashtable<String, Integer>();

    public Variable(String variable){
        this.variable_name = variable;
    }

    public int Eval(){
        return this.var_dict.get(this.variable_name);
    }

    @Override
    public String toString() {
        return variable_name;
    }
}

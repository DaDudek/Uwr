import java.util.HashMap;

public class Context {
    private HashMap<String,Boolean> environment;

    public Context() {
        environment = new HashMap<>();
    }

    public boolean getValue(String variableName){
        if (environment.containsKey(variableName)){
            return environment.get(variableName);
        }
        throw new NoVariableInContextException("no variable in context");
    }

    public boolean setValue(String variableName, boolean value){
        environment.put(variableName,value);
        return true;
    }
}

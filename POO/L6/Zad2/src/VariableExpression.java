public class VariableExpression extends AbstractExpression {
    private String name;

    public VariableExpression(String name) {
        this.name = name;
    }

    @Override
    public boolean Interpret(Context context) {
        return context.getValue(name);
    }
}

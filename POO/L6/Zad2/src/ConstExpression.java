public class ConstExpression extends AbstractExpression {
    private boolean value;

    public ConstExpression(boolean value) {
        this.value = value;
    }

    @Override
    public boolean Interpret(Context context) {
        return value;
    }
}

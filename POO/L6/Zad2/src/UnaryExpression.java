public class UnaryExpression extends AbstractExpression{
    private AbstractExpression expression;
    private UnaryOperator operator;

    public UnaryExpression(AbstractExpression expression, UnaryOperator operator) {
        this.expression = expression;
        this.operator = operator;
    }

    @Override
    public boolean Interpret(Context context) {
        boolean expr = expression.Interpret(context);
        switch (operator){
            case NOT :
                return !expr;
        }
        throw new BadOperatorException();
    }
}

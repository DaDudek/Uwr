public class BinaryExpression extends AbstractExpression{
    private AbstractExpression leftExpression;
    private AbstractExpression rightExpression;
    private BinaryOperator operator;

    public BinaryExpression(AbstractExpression leftExpression, AbstractExpression rightExpression, BinaryOperator operator) {
        this.leftExpression = leftExpression;
        this.rightExpression = rightExpression;
        this.operator = operator;
    }

    @Override
    public boolean Interpret(Context context) {
        boolean left = leftExpression.Interpret(context);
        boolean right = rightExpression.Interpret(context);
        switch (operator){
            case OR:
                return left || right;
            case AND:
                return left && right;
        }
        throw new BadOperatorException("no match for operator");
    }

}

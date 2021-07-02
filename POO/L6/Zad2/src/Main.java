public class Main {
    public static void main(String[] args) {
        Context context = new Context();
        context.setValue("x",false);
        context.setValue("y",true);

        AbstractExpression expression = new BinaryExpression(
                                            new BinaryExpression(
                                                    new VariableExpression("x"),
                                                    new ConstExpression(true),
                                                    BinaryOperator.OR),
                                            new UnaryExpression(new VariableExpression("y"), UnaryOperator.NOT),
                                            BinaryOperator.AND);

        boolean value = expression.Interpret(context);
        System.out.println(value);

    }
}

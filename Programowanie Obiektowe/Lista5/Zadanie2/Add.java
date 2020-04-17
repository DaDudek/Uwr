public class Add implements Expression{

    Expression x;
    Expression y;

    public Add(Expression x, Expression y){
        this.x = x;
        this.y = y;
    }

    @Override
    public int Eval() {
        return this.x.Eval() + this.y.Eval();
    }

    @Override
    public String toString() {
        return "( " + this.x.toString() +" + " + this.y.toString() +" )";
        }
    }

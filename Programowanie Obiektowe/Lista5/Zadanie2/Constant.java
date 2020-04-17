public class Constant implements Expression{
    int val;

    public Constant(int val){
        this.val = val;
    }

    public int Eval(){
        return this.val;
    }

    @Override
    public String toString() {
        return String.valueOf(this.val);
    }
}

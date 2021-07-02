package version2;

public class HeightTreeVisitorT extends TreeVisitorT {
    private int maxDepth;
    private int currentDepth;

    public int getMaxDepth() {
        return maxDepth;
    }

    public void setMaxDepth(int maxDepth) {
        this.maxDepth = maxDepth;
    }

    public int getCurrentDepth() {
        return currentDepth;
    }

    public void setCurrentDepth(int currentDepth) {
        this.currentDepth = currentDepth;
    }

    public HeightTreeVisitorT() {
        maxDepth = 0;
        currentDepth = 0;
    }

    public void visit(TreeT tree){
        if (tree instanceof TreeNodeT){
            VisitNode((TreeNodeT)tree);
        }
        if(tree instanceof TreeLeafT){
            VisitLeaf((TreeLeafT)tree);
        }
    }

    @Override
    public void VisitNode(TreeNodeT node) {
        currentDepth++;
        visit(node.left);
        currentDepth--;

        currentDepth++;
        visit(node.right);
        currentDepth--;
    }

    @Override
    public void VisitLeaf(TreeLeafT leaf) {
        if (maxDepth < currentDepth){
            maxDepth = currentDepth;
        }
    }
}

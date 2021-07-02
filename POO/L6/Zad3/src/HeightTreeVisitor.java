public class HeightTreeVisitor extends TreeVisitor {

    public int visit(Tree tree){
        if (tree instanceof TreeNode){
            return visitNode((TreeNode)tree);
        }
        else if(tree instanceof  TreeLeaf){
            return visitLeaf((TreeLeaf)tree);
        }
        throw new IllegalArgumentException();
    }

    @Override
    public int visitNode(TreeNode node) {
        return Math.max(visit(node.left),visit(node.right)) +1;
    }

    @Override
    public int visitLeaf(TreeLeaf leaf) {
        return 0;
    }
}

import version2.HeightTreeVisitorT;
import version2.TreeLeafT;
import version2.TreeNodeT;
import version2.TreeT;

public class Main {
    public static void main(String[] args) {
        Tree root = new TreeNode(
                        new TreeNode(
                                new TreeLeaf(5),
                                new TreeNode(new TreeLeaf(3),new TreeLeaf(2))),
                        new TreeNode(new TreeLeaf(1),new TreeLeaf(6)));
        HeightTreeVisitor visitor = new HeightTreeVisitor();
        System.out.println(visitor.visit(root));


        // W wersji 2 metoda zwraca void dzięki czemu jest bardziej uniwersalna jednak bardziej złożona koncepcyjnie
        // dodatko do rozwiązania zadania lepsza jest wersja w której visitor zna strukture

        TreeT root1 = new TreeNodeT(
                new TreeNodeT(
                        new TreeLeafT(5),
                        new TreeNodeT(new TreeLeafT(3),new TreeLeafT(2))),
                new TreeNodeT(new TreeLeafT(1),new TreeLeafT(6)));
        HeightTreeVisitorT visitor1 = new HeightTreeVisitorT();
        visitor1.visit(root1);
        System.out.println(visitor1.getMaxDepth());


        TreeT root2 = new TreeLeafT(5);
        HeightTreeVisitorT visitor2 = new HeightTreeVisitorT();
        visitor2.visit(root2);
        System.out.println(visitor2.getMaxDepth());
    }
}

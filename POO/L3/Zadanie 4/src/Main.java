import after.AreaCalculatorB;
import after.RectangleB;
import after.Shape;
import after.SquareB;
import before.AreaCalculator;
import before.Rectangle;
import before.Square;

/*
Jest to przykład zadania które pokazuje, że istnienie jakieś relacji w rzeczywistości
nie zawsze jest dobrym przykładem relacji w obiektowym podejściu. Pomimo, że kwadrat w prawdziwym świecie
jest przykładem prostokąta to ich logika różni się diametralnie - nie można powiedzieć że kwadrat tylko rozszerza
prostokąt - on go całkowicie zmienia. W takim przypadku warto rozważyć inny sposób wspólnej abstrakcji pomiędzy typami.
Zdecydowalem się na zastosowanie klasy abstrakcyjnej shape ponieważ chciałem zachować informacje o polach width height
również w klasach potomnych.
 */

public class Main {
    public static void main(String[] args) {
        int w = 4;
        int h = 5;
        Rectangle rectangle = new Square();
        rectangle.setWidth(w);
        rectangle.setHeight(h);


        AreaCalculator areaCalculator =new AreaCalculator();
        System.out.printf("prostokąt o wymiarach %d na %d ma pole %d\n",w,h,areaCalculator.CalculateArea(rectangle));


        int w1 = 4;
        int h1 = 5;
        Shape rectangle1 = new RectangleB();
        rectangle1.setWidth(w);
        rectangle1.setHeight(h);

        Shape square1 = new SquareB();
        square1.setWidth(w);
        square1.setHeight(h);


        AreaCalculatorB areaCalculator1 =new AreaCalculatorB();
        System.out.printf("prostokąt o wymiarach %d na %d ma pole %d\n",w,h,areaCalculator1.CalculateArea(rectangle1));
        System.out.printf("kwadrat o wymiarach %d na %d ma pole %d\n",h,h,areaCalculator1.CalculateArea(square1));

    }
}

public class Main {
    public static void main(String[] args){
        MyCollection collection = new MyCollection<Integer>();
        Integer x =5;
        Integer y = 7;
        Integer z = 4;
        Integer a = 6;
        Integer b = 7;
        Integer c = 3;
        Integer d = 9;

        collection.addElement(x);
        System.out.println(collection.myList);
        collection.addElement(y);
        System.out.println(collection.myList);
        collection.addElement(z);
        System.out.println(collection.myList);
        collection.addElement(a);
        System.out.println(collection.myList);
        collection.addElement(b);
        System.out.println(collection.myList);
        collection.addElement(c);
        System.out.println(collection.myList);
        collection.addElement(d);
        System.out.println(collection.myList);
        Army szeregowy = new Szeregowy();
        Army kapral = new Kapral();
        Army general = new General();
        System.out.println(szeregowy.compareTo(kapral));
        System.out.println(general.compareTo(szeregowy));
        MyCollection collection1 = new MyCollection<Army>();
        collection1.addElement(general);
        collection1.addElement(szeregowy);
        collection1.addElement(kapral);
        System.out.println(collection1.myList);
        System.out.println(collection1.removeElement());
        System.out.println(collection1.myList);
        collection1.removeElement();
        System.out.println(collection1.myList);
        collection1.removeElement();
        System.out.println(collection1.myList);
        collection1.removeElement(); //throw error because of empty list;
        System.out.println(collection1.myList);


    }

}


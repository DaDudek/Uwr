import java.util.ArrayList;
import java.util.List;

public class XMLDatabase {
    public List<XMLDocument> getData(){
        XMLDocument marka1 = new XMLDocument("audi",null);
        XMLDocument rocznik1 = new XMLDocument("1994",null);
        List<XMLDocument> DaneAuta1 = new ArrayList<>();
        DaneAuta1.add(marka1);
        DaneAuta1.add(rocznik1);
        XMLDocument samochod1 = new XMLDocument("samochod1",DaneAuta1);


        XMLDocument marka2 = new XMLDocument("BardzoDlugaNazwaMarki", null);
        XMLDocument rocznik2 =  new XMLDocument("2001",null);
        List<XMLDocument> DaneAuta2 = new ArrayList<>();
        DaneAuta2.add(marka2);
        DaneAuta2.add(rocznik2);
        XMLDocument samochod2 = new XMLDocument("samochod2",DaneAuta2);


        List<XMLDocument> Samochody = new ArrayList<>();
        Samochody.add(samochod1);
        Samochody.add(samochod2);

        XMLDocument garaz = new XMLDocument("garaz",Samochody);
        List<XMLDocument> xml = new ArrayList<>();
        xml.add(garaz);
        return xml;
    }



}

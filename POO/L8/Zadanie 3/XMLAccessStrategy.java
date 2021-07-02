import javax.swing.text.Document;
import javax.xml.XMLConstants;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.File;
import java.util.List;

public class XMLAccessStrategy implements DataAccessHandlerStrategy<List<XMLDocument>>{
    public void connectToDatabase() {
        System.out.println("Połączono z bazą xml");
    }

    public List<XMLDocument> getData() {
        return new XMLDatabase().getData();
    }

    public void processData(List<XMLDocument> data) {
        int longest = 0;
        for (int i = 0; i < data.size(); i++) {
            int score = countLongest(data.get(i));
            if (score > longest){
                longest = score;
            }
        }
        System.out.println("Najdłuższa nazwa ma długość: "+ longest);;
    }

    private int countLongest(XMLDocument doc){
        if (doc == null){
            return 0;
        }
        int longest = 0;
        int nodeLongest = 0;
        if (doc.getDocument() != null){
            for (int i = 0; i < doc.getDocument().size(); i++){
                nodeLongest = countLongest(doc.getDocument().get(i));
                if (longest < nodeLongest){
                    longest = nodeLongest;
                }
            }
        }
        if (doc.getName().length() > longest){
            longest = doc.getName().length();
        }
        return longest;
    }

    public void closeConnection() {
        System.out.println("Zakończono połączenie z bazą xml");
    }
}

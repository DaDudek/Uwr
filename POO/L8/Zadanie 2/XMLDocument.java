import java.util.List;

public class XMLDocument {
    private String name;
    private List<XMLDocument> document;

    public XMLDocument(String name, List<XMLDocument> document) {
        this.name = name;
        this.document = document;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<XMLDocument> getDocument() {
        return document;
    }

    public void setDocument(List<XMLDocument> document) {
        this.document = document;
    }

    @Override
    public String toString() {
        return "XMLDocument{" +
                "name='" + name + '\'' +
                '}';
    }
}

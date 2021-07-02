package AfterChange;

public class Report {
    private String data;

    public String getData() {
        return data;
    }

    public void formatDocument(){
        this.data = this.data.substring(0,1).toUpperCase()+this.data.substring(1);
    }

    public Report(String data) {
        this.data = data;
    }
}

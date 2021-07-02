package BeforeChange;

public class ReportPrinter {

    public String getData(){
        return "wydrukuj mnie";
    }

    public String FormatDocument(String data){
        return getData().substring(0,1).toUpperCase()+getData().substring(1);
    }

    public void PrintReport(){
        System.out.println(FormatDocument(getData()));
    }


}

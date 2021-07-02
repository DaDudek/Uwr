import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Option> list = new ArrayList<>();
        list.add(Option.Skarga);
        list.add(Option.Pochwala);
        list.add(Option.Zamowienie);
        Request request = new Request("to jest wiadomość która wymaga kilka handlerów",list);
        AbstractHandler handler = AbstractHandler.prepareHandlerByTags(request);
        handler.DispatchRequest(request);
    }
}

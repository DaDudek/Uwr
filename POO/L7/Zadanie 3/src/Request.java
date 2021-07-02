import java.util.List;

public class Request {
    private String message;
    private List<Option> tags;

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public List<Option> getTags() {
        return tags;
    }

    public void setTags(List<Option> tags) {
        this.tags = tags;
    }


    public Request(String message, List<Option> tags) {
        this.message = message;
        this.tags = tags;
    }
}

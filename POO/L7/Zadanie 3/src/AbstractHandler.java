public abstract class AbstractHandler {
    private AbstractHandler next;

    public AbstractHandler getNext() {
        return next;
    }

    public void setNext(AbstractHandler next) {
        this.next = next;
    }

    public static AbstractHandler prepareHandlerByTags(Request request){
        AbstractHandler handler = new ArchiwumHandler();
        for (Option option : request.getTags()) {
            handler.AttachNextHandler(prepareSwitch(option));
        }
        return handler;
    }

    public void AttachNextHandler(AbstractHandler Next){
        if(this.next != null){
            this.next.AttachNextHandler(Next);
        }else{
            this.next = Next;
        }
    }

    public void DispatchRequest(Request request){
        boolean result = this.ProcessRequest(request);
        if (result && (this.next != null)){
            this.next.DispatchRequest(request);
        }
    }

    public abstract boolean ProcessRequest(Request request);

    private static AbstractHandler prepareSwitch(Option option){
        switch (option){
            case Skarga:
                return new SkargiHandler();
            case Archiwum:
                return new ArchiwumHandler();
            case Pochwala:
                return new PochwalneHandler();
            case Pozostale:
                return new PozostaleHandler();
            case Zamowienie:
                return new ZamowieniaHandler();
        }
        return null;
    }
}

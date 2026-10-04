
public abstract class BaseRequestHandler implements RequestHandler {
    protected RequestHandler next;

    @Override
    public void setNext(RequestHandler next) {
        this.next = next;
    }

    @Override
    public abstract void handle(Request request);
}
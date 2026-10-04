


class AuthenticationHandler extends BaseRequestHandler{
    @Override
    public void handle(Request request) {
        if (request.isAuthenticated()) {
            if (next != null) {
                next.handle(request);
            }
        } else {
            throw new RuntimeException("Authentication failed");
        }
    }
}

class LoggingHandler extends BaseRequestHandler {
    @Override
    public void handle(Request request) {
        System.out.println("Simulating logging data into log file");
        if (next != null) {
            next.handle(request);
        }
    }
}

class ValidationHandler extends BaseRequestHandler {
    @Override
    public void handle(Request request) {
        if (validateData(request.getData())) {
            if (next != null) {
                next.handle(request);
            }
        } else {
            throw new RuntimeException("Validation failed");
        }
    }

    public boolean validateData(String data){
        System.out.println("Simulating data validation");
        return true;
    }
}

class RequestProcessingHandler extends BaseRequestHandler {
    @Override
    public void handle(Request request) {
        System.out.println("Simulating request processing...");
        if (next != null) {
            next.handle(request);
        }
    }
}

// LoggingHandler, ValidationHandler, and RequestProcessingHandler classes similar to AuthenticationHandler

class Request {
    private final boolean authenticated;
    private final String data;
    // constructor and getters

    public Request(boolean authenticated, String data) {
        this.authenticated = authenticated;
        this.data = data;
    }

    public boolean isAuthenticated(){
        return this.authenticated;
    }

    public String getData(){
        return this.data;
    }
}

// Usage:
public class HTTPRequest{
    public static void main(String[] args) {
        RequestHandler authHandler = new AuthenticationHandler();
        RequestHandler loggingHandler = new LoggingHandler();
        RequestHandler validationHandler = new ValidationHandler();
        RequestHandler requestHandler = new RequestProcessingHandler();
        
        authHandler.setNext(loggingHandler);
        loggingHandler.setNext(validationHandler);
        validationHandler.setNext(requestHandler);
        
        Request request = new Request(true, "some data");
        
        authHandler.handle(request);       
    }
}
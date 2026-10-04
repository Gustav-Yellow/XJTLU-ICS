public interface State {
    void review(Document doc);
    void approve(Document doc);
    void disapprove(Document doc);    
}

class Draft implements State {

    @Override
    public void review(Document doc){
        System.out.println("Start to review the document");
        doc.setState(new Review());
    }

    @Override
    public void approve(Document doc){
        System.out.println("The document is not being reviewed yet, please review the document before approve");
    }

    @Override
    public void disapprove(Document doc){
        System.out.println("The document is not being reviewed yet, please review the document before disapprove");
    }    
}

class Review implements State {

    @Override
    public void review(Document doc){
        System.out.println("The document is in the middle of reviewing.");
    }

    @Override
    public void approve(Document doc){
        System.out.println("You have approved the document");
        doc.setState(new Approved());        
    }

    @Override
    public void disapprove(Document doc){
        System.out.println("You have disapproved the document");
        doc.setState(new Disapproved());         
    }     
}

class Approved implements State {
    @Override
    public void review(Document doc){
        System.out.println("The document is already approved.");
    }

    @Override
    public void approve(Document doc){
        System.out.println("The document is already approved.");       
    }

    @Override
    public void disapprove(Document doc){
        System.out.println("You have disapproved the previously approved document.");      
        doc.setState(new Disapproved());
    } 
}

class Disapproved implements State {
    @Override
    public void review(Document doc){
        System.out.println("The document is already approved.");
    }

    @Override
    public void approve(Document doc){
        System.out.println("You have approved the previously disapproved document.");       
        doc.setState(new Approved());
    }

    @Override
    public void disapprove(Document doc){
        System.out.println("The document is already disapproved.");      
    } 
}

class Document {

    private State state;

    public Document() {
        state = new Draft(); // initial state
    }

    public void setState(State state) {
        this.state = state;
    }

    public void review(){
        state.review(this);
    }

    public void approve(){
        state.approve(this);
    }

    public void disapprove(){
        state.disapprove(this);
    }
}

public class Workflow {
    public static void main(String[] args)
    {
        Document document = new Document();

        // Edit the document here

        document.review();

        // Review the document here

        document.approve();

        document.approve();
        
        document.review();
        
        document.disapprove();        
    }
}
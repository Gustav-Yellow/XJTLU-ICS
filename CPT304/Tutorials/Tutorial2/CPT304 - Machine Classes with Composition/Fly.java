public class Fly extends Movement{

    @Override
    public void move() {
        // You could implement code that specific to flying

        System.out.println("I am FLYING to (" + super.getPositionX() +
                            "," + super.getPositionY() + 
                            ")");  
    }
    
}

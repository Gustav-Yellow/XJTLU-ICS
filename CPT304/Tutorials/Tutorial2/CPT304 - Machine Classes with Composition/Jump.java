public class Jump extends Movement{

    @Override
    public void move() {
        // You could implement code that specific to jumping

        System.out.println("I am JUMPING to (" + super.getPositionX() +
                            "," + super.getPositionY() + 
                            ")");  
    }
    
}

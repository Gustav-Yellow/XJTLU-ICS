public class Main {
    public static void main(String[] argv){
        
        Machine flyingRifleMachine = new Machine(new Rifle(), new Fly());

        flyingRifleMachine.moveToPosition(122, 94);
        flyingRifleMachine.attack();


        Machine jumpingRifleMachine = new Machine(new Rifle(), new Jump());

        jumpingRifleMachine.moveToPosition(122, 94);
        jumpingRifleMachine.attack();   
        
        

        Machine jumpingLaserMachine1 = new Machine(new Laser(), new Jump());

        jumpingLaserMachine1.moveToPosition(122, 94);
        jumpingLaserMachine1.attack();   
        
        
        Machine jumpingLaserMachine2 = new Machine(new Laser(), new Jump());

        jumpingLaserMachine2.moveToPosition(122, 94);
        jumpingLaserMachine2.attack();         
    }
}

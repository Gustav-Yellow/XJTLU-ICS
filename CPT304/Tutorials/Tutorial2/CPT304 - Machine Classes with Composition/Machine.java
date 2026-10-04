public class Machine {
    private Weapon weapon;
    private Movement movement;

    public Machine(Weapon w, Movement m){
        this.weapon = w;
        this.movement = m;
    }

    public void attack(){
        weapon.shot();
    }

    public void moveToPosition(int x, int y){
        movement.setPositionX(x);
        movement.setPositionY(y);
        movement.move();
    }
}

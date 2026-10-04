public class Laser implements Weapon {
    @Override
    public double shot(){
        System.out.println("I am shoting using Laser");
        return 1.5;
    }
}

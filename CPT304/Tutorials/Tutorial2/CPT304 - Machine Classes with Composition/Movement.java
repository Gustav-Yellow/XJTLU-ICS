public abstract class Movement {
    private int x, y;

    public void setPositionX(int x){
        this.x = x;
    }

    public void setPositionY(int y){
        this.y = y;
    }

    public int getPositionX(){
        return x;
    }

    public int getPositionY(){
        return y;
    }

    public abstract void move();
}

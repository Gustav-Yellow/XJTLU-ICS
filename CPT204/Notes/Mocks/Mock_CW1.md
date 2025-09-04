```java
/*
 * Mock CW1
 */

public class EuclideanPoint {
    private double x;
    private double y;
    
    public EuclideanPoint(double x, double y) {
        this.x = x;
        this.y = y;
    }
    
    public EuclideanPoint() {
        this(0.0, 0.0);
    }
    
    public double getX() {
        return x;
    }
    
    public double getY() {
        return y;
    }

    
    public void setCoordinates(double x, double y) {
		
		this.x = x;
		this.y = y;
		
    }

    // Mock CW1
    public double distanceTo(EuclideanPoint otherPoint) {
		
        double firstPart = otherPoint.x - this.x;
   		double secondPart = otherPoint.y - this.y;
    
    	return Math.sqrt(firstPart * firstPart + secondPart * secondPart);
    }

    public static void main(String[] args) {

        EuclideanPoint point1 = new EuclideanPoint(3.5, 5.2);
        EuclideanPoint point2 = new EuclideanPoint();		
		point2.setCoordinates(7.0, 8.5);

        double distance = point1.distanceTo(point2);
        System.out.println("Distance between Point 1 and Point 2: " + distance);
    }

}
```
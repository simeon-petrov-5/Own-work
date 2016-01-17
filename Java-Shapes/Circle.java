/**
 *
 * @author student
 */
public class Circle implements Figure {
    private double r;
    public Circle(){};
    public Circle(double r) {this.r = r;}
    public void setR(double x){r = x;}
    public double getR(){return r;}
    public double area(){return Math.PI*r*r;}
    public double perimeter(){return Math.PI*2*r;}
    public String toString(){return "Circle: "+"\tR = "+r;}
}

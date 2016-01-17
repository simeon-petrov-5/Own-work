/**
 *
 * @author student
 */
public class Rectangle implements Figure{
    public double w;
    public double h;
    
    public Rectangle(){};
    public Rectangle(double w, double h){
    this.w=w;
    this.h=h;
    }
    
    public void setW(double x){w = x;}
    public double getW(){return w;}
    public void setH(double x){h = x;}
    public double getH(){return h;}
    
    public double area(){return w*h;}
    public double perimeter(){return 2*w + 2*h;}
    public String toString()
    {return "\nRectangle: \tWidth = "+w+"\tHight = "+h;}
}

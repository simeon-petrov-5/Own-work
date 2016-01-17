/**
 *
 * @author student
 */
public class Triangle implements Figure{
    public double a;
    public double b;
    public double c;
    
    public Triangle(){};
    public Triangle(double a, double b, double c){
    this.a = a;
    this.b = b;
    this.c = c;
    }
    public void setA(double x){a = x;}
    public double getA(){return a;}
    public void setB(double x){b = x;}
    public double getB(){return b;}
    public void setC(double x){c = x;}
    public double getC(){return c;}

    public double perimeter(){return (a+b+c)/2;}
    public double area(){return Math.sqrt(perimeter()*(perimeter()-a)*(perimeter()-b)*(perimeter()-c)) ;}
    public String toString()
    {return "\nTriangle: \tSide A = "+a+"\tSide b = "+b+"\tSide c = "+c;}
}

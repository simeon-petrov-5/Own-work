/**
 *
 * @author student
 */
public class Cilinder extends Circle implements Trimeric_Figure{
    private double h;
    public Cilinder(){};
    public Cilinder(double r, double h){
        super(r);
        this.h = h;
    };
    public void setH(double x){h = x;}
    public double getH(){return h;}
    
    public double areaHalf(){return 2*Math.PI*h*super.getR();}
    public double areaFull(){return areaHalf()+2*Math.PI*(super.getR()*super.getR());}
    public double volume(){return Math.PI*(super.getR()*super.getR())*h;}
}


import java.util.Scanner;

/**
 *
 * @author student
 */
public class Test {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Circle c1 = new Circle();
        c1.setR(input.nextDouble());
        System.out.println(c1);
        System.out.println("Area " + c1.area());
        System.out.println("Perimeter " + c1.perimeter());
        
        Rectangle r1 = new Rectangle();
        r1.setH(input.nextDouble());
        r1.setW(input.nextDouble());
        System.out.println(r1);
        System.out.println("Area " + r1.area());
        System.out.println("Perimeter " + r1.perimeter());
        
        Triangle t1 = new Triangle();
        t1.setA(input.nextDouble());
        t1.setB(input.nextDouble());
        t1.setC(input.nextDouble());
        System.out.println(t1);
        System.out.println("Area " + t1.area());
        System.out.println("Perimeter " + t1.perimeter());
        
        Cilinder c2 = new Cilinder();
        c2.setR(input.nextDouble());
        c2.setH(input.nextDouble());
        System.out.println(c2);
        System.out.println("Half area: " + c2.areaHalf());
        System.out.println("Full area: " + c2.areaFull());
        System.out.println("Volume: " + c2.volume());
    }
    
}

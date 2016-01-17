public abstract class Animals {
    private int age;
    private double size;
    public Animals(){}
    public Animals(int age, double size){
    this.age=age;
    this.size=size;    }
    public void setAge(int x){age = x; }
    public int getAge(){return age;}
    public void setSize(double y){size=y;}
    public double getSize(){return size;}
    public abstract void makeNoise();
    public String toString(){
    return "\nSize:"+size+"\tAge:"+age;
    }
}

public class Birds extends Animals{
    private String name;
    private String species;
    private String active;
    private boolean migration;
    public Birds(){super();}
    public Birds(String n, String s, int age, double size, String a, boolean m){
    super(age, size);
    name = n;
    species = s;
    active = a;
    migration = m;    }
    public void setName(String n){name=n;}
    public String getName(){return name;}
    public void setSpecies(String s){species = s;}
    public String getSpecies(){return species;}
    public void setActive(String a){active=a;}
    public String getActive(){return active;}
    public void setMigration(boolean m){migration=m;}
    public boolean getMigration(){return migration;}
    public String toString(){
    return "\nName: "+name+"\nSpecies: "+species+"\nActivness: "+active+"\nMigration: "+migration+super.toString();    }
    public void makeNoise(){
        System.out.println("Gaaaa!");
    }
}
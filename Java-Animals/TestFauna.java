public class TestFauna {
    public static void main(String[] args) {
    String max_brand;
    Birds eagle = new Birds("Johny", "Eagle", 6, 23.5, "During the day", false);
    Birds sparrow = new Birds("Bobi", "Sparrow", 1, 4, "During the day", false);
    System.out.println("Info about my first bird:"+eagle+"\n");
    System.out.println("Info about my second bird:"+sparrow+"\n");
    eagle.makeNoise();
    sparrow.makeNoise();
    }
  }

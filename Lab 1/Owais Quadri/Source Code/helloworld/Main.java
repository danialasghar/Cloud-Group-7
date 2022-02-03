public class Main {
    public static void main(String[] args) {
        System.out.println("Welcome to the Hello World Counter App!");
         int count = 0;
        try {
            while (true) {
                 Thread.sleep(2*1000);
                 System.out.println("Hello World : " + count++);
         }
         } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    }
public class Main {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("Hello world");
        int count = 0;
        while (true) {
            Thread.sleep(1000);
            System.out.println("This is a periodic message #" + count++);
        }
    }
}

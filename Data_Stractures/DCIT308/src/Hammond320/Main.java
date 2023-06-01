package Hammond320;

public class Main {
    public static void main(String[] args) {
        StackArray collection = new StackArray(10);
        for(int i=1; i < 11; i++){
            collection.push(i);
        }
        System.out.println(collection.displayContent());
        System.out.println(collection.pop());
        System.out.println(collection.top());
        collection.push(11);
        System.out.println(collection.displayContent());
        System.out.println(collection.isEmpty());


    }
}
package Hammond320;

public class Main {
    public static void main(String[] args) {
        StackArrayList collection = new StackArrayList();
        for(int i=1; i < 11; i++){
            collection.push(i);
        }

        System.out.println(collection.displayContent());
        collection.push(1010);
        System.out.println(collection.displayContent());
        System.out.println(collection.pop());
        System.out.println(collection.isEmpty());
        System.out.println(collection.top());



    }
}
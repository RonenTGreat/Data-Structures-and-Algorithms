package Hammond320;

public class Main {
    public static void main(String[] args) {
        StackLinkedList<String> collection = new StackLinkedList<>();

        collection.push("Ronen");
        collection.push("Ben");
        collection.push("Ethel");
        collection.push("Vanessa");
        collection.push("William");
        collection.displayContent();


        System.out.println(collection.pop());
        System.out.println(collection.isEmpty());
        System.out.println(collection.top());
        collection.displayContent();



    }
}
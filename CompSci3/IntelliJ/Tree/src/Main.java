
public class Main {

    public static void main(String[] args) {
        Node T = new Node(4);
        T.insert(2);
        T.insert(5);
        T.printInOrder();
        System.out.println(T.contains(5));
        T.printRevOrder();
    }
}

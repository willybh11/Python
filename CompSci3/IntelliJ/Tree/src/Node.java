
public class Node {
    Node left;
    Node right;
    int data;

    public Node(int data) {
        this.data = data;
    }

    public void insert(int value) {
        if (value <= this.data) {
            if (this.left == null) {
                this.left = new Node(value);
            } else {
                this.left.insert(value);
            }
        } else if (this.right == null) {
            this.right = new Node(value);
        } else {
            this.right.insert(value);
        }
    }

    public boolean contains(int value) {
        if (value == this.data) {
            return true;
        } else if (value < this.data) {
            return this.left == null ? false : this.left.contains(value);
        } else {
            return this.right == null ? false : this.right.contains(value);
        }
    }

    public void printInOrder() {
        if (this.left != null) {
            this.left.printInOrder();
        }

        System.out.println(this.data);

        if (this.right != null) {
            this.right.printInOrder();
        }
    }

    public void printRevOrder() {
        if (this.right != null) {
            this.right.printRevOrder();
        }

        System.out.println(this.data);

        if (this.left != null) {
            this.left.printInOrder();
        }
    }
}


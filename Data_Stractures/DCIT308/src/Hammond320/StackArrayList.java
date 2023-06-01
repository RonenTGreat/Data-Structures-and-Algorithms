package Hammond320;

import java.util.ArrayList;
import java.util.List;

public class StackArrayList {
    private final List<Integer> stackList;

    public StackArrayList(){
        this.stackList = new ArrayList<>();
    }

    public void push(int value){
        stackList.add(value);
    }

    public  int pop(){
        if(!isEmpty()){
            int popValue = stackList.get(stackList.size() - 1);
            stackList.remove(stackList.size() - 1);
            return popValue;
        } else{
            throw new RuntimeException("Stack is empty");
        }
    }

    public boolean isEmpty(){
        return  stackList.isEmpty();
    }

    public int top(){
        if (!isEmpty()){
            return stackList.get(stackList.size() - 1);
        } else{
            throw new RuntimeException("Stack is empty");
        }
    }

    public String displayContent(){
        return stackList.toString();
    }
}

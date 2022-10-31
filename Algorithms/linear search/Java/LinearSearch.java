class LinearSearch{
  
  public static int search(int array[], int target){

    for(int i = 0; i < array.length; i++){
      if(array[i] == target){
        return i;
      }
    }
    return -1;
  }

  public static void verify(int index){
    if (index != -1){
      System.out.println("Target found at index: " + index);
    }else{
      System.out.println("Target is not found.");
    }
  }
  public static void main(String[] args){
    int number [] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result_1 = search(number, 5);
    verify(result_1);

    int result_2 = search(number, 11);
    verify(result_2);
  }

}
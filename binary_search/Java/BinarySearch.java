class BinarySearch{
  
  public static int search(int list [], int target){
    int first = 0;
    int last = list.length - 1;

    while(first <= last){
      int midPoint = (first + last) / 2;

      if(list[midPoint] == target){
        return midPoint;
      }else if(midPoint < target){
        first = midPoint + 1;
      }else{
        last = midPoint - 1;
      }
    }
    return -1;
  }


  public static void verify(int index) {
    if (index != -1) {
      System.out.println("Target found at index: " + index);
    } else {
      System.out.println("Target is not found.");
    }
  }

  public static void main(String[] args){
    int number [] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int result_1 = search(number, 1);
    verify(result_1);

    int result_2 = search(number, 11);
    verify(result_2);
}

}
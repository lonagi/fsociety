public class MyBubbleSort {
    public static void main(String[] args) {
        int arr[] = {19,228,173,64,42,106,69,1337,256};

        int n = arr.length;

        //BUBBLE
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-1-i; j++) {

                //SORT
                if(arr[j] < arr[j+1]) {

                    //SWAP
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }

        //OUTPUT
        for(int i = 0; i<n; i++)
            System.out.print(arr[i]+" ");
        System.out.println();
    }
}
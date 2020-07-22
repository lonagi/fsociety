public class MyMergeSort {
    public static void merge(int arr[], int a, int b, int c) {
        int l1 = b-a+1;
        int l2 = c-b;

        int L[] = new int[l1];
        int R[] = new int[l2];

        for(int i = 0; i < l1; i++)
            L[i]=arr[i+a];
        for(int i = 0; i < l2; i++)
            R[i]=arr[i+b+1];

        int i = 0, j = 0;
        int t=a;
        while (i < l1 && j < l2) {
            if(L[i] <= R[j])
            {
                arr[t]=R[j];
                j++;
            }
            else
            {
                arr[t]=L[i];
                i++;
            }
            t++;
        }

        while(i < l1) {
            arr[t]=L[i];
            i++;
            t++;
        }

        while(j < l2) {
            arr[t]=R[j];
            j++;
            t++;
        }
    }

    public static void sort(int arr[], int a, int b) {
        if(a < b){
            int temp = (a+b)/2;

            sort(arr,a,temp); //LEFT
            sort(arr,temp+1,b); //RIGHT

            merge(arr,a,temp,b);
        }
    }

    public static void main(String[] args) {
        int arr[] = {19,228,173,64,42,106,69,1337,256};
        int n = arr.length;

        sort(arr,0,n-1);

        //OUTPUT
        for(int i = 0; i<n; i++)
            System.out.print(arr[i]+" ");
        System.out.println();
    }
}
package JAVA.Sort;
import java.util.Arrays;

class Bubble_sort {
    public static void main(String[] args) {
        int[] lst = {1, 5, 2, 8, 6, 3, 9, 4, 7};
        System.out.println(Arrays.toString(lst));
        for (int i = 0; i < lst.length; i++) {
            for (int j = 0; j < lst.length - i - 1; j++) {
                if (lst[j] > lst[j + 1]) {
                    int tmp = lst[j];
                    lst[j] = lst[j + 1];
                    lst[j + 1] = tmp;
                }
            }
        }
        System.out.println(Arrays.toString(lst));
    }
}
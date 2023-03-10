package JAVA.Sort;

import java.util.Arrays;

public class Select_sort {
    public static void main(String[] args) {
        int[] lst = {1, 5, 2, 8, 6, 3, 9, 4, 7};
        System.out.println(Arrays.toString(lst));
        for (int i = 0; i < lst.length; i++) {
            int min_index = i;
            for (int j = i + 1; j < lst.length; j++) {
                if (lst[min_index] > lst[j])
                    min_index = j;
            }
            int tmp = lst[min_index];
            lst[min_index] = lst[i];
            lst[i] = tmp;
        }
        System.out.println(Arrays.toString(lst));
    }
}

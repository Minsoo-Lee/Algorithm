package JAVA.Sort;

import java.util.Arrays;

public class Quick_sort {
    public static void quickSort(int[] nums) {
        quickSortRecursive(nums, 0, nums.length - 1);
    }

    public static void quickSortRecursive(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int pivotPos = partition(nums, left, right);
        quickSortRecursive(nums, left, pivotPos - 1);
        quickSortRecursive(nums, pivotPos + 1, right);
    }

    public static int partition(int[] nums, int left, int right) {        
        for (int i = left; i < right; i++) {
            if (nums[i] < nums[right]) {
                int tmp = nums[i];
                nums[i] = nums[left];
                nums[left] = tmp;
                left++;
            }
        }
        if (nums[left] > nums[right])
        {
            int tmp = nums[left];
            nums[left] = nums[right];
            nums[right] = tmp;
        }
        return left;
    }
    // POPE쌤 partition
    // public static int partition(int[] nums, int left, int right) {
    //     int pivot = nums[right];

    //     int i = (left - 1);
    //     for (int j = left; j < right; ++j) {
    //         if (nums[j] < pivot) {
    //             ++i;
    //             // swap 함수는 만들면 됨
    //             swap(nums, i, j);
    //         }
    //     }
    //     int pivotPos = i + 1;
    //     swap(nums, pivotPos, right);

    //     return pivotPos;
    // }
    
    public static void main(String[] args) {
        int[] nums = {2, 5, 3, 1, 6, 4, 9, 8, 7};
        quickSort(nums);
        System.out.println(Arrays.toString(nums));
    }
}
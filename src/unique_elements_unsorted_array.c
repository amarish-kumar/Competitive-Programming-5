int unique_elements(int arr[], int len) {

    int distinct_elements[len], i, j, count, flag;

    distinct_elements[0] = arr[0]; // Will always have 'count' elements

    count = 1;

        for(i=0; i < len; i++) {
            flag = 1;

            for(j=0; j < count; j++) {
                
                if(arr[i] == distinct_elements[j]) {
                    flag = 0;
                }
            }

            if(flag == 1) {
                ++count;
                distinct_elements[count-1] = arr[i];
            }
        
            // for(j=0;j<count;j++)
            //     printf("%d ", distinct_elements[j]);
            // printf("\n");
    }
    return count;
}


int main() {
    int arr[15] = {6, 2, 2, 4, 5, 4, 1, 1, 7, 1, 7, 6, 2, 5, 3};
    printf("%d", unique_elements(arr, 15));
    return 0;
}
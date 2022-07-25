void duplicateZeros(int* arr, int arrSize){ 
     
    int *tmp = malloc(arrSize * sizeof(int)); 
    for (int i=0; i < arrSize; i++){ 
        tmp[i] = arr[i]; 
    } 
    int i = 0; 
    for (int p=0; p < arrSize; i++, p++){ 
        arr[p] = tmp[i]; 
        if (tmp[i] == 0){ 
            p++; 
            if (p < arrSize) arr[p] = 0; 
        } 
    } 
}

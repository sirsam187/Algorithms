#include<stdio.h>
int partition(int arr[],int l,int h);
void swap(int *a,int *b){
    int temp=*a;
    *a=*b;
    *b=temp;
}
void quicksort(int arr[],int l,int h){
   if(l<h){
       int p=partition(arr,l,h);
       quicksort(arr,l,p);
       quicksort(arr,p+1,h);
   } 
}
int partition(int arr[],int l,int h){
    int pivot=arr[l];
    int i=l,j=h;
    while(i<j){
        do{
            i++;
        }while(arr[i]<=pivot);
        do{
            j--;
        }while(arr[j]>pivot);
        if(i<j){
            swap(&arr[i],&arr[j]);
        }
    }
    swap(&arr[l],&arr[j]);
    return j;
}
void main(){
    int n,arr[100];
    printf("Enter the length of array \n");
    scanf("%d",&n);
    printf("Enter array:");
    for(int i=0;i<n;i++){
        scanf("%d",&arr[i]);
    }
    quicksort(arr,0,n);
    printf("Sorted array: \n");
    for(int i=0;i<n;i++)
        printf("%d \n",arr[i]);
}

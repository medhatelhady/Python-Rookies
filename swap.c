#include<stdio.h>
#include<stdlib.h>



void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main(){
    int x,y;
    printf("x = ");
    scanf("%d",&x);

    printf("y = ");
    scanf("%d",&y);

    printf("before swapping\n");
    printf("x = %d Y = %d\n", x, y);

    swap(&x, &y);

    printf("After swapping\n");
    printf("x = %d Y = %d\n", x, y);
}


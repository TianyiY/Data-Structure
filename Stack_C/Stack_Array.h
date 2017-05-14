//
//  Stack_Array.h
//  Stack
//
//  Created by Tianyi Yang on 17-3-7.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#ifndef __Stack__Stack_Array__
#define __Stack__Stack_Array__

#include <iostream>
#define MAX_SIZE 101

#endif /* defined(__Stack__Stack_Array__) */


int A[MAX_SIZE];
int top=-1;

void Push(int x){
    if(top==MAX_SIZE-1){
        printf("Error: stack overflow\n");
        return;
    }
    top++;
    A[top]=x;
}

void Pop(){
    if(top==-1){
        printf("Error: no element to pop\n");
        return;
    }
    top--;
}

int Top(){
    return A[top];
}


void Print(){
    int i;
    printf("Stack: ");
    for(i=0; i<=top; i++)
        printf("%d ",A[i]);
    printf("\n");
}



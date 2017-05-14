//
//  Stack_LinkedList.h
//  Stack
//
//  Created by Tianyi Yang on 17-3-7.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#ifndef __Stack__Stack_LinkedList__
#define __Stack__Stack_LinkedList__

#include <iostream>

#endif /* defined(__Stack__Stack_LinkedList__) */

struct Node{
    int data;
    struct Node* link;
};

struct Node* top=NULL;

void Push(int x){
    struct Node* temp=(struct Node*)malloc(sizeof(struct Node*));
    temp->data=x;
    temp->link=top;
    top=temp;
}

void Pop(){
    struct Node* temp;
    if(top==NULL) return;
    temp=top;
    top=top->link;
    free(temp);
}
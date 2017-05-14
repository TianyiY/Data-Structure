//
//  Queue_Linkedlist.h
//  Queue
//
//  Created by Tianyi Yang on 17-3-7.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#ifndef __Queue__Queue_Linkedlist__
#define __Queue__Queue_Linkedlist__

#include <iostream>

#endif /* defined(__Queue__Queue_Linkedlist__) */

struct Node{
    int data;
    struct Node* next;
};

struct Node* front=NULL;
struct Node* rear=NULL;

void Enqueue(int x){
    struct Node* temp=(struct Node*)malloc(sizeof(struct Node*));
    temp->data=x;
    temp->next=NULL;
    if(front==NULL && rear==NULL){
        front=rear=temp;
        return;
    }
    rear->next=temp;
    rear=temp;
}


void Dequeue(){
    struct Node* temp=front;
    if(front==NULL) return;
    if(front==rear){
        front=rear=NULL;
    }
    else{
        front=front->next;
    }
    free(temp);
}
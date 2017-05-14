//
//  ContactList.cpp
//  linkedlist
//
//  Created by Tianyi Yang on 17-2-23.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#include "ContactList.h"
using namespace std;

ContactList::ContactList():head(0), size(0)
{
    
};

void ContactList::addToHead(const string& name)
{
    Contact* newOne=new Contact(name);
    
    if(head==0)
    {
        head=newOne;
    }
    else
    {
        newOne->next=head;
        head=newOne;
    
    }
    
    size++;
};


void ContactList::printList()
{
    Contact* tp=head;
    while(tp!=0)
    {
        cout << *tp<<endl;
        tp=tp->next;
    };

};


void ContactList::insert(const string& name)
{
    Contact* newNode=new Contact(name);
    // case 1- empty list
    if(head==0)
    {
        head=newNode;
    }
    else
    {
        Contact* curr=head;
        Contact* trail=0;
        
        //Terverse list to find insert location
        while(curr!=0)
        {
            if(curr->name >= newNode->name)
            {
                break;
            }
            else
            {
                trail=curr;
                curr=curr->next;
            }
        }
        
        // case 2- insert at head (not empty)
        if (curr==head)
        {
            newNode->next=head;
            head=newNode;
        }
        else
        {
            // case 3- insert after head (not empty)
            newNode->next=curr;
            trail->next=newNode;
        }
    }
    
    size++;
       
};


void ContactList::deleteNode(const string& name)
{
    //case 1 -empty list
    if (head==0)
    {
        cout<<"Contact can not be deleted from an empty list."<<endl;
    }
    else
    {
        Contact* curr=head;
        Contact* trail=0;
        
        //traverse list to find node to delete
        while(curr!=0)
        {
            if (curr->name==name)
            {
                break;
            }
            else
            {
                trail=curr;
                curr=curr->next;
            }
        }
        //case 2- Node with "name" not found in list
        if (curr==0)
        {
            cout<<"Contact with name: "<<name<<" not found."<<endl;
        }
        else
        {
            //case 3- delete from the head node
            if (head==curr)
            {
                head=head->next;
            }
            //case 4- delete beyond the head node
            else
            {
                trail->next=curr->next;
            }
            delete curr;
            size--;
        }
    }
}


void ContactList::reversePrintList()
{
    reversePrintWorker(head);
}


void ContactList::reversePrintWorker(Contact* curr)
{
    if(curr!=0)
    {
        reversePrintWorker(curr->next);
        cout << *curr << endl;
    }
}
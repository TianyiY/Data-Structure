//
//  ContactListApp.cpp
//  linkedlist
//
//  Created by Tianyi Yang on 17-2-23.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#include "ContactList.h"
using namespace std;

int main()
{
    ContactList* cl1=new ContactList();
    
    string name;
    
    while(true)
    {
        cout<<"Enter the name of the contact or q to quit."<<endl;
        cin>>name;
        if(name=="q")
            break;
        cl1->insert(name);
        
    }
    
    while(true)
    {
        cout<<"Enter the name of the contact to delete or q to quit."<<endl;
        cin>>name;
        if(name=="q")
            break;
        cl1->deleteNode(name);
        cl1->printList();
    }
    
    cl1->reversePrintList();
    
};

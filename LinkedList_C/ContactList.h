//
//  ContactList.h
//  linkedlist
//
//  Created by Tianyi Yang on 17-2-23.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#ifndef __linkedlist__ContactList__
#define __linkedlist__ContactList__

#include "Contact.h"
#include <iostream>

class ContactList
{
public:
    ContactList();
    void addToHead(const std::string&);
    void printList();
    void insert(const std::string&);
    void deleteNode(const std::string&);
    void reversePrintList();
    
private:
    void reversePrintWorker(Contact*);
    Contact* head;
    int size;
};

#endif /* defined(__linkedlist__ContactList__) */

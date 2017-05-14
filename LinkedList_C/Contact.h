//
//  Contact.h
//  linkedlist
//
//  Created by Tianyi Yang on 17-2-23.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#ifndef __linkedlist__Contact__
#define __linkedlist__Contact__

#include <iostream>
#include <string>

class Contact
{
    friend std::ostream& operator<<(std::ostream& os, const Contact& c);
    friend class ContactList;
    
public:
    Contact(std::string name="none");
    
private:
    std::string name;
    Contact* next;

};



#endif /* defined(__linkedlist__Contact__) */

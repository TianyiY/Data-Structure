//
//  Contact.cpp
//  linkedlist
//
//  Created by Tianyi Yang on 17-2-23.
//  Copyright (c) 2017年 Tianyi Yang. All rights reserved.
//

#include "Contact.h"

using namespace std;

Contact::Contact(string n):name(n), next(NULL)
{
    

};

ostream& operator<<(ostream& os, const Contact& c)
{
    return os<<"Name: "<<c.name;

};
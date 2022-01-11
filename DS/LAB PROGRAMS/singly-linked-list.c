#include <stdio.h>
#include <stdlib.h>

struct node
{
    int info;
    struct node *link;
};

typedef struct node *NODE;

NODE getnode()
{
    NODE temp;
    temp = (NODE)malloc(sizeof(struct node));
    if (temp == NULL)
    {
        printf("out of memory\n");
        return NULL;
    }
    return temp;
}

NODE insert_front(int item, NODE first)
{
    NODE temp;
    temp = getnode();
    temp->info = item;
    temp->link = NULL;
    if (first == NULL)
    {
        return temp;
    }
    temp->link = first;
    return temp;
}
NODE insert_rear(int item, NODE first)
{
    NODE temp, cur;
    temp = getnode();
    temp->info = item;
    temp->link = NULL;
    if (first == NULL)
    {
        return temp;
    }
    cur = first;
    while (cur->link != NULL)
    {
        cur = cur->link;
    }
    cur->link = temp->link;
    return first;
}

NODE delete_front(NODE first){
    NODE temp;
    temp=first->link;
    if (first==NULL){
    printf("list is empty\n");
    return NULL;    
    }
    if (first->link==NULL)
    {
    printf("deleted item is %d",first->info);
    free(first);
    return NULL;       
    }

    printf("deleted item is %d",first->info);
    free(first);
    return temp;
}


NODE delete_rear(NODE first){
    NODE cur, prev;
    if (first==NULL){
    printf("list is empty\n");
    return NULL;    
    }
    if (first->link==NULL)
    {
    printf("deleted item is %d",first->info);
    free(first);
    return NULL;       
    }

    printf("deleted item is %d",first->info);
    free(first);
    cur=first->link;
    prev=NULL;

    while (cur->link!=NULL){
        prev=cur;
        cur=cur->link;
    }
    free(cur);
    prev->link=NULL;
    return first;
}

void display(NODE first){
    if (first==NULL)
    {
        printf("list is empty\n");
        return;
    }
    NODE cur;
    cur=first;
    while(cur!=NULL)
    {
        printf("%d\t",cur->info);
        cur=cur->link;
    }
    printf("\n");
}


int main()
{
    int item,ch;
    NODE first=NULL;

    for (;;)
    {
        printf("enter the choice 1 2 3 4 5 6\n");
        scanf("%d",&ch);
        switch (ch)
        {
        case 1: 
            printf("enter the item\n");
            scanf("%d",&item);
            first = insert_front(item,first);
            break;
        
        case 2: 
            printf("enter the item\n");
            scanf("%d",&item);
            first = insert_rear(item,first);
            break;
        
        case 3: 
            first = delete_front(first);
            break;
        
        case 4: 
            first = delete_rear(first);
            break;
        case 5:
            display(first);
            break;
        default:
            exit(0);
            break;
        }
    }
    
    return 0;
}
#include<stdio.h>
#include<stdlib.h>
#define SIZE 5

int s[SIZE], top = -1, element;
void push();
int pop();
void display();

int main()
{
    int ch,item,del;
    for (;;)
    {
        printf("enter 1 2 3 4 \n");
        scanf("%d",&ch);
        switch (ch)
        {
        case 1:
            printf("enter the item\n");
            scanf("%d",&element);
            push();
            break;
        case 2:
            del=pop();
            if(del==-1){
                printf("stack underflow\n");
            }
            else{
                
                printf("deleted item is %d\n",del);
            }
            break;
        case 3:
            display();
            break;
        default:
            break;
        }
    }
    return 0;
}

void push(){
    if(top==SIZE-1){
        printf("stack overflow\n");
        return;
    }
    s[++top]=element;
}

int pop(){
    if(top==-1){
    return -1;
    }
    return s[top--];
}

void display(){
    if(top==-1){
        printf("stack underflow\n");
        return ;
    }

    for (int i = 0; i <= top; i++)
    {
        printf("%d\t",s[i]);
        
    }
    printf("\n");
    return;
    
}
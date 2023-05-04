#include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
};
struct node *insert_after(struct node *);
struct node *delete_after(struct node *);

int main(){
    struct node *head = malloc(sizeof(struct node));//머리 노드 생성 및 데이터 저장 x

    struct node *node1 = malloc(sizeof(struct node));//첫 번째 노드 생성
    head->next = node1;//머리 노드와 노드1 연결
    node1->data = 10;// 노드1 data 10 저장

    struct node *node2 = malloc(sizeof(struct node));//두 번째 노드 생성
    node1->next = node2;
    node2->data = 20;
    node2->next = NULL;

    insert_after(head);
    struct node *PTR = head->next;
    while(PTR != NULL){
        printf("%d\n", PTR->data);
        PTR = PTR->next;
    }

    delete_after(head);
    PTR = head->next;
    while(PTR != NULL){
        printf("%d\n", PTR->data);
        PTR = PTR->next;
    }
    return 0;
}

struct node *insert_after(struct node *start){
    struct node *new_node, *ptr, *preptr;
    int num, val;

    printf("\n Enter the data: ");
    scanf("%d", &num);
    printf("\n Enter the value after which the data has to be inserted : ");
    scanf("%d", &val);

    new_node = (struct node *)malloc(sizeof(struct node));
    new_node -> data = num;
    ptr = start;
    preptr = ptr;

    while(preptr->data != val){
        preptr = ptr;
        ptr = ptr->next;
    }

    preptr->next = new_node;
    new_node -> next = ptr;

    return start;
}

struct node *delete_after(struct node *start){
    struct node *ptr, *preptr;
    int num;
    printf("\nEnter the data you want to delete : ");
    scanf("%d", &num);
    ptr = start;
    preptr = ptr;

    while(ptr->data != num){
        preptr = ptr;
        ptr = ptr->next;
    }
    preptr->next = ptr->next;
    free(ptr);

    return start;
}

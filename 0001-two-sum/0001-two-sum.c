#include <stdlib.h>

#define HASH_SIZE 10007

typedef struct Node {
    int key;
    int index;
    struct Node *next;
} Node;

int hash(int key) {
    if (key < 0)
        key = -key;
    return key % HASH_SIZE;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {

    Node* table[HASH_SIZE] = {NULL};

    int* result = (int*)malloc(2 * sizeof(int));

    for (int i = 0; i < numsSize; i++) {

        int complement = target - nums[i];
        int h = hash(complement);

        Node* curr = table[h];

        while (curr) {
            if (curr->key == complement) {
                result[0] = curr->index;
                result[1] = i;
                *returnSize = 2;
                return result;
            }
            curr = curr->next;
        }

        h = hash(nums[i]);

        Node* newNode = (Node*)malloc(sizeof(Node));
        newNode->key = nums[i];
        newNode->index = i;
        newNode->next = table[h];
        table[h] = newNode;
    }

    *returnSize = 0;
    return NULL;
}
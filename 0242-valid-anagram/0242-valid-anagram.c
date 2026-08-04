#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(char*)a - *(char*)b);
}

bool isAnagram(char* s, char* t) {
    int n1 = strlen(s);
    int n2 = strlen(t);

    if (n1 != n2)
        return false;

    qsort(s, n1, sizeof(char), compare);
    qsort(t, n2, sizeof(char), compare);

    return strcmp(s, t) == 0;
}
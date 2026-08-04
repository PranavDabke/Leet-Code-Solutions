#include <string.h>

int firstUniqChar(char *s) {
    int count[26] = {0};

    // Count frequency of each character
    for (int i = 0; s[i] != '\0'; i++)
        count[s[i] - 'a']++;

    // Find first character with frequency 1
    for (int i = 0; s[i] != '\0'; i++) {
        if (count[s[i] - 'a'] == 1)
            return i;
    }

    return -1;
}
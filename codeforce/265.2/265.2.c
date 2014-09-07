#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *lexicographicalNextString(char *src, char *dest, int p)
{
    int n = strlen(src);
    int i;
    strcpy(dest, src);
    for (i = n - 1; i >= 0; i--)
    {
        if (dest[i] + 1 <= 'a' + p - 1)
        {
            dest[i]++;
            return dest;
        }
        else
        {
            dest[i] = 'a';
        }
    }
    return NULL;
}

int main(int argc, char **argv)
{
    int n, p;
    char text[1024], newText[1024];
    char ch, *ptr = NULL;
    int i, j;
    int subPalin = 0;
    scanf("%d%d", &n, &p);
    scanf("%s", text);
    strcpy(newText, text);

    while ((ptr = lexicographicalNextString(newText, newText, p)))
    {
        if (!palindromeSubstring(newText))
        {
            /*printf("YES:\n");*/
            printf("%s\n", newText);
            return 1;
        }
    }

    if (!ptr)
    {
        printf("NO\n");
        return 0;
    }
    /*for (i = n - 1; i >= 0; i--)*/
    /*{*/
    /*for (ch = text[i] + 1; ch <= 'a' + p - 1; ch++)*/
    /*{*/
    /*newText[i] = ch;*/
    /*if (!palindromeSubstring(newText))*/
    /*{*/
    /*printf("%s", newText);*/
    /*return 1;*/
    /*}*/
    /*else*/
    /*{*/
    /*newText[i] = text[i];*/
    /*}*/
    /*}*/
    /*}*/
}

int isPalindrome(char *text)
{
    int i, j;
    int n = strlen(text);

    for (i = 0, j = n - 1; i < j; i++, j--)
    {
        if (text[i] != text[j])
        {
            return 0;
        }
    }
    return 1;
}

int palindromeSubstring(char *text)
{
    int n = strlen(text);
    int(*table)[n] = malloc(sizeof(int) * n * n);
    int i, j;
    memset(table, 0, sizeof(int) * n * n);
    /*printf("%s,%d\n", text, n);*/
    for (j = 0; j < n; j++)
        for (i = 0; i <= j; i++)
        {
            if (text[i] == text[j] && (j - i < 2 || table[i + 1][j - 1]))
            {
                table[i][j] = 1;
                if (j - i >= 1)
                {
                    return 1;
                }
            }
        }
    return 0;
}

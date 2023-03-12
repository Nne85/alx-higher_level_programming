#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if not palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
    listint_t *end = *head;
    int count = 0;
    int arr[10000];

    while (end != NULL)
    {
        arr[count] = end->n;
        end = end->next;
        count++;
    }

    for (int i = 0; i < count / 2; i++)
    {
        if (arr[i] != arr[count - i - 1])
            return (0);
    }

    return (1);
}


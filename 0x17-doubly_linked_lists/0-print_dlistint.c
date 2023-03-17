#include "lists.h"
#include <stdio.h>
/**
 * print_dlistint - Prints all the elements of a dlistint_t list.
 *
 * @h: A pointer to the head of the dlistint_t list.
 *
 * Return: The number of nodes in the dlistint_t list.
 */
size_t print_dlistint(const dlistint_t *h)
{
    const dlistint_t *current = h;
    size_t count = 0;

    while (current != NULL)
    {
        printf("%d\n", current->n);
        current = current->next;
        count++;
    }

    return (count);
}

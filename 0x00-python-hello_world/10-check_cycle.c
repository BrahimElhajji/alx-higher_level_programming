#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * check_cycle - Checks if the list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 1 If there is no cycle and 0 If there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *quick, *lazy;

	if (list == NULL || list->next == NULL)
		return (0);

	lazy = list->next;
	quick = list->next->next;

	while (lazy && quick && quick->next)
	{
		lazy = lazy->next;
		quick = quick->next->next;

		if (lazy == quick)
			return (1);

	}

	return (0);
}

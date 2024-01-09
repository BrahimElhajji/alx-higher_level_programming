#include "lists.h"



int is_palindrome(listint_t **head)
{
	listint_t *p = *head;
	listint_t *q = *head;
	listint_t *lunch_sec = NULL;

	while (1)
	{

		if (p == NULL || p->next == NULL)
		{
			lunch_sec = q->next;
			break;
		}

		p = p->next->next;
		q = q->next;
	}

	rev_list(&lunch_sec);

	int is_palindrome = c(*head, lunch_sec);

	rev(&lunch_sec);

	return (is_palindrome);
}

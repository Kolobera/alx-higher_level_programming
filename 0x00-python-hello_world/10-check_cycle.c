#include "lists.h"

/**
 * check_cycle - check if it exist a cycle in a linked list
 * @list: listint_t type
 * Return: 1 if there is a cycle or 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = list;
	second = list;
	while (first != NULL && second != NULL && second->next != NULL)
	{
		second = second->next->next;
		first = first->next;
		if (second == first)
			return (1);
	}
	return (0);
}

#include "lists.h"

/**
 *print_dlistint - print all the elements
 *@h: The head oh the list
 *Return: the number of numbers
 */
size_t print_dlistint(const dlistint_t *h)
{
const dlistint_t *tempo = h;
size_t x = 0;
if (tempo)
{
	while (tempo)
	{
		printf("%d\n", tempo->n);
		x += 1;
		tempo = tempo->next;
	}

}
return (x);
}

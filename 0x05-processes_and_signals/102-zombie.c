#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
/**
 * infinite_while - runs indefinitely
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main program
 * Return: always 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		if (fork() > 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
		}
		else
		{
			sleep(1);
			exit(0);
		}
	}
	infinite_while();

	return (0);
}

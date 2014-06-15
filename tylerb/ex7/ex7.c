#include <stdio.h>

int main(int argc, char *argv[]){
	long universe_of_defects = 1 * 1024 * 1024 * 1024;
	printf("the entire universe has %ld.\n",universe_of_defects);

	int bugs = 100;
	double bug_rate = 1.2;
	printf("You have %d bugs at the imaginary rate of %f.\n", bugs, bug_rate);


	double part_of_universe = 100.00 / 20;
	printf("that is only a %e portion of the universe\n",part_of_universe);

	char nul_byte = '\0';
	int care_percentage = 8 * nul_byte;
	printf("which means you should care %d%%.\n",care_percentage);
	
	return 0;
}

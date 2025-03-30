#include <stdio.h>

int main() {
    float marks[5], total = 0, percentage;
    char *subjects[] = {"Physics", "Chemistry", "Biology", "Mathematics", "Computer"};
    
    // Input marks using loop
    for (int i = 0; i < 5; i++) {
        printf("Enter marks for %s: ", subjects[i]);
        scanf("%f", &marks[i]);
        total += marks[i];
    }
    
    // Calculate percentage
    percentage = (total / 500) * 100;
    
    // Determine grade using switch
    char grade;
    switch ((int)percentage / 10) {
        case 10:
        case 9: grade = 'A';
            break;
        case 8: grade = 'B';
            break;
        case 7: grade = 'C';
            break;
        case 6: grade = 'D';
            break;
        case 5: grade = 'E';
            break;
        default: grade = 'F';
    }
    
    // Output results
    printf("Total Marks: %.2f\n", total);
    printf("Percentage: %.2f%%\n", percentage);
    printf("Grade: %c\n", grade);
    
    return 0;

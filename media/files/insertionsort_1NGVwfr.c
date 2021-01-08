#include <stdio.h>
int main()
{
// insert sort
int A[12] = {3, 7, 5, 9, 7, 1, 2, 5, 3, 8, 20, 15};
int size = 12;
int t, i, j;
for (i = 1; i < size+1; i++)
{
t = A[i];
j = i - 1;
while ((t < A[j]) && (j >= 0))
{
A[j + 1] = A[j];
j = j - 1;
}
A[j + 1] = t;
}
for (size_t i = 0; i < size; i++)
{
printf("%d ", A[i]);
}
}

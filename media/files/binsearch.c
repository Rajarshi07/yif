#include<stdio.h>
int main()
{
// binary search
int last = 12, first = 0, middle, i;
int num = 7;
int a[12] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20};
while (last>=first)
{
middle = (first + last) / 2;
if (a[middle] == num)
{
printf("%d", middle);
break;
}
else
{
if (a[middle]>num)
{
last = middle - 1;
}
else
{
first = middle + 1;
}
}
}
}

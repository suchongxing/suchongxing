#include<stdio.h>
void disp(int a[],int n)
{
	int i;
	for(i=0;i<n;i++)
		printf(" %d",a[i]);
}
int HF(int a[],int s ,int t)
{
	int i=s,j=t;
	int tmp=a[s];
	while (i!=j)
	{
		while (j>i&&a[j]>=tmp)
			j--;
		a[i]=a[j];
		while (i<j&&a[i]<=tmp)
			i++;
		a[j]=a[i];
		
	}
	a[i]=tmp;
	return i;
}

void QS(int a[],int s,int t)
{
	if (s<t)
	{
		int i = HF(a,s,t);
		QS(a,s,i-1);
		QS(a,i+1,t);
		 
	}
}
int main()
{
	int n=10;
	int a[]={2, 5, 1, 7, 10, 6, 9, 4, 3, 8};
	printf("ÅÅÐòÇ°£º");
	disp(a,n);
	QS(a,0,n-1);
	printf("ÅÅÐòºó£º");
	disp(a,n);
	 
}

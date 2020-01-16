//递归方法实现二分查找 
#include<stdio.h>
int DS(int a[],int low,int higt,int k)
{
	int mid;
	if(low<=higt)
	{
		mid=(low+higt)/2;
		if (a[mid]==k)
			return mid;
		if(a[mid]>k)
			return DS(a,low,mid-1,k);
		else 
			return DS(a,mid+1,higt,k);
		
	}
	else 
	   return -1;
	  	
} 

int main()
{
	int n=10,i;
	int k=6;

	int a[]={1,2,3,4,5,6,7,8,9,10}; 
	printf("数组为：");
    for(int i=0;i<n;i++)
	printf("%3d",a[i]);
	i=DS(a,0,n-1,k);
	if(i>=0)
		printf("\na[%d]=%d",i,k);
	else
		printf("未找到%d元素\n",k); 
}

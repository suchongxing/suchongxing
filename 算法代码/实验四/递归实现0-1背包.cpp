//https://blog.csdn.net/luojinping/article/details/6900788�ο����� 

#include<iostream>
using namespace std;
 
const int W = 150;
const int number = 5;
const int VALUE[] = {60, 20, 10, 60, 100};
const int WEIGHT[] = {20, 30, 50, 60, 80};
 
 
//function Make( i {������i����Ʒ} , j{ʣ��Ŀռ�Ϊj}) :integer;
int Make(int i, int j)
{  
	int r1 = 0;
	int r2 = 0;
	int r = 0;
	
	if (i == -1)
	{
		return 0;
	}
 
	if(j >= WEIGHT[i])   //����ʣ��ռ���Է�����Ʒ i  
	{
		r1 = Make(i-1,j - WEIGHT[i]) + VALUE[i]; //��i����Ʒ�������ܵõ��ļ�ֵ
		r2 = Make(i-1,j); //��i����Ʒ�������ܵõ��ļ�ֵ  
		r = (r1>r2)?r1:r2;
	}   
 
	return r;
}
 
 
int main()
{
	int maxValue = Make(number-1, W);
	cout<<"maxValue: "<<maxValue<<endl;
}
 

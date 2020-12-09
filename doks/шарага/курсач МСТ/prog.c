#include<reg51.h>

sbit P1_0 = 0x90;
sbit P1_1 = 0x91;
sbit P1_2 = 0x92;
sbit P1_3 = 0x93;

sbit P0_4 = 0x84;
sbit P0_5 = 0x85;
sbit P0_6 =0x86;

sbit P3_3=0xb3;

unsigned char KeyNum(void)	
				
{
P1=0;
P0_4=0;
P0_5=1;
P0_6=1;
if(P1_0==0)return(6);		//do
if(P1_1==0)return(46);	//re diez
if(P1_2==0)return(79);	//fa diez
if(P1_3==0)return(107);	//la
P0_4=1;
P0_5=0;
P0_6=1;
if(P1_0==0)return(20);	//do diez
if(P1_1==0)return(57);	//mi
if(P1_2==0)return(89);	//sol
if(P1_3==0)return(116);	//la diez
P0_4=1;
P0_5=1;
P0_6=0;
if(P1_0==0)return(33);	//re
if(P1_1==0)return(68);	//fa
if(P1_2==0)return(98);	//sol diez
if(P1_3==0)return(123);	//si
return(0);
}

void main(void)
{
unsigned char I;

TMOD=(TMOD & 0xcf);
TMOD=(TMOD | 0x20);
TF1=0;
TR1=0;
while (1)
{
	
while(KeyNum() == 0);
	
TH1=KeyNum();


TR1=1;

for(I=0;I<16;I++)
{
while(TF1==0);
TF1=0;
}
P3_3=!P3_3;
}
}
void setup(){
 
  size(500,500);
}

void draw (){
  background(200,70,100);
  translate(width/2,height/2);
  int r = 220;
  int r2 = 210;
  int r3 = 200;
 
  int h = 12;
  int m = 60;
  float angulo = TWO_PI/h;
  float angulo2 = TWO_PI/m;
  ellipse(0, 0, r*2,r*2);
  ellipse(0, 0, 8, 8);
 
  stroke(10, 70, 255);
  for(int i = 0; i<h; i++){
    int hour = hour();
    float xfirst= r3*cos(angulo*i-HALF_PI);
    float yfirst = r3 *sin(angulo*i-HALF_PI);
    float xsecond= r *cos(angulo*i-HALF_PI) ;
    float ysecond = r *sin(angulo*i-HALF_PI) ;
   
    line(xfirst,yfirst,xsecond,ysecond);
   
    if(i == hour || i == (hour-12)){
      float teste= (r3-70)*cos(angulo*i-HALF_PI);
      float teste2 = (r3-70) *sin(angulo*i-HALF_PI);
     
      line(teste,teste2,0,0);
    }
  }
   
  for(int i = 0; i<m; i++){
    int minute = minute();
    float xfirst = r3 *cos(angulo2*i-HALF_PI) ;
    float yfirst= r3 *sin(angulo2*i-HALF_PI) ;
    float xsecond = r2 *cos(angulo2*i-HALF_PI) ;
    float ysecond= r2 *sin(angulo2*i-HALF_PI) ;
   
    line(xfirst,yfirst,xsecond,ysecond);  
   
    if(i == minute){
      float teste= (r3-20)*cos(angulo2*i-HALF_PI);
      float teste2 = (r3-20) *sin(angulo2*i-HALF_PI);

      line(teste,teste2,0,0);
    }
  }  
}

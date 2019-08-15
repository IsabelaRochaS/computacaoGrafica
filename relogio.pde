void setup(){
 
  size(500,500);
  ellipseMode(CENTER);
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
  fill(241,207,225);
  ellipse(0, 0, r*2,r*2);
  ellipse(0, 0, 8, 8);
  
  stroke(10, 70, 255);
  for(int i = 0; i<h; i++){

    float xfirst= r3*cos(angulo*i-HALF_PI);
    float yfirst = r3 *sin(angulo*i-HALF_PI);
    float xsecond= r *cos(angulo*i-HALF_PI) ;
    float ysecond = r *sin(angulo*i-HALF_PI) ;
    
    //fill(10, 70, 255);
    //textSize(15);
    //text(str(i), xfirst,yfirst); 
    line(xfirst,yfirst,xsecond,ysecond);
  }
  
  float hour = hour() + minute()/60.0;
  float testea= (r3-70)*cos(angulo*hour-HALF_PI);
  float teste2b = (r3-70) *sin(angulo*hour-HALF_PI);
 
  line(testea,teste2b,0,0);
   
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

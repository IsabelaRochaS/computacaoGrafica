void setup(){
  size(1000,650);
  ellipseMode(CENTER);
}

float somaAnguloTerra = PI;
float somaAnguloLua = PI;

void draw (){
  background(0,0,0);
  translate(width/2,height/2);

  //Sol
  fill(255, 255, 0);
  ellipse(0, 0, 200, 200);
  
  //Terra
  float xTerra= 250*sin(somaAnguloTerra);
  float yTerra= 250*cos(somaAnguloTerra);
  
  fill(0, 0, 255);
  ellipse(xTerra, yTerra, 70, 70);
  
  somaAnguloTerra += PI/1000;
  
  //Lua
  float xLua = xTerra+70 * sin(somaAnguloLua);
  float yLua = yTerra+70 * cos(somaAnguloLua);
  
  fill(255, 255, 255);
  ellipse(xLua, yLua, 30, 30);
  
  somaAnguloLua += PI/100;
}

########################## Addition
add <- function(x, y) {
  return(x + y)
}
add(2,3)
add(10,2)
########################## Factorial
factorial <- function(x){
  y <- 1
  for(i in 1:x){
    y <-y*((1:x)[i])
    print(y)
  }
  
}
factorial(6)
factorial(5)
############################Subtration
sub<-function(x,y){
  return(x-y)
}
sub(5,3)
################################# Multiplication
multiply <- function(x, y) {
  return(x * y)
}
multiply(4,2)
################################# Division
divide <- function(x, y) {
  return(x / y)
}
divide(8,2)
################################# Exponential
exp<- function(x,y){
  return(x**y)
}
exp(2,3)
################################# Square
square<-function(x){
  return(x**2)
}
square(10)
################################ Square root
sqrt<-function(x){
  return(x**0.5)
}
sqrt(4)
################################ Cube
cube<-function(x){
  return(x**3)
}
cube(5)
##############################  Sine function
sin<-function(x){
  return(sin(x))
}

############################  Cos function
cos<-function(x){
  return(cos(x))
}

############################### tan function
tan<-function(x){
  return(tan(x))
}
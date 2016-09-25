#ifndef GLOBAL_H
#define GLOBAL_H

const double PI = 3.14159265359;
const int WIDTH  = 800;             // width in pixels
const int HEIGTH = 600;             // height in pixels



 //  ------------------ SFML specific ---------------------
            // RenderWindow er en sfml-type
            // Creating the SFML window

sf::RenderWindow window( sf::VideoMode(WIDTH, HEIGTH), "mywindow" );

//sf::VertexArray( )

#endif
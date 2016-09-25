//
//  main.cpp
//  matrixPractice
//
//  Created by Jonas Solsvik on 21.09.2016.
//  Copyright © 2016 Jonas Solsvik. All rights reserved.
//


// Standard
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

// SFML
#include <SFML/Graphics.hpp>

// Local
#include "global.h"
#include "cube.h"


void pollEvent(sf::Event& event);
void checkKeyboard();

// ----------- Main -------------

int main() {

    Cube theCube;
    sf::VertexArray cubePoints;


                // Run program as long as window is open.
    while (window.isOpen()) {

        sf::Event event;
        pollEvent(event);

                // Clear the window
        window.clear(sf::Color::Black);    // mandatory

                // Draw everything here.
        theCube.update();
        cubePoints = theCube.render();

        window.draw(cubePoints);
        window.display();                  // mandatory
    }
    return 0;
}


void pollEvent(sf::Event& event){

                // Checks all windows events that has been triggered
                //  since last iteration of the loop
    while (window.pollEvent(event)) {

                // Mandatory to have a way to close the window
        if (event.type == sf::Event::Closed) {
            window.close();
        }
                // A - released
        if ( (event.type == sf::Event::KeyReleased) && (event.key.code == sf::Keyboard::A)){
            std::cout << "A pressed\n";
        }

        if ( (event.type == sf::Event::KeyReleased) && (event.key.code == sf::Keyboard::Q)){
            std::cout << "Bye\n";
            window.close();
        }
    }
}







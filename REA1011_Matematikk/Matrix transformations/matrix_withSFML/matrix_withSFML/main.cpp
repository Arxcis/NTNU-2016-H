
//  Jonas tester keydown, keyup, 


#include <SFML/Graphics.hpp>
#include <iostream>

int main()
{
    bool               go     = true;
    unsigned long long looper = 1;
        
        // Switches
    bool rightTrigger = true; 
    int  rightOnOff   =    0;

    bool leftTrigger = true; 
    int  leftOnOff   =    0;

        // Event triggers
    bool rightDown   ;
    bool rightPressed;
    bool rightUp     ;

    bool leftDown   ;
    bool leftPressed;
    bool leftUp     ;
    

    while (go)
    {
            // Key resets
        rightDown    = false;
        rightUp      = false;
        rightPressed = false;

        leftDown     = false;
        leftUp       = false;
        leftPressed  = false;

        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Q))
        {
            std::cout << "Q pressed";
            go = false;
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
        {
            rightPressed = true;
            looper ++;
        }
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
        {
            leftPressed = true;
            looper ++;
        }

        if (looper % 50000 == 0) {

            std::cout << "Key pressed!\n";
        }
        
            // Keydown/keyup - gate
        if (rightPressed == rightTrigger){

            switch (rightOnOff) {

                case 0:
                    std::cout << "Right Down!\n";
                    rightDown    =  true;
                    rightTrigger = false;
                    rightOnOff   = 1;
                    break;
                case 1:
                    std::cout << "Right Up!\n";
                    rightUp      = true;
                    rightTrigger = true;
                    rightOnOff   = 0;
                    break;
            }   
        }
            // Keydown/keyup - gate
        if (leftPressed == leftTrigger){

            switch (leftOnOff) {

                case 0:
                    std::cout << "Left Down!\n";
                    leftDown    =  true;
                    leftTrigger = false;
                    leftOnOff = 1;
                    break;
                case 1:
                    std::cout << "Left Up!\n";
                    leftUp      = true;
                    leftTrigger = true;
                    leftOnOff = 0;
                    break;
            }   
        }
    }

    return EXIT_SUCCESS;
}

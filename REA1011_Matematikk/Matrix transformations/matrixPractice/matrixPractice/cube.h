#ifndef CUBE_H
#define CUBE_H

#include <SFML/Graphics.hpp>
#include <vector>
#include "graphics.h"

struct Camera {

    Vector3 pos { 0.0, 0.0, 10.0 };  

    double fieldOfViewY = PI / 4.0;
    double            w = cos(fieldOfViewY/2) / sin(fieldOfViewY/2);
    double  aspectRatio = 1.0;
    double            h = w / aspectRatio;
    double        zNear = 0.1;
    double        zFar  = 1000.0;

        // Documentation: https://msdn.microsoft.com/en-us/library/windows/desktop/ms918172.aspx
    double projectionMatrix [16] = {    w, 0.0,                          0.0, 0.0,
                                      0.0,   h,                          0.0, 0.0,
                                      0.0, 0.0,          zFar / (zFar-zNear), 1.0,
                                      0.0, 0.0, -(zNear*zFar) / (zFar-zNear), 0.0   };
};

struct Cube {

            // Default position, rotation, and scale.
    Camera * camera   = new Camera {};
    Vector4* position = new Vector4 { 500.0,  350.0,-10.0, 1.0 };
    Vector4* rotation = new Vector4 { 0.0,  0.0,  0.0, 1.0 };
    Vector3  speed     { 0.001,  0.0,  0.0 };
    Vector3  rspeed    { 0.0,  0.0,  0.0 };
    Vector3  scale     {100.0, 100.0, 100.0 };

    static const int pointNo = 8;
    Vector4 points[pointNo] = {{ 1, 1, 1}, { 1,1,-1}, { 1,-1,1}, { 1,-1,-1},
                               {-1, 1, 1}, {-1,1,-1}, {-1,-1,1}, {-1,-1,-1}};

                // Translate model
    double translatePosition [16] = {   1.0, 0.0, 0.0, speed.x,
                                        0.0, 1.0, 0.0, speed.y,
                                        0.0, 0.0, 1.0, speed.z,
                                        0.0, 0.0, 0.0, 1.0    };

    double translateRotation [16] = {   1.0, 0.0, 0.0, rspeed.x,
                                        0.0, 1.0, 0.0, rspeed.y,
                                        0.0, 0.0, 1.0, rspeed.z,
                                        0.0, 0.0, 0.0, 1.0     };

                // Translate points
    double scalingMatrix    [16] = {    scale.x, 0.0, 0.0, 0.0,
                                        0.0, scale.y, 0.0, 0.0,
                                        0.0, 0.0, scale.z, 0.0,
                                        0.0, 0.0,     0.0, 1.0 };

    double rotationMatrix_Z [16] = {  cos(rotation->z), -sin(rotation->z), 0.0, 0.0,
                                      sin(rotation->z),  cos(rotation->z), 0.0, 0.0,
                                                  0.0,              0.0, 1.0, 0.0,
                                                  0.0,              0.0, 0.0, 1.0 };

    double rotationMatrix_Y[ 16] = {  cos(rotation->y), 0.0, sin(rotation->y), 0.0,
                                                    0.0, 1.0,             0.0, 0.0,
                                     -sin(rotation->y), 0.0, cos(rotation->y), 0.0,
                                                  0.0, 0.0,             0.0, 1.0 };

    double rotationMatrix_X [16] = {  1.0,             0.0,              0.0, 0.0,
                                      0.0, cos(rotation->x), -sin(rotation->x), 0.0,
                                      0.0, sin(rotation->x),  cos(rotation->x), 0.0,
                                      0.0,             0.0,              0.0, 1.0 };


    double  translatePoint  [16] = {    1.0, 0.0, 0.0, position->x,
                                        0.0, 1.0, 0.0, position->y,
                                        0.0, 0.0, 1.0, position->z,
                                        0.0, 0.0, 0.0, 1.0       };


    double  viewMatrix      [16] = {  1.0, 0.0, 0.0,    ∂((position->x) - (camera->pos.x)),
                                      0.0, 1.0, 0.0,     (position->y - camera->pos.y),
                                      0.0, 0.0, 1.0,     (position->z - camera->pos.z),
                                      0.0, 0.0, 0.0, 1.0                         };


    void update() {
        vectorDotMatrix(position, translatePosition);     // 1  Update model position
        vectorDotMatrix(rotation, translateRotation);     // 2  Update model rotation
    }


    sf::VertexArray render () {

        Vector4* temp = points;
        sf::VertexArray vxPoints(sf::Points, 8);

        for (int i = 0; i < 8; i++) {

            *temp = points[i];                                  // 3-9 loop points

            vectorDotMatrix(temp, scalingMatrix           );    // 3  Scale points
            vectorDotMatrix(temp, rotationMatrix_Z        );    // 4  Rotate Z
            vectorDotMatrix(temp, rotationMatrix_Y        );    // 5  Rotate Y
            vectorDotMatrix(temp, rotationMatrix_X        );    // 6  Rotate x

            vectorDotMatrix(temp, translatePoint          );    // 7 Translate to model
            vectorDotMatrix(temp, viewMatrix              );    // 8 Translate to view
            vectorDotMatrix(temp, camera->projectionMatrix);    // 9 Translate to projection

            std::cout << i <<" x: "<< temp->x <<"   y: " << temp->y << std::endl;
            vxPoints[i].position = sf::Vector2f(temp->x, temp->y);
        }
        return vxPoints;
    }
};


#endif
#ifndef GRAPHICS_H
#define GRAPHICS_H

#include <iostream>
#include <vector>

struct Vector3 {    double    x, y, z;    };
struct Vector4 {    double x, y, z, w;    };

// Declarations

void vectorDotMatrix (Vector4 * vec4, const double mat[16]);
void vectorDotMatrix (Vector4 * vec4, std::vector<double> mat);
void printVector4 (Vector4 vec);


// Definitions

void vectorDotMatrix (Vector4 * vec4, const double mat[16]) {

    *vec4 = {(mat[0]*vec4->x) +  (mat[1]*vec4->y) +  (mat[2]*vec4->z) +  (mat[3]*vec4->w),
              (mat[4]*vec4->x) +  (mat[5]*vec4->y) +  (mat[6]*vec4->z) +  (mat[7]*vec4->w),
              (mat[8]*vec4->x) +  (mat[9]*vec4->y) +  (mat[10]*vec4->z) + (mat[11]*vec4->w),
              (mat[12]*vec4->x) + (mat[13]*vec4->y) + (mat[14]*vec4->z) + (mat[15]*vec4->w)};

}

void vectorDotMatrix (Vector4 * vec4, std::vector<double> mat) {

    *vec4 = {(mat[0]*vec4->x) +  (mat[1]*vec4->y) +  (mat[2]*vec4->z) +  (mat[3]*vec4->w),
              (mat[4]*vec4->x) +  (mat[5]*vec4->y) +  (mat[6]*vec4->z) +  (mat[7]*vec4->w),
              (mat[8]*vec4->x) +  (mat[9]*vec4->y) +  (mat[10]*vec4->z) + (mat[11]*vec4->w),
              (mat[12]*vec4->x) + (mat[13]*vec4->y) + (mat[14]*vec4->z) + (mat[15]*vec4->w)};

}

void printVector4(Vector4 vec){
    std::cout << "\nMyvec: " << vec.x << ", " << vec.y << ", " <<  vec.z << ", " << vec.w << "\n";
}


#endif
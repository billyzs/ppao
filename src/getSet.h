//
// Created by billyzs on 10/16/16.
//

#ifndef PPAO_GETSET_H
#define PPAO_GETSET_H

#endif //PPAO_GETSET_H
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>
#include <iostream>
using namespace cv;
using namespace std;

int getSet(string path){
    Mat* img = new Mat(imread(path, IMREAD_COLOR));
    // Mat& r_img = *img;
    if (img->empty()){
        cout << "failed to load image" << endl;
        return -1;
    }
    // Mat* slice = new Mat(img->rowRange(0, 100).colRange(0, 100));
    cout << img->type() << endl; // type of the image (8UC3, 32F, etc)
    cout << CV_8UC3 << endl;
    int w(50); int h(100);
    Mat* black = new Mat(h, w, CV_8UC3, Scalar(0,0,0));  // a black matrix
    // bitwise_and(img->rowRange(0, 100).colRange(0, 100), Scalar(0, 0, 0), *img);
    Mat* header = new Mat(*img, Rect(0,0, 50, 100));// Rect() takes in vertex, width and height; Mat()takes height and width
    imshow("slice", *header);
    black->copyTo(*header);
    imshow("img", *img);

    waitKey(0);
    delete img, black, header;
    return 0;
}
//
// Created by billyzs on 10/16/16.
//

#ifndef PPAO_DRAWING_H
#define PPAO_DRAWING_H

#endif //PPAO_DRAWING_H

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <string>
#include <iostream>
#include <opencv2/imgproc.hpp>

using namespace cv;

int drawLine(){
    Mat* canvas = new Mat();
    *canvas = Mat::zeros(300, 300, CV_8UC3);
    line(*canvas, CvPoint(0,0), CvPoint(300,300), Scalar(0, 255, 0));
    imshow("canvas", *canvas);
    waitKey(0);
    line(*canvas, CvPoint(300, 0), CvPoint(0, 300), Scalar(0, 0, 255));
    imshow("canvas", *canvas);
    waitKey(0);
    delete canvas;
    return 0;
}
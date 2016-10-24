//
// Created by billyzs on 10/15/16.
//

#ifndef PPAO_LOADDISPLAYSAVE_H
#define PPAO_LOADDISPLAYSAVE_H

#endif //PPAO_LOADDISPLAYSAVE_H

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include "opencv2/imgcodecs.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <string>
#include <iostream>
using namespace cv;
using namespace std;
int loadPicture(String path){
    Mat img;
    img = imread(path.c_str(), IMREAD_COLOR);
    if (img.empty()){
        cout << "Could not open the image" << endl;
        return -1;
    }
    cout << "width: " << img.cols << endl;
    cout << "height: " << img.rows << endl;
    cout << "channels: " << img.channels() << endl;
    imshow("Image", img);
    waitKey(0);
    return 0;
}

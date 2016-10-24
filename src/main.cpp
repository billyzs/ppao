#include <iostream>
#include "loadDisplaySave.h"
#include "getSet.h"
#include "drawing.h"


int main(int argc, char** argv) {
   string path;
    if (argc > 1){
        path = argv[1];
        cout << path << endl;
        // return loadPicture(path);
        // return getSet(path);
        Mat img = imread(path);
        Rect roi = Rect(Point(100, 100), Size(50, 50));
        Mat subimg = img(roi);
        imshow("subimage", subimg);
        waitKey(0);
        // Mat* shifted = new Mat;
        Mat* shifted = new Mat();
        Point center(img.cols / 2, img.rows/2);
        Mat rot = getRotationMatrix2D(center, 90.0, 1.0);
        warpAffine(img, *shifted, rot, Size());
        imshow("rotated", *shifted);
        waitKey(0);

        float m[] = {1, 0, 0, 0, 1, 20};
        // Mat shift_up = (Mat_<double>(2,3) << 1.0, 0.0, 0.0, 0.0, 1.0, 20.0);
        Mat shift_up = Mat(2,3,CV_32F, m);
        warpAffine(img, *shifted, shift_up, Size());
        imshow("shifted up", *shifted);
        waitKey(0);
        Mat add = Mat::ones(img.size(), img.type())*150;
        cv::add(img, add, *shifted);
        Mat mask = Mat::zeros(img.size(), img.type());
        mask(roi) = Scalar(255, 255, 255);
        cv::circle(mask, Point(200, 200), 50,Scalar(255,255,255), -1);
        bitwise_and(img, mask, img);
        imshow("masked", img);
        waitKey(0);
        delete shifted;
        return 0;

    }
    else
        cout << "Please specify a path" << endl;
        return -1;
    // return drawLine();
}
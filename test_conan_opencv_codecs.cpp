#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <iostream>


int main(int, char **)
{
    cv::Mat m = cv::imread("smiley.png");

    std::cout << "Size :" << m.cols << "x" << m.rows << "\n";
}
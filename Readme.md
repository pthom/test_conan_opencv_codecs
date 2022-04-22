
Demonstration of the failure to link `cv::imread` with Conan's recipe opencv/4.5.5 under ubuntu 22.04.

How to use: 

````bash
git clone https://github.com/pthom/test_conan_opencv_codecs.git
cd test_conan_opencv_codecs
# this will instantiate a docker container based on ubuntu 22.04 and run the build inside
./do_build_docker.py
````

You will get the error message: ` undefined reference to cv::imread`
````
/usr/bin/ld: CMakeFiles/test_conan_opencv_codecs.dir/test_conan_opencv_codecs.cpp.o: in function `main':
test_conan_opencv_codecs.cpp:(.text+0x72): undefined reference to `cv::imread(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, int)'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/test_conan_opencv_codecs.dir/build.make:99: test_conan_opencv_codecs] Error 1
make[1]: *** [CMakeFiles/Makefile2:83: CMakeFiles/test_conan_opencv_codecs.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
````

This fails with Ubuntu 22.04 + opencv/4.5.5 and with Ubuntu 20.04 + opencv/4.5.0

Details of the Opencv Configuration during `conan install`:
It includes:
````
--   OpenCV modules:
--     To be built:                 calib3d core features2d flann gapi highgui imgcodecs imgproc ml photo stitching video videoio
````

Full detail:
````
-- General configuration for OpenCV 4.5.5 =====================================
--   Version control:               unknown
-- 
--   Platform:
--     Timestamp:                   2022-04-22T15:48:51Z
--     Host:                        Linux 5.10.76-linuxkit x86_64
--     CMake:                       3.22.1
--     CMake generator:             Unix Makefiles
--     CMake build tool:            /usr/bin/gmake
--     Configuration:               Release
-- 
--   CPU/HW features:
--     Baseline:                    SSE SSE2 SSE3
--       requested:                 SSE3
--     Dispatched code generation:  SSE4_1 SSE4_2 FP16 AVX AVX2 AVX512_SKX
--       requested:                 SSE4_1 SSE4_2 AVX FP16 AVX2 AVX512_SKX
--       SSE4_1 (16 files):         + SSSE3 SSE4_1
--       SSE4_2 (1 files):          + SSSE3 SSE4_1 POPCNT SSE4_2
--       FP16 (0 files):            + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 AVX
--       AVX (3 files):             + SSSE3 SSE4_1 POPCNT SSE4_2 AVX
--       AVX2 (29 files):           + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2
--       AVX512_SKX (3 files):      + SSSE3 SSE4_1 POPCNT SSE4_2 FP16 FMA3 AVX AVX2 AVX_512F AVX512_COMMON AVX512_SKX
-- 
--   C/C++:
--     Built as dynamic libs?:      NO
--     C++ standard:                11
--     C++ Compiler:                /usr/bin/c++  (ver 11.2.0)
--     C++ flags (Release):         -m64   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -O3 -DNDEBUG   -DNDEBUG
--     C++ flags (Debug):           -m64   -fsigned-char -W -Wall -Werror=return-type -Werror=non-virtual-dtor -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wundef -Winit-self -Wpointer-arith -Wshadow -Wsign-promo -Wuninitialized -Wsuggest-override -Wno-delete-non-virtual-dtor -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -fvisibility-inlines-hidden -g   -O0 -DDEBUG -D_DEBUG
--     C Compiler:                  /usr/bin/cc
--     C flags (Release):           -m64   -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -O3 -DNDEBUG   -DNDEBUG
--     C flags (Debug):             -m64   -fsigned-char -W -Wall -Werror=return-type -Werror=address -Werror=sequence-point -Wformat -Werror=format-security -Wmissing-declarations -Wmissing-prototypes -Wstrict-prototypes -Wundef -Winit-self -Wpointer-arith -Wshadow -Wuninitialized -Wno-comment -Wimplicit-fallthrough=3 -Wno-strict-overflow -fdiagnostics-show-option -Wno-long-long -pthread -fomit-frame-pointer -ffunction-sections -fdata-sections  -msse -msse2 -msse3 -fvisibility=hidden -g   -O0 -DDEBUG -D_DEBUG
--     Linker flags (Release):      -m64  -Wl,--gc-sections -Wl,--as-needed   
--     Linker flags (Debug):        -m64  -Wl,--gc-sections -Wl,--as-needed   
--     ccache:                      NO
--     Precompiled headers:         NO
--     Extra dependencies:          /root/.conan/data/libjpeg/9d/_/_/package/dfbe50feef7f3c6223a476cd5aeadb687084a646/lib/libjpeg.a /root/.conan/data/libwebp/1.2.2/_/_/package/ec17d365d82d936171699c4130c92bcc8b6f5f90/lib/libwebp.a /root/.conan/data/libpng/1.6.37/_/_/package/025ffc7158b5e62f5f3ed9af91d48958d216f972/lib/libpng16.a /root/.conan/data/libtiff/4.3.0/_/_/package/ccce7e478ec9029b815a64f57eee1845e01521b0/lib/libtiffxx.a /root/.conan/data/libtiff/4.3.0/_/_/package/ccce7e478ec9029b815a64f57eee1845e01521b0/lib/libtiff.a /root/.conan/data/jasper/2.0.33/_/_/package/91200d30078a4be9d45e18575148f5a04efeebe8/lib/libjasper.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libImath-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libIlmImf-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libIex-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libHalf-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libIlmThread-2_5.a /root/.conan/data/zlib/1.2.12/_/_/package/dfbe50feef7f3c6223a476cd5aeadb687084a646/lib/libz.a dl m pthread rt
--     3rdparty dependencies:
-- 
--   OpenCV modules:
--     To be built:                 calib3d core features2d flann gapi highgui imgcodecs imgproc ml photo stitching video videoio
--     Disabled:                    python_tests world
--     Disabled by dependency:      objdetect
--     Unavailable:                 dnn java python2 python3 ts
--     Applications:                -
--     Documentation:               NO
--     Non-free algorithms:         NO
-- 
--   GUI:                           NONE
-- 
--   Media I/O: 
--     ZLib:                        /root/.conan/data/zlib/1.2.12/_/_/package/dfbe50feef7f3c6223a476cd5aeadb687084a646/lib/libz.a  (ver )
--     JPEG:                        (ver 90)
--     WEBP:                        /root/.conan/data/libwebp/1.2.2/_/_/package/ec17d365d82d936171699c4130c92bcc8b6f5f90/lib/libwebp.a (ver encoder: 0x020f)
--     PNG:                         (ver ..)
--     TIFF:                        (ver 42 / 4.3.0)
--     JPEG 2000:                   (ver 2.0.33)
--     OpenEXR:                     /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libImath-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libIlmImf-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libIex-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libHalf-2_5.a /root/.conan/data/openexr/2.5.7/_/_/package/62354f337a7e19ba43d02028e4df4c3103ffc018/lib/libIlmThread-2_5.a (ver 2_5)
--     HDR:                         NO
--     SUNRASTER:                   NO
--     PXM:                         NO
--     PFM:                         NO
-- 
--   Video I/O:
-- 
--   Parallel framework:            pthreads
-- 
--   Trace:                         YES (built-in)
-- 
--   Other third-party libraries:
--     Eigen:                       YES (ver ..)
--     Custom HAL:                  NO
-- 
--   Python (for build):            NO
-- 
--   Install to:                    /root/.conan/data/opencv/4.5.5/_/_/package/b6aebd1679d43bbd75c63f0647e176aa9e67c2c3
-- -----------------------------------------------------------------

````




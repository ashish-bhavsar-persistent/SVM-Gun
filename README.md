# SVM-classification-detection
HoG, PCA, PSO, Hard Negative Mining, Sliding Window, NMS


Best way to do detection is:

HoG(features) -> PCA(less features) + PSO(best C&gamma) -> origin SVM -> HNM(more features) -> better SVM -> SW -> NMS(bbox regression)

Sorry for my laziness.

I think I should clarify the steps for the program.

1. Extract HoG features (script 1)

2. Train an initial model for pso (script 2)

3. Do pca and pso for better parameters C and gamma (script 6)

4. Use no-pca features and the best parameters to train the second model (script 2)

5. In order to increase the accuracy, use the second model to do hnm and get the final model(script 7)

6. Finally, choose an algorithm you like to do location(script 8 or 9 or 10)

**PS:**

1. The reason I use pca is to accelerate the speed of pso. To be honestly, pso is really slow.

2. For step 4, you can also use features processed by pca, but I strongly advise you to hold as possible as more features. Because more features, higher accuracy.

中文地址：http://blog.csdn.net/renhanchi/article/category/7007663

强烈建议将6篇文章都仔细看一遍，再来跑代码，或者边看边跑。内容不是很多，但是会对你理解算法和代码有很大帮助。


 For 32 Bit 
"c:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvars32.bat"
(optional) To build 32-bit windows binaries, you must
	(1) Setup "C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\vcvars32.bat" instead of vcvars64.bat
	(2) Change CFLAGS in Makefile.win: /D _WIN64 to /D _WIN32
	
For 64 Bit 
"c:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Auxiliary\Build\vcvars64.bat"

You may have to modify the above command according which version of
VC++ or where it is installed.

2. Type

nmake -f Makefile.win clean all

3. (optional) To build shared library libsvm.dll, type

nmake -f Makefile.win lib
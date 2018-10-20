## running the raster_plot.r in HPC
1. sign in (see details in 电镜中心集群资料 in FTP)

![](resources/E60DBF0191AE148AB173EAE29A07EE65.jpg)

2. ssh into a computing node
`ssh c03n10`

![](resources/B440B520483790D18A3DE221EFFA3139.jpg)

3. activate the R environment
`source activate my-r-env`

![](resources/BA822AE6825FD2D54F1415989F184BCF.jpg)

4. enter your personal folder and run the R script (your data need to be upload by _filezilla_ software first)
* cd **the_path_of_your_folder**
* cp **the_path_of_original_script**
* Rscript **the_path_of_your_raster_plot_script** **your_original_data** 

![](resources/3E27A37FE1A957D1C3636527BE56F749.jpg)

5. the pdf will be generated
* e.g demo_output.pdf

![](resources/8C00BF6943A1B4C06CC61797574AADAA.jpg)

here is the result![](resources/28B1D344A4102E53006F897C087F0823.jpg)

6. if you want to name your pdf first, you can use the following command
* Rscript **the_path_of_your_raster_plot_script** **your_original_data** **the_name_you_want.pdf**

## batch processing for your data
if you have lots of csv file need to be processed, you can use a _for_ loop to generate pdf files. 

![](resources/E1BE79B8F35B5C9703A6004AE4A634F3.jpg)

## modify the color of your plot

you can change the defult color setting by modifying the script (you have to copy the script into your own folder first)
* `vi raster_plot.r`
* press _i_
* cahnge color
* press _esc_
* press _:wq_

![](resources/EE96BC179410C0C126031D76B2F76B36.jpg)




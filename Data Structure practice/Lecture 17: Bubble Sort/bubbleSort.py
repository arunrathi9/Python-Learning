# GFG - Bubble sort

def bubbleSort(arr, n):
    # code here
    for i in range(n-1):
        for j in range(1,n):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr

#arr = [4, 1, 3, 9, 7]
arr = [886,777,915,793,335,386,492,649,421,362,27,690,59,763,926,540,426,172,736,211,368,567,429,782,530,862,123,67,135,929,802,22,58,69,167,393,456,11,42,229,373,421,919,784,537,198,324,315,370,413,526,91,980,956,873,862,170,996,281,305,925,84,327,336,505,846,729,313,857,124,895,582,545,814,367,434,364,43,750,87,808,276,178,788,584,403,651,754,399,932,60,676,368,739,12,226,586,94,539,795,570,434,378,467,601,97,902,317,492,652,756,301,280,286,441,865,689,444,619,440,729,31,117,97,771,481,675,709,927,567,856,497,353,586,965,306,683,219,624,528,871,732,829,503,19,270,368,708,715,340,149,796,723,618,245,846,451,921,555,379,488,764,228,841,350,193,500,34,764,124,914,987,856,743,491,227,365,859,936,432,551,437,228,275,407,474,121,858,395,29,237,235,793,818,428,143,11,928,529,776,404,443,763,613,538,606,840,904,818,128,688,369,917,917,996,324,743,470,183,490,499,772,725,644,590,505,139,954,786,669,82,542,464,197,507,355,804,348,611,622,828,299,343,746,568,340,422,311,810,605,801,661,730,878,305,320,736,444,626,522,465,708,416,282,258,924,637,62,624,600,36,452,899,379,550,468,71,973,131,881,930,933,894,660,163,199,981,899,996,959,773,813,668,190,95,926,466,84,340,90,684,376,542,936,107,445,756,179,418,887,412,348,172,659,9,336,210,342,587,206,301,713,372,321,255,819,599,721,904,939,811,940,667,705,228,127,150,984,658,920,224,422,269,396,81,630,84,292,972,672,850,625,385,222,299,640,42,898,713,298,190,524,590,209,581,819,336,732,155,994,4,379,769,273,776,850,255,860,142,579,884,993,205]
print(bubbleSort(arr, len(arr)))
#!/usr/bin/Rscript
# 引数を設定
args1 <- commandArgs(trailingOnly = T)[1]
args2 <- commandArgs(trailingOnly = T)[2]

sink(args2)
# i回ハローワールドする。
for(i in 1:args1){
    print('Hello World!!')
}
sink()


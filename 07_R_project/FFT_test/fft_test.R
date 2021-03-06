library(dplyr)

# time signal?? FFT ?°?΄?° μΆμΆ ?¨? -----------------------------
Noise_DB <- function(file_name){
  
  # A weighting ?¨?
  A_weighting <- function(max_f, df) {
    f <- seq(from=0, to=max_f-1, by=df)
    Ra_f <- 12194^2*f^4/((f^2+20.6^2)*(f^2+12194^2)*sqrt((f^2+107.7^2)*(f^2+737.9^2)))
    Ra_f1000 <- 12194^2*1000^4/((1000^2+20.6^2)*(1000^2+12194^2)*sqrt((1000^2+107.7^2)*(1000^2+737.9^2)))
    A_fdB <- 20*log10(Ra_f)-20*log10(Ra_f1000)
    s_f <- Ra_f^2/Ra_f1000^2
    return(s_f)
  }
  library(readxl)
  T <- read_excel(file_name)
  
  samp_freq <- as.numeric(T[2,1]-T[1,1])
  
  # ?? ?°?΄?° μΆμΆ
  pres <- T[,2]; rm(T)
  #df <- readline("set the delta frequency?")
  df <- 1 # μ£Όν? κ°κ²©?? 1Hz
  
  t_sel <- df/samp_freq #fft ?λ²μ ??? κ°??
  max_f <- t_sel/2
  d_f <- seq(from=0, to=(t_sel/2)-1, by=df)
  
  # Hanning window --------------------------------
  hann_win = matrix(,t_sel,1)
  for (i in 1:t_sel[1]) {
    hann_win[i,1] <- 0.5-0.5*cos(2*pi*(i-1)/t_sel)
  }
  #------------------------------------------------
  
  A_weight_func <- A_weighting(max_f, df)
  
  avg_num <- 30
  # overlab 67%
  overlab <- 0.67
  overlab_num <- round(overlab*t_sel,0)
  
  # for λ¬? ?? €? κ°? ?? λΉΌκΈ°
  #--------------------------------------
  sta = 1
  fin = t_sel
  
  t_raw <- data.frame()
  FT <- data.frame()
  FT_A <- data.frame()
  
  #t_raw[1:51200,1] <- pres[sta:fin,1]*hann_win
  
  for (i in 1:30) {
    t_raw[1:51200,i] <- pres[sta:fin,1]*hann_win
    FT[1:51200,i] <- 2*abs(fft(t_raw[1:51200,i]))/(sqrt(2)*t_sel[1])
    FT_A[1:25600,i] <- FT[1:25600,i]*A_weight_func
    LFT <- 10*log10(FT_A^2/0.00002^2)
    sta <- fin-overlab_num+1
    fin <- sta+t_sel-1
  }
  # ** μΆν FFT ?κ·? λ°? comp Hz ? λ³? μΆμΆ μ½λ© μΆκ?
  d = data.frame(d_f)
  
  gFT_A <- tidyr::gather(data=LFT, V1:V30, key="Comp.Hz", value="dBA")
  
  library(magrittr)
  
  gFT_A %<>%
    mutate(Freq=rep(1:25600, times=30))
  
  library(writexl)
  # ?€??Έ?Ό ?°?΄?° ???₯?κΈ? -----------------------------------
  write_xlsx(gFT_A,"./output/Noise_DB.xlsx",col_names=TRUE)
  # ** μΆν DB κ³μ ??°?΄?Έ ??λ‘? ???₯λͺ? λ°? κ²½λ‘ μ§?  ?± κ΄λ¦? ?? 
}

# MV data ??©??¬ κ΄?¬ μ£Όν?? ????? ? λ³? ???₯
MV_DB <- function(file_name) {
  library(data.table)
  mv <- fread(file_name,encoding="UTF-8", header=TRUE, skip=6, stringsAsFactor=FALSE)
  
  # μ€λ³΅?΄λ¦? λ³κ²?
  # ---------------------
  
  names(mv)[38] <- "INV_I"
  names(mv)[39] <- "INV"
  names(mv)[40] <- "INV2_I"
  names(mv)[41] <- "INV2_W"
  
  # NAκ° ?? ?΄ ?­? 
  xx <- which(is.na(mv[1,]))
  
  # ???? ?°?΄?° ?­?  (μΆκ? ?? ??)
  mv1 <- select(mv, -xx)
  #mv2 <- select(mv1, -c("siter","time","?΄? λͺ¨λ","λͺ©νκ³Όμ΄","λͺ©νκ³Όλκ³Όμ΄","ACCUM.","4WAY","HEX V/V","λͺ©νκ³ μ", "λͺ©ν???", "??? λ²?", "?€?Ό? ?΄2", "Dry Contact", "?€?Ό? ?΄1", "INV1 ??΄", "INV2 ??΄", "?΄κ΅νκΈ°μλΆ", "?΄κ΅νκΈ°νλΆ","κ· μ  V/V","λ¦¬μλ²? IN","λ¦¬μλ²? OUT","?‘? V/V","?€?Ό?Ό?","?€?Ό?Ό?2","? ?€","FAN λͺ©ν","FAN2 λͺ©ν"))
#  mv_re <- select(mv1, c("INV", "FAN ??¬", "FAN2 ??¬", "Main EEV", "κ³΅κΈ°?¨?", "?‘??¨?", "INV ? μΆμ¨?", "?΄κ΅νκΈ°μ¨?"))
#  r_ch <- seq(500, 1000, length=30)
#  mv_sel <- slice(mv_re, r_ch)
  
#  mv_sel$INV <- c("V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","V29","V30") 
  
  # MV ?°?΄?° ???₯
#  library(writexl)
  
#  write_xlsx(mv_sel,"./output/MV_DB.xlsx",col_names=TRUE)
  
}
# ?¨? ?€?
#Noise_DB("./data/time_29Hz.xlsx")
#MV_DB("./data/time tracking_ODU1.csv")

#?°?΄?° ?ΈμΆνκΈ?---------------------------------------
#N_spectrums <- readxl::read_excel("./output/Noise_DB.xlsx")
#MV_sel <- readxl::read_excel("./output/MV_DB.xlsx")

#N_spectrums$dBA <- as.numeric(N_spectrums$dBA)
#plot(d_f, FT_A2[,1]) 
#for(j in 2:5){
#  points(d_f, FT_A2[,j], col=j)
#}

# κ·Έλ? κ·Έλ¦¬κΈ?
g <- N_spectrums %>% ggplot(aes(x=Freq, y=dBA, group=Comp.Hz)) 
g + geom_line(aes(group=Comp.Hz, color=Comp.Hz))

# μΆν ?? ?λ¬?
# 1. DB??Ό ? ? λ°? κ΄?¬ μ‘°κ±΄??? ?€??Έ?Ό λ°? ??? λ³? ??Έ?© GUI ??±
# 2. FFT ?°?΄?° cross check λ°? DB ??°?΄?Έ μ½λ© ??±
# 3. ?? MV data μΆμΆ ?? 

# κ³Όμ  ??±? κΈ°λ??¨κ³?
# - ?? ?Έ? ?? ?°?΄?° DB? κ°?₯
# - ?°?΄?°κ° μΆ©λΆ? ??΄λ©? λΉλ°?΄?°λ₯? ?΅? ?? κ°μ  κ°?₯
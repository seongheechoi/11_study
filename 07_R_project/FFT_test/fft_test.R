library(dplyr)

# time signal?—?„œ FFT ?°?´?„° ì¶”ì¶œ ?•¨?ˆ˜ -----------------------------
Noise_DB <- function(file_name){
  
  # A weighting ?•¨?ˆ˜
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
  
  # ?Œ?•• ?°?´?„° ì¶”ì¶œ
  pres <- T[,2]; rm(T)
  #df <- readline("set the delta frequency?")
  df <- 1 # ì£¼íŒŒ?ˆ˜ ê°„ê²©??€ 1Hz
  
  t_sel <- df/samp_freq #fft ?•œë²ˆì— ?•„?š”?•œ ê°??ˆ˜
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
  
  # for ë¬? ?Œ? ¤?„œ ê°? ?ƒ˜?”Œ ë¹¼ê¸°
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
  # ** ì¶”í›„ FFT ?‰ê·? ë°? comp Hz ? •ë³? ì¶”ì¶œ ì½”ë”© ì¶”ê?€
  d = data.frame(d_f)
  
  gFT_A <- tidyr::gather(data=LFT, V1:V30, key="Comp.Hz", value="dBA")
  
  library(magrittr)
  
  gFT_A %<>%
    mutate(Freq=rep(1:25600, times=30))
  
  library(writexl)
  # ?Š¤?Ž™?Š¸?Ÿ¼ ?°?´?„° ??€?ž¥?•˜ê¸? -----------------------------------
  write_xlsx(gFT_A,"./output/Noise_DB.xlsx",col_names=TRUE)
  # ** ì¶”í›„ DB ê³„ì† ?—…?°?´?Š¸ ?˜?„ë¡? ??€?ž¥ëª? ë°? ê²½ë¡œ ì§€? • ?“± ê´€ë¦? ?˜ˆ? •
}

# MV data ?™œ?š©?•˜?—¬ ê´€?‹¬ ì£¼íŒŒ?ˆ˜?— ??€?‘?•˜?Š” ? •ë³? ??€?ž¥
MV_DB <- function(file_name) {
  library(data.table)
  mv <- fread(file_name,encoding="UTF-8", header=TRUE, skip=6, stringsAsFactor=FALSE)
  
  # ì¤‘ë³µ?´ë¦? ë³€ê²?
  # ---------------------
  
  names(mv)[38] <- "INV_I"
  names(mv)[39] <- "INV"
  names(mv)[40] <- "INV2_I"
  names(mv)[41] <- "INV2_W"
  
  # NAê°€ ?žˆ?Š” ?—´ ?‚­? œ
  xx <- which(is.na(mv[1,]))
  
  # ?•„?š”?—†?Š” ?°?´?„° ?‚­? œ (ì¶”ê?€ ?˜‘?˜ ?•„?š”)
  mv1 <- select(mv, -xx)
  #mv2 <- select(mv1, -c("siter","time","?š´? „ëª¨ë“œ","ëª©í‘œê³¼ì—´","ëª©í‘œê³¼ëƒ‰ê³¼ì—´","ACCUM.","4WAY","HEX V/V","ëª©í‘œê³ ì••", "ëª©í‘œ??€?••", "?†Œ?Œ? ˆë²?", "?˜¤?¼? œ?–´2", "Dry Contact", "?˜¤?¼? œ?–´1", "INV1 ?˜ˆ?—´", "INV2 ?˜ˆ?—´", "?—´êµí™˜ê¸°ìƒë¶€", "?—´êµí™˜ê¸°í•˜ë¶€","ê· ìœ  V/V","ë¦¬ì‹œë²? IN","ë¦¬ì‹œë²? OUT","?¡?ž… V/V","?˜¤?¼?„¼?„œ","?˜¤?¼?„¼?„œ2","? ?„¤","FAN ëª©í‘œ","FAN2 ëª©í‘œ"))
#  mv_re <- select(mv1, c("INV", "FAN ?˜„?ž¬", "FAN2 ?˜„?ž¬", "Main EEV", "ê³µê¸°?˜¨?„", "?¡?ž…?˜¨?„", "INV ?† ì¶œì˜¨?„", "?—´êµí™˜ê¸°ì˜¨?„"))
#  r_ch <- seq(500, 1000, length=30)
#  mv_sel <- slice(mv_re, r_ch)
  
#  mv_sel$INV <- c("V1","V2","V3","V4","V5","V6","V7","V8","V9","V10","V11","V12","V13","V14","V15","V16","V17","V18","V19","V20","V21","V22","V23","V24","V25","V26","V27","V28","V29","V30") 
  
  # MV ?°?´?„° ??€?ž¥
#  library(writexl)
  
#  write_xlsx(mv_sel,"./output/MV_DB.xlsx",col_names=TRUE)
  
}
# ?•¨?ˆ˜ ?‹¤?–‰
#Noise_DB("./data/time_29Hz.xlsx")
#MV_DB("./data/time tracking_ODU1.csv")

#?°?´?„° ?˜¸ì¶œí•˜ê¸?---------------------------------------
#N_spectrums <- readxl::read_excel("./output/Noise_DB.xlsx")
#MV_sel <- readxl::read_excel("./output/MV_DB.xlsx")

#N_spectrums$dBA <- as.numeric(N_spectrums$dBA)
#plot(d_f, FT_A2[,1]) 
#for(j in 2:5){
#  points(d_f, FT_A2[,j], col=j)
#}

# ê·¸ëž˜?”„ ê·¸ë¦¬ê¸?
g <- N_spectrums %>% ggplot(aes(x=Freq, y=dBA, group=Comp.Hz)) 
g + geom_line(aes(group=Comp.Hz, color=Comp.Hz))

# ì¶”í›„ ?•„?š” ?—…ë¬?
# 1. DB?ŒŒ?¼ ? ‘?† ë°? ê´€?‹¬ ì¡°ê±´?—?„œ?˜ ?Š¤?Ž™?Š¸?Ÿ¼ ë°? ?•„?š”? •ë³? ?™•?¸?š© GUI ?ƒ?„±
# 2. FFT ?°?´?„° cross check ë°? DB ?—…?°?´?Š¸ ì½”ë”© ?™„?„±
# 3. ?•„?š” MV data ì¶”ì¶œ ?™•? •

# ê³¼ì œ ?™„?„±?‹œ ê¸°ë?€?š¨ê³?
# - ?†Œ?Œ ?¸? •?‹œ?—˜ ?°?´?„° DB?™” ê°€?Š¥
# - ?°?´?„°ê°€ ì¶©ë¶„?žˆ ?Œ“?´ë©? ë¹…ë°?´?„°ë¥? ?†µ?•œ ?†Œ?Œ ê°œì„  ê°€?Š¥
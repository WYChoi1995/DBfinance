library(rmgarch)
library(rugarch)

data <- read.csv("DCC.csv", row.names = "Date")
return <- na.omit(subset(data, select = c("WTICL_return", "HSCEI_return", "STOXX50E_return")))

garch_model <- ugarchspec(mean.model = list(armaOrder = c(0, 0)),
                          variance.model = list(garchOrder = c(1,1), model = "eGARCH"),
                          distribution.model = "norm")

dcc_garch_model <- dccspec(uspec = multispec(replicate(3, garch_model)),
                           dccOrder = c(1,1),
                           distribution = "mvnorm")

dcc_garch_fit <- dccfit(dcc_garch_model, data=return)

dsigma <- data.frame(sigma(dcc_garch_fit))
dcorr <- rcor(dcc_garch_fit)
dcov <- rcov(dcc_garch_fit)

condcorr <- data.frame(cbind(dcorr[1,2,], dcorr[1,3,], dcorr[2,3,]))
condcov <- data.frame(cbind(dcov[1,2,], dcov[1,3,], dcov[2,3,]))
colnames(dsigma) <- c("WTICL_sigma", "HSCEI_sigma", "STOXX50E_sigma")
colnames(condcorr) <- c("WTI-HSCEI", "WTI-STOXX50E", "HSCEI-STOXX50E")
colnames(condcov) <- c("WTI-HSCEI", "WTI-STOXX50E", "HSCEI-STOXX50E")

variance <- cbind(dsigma, condcov)
write.csv(variance, "variance.csv")
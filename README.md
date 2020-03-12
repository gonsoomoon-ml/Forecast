# Forecasting Traffic Volume with AWS Forecast
**이 노트북의 원본은 https://github.com/chrisking/ForecastPOC.git 으로서, 원본 내용의 기반하에 추가 내용등을 기술한 버전 입니다.**

* AWS Forecast AI 서비스를 가지고 미국 미네라폴리스 근처 고속도로의 차량 통행량을 시간별로 예측하는 문제를 풀어가는 과정을 아래 4개의 노트북으로 구성 함.

* Process: (Traffic Volume 폴더 안에 노트북을 아래 순서대로 실행 하셔야 합니다.)
    * Validating_and_Importing_Target_Time_Series_Data
        * 데이타를 준비하고 Target Time Series Data를 정의 함.
    * Creating_and_Evaluating_Predictors
        * Target Time Series Data와 ARIMA, Prophet, DeepAR+ 알고리즘을 가지고 Predictors 및 Forecasts를 생성한 후에 모델의 성능 분석을 함.
    * Validating_and_Importing_Related_Time_Series_Data 
        * Related Time Series Data를 정의 함.
    * Creating_and_Evaluating_Related_Time_Predictors
        * Target Time Series Data 및 Related Time Series Data 와 Prophet, DeepAR+ 알고리즘을 가지고 Predictors 및 Forecasts를 생성한 후에 모델의 성능 분석을 함.
    
    
    
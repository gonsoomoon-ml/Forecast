# Forecasting Store Item Demanding with AWS Forecast  
(Data Source: https://www.kaggle.com/c/demand-forecasting-kernels-only/overview)

* **Content: Using AWS Forecast AI, forecasting the store item demanding problem (Daily Data)**

* **Technique included**
    * Use two dimenstions, item_id and store on Target Data
    * Use QueryForecast with two filters, item_id and store
    * Use QueryForecast with one filters, item_id 
    * Use HPO for building DeepARP 
    * Measure MAPE on Prophet and Deeparp campaigns    
    * Compare Prophet and DeepARP performance with actual value


* Process: (In the folder the StoreItemDemand, run the following notebooks in order)
    * 1.Prepare_Data_File.ipynb
        * Prepare data file handling a raw data file
    * 2.Import_Dataset.ipynb (About 10 mins elapsed)
        * Create dataset group, dataset and dataset import job as well as importing the data file from S3
        * The dataset file as target time series data has two dimensions such as item_id and store
    * 3.Create_Target_Predictors.ipynb (About 40 mins elapsed)
        * Create predictors with the prophet and deepar+ 
    * 4.Create_Target_Forecast.ipynb (About 50 mins elapsed)
        * Create forecasts with the two predictors 
    * 5.Analyze_Target_Forecast.ipynb (About 10 mins elapsed)
        * Analyze results on the forecasts
    * 6.Cleanup.ipynb (About 10 mins elapsed)
        * Clean up resources
    * 7.Option_Create_Target_Predictors_HPO.ipynb (About 90 mins elapsed)
        * Turning on HPO option, create  a predictor with deepar+ 
            

# Forecasting Walmart Weekly Sale with AWS Forecast
(Data Source: https://www.kaggle.com/fernandol/cracking-the-walmart-sales-forecasting-challenge)


*  AWS Forecast AI 서비스를 가지고 미국 월마트 45개의 상점의 주간 매출을 예측 함.(Weekly Data)

* **Technique included**
    * Use **three data sets of Target, Related and Item Meta**
    * Compare Prophet and DeepARP performance with actual value    


* Process: (WalmartSale 폴더 안에 노트북을 아래 순서대로 실행 하셔야 합니다.)
    * Import_Target_Dataset.ipynb
        * 데이타를 준비하고 Target Time Series Data를 정의, Dataset 생성, Dataset Import 함
    * Create_Target_DatasetGroup.ipynb
        * Target 데이타만을 가지고 Dataset Group을 생성 함.
    * Create_Target_Predictors.ipynb
        * Target 데이타만을 이용하여  Prophet, DeepAR+ 알고리즘을 가지고 Predictors 생성
    * Create_Target-Campaign.ipynb
        * Target 데이타만을 이용하여  Prophet, DeepAR+ Predictors 생성
    * **옵선 Related, Item Meta 데이타를 추가**
    * Import_Related_Dataset.ipynb
        * Related 데이타 준비, Dataset 생성, Dataset Import 함
    * Import_ItemMeta_Dataset.ipynb
        * Item Meta 데이타 준비, Dataset 생성, Dataset Import 함
    * Create_Related_ItemMeta_DatasetGroup.ipynb
        * Target, Related, Item Meta 를 가지고 Dataset Group 생성
    * Create_ItemMeta_Predictors.ipynb
        * Target, Related, Item Meta 를 가지고 Prophet, DeepAR_ Predictor 생성
    * Create_ItemMeta_Campaign.ipynb
        * Target, Related, Item Meta 를 가지고 Prophet, DeepAR_ Campaingn 생성    
    
# Forecasting Traffic Volume with AWS Forecast
**이 노트북의 원본은 https://github.com/chrisking/ForecastPOC.git 으로서, 원본 내용의 기반하에 추가 내용등을 기술한 버전 입니다.**

* AWS Forecast AI 서비스를 가지고 미국 미네라폴리스 근처 고속도로의 차량 통행량을 시간별로 예측하는 문제를 풀어가는 과정을 아래 4개의 노트북으로 구성 함.
(Hourly Data)


* **Technique included**
    * Compare Target Data vs. Target + Related Data
    * Compare ARIMA, Prophet and DeepARP performance with Acutal value


* Process: (Traffic Volume 폴더 안에 노트북을 아래 순서대로 실행 하셔야 합니다.)
    * Validating_and_Importing_Target_Time_Series_Data
        * 데이타를 준비하고 Target Time Series Data를 정의 함.
    * Creating_and_Evaluating_Predictors
        * Target Time Series Data와 ARIMA, Prophet, DeepAR+ 알고리즘을 가지고 Predictors 및 Forecasts를 생성한 후에 모델의 성능 분석을 함.
    * Validating_and_Importing_Related_Time_Series_Data 
        * Related Time Series Data를 정의 함.
    * Creating_and_Evaluating_Related_Time_Predictors
        * Target Time Series Data 및 Related Time Series Data 와 Prophet, DeepAR+ 알고리즘을 가지고 Predictors 및 Forecasts를 생성한 후에 모델의 성능 분석을 함.

    
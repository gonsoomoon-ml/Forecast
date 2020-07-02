
# 아래 링크를 누르시고 핸즈온 사전 단계를 진행 해주세요.(This is a Prerequisite Step for later Contents)

[핸즈온 준비 필수 단게: Prerequisite](Prerequisite.md)

**Prerequisite Task: Make sure that a role for SageMaker notebook instance has these policies attached such as AmazonSageMakerFullAccess, AmazonS3FullAccess, AmazonForecastFullAccess, IAMFullAccess**

## 처음 핸즈온의 경우는 아래 Forecasting Store Item Demanding with AWS Forecast 를 먼저 하시면 좋습니다.

## Forecasting Store Item Demanding with AWS Forecast  
(Data Source: https://www.kaggle.com/c/demand-forecasting-kernels-only/overview)

* **Description: Using AWS Forecast AI, forecasting the store item demanding problem (Daily Data)**

* **Technique included**
    * Use two dimenstions, item_id and store on Target Data
    * Use QueryForecast with two filters, item_id and store
    * Use QueryForecast with one filters, item_id 
    * Use HPO for building DeepARP 
    * Measure MAPE on Prophet and Deeparp campaigns    
    * Compare Prophet and DeepARP performance with actual value

## 아래 단계에서 1~6번까지의 노트북을 실행 하시면 됩니다.

* Process: (In the folder StoreItemDemand, run the following notebooks in order)
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
            

## Forecasting Walmart Weekly Sale with AWS Forecast
(Data Source: https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)

* **Description: Forecasting item's weekly sales in 45 U.S. Walmart stores with Amazon Forecast**

* **Technique included**
    * Use **three data sets of Target, Related and Item Meta**
    * Compare Prophet and DeepARP performance with actual value    


* Process: ( In the folder WalmartSale, run the following notebooks in order)
    * **1. Only using target time series dataset**
        * 0.LookAt_RawData.ipynb
        * 1.1.Prepare_Target_Data_File.ipynb
        * 1.2.Import_Dataset.ipynb
            * Create dataset group, dataset, and make dataset import job
        * 1.3.Create_Target_Predictors.ipynbe (About 40 mins elapsed)
            * Use Prophet and Deepar+ algorithm
        * 1.4.Create_Target_Forecast.ipynb (About 50 mins elapsed)
        * 1.5.Analyze_Target_Forecast.ipynb (About 10 mins elapsed)
            * Compute MAPE and show charts with p10,p50 and p90 as well as actual sales value
        * 1.6.Cleanup.ipynb
    * **2. Using target time series dataset plus related and item metadata dataset**
        * 0.LookAt_RawData.ipynb    
        * 2.0.Prepare_Target_Data_File.ipynb 
        * 2.1.Prepare_Related_Data_File.ipynb
        * 2.2.Prepare_Item_Meta_Data_File.ipynb
        * 2.3.Import_Target_Related_ItemMeta_Dataset.ipynb (About 5 mins elapsed)
            * Create dataset group and target, related, and item meta dataset
        * 2.4.Create_Target_Related_ItemMeta_Predictors.ipynb (About 40 mins elapsed)
            * Use Prophet and Deepar+ algorithm
        * 2.5.Create_Target_Related_ItemMeta_Forecast.ipynb (About 50 mins elapsed)
        * 2.6.Analyze_Target_Related_ItemMeta_Forecast.ipynb (About 10 mins elapsed)
            * Compute MAPE and show charts with p10,p50 and p90 as well as actual sales value        
        * 2.7.Cleanup.ipynb

    
## Forecasting Traffic Volume with AWS Forecast
**The following noteboos are based on the https://github.com/chrisking/ForecastPOC.git **

* **Description: Forecasting traffic volume in interstate highway near Minneapolis city (AWS Forecast AI 서비스를 가지고 미국 미네라폴리스 근처 고속도로의 차량 통행량을 시간별로 예측하는 문제를 풀어가는 과정을 아래 4개의 노트북으로 구성 함.)**
(Hourly Data)


* **Technique included**
    * Compare Target Data vs. Target + Related Data
    * Compare ARIMA, Prophet and DeepARP performance with Acutal value


* Process: (Traffic Volume 폴더 안에 노트북을 아래 순서대로 실행 하셔야 합니다.)
    * Validating_and_Importing_Target_Time_Series_Data
        * Prepare data and create Target Time Series Data
    * Creating_and_Evaluating_Predictors
        * With ARIMA, Prophet and DeepAR+, create Predictors and Forecasts
    * Validating_and_Importing_Related_Time_Series_Data 
        * Create Related Time Series Data
    * Creating_and_Evaluating_Related_Time_Predictors
        * Using Target Time Series Data and Related Time Series Data, with Prophet and DeepAR+, create predictors and Forecasts

    
# 핸즈온 사전 단계

- 이벤트 엔진, Cloud Formation 이용: 
    - [핸즈온 준비 필수 단게: Prerequisite](0.0.Prerequisite/CF-Prerequisite.md)
- 이벤트 엔진, 수동 설정: 
    - [여기](0.0.Prerequisite/Prerequisite.md) 를 클릭해서 해주세요.
- SageMaker notebook instance 를 이미 가지고 있는 경우
    - SageMaker notebook instance를 실행하는 Role이 아래 4개의 권한을 꼭 가지고 있어야 합니다. 아래 권한을 추가 해주세요. 참고로 위의 수동 설정에는 아래 4가지 권한을 추가하는 과정이 있습니다. 참고 하세요. (AmazonSageMakerFullAccess, AmazonS3FullAccess, AmazonForecastFullAccess, IAMFullAccess)

# Amazon Forecast 3가지 사례

### 1. Store Item Demand (가장 처음 진행시 먼저 진행 권장)

- Retail에서 item, store, # of sales 의 기본 세가지를 가지고 10개의 상점, 50개의 아이템 종류를 가지고 "일별" 로 판매 개수를 예측 하는 사례 입니다.
- Target Time Series 하나만을 가지고 예측 합니다. 
- 사용 알고리즘: DeepARP, Prophet, CNN-QR
- Data Source:
    - https://www.kaggle.com/c/demand-forecasting-kernels-only/overview  
    - **여기 누르시면 바로 갑니다. [바로 가기](StoreItemDemand/)**    


### 2. Traffic Volume 예측
- 미국 미네라폴리스 근처 고속도로의 차량 통행량을 시간별로 예측하는 문제를 풀어가는 과정입니다.
- 여기 누르시면 바로 갑니다. [바로가기](TrafficVolume/)
- [예측분석보고서](TrafficVolume/20200313_Forecasting_Traffic_Volume_Model_Analysis_Gonsoo.pdf) 에 요약 정보가 있습니다   


### 3. Walmart Store Sales
- 월마트 49개의 Store의 주별 매출액을 예측하는 문제 임.
- 실제 예측에 대한 내용 는 Target, Related, Item-Meta Dataset의 사용에 대한 코드 예제를 확인 하는 것이 유용 함.
- Data Source: 
    - https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting
- **여기 누르시면 바로 갑니다. [바로 가기](WalmartSale/)**    
    
    
    

    
    
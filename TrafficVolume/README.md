# Forecasting Traffic Volume (고속도로 교통량 예측)
이 소스는 https://github.com/chrisking/ForecastPOC.git 를 원본으로 하고 있습니다.

- 미국 미네라폴리스 근처 고속도로의 차량 통행량을 시간별로 예측하는 문제를 풀어가는 과정을 아래 4개의 노트북으로 구성 함.
- 이 사례에 대한 분석 보고서는 아래 PDF를 참고 하세요.
    - [Forecasting_Traffic_Volume_Model_Analysis](20200313_Forecasting_Traffic_Volume_Model_Analysis_Gonsoo.pdf)

## 실행 단계
1.0~4.0번까지의 노트북을 실행하시면 됩니다.

**옵션으로서 1.0 을 통해서 데이터에 대한 이해를 높이면 좋습니다.**

- 1.0 Validating_and_Importing_Target_Time_Series_Data
    - Target Data 를 만들고 data import 합니다. 
- 2.0.Creating_and_Evaluating_Predictors.ipynb
    - Predictor, Forecast를 생성하고 평가 합니다.
- 3.0.Validating_and_Importing_Related_Time_Series_Data.ipynb
    - Target, Related 데이타 셋을 준비하고 Data Import 합니다.
- 4.0.Creating_and_Evaluating_Related_Time_Predictors.ipynb
    - Predictor, Forecast를 생성하고 평가 합니다.

위의 노트북은 아래와 같은 기술적 부분을 가지고 있습니다.

* Compare Target Data vs. Target + Related Data
    * Compare ARIMA, Prophet and DeepARP performance with Acutal value


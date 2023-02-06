### 仕様
- 言語はPython3.10を用いる．
- 各設問に対する解答のプログラムが記されたファイルは，question*.pyである．
- 監視ログは確認日時で昇順にソートされていることを前提とする．
- あるサーバがN回連続でタイムアウトした後，そのサーバの次のping応答記録が監視ログに残されていない場合は，故障と看做さない．
- 過負荷状態の計算において，タイムアウトはスルーし，直近m回のうちに含まない．

### テスト

- テストデータとして，log/ping*.logを利用した．
- 各設問のテストデータに対する実行結果は，result/question*.txtにある．

## 設問1

監視ログを読み込んだ後，calculate_downtime関数にて故障期間を求める処理を行う．
calculate_downtime関数では，繰り返し処理を用いて監視ログを1行ずつ解析する．
応答結果がタイムアウトである場合は，タイムアウトした日時をdowntimeに記録しておく．
あるサーバがタイムアウトした後，そのサーバから正常なping応答が返ってきたら，タイムアウトした日時を故障開始，正常なping応答が返った日時を故障終了として，故障期間の出力を行う．

## 設問2

処理の流れは設問1と同じである．
設問1との処理の相違点としては，calculate_downtime関数において，downtimeにて各サーバが記録しているタイムアウト件数がN以上になったら，故障期間の出力を行うという点である．

## 設問3

監視ログを読み込んだ後，calculate_overtime関数にて過負荷状態期間を求める処理を行う．
calculate_overtime関数では，繰り返し処理を用いて監視ログを1行ずつ解析する．
タイムアウトの場合はスルーする．
response_timesに応答結果をサーバごとに記録する．それと同時に，datesに応答日時をサーバごとに記録する．
あるサーバにおいてresponse_timesに記録している応答結果の件数がmを超えてしまった場合は，response_timeとdatesの一番先頭の要素をpopする．
avg_response_timeに，平均応答時間を記録しておく．
avg_response_timeがtを超え，かつresponse_timesの長さがm以上である場合は，過負荷状態期間を出力する処理を行う．datesの先頭に記録されている日時を過負荷状態開始，datesの最後尾に記録されている日時を過負荷状態終了として，過負荷状態期間の出力を行う．


## 設問4

未完成

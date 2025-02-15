from google.cloud import bigquery
import pandas as pd
from typing import Iterator

def get_data_in_batches(query: str, batch_size: int) -> Iterator[pd.DataFrame]:
    """
    지정된 쿼리를 사용하여 데이터를 배치 단위로 가져오는 제너레이터 함수.
    
    :param query: 실행할 BigQuery 쿼리
    :param batch_size: 한 번에 가져올 데이터의 배치 크기
    :return: 각 배치마다 pd.DataFrame 객체를 반환하는 제너레이터
    """
    query_job = bigquery.Client().query(query)
    start_index = 0

    while True:
        rows = bigquery.Client().list_rows(query_job.destination, start_index=start_index, max_results=batch_size)
        results = rows.to_dataframe()
        
        if results.empty:
            break
        yield results

        start_index += batch_size


batch_size = 10
query = """
    SELECT *
    FROM `프로젝트명.pokemon.generation_1`
"""

for batch in get_data_in_batches(query, batch_size):
    print(batch)
# 제너레이터를 사용하는것으로...
#- **한 번에 한 줄씩 메모리에 로드**되므로, 전체 파일 크기와 상관없이 **메모리 사용량이 일정**합니다.
# 예를 들어, **1GB짜리 파일이라도 한 줄 크기만큼의 메모리만 사용**합니다.
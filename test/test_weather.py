from unittest.mock import patch, MagicMock
import pytest
from pytest_mock import MockerFixture
import weather


# mocker를 이용한 fixture 생성
@pytest.fixture
def mock_weather_service(mocker: MockerFixture) -> MagicMock:
    mock_service = mocker.MagicMock()  # MagicMock 객체 생성
    mock_service.get_temperature = mocker.MagicMock(return_value=25)  # 가짜 온도 반환 (25도)
    return mock_service  # 가짜 객체 반환

# 테스트
def test_get_temperature(mock_weather_service):
    temperature = mock_weather_service.get_temperature("Seoul")  # mock을 통해 테스트
    assert temperature == 25  # 예상한 값과 비교
    mock_weather_service.get_temperature.assert_called_once_with("Seoul")  # 함수 호출 검증

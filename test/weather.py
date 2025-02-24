# 실제 클래스 (외부 API를 호출하는 경우)
class WeatherService:
    def get_temperature(self, city: str) -> int:
        """실제 API를 호출하여 온도를 가져오는 함수 (테스트에서는 사용하지 않음)"""
        raise NotImplementedError("이 함수는 실제 API 호출을 포함합니다.")

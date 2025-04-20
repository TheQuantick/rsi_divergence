from src.strategy.strategy import strategy


class TestRSIDivergenceStrategyHappyPath:


    def test_strategy(self):
        # Given
        strategy_instance = strategy()
        # When
        result = strategy_instance.run()
        # Then
        assert result == 1


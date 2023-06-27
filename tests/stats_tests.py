import pytest
from train_utils.data import StatsManager

class TestAddItem: 

    @pytest.fixture(autouse=True)
    def setup_stats_manager(self):
        stats = StatsManager(name="bruh")
        yield stats

    def test_add_item_valid(self, setup_stats_manager):
        stats = setup_stats_manager
        stats.add("weight",1)
        stats.add("weight",2)
        stats.add("weight",3)
        stats.add("weight",4)
        stats.add("weight",5)
        stats.add("weight",6)
        stats.add("weight",7)
        stats.add("weight",8)
        assert stats.get("weight") == [1,2,3,4,5,6,7,8]
    
    def test_add_item_invalid(self, setup_stats_manager):
        stats = setup_stats_manager
        stats.add("hmmm", None)
        assert stats.get("hmmm") != [None]


class TestFileManagement:
    @pytest.fixture(autouse=True)
    def setup(self):
        stats = StatsManager(name = "MyStats")
        yield stats
    
    def test_saving_and_loading(self, setup):
        stats = setup
        stats.add("bruh", 1)
        stats.add("bruh", 2)

        name = stats.save()
        del stats
        stats = StatsManager()

        assert stats.load(name).get("bruh") == [1,2]
        assert stats.name == "MyStats"



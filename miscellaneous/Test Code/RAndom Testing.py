import hypothesis
from hypothesis import given
from hypothesis.strategies import integers, lists

@hypothesis.given(lists(integers()), integers())
def test_reverse_count_unchanged(lst, item):
    found_items = lst.count(item)
    lst = lst.reverse()
    found_items2 = lst.count(item)
    assert found_items == found_items2





if self.lifespan - time_played < 0:
    self.lifespan = 0
    print('Sorry, I am broken and cannot play')
else:

from ..dashboards.children import review as review_children

def test_get_review_dash_children():
    children = review_children.Get_Review_Children()
    n = len(children)
    assert n >= 1
    assert isinstance(children, (list,))
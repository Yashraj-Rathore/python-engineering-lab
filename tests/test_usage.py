from src.usage import summarize_usage
import pytest

def test_summarize_usage_normal_records():
    records = [
        {"project_id": "p1", "tokens": 100},
        {"project_id": "p1", "tokens": 150},
        {"project_id": "p2", "tokens": 50},
    ]
    result= summarize_usage(records)

    assert result == {
    "total_requests": 3,
    "total_tokens": 300
}

def test_summarize_usage_empty_records():
    records=[]
    result=summarize_usage(records)
    assert result == {
    "total_requests": 0,
    "total_tokens": 0
}

def test_summarize_usage_single_record():
    records = [
        {"project_id": "p1", "tokens": 200},
    ]
    result = summarize_usage(records)
    assert result == {
        "total_requests": 1,
        "total_tokens": 200
    }


def test_summazrize_usage_missing_tokens():
    records =[
        {"project_id": "p1"}
    ]

    with pytest.raises(KeyError):
        summarize_usage(records)
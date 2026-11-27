# tests/test_csv_report.py

from orderlab.csv_report import revenue_from_csv


# 테스트마다 임시 디렉터리에 테스트 전용 데이터 생성
def test_csv_revenue(tmp_path):
    csv_file = tmp_path / "orders.csv"
    csv_file.write_text(
        "price,quantity\n10000,2\n5000,3",
        encoding="utf-8",
    )
    assert revenue_from_csv(csv_file) == 35_000


def test_csv_empty(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("price,quantity", encoding="utf-8")
    assert revenue_from_csv(csv_file) == 0


def test_fixture_revenue(sample_csv):
    assert revenue_from_csv(sample_csv) == 35_000

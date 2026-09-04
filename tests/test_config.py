from qi.config import Config


def test_has_sql_true():
    cfg = Config(sql_dbs=["postgresql", "mysql"])
    assert cfg.has_sql is True


def test_has_sql_false():
    cfg = Config(sql_dbs=[])
    assert cfg.has_sql is False


def test_has_nosql_true():
    cfg = Config(nosql_dbs=["mongodb"])
    assert cfg.has_nosql is True


def test_has_nosql_false():
    cfg = Config()
    assert cfg.has_nosql is False


def test_has_ui_web():
    cfg = Config(ui_web=True)
    assert cfg.has_ui is True


def test_has_ui_mobile():
    cfg = Config(ui_mobile_ios=True)
    assert cfg.has_ui is True


def test_has_ui_false():
    cfg = Config(ui_web=False, ui_mobile_ios=False, ui_mobile_android=False)
    assert cfg.has_ui is False


def test_has_queues_true():
    cfg = Config(queues=["sqs"])
    assert cfg.has_queues is True


def test_has_queues_false():
    cfg = Config(queues=[])
    assert cfg.has_queues is False


def test_has_cloud_true():
    cfg = Config(cloud="aws")
    assert cfg.has_cloud is True


def test_has_cloud_false():
    cfg = Config(cloud="none")
    assert cfg.has_cloud is False

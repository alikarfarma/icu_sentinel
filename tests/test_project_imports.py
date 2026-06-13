import icu_sentinel
import icu_sentinel.data
import icu_sentinel.features
import icu_sentinel.models
import icu_sentinel.training
import icu_sentinel.evaluation
import icu_sentinel.interpretability
import icu_sentinel.utils


def test_package_imports():
    assert icu_sentinel.__version__ == "0.1.0"

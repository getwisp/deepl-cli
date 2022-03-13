import pytest

from deepl import deepl


def test1() -> None:
    t = deepl.DeepLCLI(langs=("en", "ja"))
    assert t.translate("hello") == "こんにちわ"


def test2() -> None:
    t = deepl.DeepLCLI(langs=("en", "ja"))
    with pytest.raises(deepl.DeepLCLIArgCheckingError):
        t.translate("\n")


def test3() -> None:
    t = deepl.DeepLCLI(langs=("en", "ja"))
    with pytest.raises(deepl.DeepLCLIArgCheckingError):
        t.chk_cmdargs()


def test4() -> None:
    t = deepl.DeepLCLI()
    with pytest.raises(AttributeError):
        t.translate("test")


def test5() -> None:
    with pytest.raises(deepl.DeepLCLIArgCheckingError):
        deepl.DeepLCLI(langs=("en", "jaa"))


def test6() -> None:
    with pytest.raises(deepl.DeepLCLIArgCheckingError):
        deepl.DeepLCLI(langs=("enn", "ja"))


def test7() -> None:
    t = deepl.DeepLCLI(langs=("", "ja"))
    assert t.translate("test") == "テスト"


def test8() -> None:
    t = deepl.DeepLCLI(langs=("ja", "de"))
    assert t.translate("今日は2022/2/22です。") == "Heute ist der 22.2.2022."


def test9() -> None:
    t = deepl.DeepLCLI(langs=("auto", "ja"))
    assert t.translate("test") == "テスト"
    assert t.translated_fr_lang == "en"
    assert t.translated_to_lang == "ja"

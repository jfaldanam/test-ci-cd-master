from main import make_upper_case, make_lower_case

def test_upper_case():
    test_words = {
        "word": "WORD",
        "hola": "HOLA",
        "HELLO": "HELLO",
        "": ""
    }

    for input_, output_ in test_words.items():
        assert make_upper_case(input_) == output_

def test_lower_case():
    test_words2 = {
        "WORD2":"word2",
        "HOLA":"hola",
        "CHAU":"chau",
        "": ""

    }

    for input_, output_ in test_words2.items():
        assert make_lower_case(input_) == output_
from hello import main


def test_main_prints_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from example_project!" in captured.out

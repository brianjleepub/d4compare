d4compare/
README.md
pyproject.toml
requirements.txt
.gitignore

data/
charProfile_v1.json
profiles/
paladin_hammerkuna.json # optional: copies/versions
cache/
equipped_items.json # created by app at runtime (gitignored)

src/
d4compare/
**init**.py
main.py

      config.py
      profile/
        __init__.py
        loader.py
        schema.py

      capture/
        __init__.py
        region.py
        screenshot.py
        calibration_ui.py

      ocr/
        __init__.py
        preprocess.py
        engine_tesseract.py
        engine_windows.py   # optional fallback later

      parse/
        __init__.py
        affix_normalize.py
        tooltip_parser.py
        patterns.py

      score/
        __init__.py
        thresholds.py
        scorer.py
        rules.py

      ui/
        __init__.py
        toast.py
        tray.py

      storage/
        __init__.py
        equipped_store.py

      utils/
        __init__.py
        logging.py
        fuzzy.py

tests/
test_parser_basic.py
test_scorer_thresholds.py
fixtures/
tooltip_samples/
weapon_01.txt
ring_01.txt

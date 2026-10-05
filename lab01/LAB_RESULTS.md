## TASK 4
```
(lab01) (base) manoftheprincess@Andreis-MacBook-Air lab01 % uv run python main.py --environment dev
APP_NAME:  DefaultAppName
ENVIRONMENT:  dev
(lab01) (base) manoftheprincess@Andreis-MacBook-Air lab01 % uv run python main.py --environment prod
APP_NAME:  DefaultAppName
ENVIRONMENT:  prod
(lab01) (base) manoftheprincess@Andreis-MacBook-Air lab01 % uv run python main.py --environment abc 
Traceback (most recent call last):
  File "/Users/manoftheprincess/Helloworld/Uni/agh/sem2/MLOps_course_AGH/lab01/main.py", line 18, in <module>
    settings = Settings(
               ^^^^^^^^^
  File "/Users/manoftheprincess/Helloworld/Uni/agh/sem2/MLOps_course_AGH/lab01/.venv/lib/python3.12/site-packages/pydantic_settings/main.py", line 262, in __init__
    super().__init__(**__pydantic_self__.__class__._settings_build_values(sources, init_kwargs))
  File "/Users/manoftheprincess/Helloworld/Uni/agh/sem2/MLOps_course_AGH/lab01/.venv/lib/python3.12/site-packages/pydantic/main.py", line 263, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for Settings
ENVIRONMENT
  Value error, ENVIRONMENT must be one of: dev, test, prod [type=value_error, input_value='abc', input_type=str]
    For further information visit https://errors.pydantic.dev/2.13/v/value_error
```

## TASK 5
After encription:
```
FAKE_KEY: ENC[AES256_GCM,data:eGFfJjSCQHI=,iv:NPmDKXjiplE2H/lsIb7TOihzTkUiTMMuPMJo/qip/Zs=,tag:43Jzgugfa9WszDpSaaP4Wg==,type:str]
sops:
    lastmodified: "2026-10-05T14:28:21Z"
    mac: ENC[AES256_GCM,data:Xv9O83y4HB9I/2Xd2uh4hBPHQIsYgQVQp+h1bSj/1qw6WL4Lz2hyPozXc7zurMHlKpM5PaDetI+vvfJtdrz+CD6dTJkqSpaCjamROM1WIDOuYKZUC4gN9vu5xMFRbe7kh3rjyfpiW+G1nOl8LzwoC6aWoafzd1/ncF+NgjUrBN8=,iv:mgXn/pimkm47Ec/ZWtD/ydRgwrNLcTEp8RI6eVkrDFk=,tag:mVSdp9Uv1LmGHBX7HWop3g==,type:str]
    pgp:
        - created_at: "2026-10-05T14:28:21Z"
          enc: |-
            -----BEGIN PGP MESSAGE-----

            hQGMAxnmPnIRtoZDAQv9HjiH3JQR44Z1P8pRNyTMKWFVPhrnSzjP73E2CiOOGS+q
            GKYnLGNVONzQv8f49e1T21Bk396DunNIuGOoIwPYo++uj1ykfa1whwLiFXRSxCc/
            zoOUAtGej/zBndYZKXmcZFZTFuv7gMmKHauF+xUlTRpI16woSeLkNXlmS7dziZ31
            XN/9INA0xbBgrSAPjkp2B0Qtp2hfe5EQSGYc1LG31DLjcYGzP1LUn2hZibOnjPGY
            N0eaJIvzjzTsWL5e/rmkYTy0Oat8diFGtoOp9vkHLFcBIzIHws4y/n8nkOKAwlfk
            xKuOT4k1n3w6j5EiTdjza7KlpHrZTuWjtpUBVvh7SGxSWodCW5qvWS4T3nuut8Wu
            cwpmBZdmRXxA/aIuYbUfsFM6NMyEE+g2LWvbdkkk0quBszhuuznN85OBKdXr2N2K
            DwlG/YqKmjurxaJu6pmtR9ftvEFYMEXFLHTARNsGY10jKft1w9bxb8NAFA9RhGld
            HdLX3ClfFIlKhDM74Qs11GgBCQIQIlKR0oeEZ3MXgkYILOAnq6TeUJKn8TcXZnY/
            JnCCDm4hy1dRQUAMJg+dDegwT2c2NAHnXqQ65l4njLghFjhavdgpvZzPonbx0+/O
            9pdLF/x2gSkfcfQwtPt6v3Wne/TNfgabeQ==
            =nuBK
            -----END PGP MESSAGE-----
          fp: 019B0D245AFE817E
    unencrypted_suffix: _unencrypted
    version: 3.13.3
```

Main app runing:
```
(lab01) (base) manoftheprincess@Andreis-MacBook-Air lab01 % uv run python main.py --environment dev
APP_NAME:  my_app
ENVIRONMENT:  dev
FAKE_KEY:  FAKE_KEY
```

## TASK 6
Test results:
```
(lab01) (base) manoftheprincess@Andreis-MacBook-Air lab01 % uv run pytest tests -rP
===================================================== test session starts =====================================================
platform darwin -- Python 3.12.13, pytest-9.1.1, pluggy-1.6.0
rootdir: /Users/manoftheprincess/Helloworld/Uni/agh/sem2/MLOps_course_AGH/lab01
configfile: pyproject.toml
plugins: platformdirs-4.12.3, dotenv-0.5.2, anyio-4.15.1
collected 2 items                                                                                                             

tests/test_app.py ..                                                                                                    [100%]

=========================================================== PASSES ============================================================
====================================================== 2 passed in 0.13s ======================================================

```